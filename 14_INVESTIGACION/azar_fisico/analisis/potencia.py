# -*- coding: utf-8 -*-
"""
potencia.py - Tamano muestral y potencia para detectar sesgo en sorteos sin reposicion.

Juego de referencia: 6 bolillas sin reposicion de un bombo de 41 (tambien se informa 14 de 25).
Unidad de observacion: el SORTEO (no la bolilla). En cada sorteo, la bolilla i aparece o no
aparece entre las k extraidas; bajo azar ideal P(aparece) = p0 = k/N.

Bloques:
  A. Bits equivalentes de una historia de sorteos frente a los minimos de NIST SP 800-22 / 800-90B.
  B. Prueba de UNA bolilla (binomial): n de sorteos para potencia 0,8, con alfa 0,05 y alfa corregido.
  C. Prueba omnibus chi-cuadrado de frecuencias con correccion por muestreo sin reposicion
     (J = (N-1) X^2 / (N-k), Joe 1993; Genest, Lockhart y Stephens 2002) y efecto w de Cohen.
  D. Potencia alcanzable con historias realistas y sesgo minimo detectable.
  E. Predictibilidad: ganancia de informacion (bits por sorteo) y sorteos para demostrarla.
  F. Comprobacion por simulacion Monte Carlo (error tipo I y potencia) de las formulas de B y C.

Uso:  python potencia.py        (escribe potencia_salida.txt junto al guion)
Dependencias: numpy, scipy. Semilla fija: resultados reproducibles.
"""
import io
import math
import os
import sys

import numpy as np
from scipy import optimize, stats

ALFA = 0.05
POTENCIA = 0.80
SESGOS = [0.01, 0.05, 0.10, 0.20]          # sesgo relativo delta: p1 = p0 (1 + delta)
SORTEOS_POR_ANIO = 150
SEMILLA = 20261009

_buf = io.StringIO()


def p(*args):
    linea = " ".join(str(a) for a in args)
    print(linea)
    _buf.write(linea + "\n")


def fmt(x):
    """Entero con separador de miles (espacio); los decimales usan punto."""
    return f"{int(round(x)):,}".replace(",", " ")


# ----------------------------------------------------------------------------------------
# A. Bits equivalentes
# ----------------------------------------------------------------------------------------
def bits_por_sorteo(N, k):
    sin_orden = math.log2(math.comb(N, k))
    con_orden = math.log2(math.perm(N, k))
    return sin_orden, con_orden


def bloque_a():
    p("=" * 92)
    p("A. BITS EQUIVALENTES DE UNA HISTORIA DE SORTEOS")
    p("=" * 92)
    p("Entropia maxima por sorteo (azar ideal): log2 C(N,k) si solo se registra el conjunto;")
    p("log2 N!/(N-k)! si se registra el orden de salida.")
    for N, k in [(41, 6), (25, 14)]:
        so, co = bits_por_sorteo(N, k)
        p(f"\nJuego {k} de {N}: C(N,k) = {fmt(math.comb(N, k))} combinaciones")
        p(f"  bits por sorteo sin orden = {so:.3f}   con orden = {co:.3f}")
        p(f"  {'anios':>6} {'sorteos':>8} {'bolillas':>9} {'bits sin orden':>15} {'bits con orden':>15}")
        for anios in [1, 5, 10, 20, 40]:
            n = anios * SORTEOS_POR_ANIO
            p(f"  {anios:>6} {fmt(n):>8} {fmt(n * k):>9} {fmt(n * so):>15} {fmt(n * co):>15}")

    so, co = bits_por_sorteo(41, 6)
    p("\nMinimos de longitud de secuencia de NIST SP 800-22 Rev. 1a (seccion 2.x.7 de cada prueba)")
    p("frente a un juego 6 de 41 con 150 sorteos al anio (anios necesarios para UNA secuencia):")
    minimos = [
        ("Frecuencia (monobit), Rachas, Sumas acumuladas, Frecuencia en bloque", 100),
        ("Racha mas larga de unos (M=8)", 128),
        ("Transformada discreta de Fourier (espectral)", 1000),
        ("Racha mas larga de unos (M=128)", 6272),
        ("Rango de matrices binarias (38 matrices 32x32)", 38912),
        ("Estadistico universal de Maurer (L=6)", 387840),
        ("Racha mas larga (M=10^4)", 750000),
        ("Plantillas solapadas, Complejidad lineal, Excursiones aleatorias (y variante)", 10 ** 6),
    ]
    p(f"  {'prueba':<78} {'n min bits':>10} {'anios s/orden':>13} {'anios c/orden':>13}")
    for nombre, nmin in minimos:
        a1 = nmin / (so * SORTEOS_POR_ANIO)
        a2 = nmin / (co * SORTEOS_POR_ANIO)
        p(f"  {nombre:<78} {fmt(nmin):>10} {a1:>13.1f} {a2:>13.1f}")
    p("\nEstrategia de SP 800-22 seccion 4.2: al menos 55 secuencias para la prueba de uniformidad")
    p("de valores p; el ejemplo de la norma usa del orden de 10^3 secuencias de 10^6 bits.")
    for etiqueta, total in [("55 secuencias x 10^6 bits", 55e6), ("1000 secuencias x 10^6 bits", 1e9)]:
        p(f"  {etiqueta:<32} = {total:.2e} bits -> {total / (so * SORTEOS_POR_ANIO):.0f} anios (sin orden), "
          f"{total / (co * SORTEOS_POR_ANIO):.0f} anios (con orden)")
    p("\nNIST SP 800-90B seccion 3.1.1: 1.000.000 de muestras consecutivas de la fuente de ruido,")
    p("mas 1000 reinicios x 1000 muestras.")
    p(f"  si la muestra es la bolilla (900 al anio): {1e6 / (6 * SORTEOS_POR_ANIO):.0f} anios")
    p(f"  si la muestra es el sorteo  (150 al anio): {1e6 / SORTEOS_POR_ANIO:.0f} anios")
    p("\nNota: C(41,6) no es potencia de 2; para obtener bits insesgados hay que numerar la")
    p("combinacion (sistema combinatorio) y rechazar los indices >= 2^22:")
    p(f"  2^22 / C(41,6) = {2 ** 22 / math.comb(41, 6):.4f} de los sorteos aprovechables, 22 bits cada uno.")


# ----------------------------------------------------------------------------------------
# B. Una bolilla
# ----------------------------------------------------------------------------------------
def n_binomial(p0, delta, alfa, potencia=POTENCIA, bilateral=True):
    """Aproximacion normal clasica para una proporcion:
       n = [ z_a sqrt(p0 q0) + z_b sqrt(p1 q1) ]^2 / (p1 - p0)^2
    """
    p1 = p0 * (1 + delta)
    za = stats.norm.ppf(1 - alfa / 2) if bilateral else stats.norm.ppf(1 - alfa)
    zb = stats.norm.ppf(potencia)
    return (za * math.sqrt(p0 * (1 - p0)) + zb * math.sqrt(p1 * (1 - p1))) ** 2 / (p1 - p0) ** 2


def potencia_binomial_exacta(n, p0, delta, alfa):
    """Potencia exacta de la prueba binomial bilateral (colas iguales alfa/2), sesgo positivo."""
    n = int(math.ceil(n))
    p1 = p0 * (1 + delta)
    c_sup = stats.binom.isf(alfa / 2, n, p0)        # rechaza si X > c_sup
    c_inf = stats.binom.ppf(alfa / 2, n, p0) - 1    # rechaza si X <= c_inf
    nivel = stats.binom.sf(c_sup, n, p0) + stats.binom.cdf(c_inf, n, p0)
    pot = stats.binom.sf(c_sup, n, p1) + stats.binom.cdf(c_inf, n, p1)
    return nivel, pot


def bloque_b(N=41, k=6):
    p0 = k / N
    p("\n" + "=" * 92)
    p(f"B. UNA BOLILLA, JUEGO {k} DE {N}: p0 = k/N = {p0:.5f}")
    p("=" * 92)
    p("Formula: n = [ z_(1-alfa/2) sqrt(p0 q0) + z_(pot) sqrt(p1 q1) ]^2 / (p1 - p0)^2,  p1 = p0 (1+delta)")
    p("n en SORTEOS. Anios a 150 sorteos/anio. Potencia objetivo 0,80. Prueba bilateral.")
    niveles = [
        ("alfa 0,05 (bolilla prerregistrada)", ALFA),
        (f"Bonferroni {N} bolillas (alfa={ALFA / N:.5f})", ALFA / N),
        ("Bonferroni 1000 hipotesis (alfa=5e-05)", ALFA / 1000),
    ]
    for etiqueta, a in niveles:
        p(f"\n  {etiqueta}")
        p(f"  {'delta':>6} {'p1':>8} {'p1-p0':>8} {'n sorteos':>11} {'anios':>9} {'nivel exacto':>13} {'pot. exacta':>12}")
        for d in SESGOS:
            n = n_binomial(p0, d, a)
            nivel, pot = potencia_binomial_exacta(n, p0, d, a)
            p(f"  {d:>6.0%} {p0 * (1 + d):>8.5f} {p0 * d:>8.5f} {fmt(math.ceil(n)):>11} "
              f"{n / SORTEOS_POR_ANIO:>9.1f} {nivel:>13.5f} {pot:>12.3f}")
    p("\n  Referencia unilateral (H1: la bolilla sale DE MAS), alfa 0,05:")
    for d in SESGOS:
        n = n_binomial(p0, d, ALFA, bilateral=False)
        p(f"  delta {d:>4.0%}: n = {fmt(math.ceil(n)):>9} sorteos = {n / SORTEOS_POR_ANIO:>7.1f} anios")


# ----------------------------------------------------------------------------------------
# C. Omnibus chi-cuadrado con correccion por muestreo sin reposicion
# ----------------------------------------------------------------------------------------
def lambda_necesaria(gl, alfa, potencia=POTENCIA):
    crit = stats.chi2.ppf(1 - alfa, gl)
    f = lambda lam: stats.ncx2.sf(crit, gl, lam) - potencia
    return optimize.brentq(f, 1e-6, 1e4)


def potencia_omnibus(n, N, k, w, alfa):
    """J = (N-1) X^2/(N-k) ~ chi2(N-1) bajo H0; bajo H1 local, no central con
       lambda = n k w^2 (N-1)/(N-k)."""
    gl = N - 1
    lam = n * k * w * w * (N - 1) / (N - k)
    return stats.ncx2.sf(stats.chi2.ppf(1 - alfa, gl), gl, lam)


def bloque_c(N=41, k=6):
    p0 = k / N
    gl = N - 1
    p("\n" + "=" * 92)
    p(f"C. OMNIBUS CHI-CUADRADO DE FRECUENCIAS, JUEGO {k} DE {N} (gl = {gl})")
    p("=" * 92)
    p("X^2 = sum (O_i - n k/N)^2 / (n k/N). Sin reposicion X^2 NO es chi2(N-1): X^2 ~ ((N-k)/(N-1)) chi2(N-1).")
    p(f"Factor (N-k)/(N-1) = {(N - k) / (N - 1):.4f}. Estadistico corregido J = (N-1) X^2/(N-k) ~ chi2(N-1).")
    crit = stats.chi2.ppf(1 - ALFA, gl)
    p(f"Si se usa X^2 sin corregir contra chi2({gl}) al 5 %, el nivel real es "
      f"{stats.chi2.sf(crit * (N - 1) / (N - k), gl):.4f} (prueba conservadora, pierde potencia).")
    p("\nEfecto w de Cohen sobre la distribucion por bolilla extraida (pi_i/k frente a 1/N):")
    p("  w^2 = sum (pi_i/k - 1/N)^2 / (1/N) = (N/k^2) sum (pi_i - k/N)^2")
    p("No centralidad (derivacion propia, alternativa local): lambda = n k w^2 (N-1)/(N-k)")
    p("  => n = lambda(gl, alfa, potencia) (N-k) / [ (N-1) k w^2 ]   (n en sorteos)")
    for a in [ALFA, ALFA / 10, ALFA / 1000]:
        p(f"  lambda necesaria, gl={gl}, alfa={a:g}, potencia 0,8: {lambda_necesaria(gl, a):.3f}")

    p("\n  C.1 Una sola bolilla sesgada, las otras compensan: w = delta / sqrt(N-1)")
    p(f"  {'delta':>6} {'w':>8} {'n (alfa 0,05)':>14} {'anios':>8} {'n (alfa 0,005)':>15} {'anios':>8} {'n 1 bolilla prerreg.':>21}")
    for d in SESGOS:
        w = d / math.sqrt(N - 1)
        fila = []
        for a in [ALFA, ALFA / 10]:
            n = lambda_necesaria(gl, a) * (N - k) / ((N - 1) * k * w * w)
            fila.append(n)
        nb = n_binomial(p0, d, ALFA)
        p(f"  {d:>6.0%} {w:>8.5f} {fmt(math.ceil(fila[0])):>14} {fila[0] / SORTEOS_POR_ANIO:>8.1f} "
          f"{fmt(math.ceil(fila[1])):>15} {fila[1] / SORTEOS_POR_ANIO:>8.1f} {fmt(math.ceil(nb)):>21}")

    p("\n  C.2 Sesgo difuso: 20 bolillas con +delta y 20 con -delta (w = delta sqrt(40/41))")
    p(f"  {'delta':>6} {'w':>8} {'n (alfa 0,05)':>14} {'anios':>8}")
    for d in SESGOS:
        w = d * math.sqrt((N - 1) / N)
        n = lambda_necesaria(gl, ALFA) * (N - k) / ((N - 1) * k * w * w)
        p(f"  {d:>6.0%} {w:>8.5f} {fmt(math.ceil(n)):>14} {n / SORTEOS_POR_ANIO:>8.1f}")

    p("\n  C.3 Convenciones de Cohen (w pequeno 0,1; mediano 0,3; grande 0,5), alfa 0,05:")
    p(f"  {'w':>6} {'n sorteos':>10} {'bolillas':>9} {'anios':>7}")
    for w in [0.02, 0.05, 0.1, 0.3, 0.5]:
        n = lambda_necesaria(gl, ALFA) * (N - k) / ((N - 1) * k * w * w)
        p(f"  {w:>6.2f} {fmt(math.ceil(n)):>10} {fmt(math.ceil(n) * k):>9} {n / SORTEOS_POR_ANIO:>7.1f}")


# ----------------------------------------------------------------------------------------
# D. Potencia con historias realistas y sesgo minimo detectable
# ----------------------------------------------------------------------------------------
def potencia_una_bolilla(n, p0, delta, alfa):
    p1 = p0 * (1 + delta)
    za = stats.norm.ppf(1 - alfa / 2)
    num = abs(p1 - p0) * math.sqrt(n) - za * math.sqrt(p0 * (1 - p0))
    return stats.norm.cdf(num / math.sqrt(p1 * (1 - p1)))


def bloque_d(N=41, k=6):
    p0 = k / N
    p("\n" + "=" * 92)
    p(f"D. POTENCIA ALCANZABLE CON HISTORIAS REALISTAS, JUEGO {k} DE {N}")
    p("=" * 92)
    historias = [150, 750, 1500, 3000, 6000]
    p("  Potencia de la prueba de UNA bolilla prerregistrada (alfa 0,05 bilateral) / Bonferroni 41 /")
    p("  omnibus J (alfa 0,05), para una sola bolilla sesgada:")
    p(f"  {'sorteos':>8} {'anios':>6} | " + " | ".join(f"delta {d:>4.0%}: 1bol  Bonf  omni" for d in SESGOS))
    for n in historias:
        celdas = []
        for d in SESGOS:
            a = potencia_una_bolilla(n, p0, d, ALFA)
            b = potencia_una_bolilla(n, p0, d, ALFA / N)
            c = potencia_omnibus(n, N, k, d / math.sqrt(N - 1), ALFA)
            celdas.append(f"            {a:5.3f} {b:5.3f} {c:5.3f}")
        p(f"  {fmt(n):>8} {n / SORTEOS_POR_ANIO:>6.0f} | " + " | ".join(celdas))

    p("\n  Sesgo relativo minimo detectable (potencia 0,8):")
    p(f"  {'sorteos':>8} {'anios':>6} {'1 bolilla a=0,05':>17} {'Bonferroni 41':>14} {'omnibus J a=0,05':>17}")
    for n in historias:
        d1 = optimize.brentq(lambda d: potencia_una_bolilla(n, p0, d, ALFA) - POTENCIA, 1e-4, 5)
        d2 = optimize.brentq(lambda d: potencia_una_bolilla(n, p0, d, ALFA / N) - POTENCIA, 1e-4, 5)
        d3 = optimize.brentq(lambda d: potencia_omnibus(n, N, k, d / math.sqrt(N - 1), ALFA) - POTENCIA, 1e-4, 5)
        p(f"  {fmt(n):>8} {n / SORTEOS_POR_ANIO:>6.0f} {d1:>17.1%} {d2:>14.1%} {d3:>17.1%}")
    p("  (un sesgo relativo del 10 % equivale a pasar de 14,63 % a 16,10 % de aparicion por sorteo)")


# ----------------------------------------------------------------------------------------
# E. Predictibilidad: ganancia de informacion
# ----------------------------------------------------------------------------------------
def bloque_e(N=41, k=6):
    p0 = k / N
    so, _ = bits_por_sorteo(N, k)
    p("\n" + "=" * 92)
    p(f"E. PREDICTIBILIDAD FRENTE A LA LINEA BASE UNIFORME, JUEGO {k} DE {N}")
    p("=" * 92)
    p("Pronosticador ORACULO: conoce cual bolilla esta sesgada y cuanto (cota superior de lo lograble).")
    p("Evento pronosticado: la bolilla aparece o no en el sorteo. Ganancia esperada de log-verosimilitud")
    p("por sorteo = divergencia KL( Bernoulli(p1) || Bernoulli(p0) ).")
    p("  n_LR  : sorteos para rechazar H0 'el azar es uniforme' con la razon de verosimilitud (unilateral,")
    p("          alfa 0,05, potencia 0,8); coincide con la binomial unilateral.")
    p("  n_DM  : sorteos para que una prueba tipo Diebold-Mariano rechace H0 'igual perdida esperada'")
    p("          n = (z_a + z_b)^2 Var(d) / E(d)^2, con d = diferencia de log-loss por sorteo.")
    p("  n_e   : tiempo esperado de parada de la martingala de prueba (e-proceso) al umbral 1/alfa = 20:")
    p("          ln(20)/KL (aproximacion de Wald; valida en cualquier momento, sin n fijo).")
    p(f"  {'delta':>6} {'KL nats':>10} {'bits/sorteo':>12} {'% de entropia':>14} {'n_LR':>9} {'n_DM':>10} {'n_e':>9} {'Brier skill':>12}")
    za, zb = stats.norm.ppf(1 - ALFA), stats.norm.ppf(POTENCIA)
    for d in SESGOS:
        p1 = p0 * (1 + d)
        kl = p1 * math.log(p1 / p0) + (1 - p1) * math.log((1 - p1) / (1 - p0))
        # momentos de d_t = log q(x)/u(x) bajo H1
        a, b = math.log(p1 / p0), math.log((1 - p1) / (1 - p0))
        media = p1 * a + (1 - p1) * b
        var = p1 * a * a + (1 - p1) * b * b - media ** 2
        n_dm = (za + zb) ** 2 * var / media ** 2
        n_lr = n_binomial(p0, d, ALFA, bilateral=False)
        n_e = math.log(1 / ALFA) / kl
        # Brier: mejora esperada (p1-p0)^2 sobre la referencia p0 q0 + (p1-p0)^2 -> skill score
        bss = (p1 - p0) ** 2 / (p1 * (1 - p1) + (p1 - p0) ** 2)
        p(f"  {d:>6.0%} {kl:>10.3e} {kl / math.log(2):>12.3e} {kl / math.log(2) / so:>14.2e} "
          f"{fmt(math.ceil(n_lr)):>9} {fmt(math.ceil(n_dm)):>10} {fmt(math.ceil(n_e)):>9} {bss:>12.2e}")
    p(f"  (entropia de un sorteo {k} de {N} sin orden: {so:.2f} bits; '% de entropia' = bits ganados / entropia)")
    p("  n_DM ~ 4 n_LR: la prueba de 'igual precision' es mas exigente porque, si el azar fuera uniforme,")
    p("  el modelo sesgado PIERDE KL por sorteo; la distancia entre hipotesis es 2 KL, no KL.")


# ----------------------------------------------------------------------------------------
# F. Monte Carlo
# ----------------------------------------------------------------------------------------
def peso_para_inclusion(N, k, pi_objetivo):
    """Extraccion sucesiva (Plackett-Luce): bolilla 1 con peso a, resto peso 1.
       P(no sale en k extracciones) = prod_{j=0}^{k-1} (N-1-j)/(a+N-1-j)."""
    def f(a):
        return 1 - math.prod((N - 1 - j) / (a + N - 1 - j) for j in range(k)) - pi_objetivo
    return optimize.brentq(f, 0.01, 100)


def simular_conteos(rng, n, N, k, peso1, reps):
    """Devuelve matriz reps x N con el numero de apariciones de cada bolilla en n sorteos.
       Truco Gumbel-top-k: equivale a extraer sin reposicion con probabilidad proporcional al peso."""
    logw = np.zeros(N)
    logw[0] = math.log(peso1)
    conteos = np.zeros((reps, N), dtype=np.int64)
    filas = np.arange(reps)[:, None]
    for _ in range(n):
        claves = logw + rng.gumbel(size=(reps, N))
        idx = np.argpartition(-claves, k - 1, axis=1)[:, :k]
        np.add.at(conteos, (filas, idx), 1)
    return conteos


def bloque_f(N=41, k=6):
    p0 = k / N
    gl = N - 1
    rng = np.random.default_rng(SEMILLA)
    p("\n" + "=" * 92)
    p(f"F. COMPROBACION MONTE CARLO, JUEGO {k} DE {N} (semilla {SEMILLA})")
    p("=" * 92)
    crit = stats.chi2.ppf(1 - ALFA, gl)
    reps = 4000

    n0 = 1500
    c = simular_conteos(rng, n0, N, k, 1.0, reps)
    x2 = ((c - n0 * p0) ** 2).sum(axis=1) / (n0 * p0)
    j = x2 * (N - 1) / (N - k)
    ee = math.sqrt(0.05 * 0.95 / reps)
    p(f"  H0 cierta, n = {n0} sorteos, {reps} replicas (error estandar MC ~ {ee:.4f}):")
    p(f"    media de X^2 = {x2.mean():.2f} (teoria {(N - k):.2f}; chi2 ingenua esperaria {gl})")
    p(f"    rechazo de X^2 sin corregir al 5 % = {(x2 > crit).mean():.4f} "
      f"(teoria {stats.chi2.sf(crit * (N - 1) / (N - k), gl):.4f})")
    p(f"    rechazo de J corregido al 5 %      = {(j > crit).mean():.4f} (teoria 0,0500)")
    z = (c[:, 0] - n0 * p0) / math.sqrt(n0 * p0 * (1 - p0))
    p(f"    rechazo binomial de la bolilla 1   = {(np.abs(z) > stats.norm.ppf(0.975)).mean():.4f} (teoria 0,0500)")

    for d in [0.20, 0.10]:
        peso = peso_para_inclusion(N, k, p0 * (1 + d))
        n1 = int(math.ceil(n_binomial(p0, d, ALFA)))
        w = d / math.sqrt(N - 1)
        n2 = int(math.ceil(lambda_necesaria(gl, ALFA) * (N - k) / ((N - 1) * k * w * w)))
        r = 2000
        c1 = simular_conteos(rng, n1, N, k, peso, r)
        z = (c1[:, 0] - n1 * p0) / math.sqrt(n1 * p0 * (1 - p0))
        pot1 = (np.abs(z) > stats.norm.ppf(0.975)).mean()
        c2 = simular_conteos(rng, n2, N, k, peso, r)
        j = ((c2 - n2 * p0) ** 2).sum(axis=1) / (n2 * p0) * (N - 1) / (N - k)
        pot2 = (j > crit).mean()
        p(f"  H1: bolilla 1 con sesgo de inclusion +{d:.0%} (peso de extraccion {peso:.4f}), {r} replicas:")
        p(f"    una bolilla, n = {fmt(n1)}: potencia simulada {pot1:.3f} (objetivo 0,80)")
        p(f"    omnibus J,   n = {fmt(n2)}: potencia simulada {pot2:.3f} (objetivo 0,80)")
        p(f"    frecuencia observada de la bolilla 1: {c2[:, 0].mean() / n2:.5f} (objetivo {p0 * (1 + d):.5f})")


def main():
    p("potencia.py - tamano muestral y potencia para sesgo en sorteos sin reposicion")
    p(f"python {sys.version.split()[0]}, numpy {np.__version__}, scipy {__import__('scipy').__version__}")
    bloque_a()
    bloque_b()
    bloque_c()
    bloque_d()
    bloque_e()
    bloque_f()
    p("\n" + "=" * 92)
    p("ANEXO: mismo calculo de una bolilla y omnibus para el juego 14 de 25")
    p("=" * 92)
    N, k = 25, 14
    p0 = k / N
    p(f"p0 = {p0:.3f}; factor de correccion (N-k)/(N-1) = {(N - k) / (N - 1):.4f}")
    p(f"  {'delta':>6} {'n 1 bolilla a=0,05':>19} {'anios':>7} {'n Bonferroni 25':>16} {'anios':>7} {'n omnibus J':>12} {'anios':>7}")
    for d in SESGOS:
        n1 = n_binomial(p0, d, ALFA)
        n2 = n_binomial(p0, d, ALFA / N)
        # una bolilla sesgada: lambda = n delta^2 p0/q0  (misma derivacion que en C.1)
        n3 = lambda_necesaria(N - 1, ALFA) * (1 - p0) / (d * d * p0)
        p(f"  {d:>6.0%} {fmt(math.ceil(n1)):>19} {n1 / SORTEOS_POR_ANIO:>7.1f} {fmt(math.ceil(n2)):>16} "
          f"{n2 / SORTEOS_POR_ANIO:>7.1f} {fmt(math.ceil(n3)):>12} {n3 / SORTEOS_POR_ANIO:>7.1f}")

    destino = os.path.join(os.path.dirname(os.path.abspath(__file__)), "potencia_salida.txt")
    with open(destino, "w", encoding="utf-8") as fh:
        fh.write(_buf.getvalue())


if __name__ == "__main__":
    main()
