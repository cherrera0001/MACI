import re
p = r'C:\dashAI\_internal\DashAI\front\build\static\js\main.25351a8e.js'
s = open(p, encoding='utf-8', errors='ignore').read()
m = re.search(r'c\.dataloader=d,j&&\(c\.inferred_types=j\)', s)
print('===== contexto construccion de c (antes)'); print(s[m.start()-1400:m.end()+80].replace('\n', ' '))
m2 = re.search(r'eC=async', s)
print('\n===== eC definicion'); print(s[m2.start()-50:m2.end()+300].replace('\n', ' '))
m3 = re.search(r'WJr=\{', s)
print('\n===== WJr estado inicial newDataset'); print(s[m3.start():m3.end()+400].replace('\n', ' '))
