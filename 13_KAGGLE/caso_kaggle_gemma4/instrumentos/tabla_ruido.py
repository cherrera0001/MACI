"""Cuánto de la tabla pública se explica por «mejor de m tiradas ruidosas». Un proceso, solo lectura."""
import csv, io, math, sys, zipfile, random
from collections import Counter, defaultdict

z = zipfile.ZipFile(sys.argv[1])
rows = list(csv.DictReader(io.TextIOWrapper(z.open(z.namelist()[0]), encoding='utf-8-sig')))
N = 58
k_de = {math.floor(k / N * 100) / 100: k for k in range(N + 1)}
teams = []
for r in rows:
    s = round(float(r['Score']), 2)
    k = k_de.get(s)
    if k is None:
        # tolerancia de coma flotante
        k = min(range(N + 1), key=lambda j: abs(math.floor(j / N * 100) / 100 - s))
    teams.append((k, int(r['SubmissionCount'])))
n = len(teams)
print('equipos', n, 'envios totales', sum(m for _, m in teams))

# 1. Nota frente a número de envíos
grupos = [(1, 1), (2, 2), (3, 4), (5, 7), (8, 12), (13, 20), (21, 999)]
print('\nm        equipos  media_k  mediana  %>=8   %>=10  %>=12')
for a, b in grupos:
    ks = sorted(k for k, m in teams if a <= m <= b)
    if not ks:
        continue
    f = lambda t: 100 * sum(k >= t for k in ks) / len(ks)
    print(f'{a:>2}-{b:<4} {len(ks):>7}  {sum(ks)/len(ks):6.2f}  {ks[len(ks)//2]:>6}  {f(8):5.1f}  {f(10):5.1f}  {f(12):5.1f}')

# 2. Distribución de una sola tirada: equipos con un envío
uno = [k for k, m in teams if m == 1]
c1 = Counter(uno)
print('\nun envío: n', len(uno), 'media', round(sum(uno) / len(uno), 2),
      'var', round(sum((k - sum(uno) / len(uno)) ** 2 for k in uno) / len(uno), 2))
p1 = sum(uno) / len(uno) / N
print('varianza binomial con esa media:', round(N * p1 * (1 - p1), 2))

def binom_cdf(N, p):
    pmf = [math.comb(N, k) * p ** k * (1 - p) ** (N - k) for k in range(N + 1)]
    cdf, s = [], 0
    for x in pmf:
        s += x
        cdf.append(s)
    return pmf, cdf

def esperado_max(p, m):
    _, cdf = binom_cdf(N, p)
    return sum(1 - cdf[k] ** m for k in range(N))  # E[max] = sum P(max>k)

# 3. Modelo nulo A: todos los envíos de todos los equipos tienen la misma tasa p (solo ruido + nº de envíos)
def loglik(p):
    _, cdf = binom_cdf(N, p)
    ll = 0
    for k, m in teams:
        hi = cdf[k] ** m
        lo = cdf[k - 1] ** m if k > 0 else 0
        ll += math.log(max(hi - lo, 1e-300))
    return ll
mejor = max((loglik(p / 1000), p / 1000) for p in range(30, 200, 2))
pA = mejor[1]
print(f'\nModelo solo-ruido: p único = {pA:.3f} ({pA*N:.1f} tareas por tirada)')
_, cdf = binom_cdf(N, pA)
esp = Counter()
for k0 in range(N + 1):
    for _, m in teams:
        esp[k0] += cdf[k0] ** m - (cdf[k0 - 1] ** m if k0 else 0)
obs = Counter(k for k, _ in teams)
print('k   observado  esperado_solo_ruido')
for k0 in range(0, 16):
    print(f'{k0:>2}  {obs[k0]:>8}  {esp[k0]:>8.0f}')
print('>=10 observado', sum(v for k, v in obs.items() if k >= 10), 'esperado', round(sum(v for k, v in esp.items() if k >= 10)))
print('>=12 observado', sum(v for k, v in obs.items() if k >= 12), 'esperado', round(sum(v for k, v in esp.items() if k >= 12), 1))
print('==0  observado', obs[0], 'esperado', round(esp[0], 1))

# 4. Nuestro caso: qué tasa es compatible con 5 y 8 (i_razona) y con 4 y 3 (base)
for nombre, xs in (('base 4,3', (4, 3)), ('i_razona 5,8', (5, 8)), ('las cuatro', (4, 3, 5, 8))):
    tot, nn = sum(xs), N * len(xs)
    p = tot / nn
    # intervalo de Wilson 95 %
    zc = 1.96
    den = 1 + zc * zc / nn
    c = (p + zc * zc / (2 * nn)) / den
    h = zc * math.sqrt(p * (1 - p) / nn + zc * zc / (4 * nn * nn)) / den
    print(f'{nombre}: p = {p:.3f} ({p*N:.1f} tareas), IC95 {max(0,c-h)*N:.1f} a {(c+h)*N:.1f} tareas')

# Fisher exacto base (7 de 116) contra i_razona (13 de 116)
def fisher(a, b, c, d):
    n1, n2, k = a + b, c + d, a + c
    den = math.comb(n1 + n2, k)
    pobs = math.comb(n1, a) * math.comb(n2, c) / den
    return sum(math.comb(n1, i) * math.comb(n2, k - i) / den for i in range(max(0, k - n2), min(n1, k) + 1)
               if math.comb(n1, i) * math.comb(n2, k - i) / den <= pobs + 1e-12)
print('Fisher 7/116 contra 13/116, p =', round(fisher(7, 109, 13, 103), 3))

# 5. Qué da enviar todos los días: mejor nota pública esperada con m tiradas, para varias tasas reales
print('\nMejor nota PÚBLICA esperada (tareas de 58) según tasa real y número de envíos:')
print('tasa(tareas)   m=1    m=4    m=10   m=20   m=54')
for kreal in (5, 6.5, 8, 10):
    p = kreal / N
    print(f'{kreal:>6}       ' + '  '.join(f'{esperado_max(p, m):5.2f}' for m in (1, 4, 10, 20, 54)))

# 6. Y lo que cuenta: la tabla privada (otras ~60 tareas) no hereda la suerte. Simulación:
# se envía m veces el mismo zip de tasa p, se eligen como finales las 2 mejores públicas; nota privada = mejor de esas 2.
random.seed(20261009)
def sim(p, m, rep=4000, Np=60):
    tot_pub = tot_priv = 0
    for _ in range(rep):
        tir = [(sum(random.random() < p for _ in range(N)), sum(random.random() < p for _ in range(Np))) for _ in range(m)]
        random.shuffle(tir)
        tir.sort(key=lambda t: t[0], reverse=True)  # el empate en la pública no mira la privada
        tot_pub += tir[0][0]
        tot_priv += max(tir[0][1], tir[1][1]) if m > 1 else tir[0][1]
    return tot_pub / rep, tot_priv / rep
print('\nMismo zip de 6,5 tareas reales: mejor pública y privada de los 2 finales elegidos por la pública')
for m in (1, 4, 10, 54):
    a, b = sim(6.5 / N, m, rep=3000 if m > 20 else 6000)
    print(f'm={m:>2}: pública {a:5.2f} de 58, privada {b:5.2f} de 60')

# 7. El envío diario como instrumento: dos zips alternados, n envíos cada uno, solo se ve el total de 58.
# Diferencia mínima detectable (alfa 0,05 bilateral, potencia 0,80) con varianza binomial (cota superior del ruido).
print()
print('Dos zips alternados, n envíos por zip; base de 6,5 tareas: diferencia detectable 8 de cada 10 veces')
for n_env in (2, 5, 10, 15, 20, 27):
    p = 6.5 / N
    for d in [x / 4 for x in range(1, 80)]:
        p2 = (6.5 + d) / N
        se = math.sqrt(N * p * (1 - p) / n_env + N * p2 * (1 - p2) / n_env)
        if d / se >= 1.96 + 0.84:
            print(f'n={n_env:>2} por zip ({2*n_env} días): +{d:.2f} tareas por envío ({d/N:.3f} de nota)')
            break
