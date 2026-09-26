
(function(){
'use strict';
const $ = id => document.getElementById(id);
const coma = (v, d) => v.toFixed(d).replace('.', ',');
const pct = v => Math.round(v * 100) + ' %';

/* ===== Predicciones: se anota la elección y el contraste aparece al usar el control ===== */
const PRED = {
  predCorte: {
    A: '<strong>Acertaste: gana A</strong> (ganancia ≈ 0,209 con Gini). No deja ningún lado puro, pero limpia los dos, y los dos pesan: 7 y 10 de los 17 puntos. B da ≈ 0,101 y C ≈ 0,035.',
    B: '<strong>No: gana A.</strong> B deja un lado casi puro (5△ 1○), pero ese lado tiene solo 6 de los 17 puntos, y el otro queda muy mezclado (4△ 7○, Gini ≈ 0,463). La ganancia pondera por tamaño: B ≈ 0,101 contra A ≈ 0,209.',
    C: '<strong>No: gana A.</strong> C deja un hijo 100 % puro… con 1 punto de 17: pesa 1/17. El otro hijo (9△ 7○) sigue casi tan mezclado como el padre. Ganancia ≈ 0,035, la peor de las tres. Un hijo puro no basta: importa <em>cuántos</em> puntos purifica el corte.'
  },
  predEns: {
    siempre: '<strong>No siempre.</strong> Pon ρ = 1: con 1 o con 51 modelos, el voto acierta p. Y pon p = 0,45 con ρ = 0: sumar modelos <em>baja</em> la exactitud. Más modelos solo ayudan si cada uno es mejor que el azar y si no se equivocan en los mismos casos.',
    depende: '<strong>Eso es.</strong> Con p = 0,65 y errores independientes (ρ = 0), 11 modelos votando llegan a ≈ 85 % y 51 a ≈ 99 %. Con ρ = 1 se quedan en 65 % por muchos que agregues. En el medio (ρ = 0,5) hay techo: con 51 modelos, ≈ 82 %. [DATITO · cifras del modelo del simulador]',
    nunca: '<strong>No.</strong> Cuando los modelos se equivocan en casos distintos, el voto corrige: con p = 0,65 y ρ = 0, pasar de 1 a 51 modelos lleva la exactitud de 65 % a ≈ 99 %. Lo que sí es cierto es que los <em>clones</em> no mejoran nada (ρ = 1).'
  }
};
const elegida = {};
document.querySelectorAll('.pred').forEach(caja => {
  if (!PRED[caja.id]) return;
  caja.querySelectorAll('button[data-v]').forEach(b => {
    b.addEventListener('click', () => {
      caja.querySelectorAll('button[data-v]').forEach(x => x.classList.remove('elegida'));
      b.classList.add('elegida');
      elegida[caja.id] = b.dataset.v;
      const v = caja.querySelector('.veredicto');
      v.classList.remove('on');
      v.innerHTML = '';
      caja.querySelector('.espera').style.display = 'block';
    });
  });
});
function contraste(id){
  const e = elegida[id];
  if (!e) return;
  const caja = $(id), v = caja.querySelector('.veredicto');
  if (v.classList.contains('on')) return;
  v.innerHTML = PRED[id][e];
  v.classList.add('on');
  caja.querySelector('.espera').style.display = 'none';
}

/* ===== 1 · Calculadora de impureza sobre el ejemplo del profesor =====
   Conteos del profesor (9 triángulos, 8 círculos); posiciones inventadas [DATITO]. */
const PUNTOS = [
  {x:1.0, y:1.5, c:'c'}, {x:2.2, y:3.0, c:'c'}, {x:3.0, y:1.0, c:'c'}, {x:1.5, y:4.5, c:'c'},
  {x:3.3, y:4.0, c:'c'}, {x:1.2, y:8.0, c:'t'}, {x:2.8, y:7.2, c:'c'}, {x:7.5, y:8.6, c:'c'},
  {x:6.0, y:6.2, c:'c'}, {x:4.8, y:2.0, c:'t'}, {x:5.5, y:4.5, c:'t'}, {x:6.2, y:1.2, c:'t'},
  {x:6.8, y:3.3, c:'t'}, {x:7.5, y:5.5, c:'t'}, {x:8.2, y:2.4, c:'t'}, {x:8.8, y:4.2, c:'t'},
  {x:9.3, y:1.6, c:'t'}
];
const NT = PUNTOS.filter(p => p.c === 't').length;
const NC = PUNTOS.length - NT;
const MEDIDAS = {gini: 'Gini', entropia: 'Entropía', error: 'Error de clasificación'};
const HOJAS_PROF = [
  {f: p => p.x <= 4 && p.y > 6,  cx: 2.0, cy: 9.3},
  {f: p => p.x <= 4 && p.y <= 6, cx: 2.0, cy: 5.4},
  {f: p => p.x > 4 && p.y > 7,   cx: 5.9, cy: 9.3},
  {f: p => p.x > 4 && p.y <= 7,  cx: 8.6, cy: 6.5}
];
const g = {attr: 'x1', umbral: 4, medida: 'gini', prof: false};

function impureza(nt, nc, m){
  const n = nt + nc;
  if (n === 0) return 0;
  const pt = nt / n, pc = nc / n;
  if (m === 'gini') return pt * (1 - pt) + pc * (1 - pc);
  if (m === 'entropia'){
    let h = 0;
    [pt, pc].forEach(p => { if (p > 0) h -= p * Math.log2(p); });
    return h;
  }
  return 1 - Math.max(pt, pc);
}
function valor(p, attr){ return attr === 'x1' ? p.x : p.y; }
function evaluarCorte(attr, t, m){
  const a = {t: 0, c: 0}, b = {t: 0, c: 0};
  PUNTOS.forEach(p => { (valor(p, attr) <= t ? a : b)[p.c]++; });
  const N = PUNTOS.length, na = a.t + a.c, nb = b.t + b.c;
  const ip = impureza(NT, NC, m), ia = impureza(a.t, a.c, m), ib = impureza(b.t, b.c, m);
  const pond = na / N * ia + nb / N * ib;
  return {a: a, b: b, N: N, na: na, nb: nb, ip: ip, ia: ia, ib: ib, pond: pond, gan: ip - pond};
}
function hojaTxt(nombre, s){
  const n = s.t + s.c;
  if (!n) return 'Lado ' + nombre + ': vacío';
  return 'Punto nuevo en el lado ' + nombre + ': P(○) = ' + s.c + '/' + n + ' = ' + pct(s.c / n) +
         ' · P(△) = ' + s.t + '/' + n + ' = ' + pct(s.t / n);
}
function mejorCorte(m){
  let mejor = null, revisados = 0;
  ['x1', 'x2'].forEach(attr => {
    const vals = Array.from(new Set(PUNTOS.map(p => valor(p, attr)))).sort((u, v) => u - v);
    for (let i = 0; i < vals.length - 1; i++){
      const t = Math.round((vals[i] + vals[i + 1]) / 2 * 100) / 100;
      const r = evaluarCorte(attr, t, m);
      revisados++;
      if (!mejor || r.gan > mejor.gan + 1e-12) mejor = {attr: attr, t: t, gan: r.gan};
    }
  });
  mejor.revisados = revisados;
  return mejor;
}

function etiqueta(k, txt, x, y, alinear, W, ML, MR){
  k.font = '600 12px system-ui';
  const w = k.measureText(txt).width + 10;
  let x0 = alinear === 'right' ? x - w : (alinear === 'center' ? x - w / 2 : x);
  x0 = Math.max(ML + 2, Math.min(W - MR - w - 2, x0));
  k.fillStyle = 'rgba(255,255,255,0.93)';
  k.fillRect(x0, y - 13, w, 18);
  k.strokeStyle = '#ddd6fe'; k.lineWidth = 1;
  k.strokeRect(x0, y - 13, w, 18);
  k.fillStyle = '#1a1a1a'; k.textAlign = 'left';
  k.fillText(txt, x0 + 5, y);
}
function figura(k, x, y, c){
  k.beginPath();
  if (c === 'c'){
    k.arc(x, y, 7, 0, 2 * Math.PI);
    k.fillStyle = '#2563eb';
  } else {
    k.moveTo(x, y - 8); k.lineTo(x + 8, y + 6); k.lineTo(x - 8, y + 6); k.closePath();
    k.fillStyle = '#d97706';
  }
  k.fill();
}
function dibujaGini(r){
  const c = $('cvGini'), k = c.getContext('2d');
  const W = c.width, H = c.height, ML = 46, MR = 16, MT = 16, MB = 40;
  const px = x => ML + x / 10 * (W - ML - MR);
  const py = y => H - MB - y / 10 * (H - MT - MB);
  const linea = (x1, y1, x2, y2) => { k.beginPath(); k.moveTo(x1, y1); k.lineTo(x2, y2); k.stroke(); };
  k.clearRect(0, 0, W, H);

  if (!g.prof){
    const t = g.umbral;
    k.fillStyle = 'rgba(37,99,235,0.07)';
    if (g.attr === 'x1') k.fillRect(px(0), py(10), px(t) - px(0), py(0) - py(10));
    else k.fillRect(px(0), py(t), px(10) - px(0), py(0) - py(t));
    k.fillStyle = 'rgba(217,119,6,0.08)';
    if (g.attr === 'x1') k.fillRect(px(t), py(10), px(10) - px(t), py(0) - py(10));
    else k.fillRect(px(0), py(10), px(10) - px(0), py(t) - py(10));
  }
  k.strokeStyle = '#eeeeee'; k.lineWidth = 1;
  for (let v = 0; v <= 10; v += 2){ linea(px(v), py(0), px(v), py(10)); linea(px(0), py(v), px(10), py(v)); }
  k.strokeStyle = '#1a1a1a'; k.lineWidth = 1.5;
  k.beginPath(); k.moveTo(px(0), py(10)); k.lineTo(px(0), py(0)); k.lineTo(px(10), py(0)); k.stroke();
  k.fillStyle = '#666'; k.font = '11px system-ui'; k.textAlign = 'center';
  for (let v = 0; v <= 10; v += 2) k.fillText(v, px(v), py(0) + 15);
  k.textAlign = 'right';
  for (let v = 0; v <= 10; v += 2) k.fillText(v, px(0) - 6, py(v) + 4);
  k.textAlign = 'center';
  k.fillText('x₁', (px(0) + px(10)) / 2, H - 8);
  k.save(); k.translate(14, (py(0) + py(10)) / 2); k.rotate(-Math.PI / 2); k.fillText('x₂', 0, 0); k.restore();

  k.setLineDash([7, 5]); k.strokeStyle = '#7c3aed'; k.lineWidth = 2.5;
  if (g.prof){
    linea(px(4), py(0), px(4), py(10));
    linea(px(0), py(6), px(4), py(6));
    linea(px(4), py(7), px(10), py(7));
  } else if (g.attr === 'x1') linea(px(g.umbral), py(0), px(g.umbral), py(10));
  else linea(px(0), py(g.umbral), px(10), py(g.umbral));
  k.setLineDash([]);

  PUNTOS.forEach(p => figura(k, px(p.x), py(p.y), p.c));

  if (g.prof){
    HOJAS_PROF.forEach(h => {
      const s = {t: 0, c: 0};
      PUNTOS.filter(h.f).forEach(p => s[p.c]++);
      const n = s.t + s.c;
      const txt = (s.c >= s.t ? pct(s.c / n) + ' ○' : pct(s.t / n) + ' △') + '  (' + s.t + '△ ' + s.c + '○)';
      etiqueta(k, txt, px(h.cx), py(h.cy) + 5, 'center', W, ML, MR);
    });
  } else {
    const ta = '≤ · ' + r.a.t + '△ ' + r.a.c + '○', tb = '> · ' + r.b.t + '△ ' + r.b.c + '○';
    if (g.attr === 'x1'){
      etiqueta(k, ta, px(g.umbral) - 8, py(9.6), 'right', W, ML, MR);
      etiqueta(k, tb, px(g.umbral) + 8, py(9.6), 'left', W, ML, MR);
    } else {
      const yb = Math.min(py(0) - 6, py(g.umbral) + 20), ya = Math.max(MT + 14, py(g.umbral) - 8);
      etiqueta(k, ta, px(9.9), yb, 'right', W, ML, MR);
      etiqueta(k, tb, px(9.9), ya, 'right', W, ML, MR);
    }
  }
}
function selBotones(){
  $('gX1').classList.toggle('sel', !g.prof && g.attr === 'x1');
  $('gX2').classList.toggle('sel', !g.prof && g.attr === 'x2');
  [['mGini', 'gini'], ['mEnt', 'entropia'], ['mErr', 'error']].forEach(par => {
    $(par[0]).classList.toggle('sel', g.medida === par[1]);
  });
  $('gProf').textContent = g.prof ? 'Volver a un solo corte' : 'Ver el árbol completo del profesor';
}
function pintaGini(){
  const r = evaluarCorte(g.attr, g.umbral, g.medida);
  const eje = g.attr === 'x1' ? 'x₁' : 'x₂';
  $('gLeyUmbral').textContent = eje + ' ≤ ' + coma(g.umbral, 2);
  $('gPadre').textContent = coma(r.ip, 4);
  $('gIzq').textContent = coma(r.ia, 4);
  $('gIzqE').textContent = 'lado ≤ · ' + r.a.t + '△ ' + r.a.c + '○';
  $('gDer').textContent = coma(r.ib, 4);
  $('gDerE').textContent = 'lado > · ' + r.b.t + '△ ' + r.b.c + '○';
  $('gPond').textContent = coma(r.pond, 4);
  $('gGan').textContent = coma(r.gan, 4);
  let txt = 'Medida: ' + MEDIDAS[g.medida] + ' · corte ' + eje + ' ≤ ' + coma(g.umbral, 2) + '
' +
    'Ponderada = ' + r.na + '/' + r.N + ' · ' + coma(r.ia, 4) + ' + ' + r.nb + '/' + r.N + ' · ' +
    coma(r.ib, 4) + ' = ' + coma(r.pond, 4) + '
' +
    'Ganancia  = ' + coma(r.ip, 4) + ' − ' + coma(r.pond, 4) + ' = ' + coma(r.gan, 4) + '
' +
    hojaTxt('≤', r.a) + '
' + hojaTxt('>', r.b);
  if (g.prof){
    txt += '

Árbol completo del profesor: primer corte x₁ ≤ 4; después x₂ ≤ 6 a la izquierda y x₂ ≤ 7 a la derecha.' +
           '
Las etiquetas del plano muestran la probabilidad que entrega cada una de las 4 hojas.';
  }
  $('gArit').textContent = txt;
  selBotones();
  dibujaGini(r);
}
function accionGini(fn){
  return function(){ fn(); pintaGini(); contraste('predCorte'); };
}
function fijarCorte(attr, t){ g.prof = false; g.attr = attr; g.umbral = t; $('gUm').value = t; }
$('gA').onclick = accionGini(() => fijarCorte('x1', 4));
$('gB').onclick = accionGini(() => fijarCorte('x1', 6.5));
$('gC').onclick = accionGini(() => fijarCorte('x2', 8.3));
$('gX1').onclick = accionGini(() => { g.prof = false; g.attr = 'x1'; });
$('gX2').onclick = accionGini(() => { g.prof = false; g.attr = 'x2'; });
$('gUm').oninput = accionGini(() => { g.prof = false; g.umbral = parseFloat($('gUm').value); });
$('mGini').onclick = accionGini(() => { g.medida = 'gini'; });
$('mEnt').onclick = accionGini(() => { g.medida = 'entropia'; });
$('mErr').onclick = accionGini(() => { g.medida = 'error'; });
$('gMejor').onclick = accionGini(() => {
  const m = mejorCorte(g.medida);
  fijarCorte(m.attr, m.t);
  $('gMejorTxt').textContent = 'C4.5 revisó ' + m.revisados + ' cortes candidatos (puntos medios entre valores vecinos, en x₁ y en x₂) con ' +
    MEDIDAS[g.medida] + '. Ganó ' + (m.attr === 'x1' ? 'x₁' : 'x₂') + ' ≤ ' + coma(m.t, 2) + ', con ganancia ' + coma(m.gan, 4) + '.';
});
$('gProf').onclick = accionGini(() => {
  g.prof = !g.prof;
  if (g.prof){ g.attr = 'x1'; g.umbral = 4; $('gUm').value = 4; }
});

/* ===== 4 · Simulador de votación con errores correlacionados [DATITO] =====
   En cada caso, con probabilidad rho todos copian un mismo resultado; si no, cada uno
   acierta por su cuenta con probabilidad p. Números aleatorios comunes: al mover un
   control cambia el parámetro, no el sorteo. */
const M = 60, NMAX = 51;
let semE = 20260807;
function rndE(){ semE = (semE * 1664525 + 1013904223) % 4294967296; return semE / 4294967296; }
let U = null;
function sortearCasos(){
  U = {sel: [], val: [], ind: []};
  for (let j = 0; j < M; j++){ U.sel.push(rndE()); U.val.push(rndE()); }
  for (let i = 0; i < NMAX; i++){
    const fila = [];
    for (let j = 0; j < M; j++) fila.push(rndE());
    U.ind.push(fila);
  }
}
function colaBinomial(N, p){
  const k0 = Math.floor(N / 2) + 1;
  let s = 0, comb = 1;
  for (let k = 0; k <= N; k++){
    if (k > 0) comb = comb * (N - k + 1) / k;
    if (k >= k0) s += comb * Math.pow(p, k) * Math.pow(1 - p, N - k);
  }
  return s;
}
function exactitudVoto(N, p, rho){ return rho * p + (1 - rho) * colaBinomial(N, p); }
function simular(N, p, rho){
  const mat = [], voto = [];
  let ind = 0, okVoto = 0, todos = 0;
  for (let i = 0; i < N; i++) mat.push([]);
  for (let j = 0; j < M; j++){
    const comun = U.sel[j] < rho, valComun = U.val[j] < p;
    let ok = 0;
    for (let i = 0; i < N; i++){
      const a = comun ? valComun : U.ind[i][j] < p;
      mat[i].push(a);
      if (a) ok++;
    }
    ind += ok;
    const v = ok > N / 2;
    voto.push(v);
    if (v) okVoto++;
    if (ok === 0) todos++;
  }
  return {mat: mat, voto: voto, accInd: ind / (N * M), okVoto: okVoto, todos: todos};
}
const e = {N: 11, p: 0.65, rho: 0};

function dibujaGrid(s){
  const c = $('cvEns'), k = c.getContext('2d');
  const W = c.width, H = c.height, ML = 96, MR = 10, MT = 26, MB = 8;
  k.clearRect(0, 0, W, H);
  const cw = (W - ML - MR) / M;
  const rh = Math.min(16, (H - MT - MB - 16) / (e.N + 1));
  k.fillStyle = '#666'; k.font = '11px system-ui'; k.textAlign = 'left';
  k.fillText('Cada columna es un caso; cada fila, un modelo. Verde = acierta, rojo = falla.', ML, 14);
  for (let i = 0; i < e.N; i++){
    for (let j = 0; j < M; j++){
      k.fillStyle = s.mat[i][j] ? '#bbf7d0' : '#f87171';
      k.fillRect(ML + j * cw + 0.5, MT + i * rh + 0.5, cw - 1, Math.max(1, rh - 1));
    }
  }
  k.fillStyle = '#666'; k.textAlign = 'right';
  if (rh >= 10){
    for (let i = 0; i < e.N; i++) k.fillText('modelo ' + (i + 1), ML - 6, MT + i * rh + rh * 0.75);
  } else {
    k.fillText('modelos 1 a ' + e.N, ML - 6, MT + e.N * rh / 2 + 4);
  }
  const yv = MT + e.N * rh + Math.max(6, rh);
  const hv = 16;
  for (let j = 0; j < M; j++){
    k.fillStyle = s.voto[j] ? '#059669' : '#dc2626';
    k.fillRect(ML + j * cw + 0.5, yv, cw - 1, hv);
  }
  k.fillStyle = '#1a1a1a'; k.font = 'bold 11px system-ui';
  k.fillText('voto', ML - 6, yv + 12);
}
function dibujaCurva(){
  const c = $('cvCurva'), k = c.getContext('2d');
  const W = c.width, H = c.height, ML = 54, MR = 190, MT = 14, MB = 38;
  const px = n => ML + (n - 1) / (NMAX - 1) * (W - ML - MR);
  const py = a => H - MB - a * (H - MT - MB);
  k.clearRect(0, 0, W, H);
  k.font = '11px system-ui'; k.strokeStyle = '#eeeeee'; k.lineWidth = 1;
  [0, 0.25, 0.5, 0.75, 1].forEach(a => {
    k.beginPath(); k.moveTo(ML, py(a)); k.lineTo(W - MR, py(a)); k.stroke();
    k.fillStyle = '#666'; k.textAlign = 'right';
    k.fillText(Math.round(a * 100) + ' %', ML - 6, py(a) + 4);
  });
  k.textAlign = 'center';
  [1, 11, 21, 31, 41, 51].forEach(n => k.fillText(n, px(n), H - MB + 15));
  k.fillText('número de modelos que votan (N)', (ML + W - MR) / 2, H - 6);
  k.strokeStyle = '#1a1a1a'; k.lineWidth = 1.5;
  k.beginPath(); k.moveTo(ML, MT); k.lineTo(ML, H - MB); k.lineTo(W - MR, H - MB); k.stroke();
  const curva = (rho, color, dash, ancho) => {
    k.strokeStyle = color; k.lineWidth = ancho; k.setLineDash(dash); k.beginPath();
    for (let n = 1; n <= NMAX; n += 2){
      const y = py(exactitudVoto(n, e.p, rho));
      if (n === 1) k.moveTo(px(n), y); else k.lineTo(px(n), y);
    }
    k.stroke(); k.setLineDash([]);
  };
  curva(0, '#059669', [6, 4], 2);
  curva(1, '#dc2626', [6, 4], 2);
  curva(e.rho, '#2563eb', [], 3);
  k.fillStyle = '#2563eb';
  k.beginPath(); k.arc(px(e.N), py(exactitudVoto(e.N, e.p, e.rho)), 6, 0, 2 * Math.PI); k.fill();
  k.textAlign = 'left'; k.font = '12px system-ui';
  k.fillStyle = '#2563eb'; k.fillText('━ ρ = ' + coma(e.rho, 2) + ' (actual)', W - MR + 14, MT + 16);
  k.fillStyle = '#059669'; k.fillText('╌ ρ = 0 (independientes)', W - MR + 14, MT + 38);
  k.fillStyle = '#dc2626'; k.fillText('╌ ρ = 1 (clones)', W - MR + 14, MT + 60);
  k.fillStyle = '#666'; k.fillText('p = ' + coma(e.p, 2) + ' en las tres', W - MR + 14, MT + 86);
}
function pintaEns(){
  $('eNv').textContent = e.N;
  $('ePv').textContent = coma(e.p, 2);
  $('eRv').textContent = coma(e.rho, 2);
  const s = simular(e.N, e.p, e.rho);
  $('eInd').textContent = pct(e.p);
  $('eIndEmp').textContent = pct(s.accInd);
  $('eTeo').textContent = coma(exactitudVoto(e.N, e.p, e.rho) * 100, 1) + ' %';
  $('eEmp').textContent = s.okVoto + ' / ' + M;
  $('eTodos').textContent = s.todos + ' / ' + M;
  dibujaGrid(s);
  dibujaCurva();
}
function accionEns(fn){
  return function(){ fn(); pintaEns(); contraste('predEns'); };
}
$('eN').oninput = accionEns(() => { e.N = parseInt($('eN').value, 10); });
$('eP').oninput = accionEns(() => { e.p = parseFloat($('eP').value); });
$('eR').oninput = accionEns(() => { e.rho = parseFloat($('eR').value); });
$('eClones').onclick = accionEns(() => { e.rho = 1; $('eR').value = 1; });
$('eIndep').onclick = accionEns(() => { e.rho = 0; $('eR').value = 0; });
$('eMoneda').onclick = accionEns(() => { e.p = 0.45; $('eP').value = 0.45; });
$('eSorteo').onclick = accionEns(() => { sortearCasos(); });

sortearCasos();
pintaGini();
pintaEns();
})();
