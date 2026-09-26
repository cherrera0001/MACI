from pathlib import Path
import re,json,sys,subprocess
import tinycss2
from playwright.sync_api import sync_playwright
ROOT=Path.cwd(); BASE=ROOT/'07_DATITO/01_CONCEPTOS/visual'; E=ROOT/'07_DATITO/07_BITACORA/learning_loop/evidence/sprint01'
name,mode=sys.argv[1:3];p=BASE/(name+'.html');e=E/name;e.mkdir(parents=True,exist_ok=True)
s=p.read_text(encoding='utf-8')
if mode=='before':
 if not (e/'original.html').exists():(e/'original.html').write_bytes(p.read_bytes())
if mode=='fix':
 template=(BASE/'_TEMPLATE_CANONICO.html').read_text(encoding='utf-8');head=template[:template.index('<main>',template.index('</head>'))+len('<main>')]
 title=re.search(r'<h1[^>]*>(.*?)</h1>',s,re.S).group(1);title=re.sub('<[^>]+>','',title)
 head=re.sub(r'^<title>.*?</title>','<title>'+title+' · Datito</title>',head,flags=re.M).replace('<meta charset="utf-8">','<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">')
 canon=re.search(r'<style>(.*?)</style>',head,re.S).group(1)
 canonical={tinycss2.serialize(r.prelude).strip() for r in tinycss2.parse_stylesheet(canon) if r.type=='qualified-rule'}
 donors={'09_regresion':'regresion_y_costo','14_arboles_decision':'arboles_y_ensambles'}
 donor=donors.get(name,name.split('_',1)[1]);css=re.search(r'<style[^>]*>(.*?)</style>',s if name.startswith(('10_','12_')) else (ROOT/'10_ARCHIVO/courses/fcd-2026-2/visual'/f'{donor}.html').read_text(encoding='utf-8'),re.S).group(1)
 extra=[];variables={}
 for r in tinycss2.parse_stylesheet(css,skip_whitespace=True,skip_comments=True):
  if r.type=='qualified-rule':
   sel=tinycss2.serialize(r.prelude).strip()
   if sel==':root':
    variables={x.name:tinycss2.serialize(x.value).strip() for x in tinycss2.parse_declaration_list(r.content) if x.type=='declaration'};continue
   if sel in canonical or sel in ['a','body','main','h1','h2','h3','p','section','footer','*','.hoja']:continue
   extra.append(tinycss2.serialize([r]))
  elif r.type=='at-rule':extra.append(tinycss2.serialize([r]))
 css='\n'.join(extra)
 # Preserve semantic widget colors without importing an alternate root or skin.
 for k,v in variables.items():
  if k not in ['--tinta','--suave','--linea','--fondo','--azul','--rojo','--verde','--ambar','--morado']:css=css.replace('var('+k+')',v)
 body=s[s.index('<!-- datito:nav:inicio -->'):]
 ph=re.search(r'<h1>T[ÍI]TULO DEL CONCEPTO',body)
 if ph:
  body=body[:body.rfind('<!-- datito:nav:fin -->',0,ph.start())].rstrip()+'\n</main>\n</body>\n</html>\n'
 if name.startswith(('10_','12_')):
  body=body.replace('</body>','</main>\n</body>')
  for k,v in variables.items():
   if k not in ['--tinta','--suave','--linea','--fondo','--azul','--rojo','--verde','--ambar','--morado']:body=body.replace('var('+k+')',v)
  css=re.sub(r'\.hoja\{[^}]*\}', '',css)
  css=css.replace('.pasos','ol.pasos')
 body=body.replace('.leccion-top,.pasos{','.leccion-top,nav.pasos{').replace('}.pasos{','}nav.pasos{').replace('}.pasos a{','}nav.pasos a{').replace('}.barra{','}.leccion .barra{').replace('}.barra span{','}.leccion .barra span{')
 css+='\n/* Preserve readable formulas and small-screen access to existing content. */\n.ec,.formula{font-family:ui-monospace,Consolas,monospace}\nmain{overflow-wrap:anywhere}\n@media(max-width:600px){nav.pasos{flex-wrap:wrap}table{display:block;overflow-x:auto}.panel,.ecu{padding:.8rem} .leccion-top{flex-wrap:wrap}}'
 head=head.replace('</style>','</style>\n<style>\n/* Controls recovered from this concept; canonical base remains intact. */\n'+css+'\n</style>')
 p.write_text(head+'\n'+body,encoding='utf-8');print('fixed',name);sys.exit()
with sync_playwright() as pw:
 b=pw.chromium.launch();context=b.new_context(viewport={'width':1280,'height':900},offline=True);page=context.new_page();errors=[];page.on('pageerror',lambda x:errors.append(str(x)));page.goto(p.as_uri());page.locator('h1').first.scroll_into_view_if_needed();page.screenshot(path=str(e/f'{mode}.png'))
 if mode=='after':
  report={'errors':errors,'h1':page.locator('h1').count(),'styles':{},'controls':[]}
  for cl in ['repreg','fuente','dist','vecino','pred','rol','met']:
   loc=page.locator('.'+cl)
   report['styles'][cl]=loc.first.evaluate('(e)=>({background:getComputedStyle(e).backgroundColor,font:getComputedStyle(e).fontSize,border:getComputedStyle(e).borderLeftWidth})') if loc.count() else None
  for i in range(page.locator('input[type=range]').count()):
   loc=page.locator('input[type=range]').nth(i);old=loc.input_value();loc.evaluate('(e)=>{e.value=e.max||100;e.dispatchEvent(new Event("input",{bubbles:true}));e.dispatchEvent(new Event("change",{bubbles:true}));}');report['controls'].append({'range':loc.get_attribute('id'),'before':old,'after':loc.input_value()})
  for i in range(page.locator('button').count()):
   loc=page.locator('button').nth(i)
   if loc.is_visible() and loc.is_enabled():
    try:loc.click(timeout=1000);report['controls'].append({'button':loc.inner_text()[:60],'clicked':True})
    except Exception as x:report['controls'].append({'button':loc.inner_text()[:60],'error':str(x)[:150]})
  report['desktopOverflow']=page.evaluate('document.documentElement.scrollWidth>innerWidth')
  if page.locator('.repreg').count():page.locator('.repreg').first.scroll_into_view_if_needed();page.screenshot(path=str(e/'after-question.png'))
  page.set_viewport_size({'width':390,'height':844});page.locator('h1').first.scroll_into_view_if_needed();page.screenshot(path=str(e/'after-mobile.png'));report['mobileOverflow']=page.evaluate('document.documentElement.scrollWidth>innerWidth');report['errors']=errors
  (e/'qa.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(report,ensure_ascii=True))
  result=subprocess.run([sys.executable,'03_CODIGO/datito_loop_eval.py','--path',str(p)],capture_output=True,text=True,encoding='utf-8');(e/'gate.json').write_text(result.stdout+result.stderr,encoding='utf-8');print(result.stdout)
 b.close()

