# 03 · Pruebas de aleatoriedad: cómo distinguir correlación accidental, sesgo persistente y predictibilidad genuina

Autor del apartado: estadístico metodólogo y criptógrafo del concilio. Fecha de consulta de todas las fuentes: 2026-10-09.
Cálculos: `F:\MACI\14_INVESTIGACION\azar_fisico\analisis\potencia.py` y su salida `potencia_salida.txt` (Python 3.14.7, numpy 2.5.2, scipy 1.18.1, semilla fija).

Convención de este documento: **[H]** = hecho documentado en una fuente abierta en esta sesión; **[I]** = inferencia o derivación mía. Los números de tamaño muestral son cálculo propio y están reproducidos por el guion.

---

## 1. Síntesis

1. **[H]** NIST SP 800-22 Rev. 1a (abril de 2010) define 15 pruebas para **secuencias binarias largas**. Los mínimos por secuencia van de 100 bits (frecuencia, rachas, sumas acumuladas) a 1 000 000 de bits (plantillas solapadas, complejidad lineal, excursiones aleatorias); además exige al menos 55 secuencias para la prueba de uniformidad de valores p y recomienda un número de secuencias del orden del inverso de alfa (alfa entre 0,001 y 0,01).
2. **[H]** El 19 de abril de 2022 NIST decidió **revisar** (no retirar) SP 800-22 Rev. 1a; entre los objetivos declarados está «rechazar su uso para evaluar generadores criptográficos de números aleatorios». El aviso decía que la preparación del borrador no había comenzado. Al 2026-10-09 la página oficial de la publicación solo muestra esa nota de planificación de 2022 y la página de noticias del proyecto RBG no registra ninguna Rev. 2 ni borrador: **no encontré Rev. 2** (ausencia de hallazgo, no prueba de inexistencia).
3. **[H]** NIST SP 800-90B (enero de 2018) estima **min-entropía** de una fuente de ruido con 1 000 000 de muestras consecutivas más una matriz de 1000 reinicios por 1000 muestras; decide entre vía IID (11 estadísticos de permutación con 10 000 permutaciones, más pruebas chi-cuadrado y de subcadena repetida más larga) y vía no IID (mínimo de 10 estimadores, tres de ellos solo para datos binarios); define dos pruebas de salud continuas (conteo de repeticiones y proporción adaptativa con ventana 1024 o 512, alfa típico 2^-20). Nota de planificación del 29-05-2025: dos erratas pendientes de una futura revisión.
4. **[H]** Las críticas publicadas a 800-22 incluyen: parámetros erróneos en la prueba espectral y en la de Lempel-Ziv (Kim, Umeno y Hasegawa 2004; Hamano 2005), errores de aproximación en las pruebas basadas en la binomial (Pareschi, Rovatti y Setti 2012), ambigüedad en la interpretación —datos verdaderamente aleatorios fallan al menos una prueba con probabilidad cercana a 80 %— (Sýs y otros 2015), dependencia entre pruebas (Doğanaksoy y otros 2017; Georgescu y otros 2017) y la objeción de fondo de Saarinen (2022): los generadores más débiles las pasan, por lo que dan falsa confianza.
5. **[I]** Una historia realista de sorteos es **diminuta** en bits: un sorteo 6 de 41 aporta como máximo 22,10 bits (31,59 con orden de salida); 150 sorteos al año son 3315 bits; 20 años, 66 301 bits. Una sola secuencia de 10^6 bits exige 302 años; la estrategia completa de 800-22 (1000 secuencias) exige unos 300 000 años; el millón de muestras de 800-90B exige 1111 años contando bolillas.
6. **[I]** Por tanto las baterías de bits (800-22, Dieharder, TestU01, PractRand, ENT) **no son aplicables** como tales a una extracción mecánica. Lo trasladable son las *ideas*: prueba de permutación con varios estadísticos (90B §5.1), chi-cuadrado de frecuencia e independencia (90B §5.2), estimador del valor más común con cota de confianza (90B §6.3.1), pruebas de salud como monitoreo secuencial, y la exigencia —común a 90B y a AIS 20/31— de un **modelo estocástico de la fuente física** en vez de pruebas de caja negra.
7. **[H]** Para sorteos sin reposición el estadístico de Pearson no sigue chi-cuadrado: para bolillas individuales hay que usar J = (N−1)·X²/(N−k) (Joe 1993), y para pares o subconjuntos mayores la distribución límite es una suma ponderada de chi-cuadrados con pesos explícitos (Genest, Lockhart y Stephens 2002). **[I]** En 6 de 41 el factor es 35/40 = 0,875; usar X² sin corregir baja el nivel real de 5 % a 1 % y pierde potencia (confirmado por simulación: 0,92 %).
8. **[I]** Números centrales (potencia 0,8, alfa 0,05 bilateral, juego 6 de 41, n en sorteos): detectar un sesgo relativo en UNA bolilla **prerregistrada** requiere 458 987 sorteos para 1 %, 18 539 para 5 %, 4689 para 10 % y 1198 para 20 %. Si la bolilla no estaba fijada de antemano (Bonferroni sobre 41): 970 741, 39 090, 9851 y 2500. Con la prueba ómnibus J: 1 607 505, 64 301, 16 076 y 4019.
9. **[I]** A 150 sorteos por año eso significa: con 20 años de historia (3000 sorteos) el sesgo mínimo detectable con potencia 0,8 es 12,5 % (bolilla prerregistrada), 18,2 % (Bonferroni 41) o 23,1 % (ómnibus). Sesgos del 1 % al 5 % son **indetectables** con cualquier historia existente; sesgos del 10 % solo con hipótesis fijada de antemano y más de 30 años.
10. **[I]** Una desviación «significativa» hallada tras explorar frecuencias, pares, rachas, posiciones y ventanas de tiempo es, con alta probabilidad, correlación accidental: la corrección adecuada no es solo por 41 bolillas sino por todo el jardín de análisis posibles (Gelman y Loken 2013; White 2000).
11. **[I]** Sesgo persistente y predictibilidad genuina se distinguen solo **prospectivamente**: hipótesis y regla de pronóstico congeladas antes de observar, puntuación con regla propia (log-loss) frente a la línea base uniforme y prueba válida en cualquier momento (martingala de prueba / e-valores: Shafer 2021; Ramdas y otros 2023).
12. **[I]** Incluso un oráculo que conociera la bolilla sesgada y su magnitud ganaría 0,0047 bits por sorteo con un sesgo del 20 % (0,02 % de los 22,1 bits del sorteo) y necesitaría unos 920 a 950 sorteos para demostrarlo; con 1 %, unos 350 000.
13. **[I]** Una prueba tipo Diebold-Mariano de «igual precisión» necesita cerca de 4 veces más sorteos que la razón de verosimilitud contra la uniforme, porque bajo azar ideal el modelo sesgado pierde KL por sorteo: la distancia entre hipótesis es 2·KL.
14. **[I]** La conclusión metodológica: con datos públicos de resultados, la única vía con potencia razonable es la **hipótesis física específica** (una máquina, un juego de bolillas, una bolilla con masa o diámetro medidos fuera de tolerancia), porque reduce la familia de comparaciones a una y permite pruebas unilaterales.

---

## 2. Aplicable / no aplicable a extracción mecánica

Supuesto del análisis **[I]**: historia de 150 sorteos por año; juego 6 de 41 (22,10 bits por sorteo sin orden, 31,59 con orden). «Años» = años de sorteos necesarios para reunir UNA secuencia del tamaño mínimo (sin orden / con orden), calculado en `potencia.py` bloque A. Convertir sorteos a bits insesgados exige numerar la combinación y rechazar índices ≥ 2^22 (se aprovecha 93,3 % de los sorteos): cualquier codificación directa (número de bolilla en binario) introduce sesgo artificial que la batería detectaría como defecto del generador.

### 2.1 NIST SP 800-22 Rev. 1a — las 15 pruebas

Los mínimos son **[H]** (sección 2.x.7 «Input Size Recommendation» de cada prueba, leída en el PDF oficial). La columna de veredicto es **[I]**.

| # | Prueba (sección) | Mínimo documentado [H] | Años para una secuencia [I] | Veredicto [I] | Motivo |
|---|---|---|---|---|---|
| 1 | Frequency (Monobit) (2.1) | n ≥ 100 | < 0,1 | Idea trasladable, prueba no | La idea (proporción de símbolos) se sustituye por el chi-cuadrado de frecuencias corregido J; aplicarla a bits codificados solo mide la codificación |
| 2 | Frequency within a Block (2.2) | n ≥ 100; M ≥ 20, M > 0,01·n, N < 100 | < 0,1 | Idea trasladable | Equivale a homogeneidad de frecuencias por bloques de tiempo (deriva); hacerlo sobre conteos de bolillas, no sobre bits |
| 3 | Runs (2.3) | n ≥ 100 | < 0,1 | Idea trasladable | Rachas de aparición/no aparición de una bolilla entre sorteos; requiere la distribución exacta con p0 = k/N, no 1/2 |
| 4 | Longest Run of Ones in a Block (2.4) | n ≥ 128 (M = 8); 6272 (M = 128); 750 000 (M = 10^4) | < 0,1 / 1,9 / 226 | No aplicable | Tablas de probabilidad precalculadas para bits con p = 1/2; sin análogo útil |
| 5 | Binary Matrix Rank (2.5) | n ≥ 38 912 (38 matrices 32×32) | 11,7 / 8,2 | No aplicable | Dependencia lineal sobre GF(2): defecto propio de generadores algorítmicos (registros de desplazamiento) |
| 6 | Discrete Fourier Transform (Spectral) (2.6) | n ≥ 1000 | 0,3 / 0,2 | No aplicable como está | Busca periodicidad en bits; para sorteos la periodicidad se prueba con periodograma de conteos por bolilla y datos sustitutos. Además es la prueba con más errores documentados (Kim y otros 2004; Hamano 2005; Okada y Fukushima 2023) |
| 7 | Non-overlapping Template Matching (2.7) | m = 9 o 10; N ≤ 100; M > 0,01·n (ejemplos con n = 10^6) | del orden de 300 | No aplicable | Patrones de 9–10 bits; con miles de bits no hay ocurrencias esperadas suficientes |
| 8 | Overlapping Template Matching (2.8) | n ≥ 10^6 | 302 / 211 | No aplicable | Tamaño |
| 9 | Maurer's «Universal Statistical» (2.9) | n ≥ 387 840 (L = 6) | 117 / 82 | No aplicable | Tamaño; mide compresibilidad de bits |
| 10 | Linear Complexity (2.10) | n ≥ 10^6; 500 ≤ M ≤ 5000; N ≥ 200 | 302 / 211 | No aplicable | Específica de LFSR; sin significado físico en un bombo |
| 11 | Serial (2.11) | m < log2(n) − 2 | — | Idea trasladable | Frecuencia de m-gramas → prueba de pares y tríos de bolillas con pesos de Genest y otros (2002) |
| 12 | Approximate Entropy (2.12) | m < log2(n) − 5 | — | No aplicable | Con n ≈ 66 000 bits (20 años) solo admite m ≤ 10 bits, menos que un sorteo |
| 13 | Cumulative Sums (2.13) | n ≥ 100 | < 0,1 | Idea trasladable | CUSUM de (aparece − p0) por bolilla: detección de deriva o cambio de régimen; es el puente natural a las pruebas secuenciales |
| 14 | Random Excursions (2.14) | n ≥ 10^6 | 302 / 211 | No aplicable | Tamaño |
| 15 | Random Excursions Variant (2.15) | n ≥ 10^6 | 302 / 211 | No aplicable | Tamaño |
| — | Estrategia §4.2: proporción de secuencias que pasan y uniformidad de valores p | ≥ 55 secuencias; muestra del orden de 1/alfa; alfa ∈ [0,001; 0,01] | 55 × 10^6 bits = 16 591 años; 1000 × 10^6 = 301 655 años | No aplicable; la idea de «prueba de dos niveles» sí | Con varios juegos o varias máquinas se puede examinar la distribución de valores p entre unidades, sabiendo que serán pocas |

### 2.2 NIST SP 800-90B — componentes

| Componente (sección) | Qué exige [H] | Veredicto [I] | Motivo |
|---|---|---|---|
| Recolección de datos (3.1.1) | ≥ 1 000 000 de muestras consecutivas de la fuente de ruido; se permiten concatenaciones de tramos de ≥ 1000 muestras; matriz de reinicio 1000 × 1000 | No aplicable | 1111 años contando bolillas; 6667 contando sorteos |
| Reducción de alfabeto (3.1.3, 6.4) | Alfabeto > 256 se reduce a ≤ 256 símbolos | Compatible | N = 41 o 25 cabe sin reducción si la muestra es la bolilla; si la muestra es el sorteo (4,5 millones de combinaciones) no |
| Supuesto de muestras de la misma distribución | Fuente estacionaria que emite símbolos de un alfabeto fijo | **Violado por construcción** | Dentro de un sorteo no hay reposición: la segunda bolilla no puede repetir la primera. La unidad IID plausible es el sorteo completo, no la bolilla |
| Pruebas de permutación IID (5.1): excursión, número y longitud de rachas direccionales, aumentos y descensos, rachas respecto de la mediana (número y longitud), colisión media y máxima, periodicidad, covarianza, compresión | 10 000 permutaciones Fisher-Yates; se rechaza IID si el rango del estadístico original es extremo (error tipo I 0,001 por estadístico) | **Método trasladable; es lo más útil de 90B** | Permutar el orden de los **sorteos** (no de las bolillas) deja intacta la estructura sin reposición y prueba intercambiabilidad temporal. Los estadísticos de periodicidad y covarianza a rezagos 1, 2, 8, 16, 32 se adaptan a conteos por bolilla. Los de colisión requieren redefinirse (dentro de un sorteo no hay colisiones) |
| Chi-cuadrado de independencia y bondad de ajuste, datos no binarios (5.2.1, 5.2.2) | Independencia de pares consecutivos; homogeneidad entre 10 subconjuntos | Trasladable con corrección | Hay que usar la covarianza sin reposición (Joe 1993; Genest y otros 2002); los pares consecutivos dentro de un sorteo no pueden coincidir |
| Subcadena repetida más larga (5.2.5) | Falla si Pr(X ≥ 1) < 0,001 | Trasladable como curiosidad | Análogo: repetición de combinaciones completas o de k−1 bolillas entre sorteos (problema del cumpleaños); potencia casi nula |
| Vía IID: estimador del valor más común (6.1, 6.3.1) | Cota superior de confianza de la proporción más frecuente; H = −log2(p_u) | **Trasladable** | Responde la pregunta correcta: ¿cuál es la mayor probabilidad compatible con los datos para la bolilla más frecuente? Con L pequeño la cota es ancha y lo dice honestamente |
| Vía no IID: colisión, Markov, compresión (6.3.2–6.3.4) | Solo se aplican a entradas binarias | No aplicable | Lo dice la norma |
| Vía no IID: t-tupla y LRS (6.3.5, 6.3.6) | Frecuencia de tuplas repetidas | No aplicable | Tamaño; las tuplas no se repiten con miles de símbolos |
| Estimadores predictores: MultiMCW, Lag, MultiMMC, LZ78Y (6.3.7–6.3.10) | Predicen la muestra siguiente y acotan la min-entropía por la tasa de aciertos global y local | **Idea trasladable; es exactamente la medida de predictibilidad** | Ventanas de 63 a 4095 muestras en MultiMCW; con 150 sorteos al año el predictor aprende casi nada. La idea (medir entropía por lo que un predictor acierta) se conserva en la sección 5 con log-loss y e-valores |
| Pruebas de reinicio (3.1.4) | Las muestras tras reinicio vienen de la misma distribución, sin dependencia de la posición | **Idea trasladable** | Cada sorteo es un «reinicio» de la máquina: la matriz sorteo × posición de extracción permite la prueba por filas y por columnas (¿la primera bolilla se distribuye igual que la sexta?) |
| Prueba de salud: conteo de repeticiones (4.4.1) | Corte C = 1 + ⌈−log2(alfa)/H⌉ | No aplicable literalmente | Dentro del sorteo no hay repeticiones. Análogo: racha de sorteos consecutivos con la misma bolilla; con p0 = 0,146 y alfa = 2^-20 el corte sería C = 1 + ⌈20/2,78⌉ = 9 apariciones seguidas |
| Prueba de salud: proporción adaptativa (4.4.2) | Ventana W = 1024 (binaria) o 512 (no binaria); alfa recomendado entre 2^-20 y 2^-40 | Idea trasladable | Es monitoreo secuencial de frecuencia; W = 512 bolillas son 85 sorteos. Mejor implementarla como e-proceso (sección 3, prueba 11) |
| Componente de acondicionamiento (3.1.5) | Funciones vetadas (hash, cifrado) sobre la salida cruda | No aplicable | Un sorteo no posprocesa |
| Requisito de análisis de la fuente (3.2.2) | El solicitante debe justificar su estimación de entropía con un análisis de la fuente de ruido | **Trasladable y central** | Coincide con AIS 20/31: sin modelo físico del bombo, las pruebas de caja negra no certifican nada |

### 2.3 Otras baterías

| Batería | Fuente verificada | Qué es [H] | Aplicabilidad a sorteos [I] |
|---|---|---|---|
| Diehard / Dieharder | Página de R. G. Brown (Duke); Marsaglia y Tsang 2002 | Dieharder (GPL, sobre GSL) reimplementa las pruebas Diehard de Marsaglia, añade Monobit, Runs y Serial de STS y pruebas propias; Diehard trabajaba con unos diez millones de números; con archivos, Dieharder rebobina y reutiliza datos, lo que distorsiona los valores p | No aplicable: órdenes de magnitud más datos de los disponibles; alimentarla con un archivo corto produce valores p inválidos por rebobinado |
| TestU01 | L'Ecuyer y Simard 2007, ACM TOMS 33(4) | Biblioteca en C con baterías SmallCrush (10 pruebas), Crush (96) y BigCrush (106); la variante de SmallCrush por archivo pide algo menos de 51 320 000 números | No aplicable por tamaño. Sí es la mejor referencia conceptual: clasifica pruebas (frecuencia, serial, colisiones, espaciamientos de cumpleaños, huecos, permutaciones) con su teoría |
| PractRand | Página del proyecto en SourceForge | Batería para generadores rápidos, sin tope de tamaño; se usa a escala de gigabytes a terabytes | No aplicable |
| ENT | J. Walker, fourmilab.ch (página fechada 28-01-2008) | Calcula entropía por byte, chi-cuadrado, media aritmética, estimación Monte Carlo de pi y coeficiente de correlación serial | Las cinco medidas tienen análogo trivial, pero trabaja sobre bytes y sin corrección por no reposición: no usar el programa, sí las ideas de chi-cuadrado y correlación serial |
| AIS 20/31 (BSI) | BSI, «A proposal for: Functionality classes for random number generators», versión 3.0, 17-09-2024 | Criterios de evaluación para generadores deterministas (AIS 20) y físicos (AIS 31) en el esquema alemán de Common Criteria; referencia matemático-técnica actualizada; NIST IR 8446 (borrador, 09-2024) compara su terminología y requisitos con la serie SP 800-90 | Las pruebas estadísticas no son aplicables por tamaño; el **principio** sí: se exige un modelo estocástico de la fuente física y pruebas en línea, que es justo lo que falta en un análisis de lotería basado solo en resultados |

---

## 3. Batería recomendada para sorteos sin reposición

Todo este apartado es **[I]** salvo donde se cita. Notación: N bolillas, k extraídas por sorteo, n sorteos, p0 = k/N, O_i = número de sorteos en que aparece la bolilla i.

**Regla general de calibración.** La hipótesis nula (k bolillas equiprobables sin reposición, sorteos independientes) se simula exactamente y a costo despreciable. Para cualquier estadístico T, el valor p de Monte Carlo es p = (b + 1)/(m + 1), con b simulaciones tan extremas como lo observado entre m (Phipson y Smyth 2010: nunca cero). Esto evita depender de aproximaciones asintóticas con n pequeño y resuelve de paso las celdas con esperados bajos.

| # | Prueba | Estadístico y distribución nula | Qué desviación detecta | Notas |
|---|---|---|---|---|
| 1 | Frecuencia por bolilla (ómnibus) | X² = Σ (O_i − n·p0)² / (n·p0); **J = (N−1)·X²/(N−k) ~ χ²(N−1)** [H: Joe 1993, citado y confirmado en Genest y otros 2002] | Bolillas favorecidas o desfavorecidas | En 6 de 41 el factor es 0,875; sin corregir el nivel real cae a 0,0099. Simulación propia: media de X² = 34,89 (teoría 35), rechazo de J = 0,047 |
| 2 | Frecuencia de pares (y tríos) | X² sobre C(N,2) celdas; límite = w1·χ²(N−1) + w2·χ²(N(N−3)/2) con pesos explícitos [H: Genest y otros 2002, ec. 3]; aproximación por transformación lineal de una χ² o Imhof | Bolillas que «salen juntas» (adherencia, carga contigua) | En 6 de 41 hay 820 pares con esperado n·15/820 = 0,0183·n: se necesitan n ≥ 274 para esperado 5; usar Monte Carlo. Genest y otros la aplican a 1798 sorteos del Lotto 6/49 de Canadá sin hallar desviación (p = 0,104 para c = 1; 0,300 para c = 2) |
| 3 | Posición de extracción | Tabla bolilla × posición (N × k): la primera bolilla es multinomial(1/N) clásica, χ²(N−1) sin corrección; homogeneidad entre posiciones por permutación dentro de cada sorteo | Efecto del orden de carga o de la dinámica inicial del bombo | Solo si se publica el orden real de salida. Es la prueba con mejor motivación física y equivale a la prueba de reinicio de 90B |
| 4 | Independencia serial entre sorteos | Solapamiento S_t = \|sorteo_t ∩ sorteo_{t+L}\| ~ hipergeométrica(N, k, k), media k²/N (0,878 en 6 de 41); suma sobre t comparada con su distribución exacta o permutación del orden de los sorteos | Memoria entre sorteos (bolillas no remezcladas, mismo orden de carga) | Rezagos L = 1, 2, 3 y el rezago que corresponde a «misma máquina» o «mismo juego de bolillas»; fijar los rezagos antes de mirar |
| 5 | Tiempos de espera (huecos) | Hueco entre apariciones de la bolilla i ~ geométrica(p0); χ² con clases agrupadas o prueba de Kolmogorov-Smirnov discreta por simulación | Agrupamiento temporal, bolillas «calientes» o «frías» | Redundante con 1 si el sesgo es constante; añade potencia solo ante deriva. Es la prueba que más alimenta la falacia del jugador: prerregistrar |
| 6 | Rachas y CUSUM por bolilla | Suma acumulada de (indicador − p0); máximo comparado con simulación | Cambio de régimen (cambio de máquina, de bolillas, desgaste) | Con punto de cambio conocido por bitácora, sustituir por comparación antes/después (χ² de homogeneidad con corrección) |
| 7 | Covariables físicas | Regresión logística condicional o χ² de homogeneidad por máquina, juego de bolillas, operador, masa y diámetro medidos | Sesgo con causa identificable | La de mayor potencia por dato: una hipótesis, prueba unilateral. Requiere datos que no están en los resultados publicados |
| 8 | Estadísticos agregados (suma, paridad, bajos/altos, consecutivos) | Distribución exacta por enumeración o simulación | Nada que 1–2 no detecten | Incluir solo como control: son funciones de las frecuencias y multiplican comparaciones sin añadir potencia |
| 9 | Permutación de sorteos (marco 90B §5.1) | Reordenar los n sorteos 10 000 veces; estadísticos de periodicidad y covarianza a rezagos fijados | No intercambiabilidad temporal en general | Calibración exacta bajo intercambiabilidad sin suponer equiprobabilidad: separa «no uniforme pero estable» de «inestable» |
| 10 | Bayesiana | Primera bolilla: Dirichlet-multinomial (Mosimann 1962) con a priori simétrico; factor de Bayes contra la hipótesis puntual uniforme (Kass y Raftery 1995). Inclusión por bolilla: beta-binomial | Cuantifica evidencia **a favor** de la uniformidad, cosa que un valor p no hace | El resultado depende de la concentración a priori: informar una banda (p. ej. sesgos a priori de 1 %, 5 %, 20 %). Con n pequeño el factor de Bayes suele favorecer la nula aunque haya sesgo pequeño: decirlo |
| 11 | Secuencial válida en todo momento | Martingala de prueba: M_t = Π q_s(x_s)/u(x_s), con q_s predicción fijada antes del sorteo s y u la uniforme. Bajo H0, P(sup M_t ≥ 1/alfa) ≤ alfa (desigualdad de Ville). SPRT de Wald (1945) como caso con alternativa simple; e-valores combinables por promedio (Vovk y Wang 2021; Shafer 2021; Ramdas y otros 2023; Grünwald y otros 2024) | Sesgo persistente o predictibilidad, con monitoreo indefinido sin inflar el error | Es la herramienta correcta para un sistema que se observa sorteo a sorteo. La alternativa q_s puede ser una mezcla o un estimador «plug-in» con datos pasados |

**Orden de uso propuesto.** Primero 1, 3 y 4 (confirmatorias, prerregistradas, tres valores p con Holm). Después 2, 5, 6 y 9 como exploratorias declaradas. La 7 solo con datos físicos. La 11 en adelante, para toda afirmación de predictibilidad.

---

## 4. Comparaciones múltiples y validación

### 4.1 Tres afirmaciones distintas y qué evidencia exige cada una [I]

| Afirmación | Definición operativa | Evidencia mínima |
|---|---|---|
| Correlación accidental | Patrón en la muestra que no persiste | Es la hipótesis por defecto; se descarta solo con lo de las dos filas siguientes |
| Sesgo persistente | Probabilidades de inclusión π_i ≠ k/N estables en el tiempo | Rechazo con control del error por familia en una prueba prerregistrada **y** réplica en datos posteriores (o en otra mitad temporal no mirada) con el mismo signo |
| Predictibilidad genuina | Existe una regla, fijada antes de cada sorteo, cuya pérdida esperada con regla propia es menor que la de la uniforme | Martingala de prueba prospectiva que cruce 1/alfa, o diferencia de log-loss fuera de muestra con intervalo que excluya el cero |

Sesgo persistente implica predictibilidad (pequeña); lo inverso no: puede haber predictibilidad condicional (dependencia serial, estado inicial) con marginales uniformes. Por eso las pruebas de frecuencia no bastan para negar predictibilidad ni las de dependencia para negar sesgo.

### 4.2 Control del error

- **Bonferroni** (procedimiento formalizado en Dunn 1961): alfa/m. Para «alguna de las 41 bolillas» alfa = 0,00122; multiplica el n necesario por 2,1 respecto de la bolilla prerregistrada (cálculo propio, sección 5).
- **Holm (1979)**: secuencial descendente, controla el error por familia bajo cualquier dependencia y nunca es menos potente que Bonferroni. Recomendado para la familia confirmatoria.
- **Benjamini-Hochberg (1995)**: controla la tasa de falsos descubrimientos; válido bajo independencia o dependencia positiva; **Benjamini-Yekutieli (2001)** para dependencia arbitraria. **[I]** Los conteos por bolilla están negativamente correlacionados (suma fija n·k), así que para barridos de bolillas corresponde Benjamini-Yekutieli o Holm, no BH simple.
- **Tasa base**: la probabilidad previa de que un bombo auditado tenga un sesgo grande es baja, así que el valor predictivo positivo de un p < 0,05 aislado es pequeño (argumento general de Ioannidis 2005). **[I]** Con potencia de 0,2 —la que da la sección 5 para sesgos del 5 % con 20 años— y una previa de 1 en 100, un resultado «significativo» al 5 % es verdadero en torno al 4 % de las veces: 0,2·0,01 / (0,2·0,01 + 0,05·0,99).

### 4.3 Jardín de senderos que se bifurcan y «data snooping»

- **[H]** Gelman y Loken (2013): el problema de comparaciones múltiples aparece aunque el investigador haga un único análisis, si los detalles del análisis dependen de los datos. Simmons, Nelson y Simonsohn (2011) y Head y otros (2015) documentan la inflación de falsos positivos por flexibilidad analítica.
- **[I]** En loterías los senderos son: qué juego, qué periodo, con o sin comodín, bolilla o par o trío, frecuencia o hueco o racha, qué rezago, qué ventana móvil, qué umbral de «caliente». Diez decisiones binarias dan 1024 análisis; a alfa 0,05 se esperan 51 «hallazgos» bajo azar ideal. La tabla de la sección 5 incluye por eso la fila de 1000 hipótesis.
- **[H]** White (2000) formaliza la corrección cuando se elige el mejor de muchos modelos de pronóstico sobre los mismos datos (prueba por remuestreo del máximo); Hansen (2005) la refina (capacidad predictiva superior); Romano y Wolf (2005) dan la versión escalonada. **[I]** Son la herramienta adecuada cuando se comparan muchas «estrategias» de predicción contra la uniforme: el valor p debe ser el del máximo, no el del ganador.
- **Datos sustitutos** [H: Theiler y otros 1992; Schreiber y Schmitz 2000]: se generan series que cumplen la nula y conservan propiedades elegidas de los datos, y se compara un estadístico discriminante. **[I]** Para sorteos hay tres niveles útiles: (a) sorteos simulados uniformes (nula completa); (b) permutación del orden de los sorteos (conserva frecuencias, destruye dinámica temporal: aísla dependencia serial del sesgo marginal); (c) permutación de etiquetas de bolilla dentro de cada sorteo (conserva tiempos, destruye identidad). Un «patrón» que sobrevive en (b) es marginal, no dinámico; uno que desaparece en (b) pero no en (a) es temporal.

### 4.4 Protocolo de validación [I]

1. **Prerregistro** (Nosek y otros 2018): hipótesis, estadístico, familia de comparaciones, alfa, regla de parada y código, con sello de tiempo, antes de descargar los datos de validación.
2. **Partición temporal**: exploración con el tramo antiguo; confirmación con el tramo reciente no mirado. Nunca partición aleatoria (mezcla regímenes de máquina).
3. **Controles negativos**: correr toda la tubería sobre sorteos simulados uniformes (debe rechazar ≈ alfa) y sobre sorteos simulados con sesgo conocido (debe recuperar la potencia de la sección 5). El bloque F de `potencia.py` es ese control para las pruebas 1 y de una bolilla.
4. **Validación prospectiva**: pronósticos emitidos y registrados antes de cada sorteo; evaluación con log-loss y martingala de prueba.
5. **Informe**: todas las pruebas hechas, no solo las significativas; tamaños de efecto con intervalo; potencia alcanzada.

---

## 5. Tamaño muestral y potencia

Todo cálculo propio **[I]**; fórmulas estándar (aproximación normal de una proporción; chi-cuadrado no central; efecto w de Cohen 1988). Salida completa en `potencia_salida.txt`. Juego 6 de 41: p0 = 6/41 = 0,14634. Sesgo relativo δ: p1 = p0·(1 + δ). **n está en sorteos**; años a 150 sorteos por año.

### 5.1 Fórmulas

- **Una bolilla (binomial, bilateral):** n = [ z(1−α/2)·√(p0·q0) + z(pot)·√(p1·q1) ]² / (p1 − p0)². Aproximación útil: n ≈ (z(1−α/2) + z(pot))² · q0 / (δ²·p0) = 7,85 · 5,83 / δ² ≈ 45,8/δ² para α = 0,05.
- **Ómnibus J:** bajo H0, J ~ χ²(N−1). Bajo alternativa local, J ~ χ² no central con **λ = n·k·w²·(N−1)/(N−k)**, donde w² = Σ (π_i/k − 1/N)² / (1/N) es el efecto de Cohen sobre la distribución por bolilla extraída. Entonces n = λ(gl, α, pot)·(N−k) / [(N−1)·k·w²]. La derivación de λ es mía (covarianza de los conteos sin reposición: Var = n·p0·q0, Cov = −n·p0·q0/(N−1)); la simulación la confirma (potencia 0,796 y 0,799 frente a 0,80 objetivo). Respecto de una multinomial ingenua con n·k observaciones, el muestreo sin reposición **mejora** la eficiencia en (N−1)/(N−k) = 1,143.
- **Una sola bolilla sesgada dentro del ómnibus:** w = δ/√(N−1) = δ/6,32 y λ = n·δ²·p0/q0. Un sesgo del 20 % en una bolilla es w = 0,032, tres veces menor que el «efecto pequeño» de Cohen (0,1).
- λ necesaria con 40 grados de libertad y potencia 0,8: 27,56 (α = 0,05); 40,01 (α = 0,005); 59,79 (α = 0,00005).

### 5.2 Sorteos necesarios (potencia 0,80)

| Sesgo relativo δ | p1 | Una bolilla prerregistrada, α = 0,05 | Una bolilla, Bonferroni 41 (α = 0,00122) | Una bolilla, Bonferroni 1000 (α = 0,00005) | Ómnibus J, α = 0,05 | Ómnibus J, α = 0,005 | Unilateral prerregistrada, α = 0,05 |
|---|---|---|---|---|---|---|---|
| 1 % | 0,14780 | 458 987 (3060 años) | 970 741 (6472 años) | 1 400 996 (9340 años) | 1 607 505 (10 717 años) | 2 333 952 (15 560 años) | 361 658 (2411 años) |
| 5 % | 0,15366 | 18 539 (124 años) | 39 090 (261 años) | 56 352 (376 años) | 64 301 (429 años) | 93 359 (622 años) | 14 625 (97,5 años) |
| 10 % | 0,16098 | 4689 (31,3 años) | 9851 (65,7 años) | 14 183 (94,5 años) | 16 076 (107 años) | 23 340 (156 años) | 3705 (24,7 años) |
| 20 % | 0,17561 | 1198 (8,0 años) | 2500 (16,7 años) | 3591 (23,9 años) | 4019 (26,8 años) | 5835 (38,9 años) | 949 (6,3 años) |

Comprobación con la binomial exacta en esos n: nivel real entre 0,045 y 0,050 y potencia entre 0,77 y 0,80 (la discreción resta hasta 3 puntos con n pequeño).

Sesgo difuso (20 bolillas con +δ y 20 con −δ, w ≈ δ): ómnibus J con α = 0,05 requiere 41 193 sorteos (1 %), 1648 (5 %), 412 (10 %) y 103 (20 %). **[I]** El ómnibus es eficiente contra sesgo repartido e ineficiente contra una sola bolilla; lo contrario vale para la prueba de una bolilla.

Por tamaño de efecto de Cohen (ómnibus J, α = 0,05): w = 0,02 → 10 047 sorteos; w = 0,05 → 1608; w = 0,10 → 402; w = 0,30 → 45; w = 0,50 → 17.

### 5.3 Potencia alcanzada con historias realistas (una sola bolilla sesgada)

Cada celda: prerregistrada α = 0,05 / Bonferroni 41 / ómnibus J.

| Sorteos (años) | δ = 1 % | δ = 5 % | δ = 10 % | δ = 20 % |
|---|---|---|---|---|
| 150 (1) | 0,029 / 0,001 / 0,050 | 0,047 / 0,002 / 0,051 | 0,081 / 0,004 / 0,053 | 0,190 / 0,020 / 0,064 |
| 750 (5) | 0,033 / 0,001 / 0,050 | 0,086 / 0,004 / 0,054 | 0,213 / 0,022 / 0,068 | 0,613 / 0,185 / 0,145 |
| 1500 (10) | 0,037 / 0,001 / 0,050 | 0,128 / 0,009 / 0,059 | 0,366 / 0,058 / 0,090 | 0,877 / 0,490 / 0,291 |
| 3000 (20) | 0,042 / 0,001 / 0,051 | 0,209 / 0,020 / 0,068 | 0,616 / 0,176 / 0,145 | 0,992 / 0,887 / 0,626 |
| 6000 (40) | 0,051 / 0,002 / 0,051 | 0,363 / 0,055 / 0,090 | 0,885 / 0,490 / 0,291 | 1,000 / 0,998 / 0,960 |

Sesgo relativo mínimo detectable con potencia 0,8:

| Sorteos (años) | Una bolilla prerregistrada | Bonferroni 41 | Ómnibus J |
|---|---|---|---|
| 150 (1) | 58,5 % | 84,6 % | 103,5 % |
| 750 (5) | 25,4 % | 36,9 % | 46,3 % |
| 1500 (10) | 17,8 % | 25,9 % | 32,7 % |
| 3000 (20) | 12,5 % | 18,2 % | 23,1 % |
| 6000 (40) | 8,8 % | 12,8 % | 16,4 % |

Lectura: con un año de datos ninguna prueba distingue un sesgo menor que 58 % de la uniformidad. Un resultado «no significativo» con 150 sorteos no dice nada sobre la equidad del bombo, y uno «significativo» hallado explorando es casi con certeza accidental.

### 5.4 Predictibilidad: ganancia de información y sorteos para demostrarla

Pronosticador oráculo (conoce la bolilla sesgada y su magnitud: cota superior de lo alcanzable). Evento: la bolilla aparece o no en el sorteo.

- **Log-loss**: L = −log q(x). Ganancia esperada sobre la uniforme = KL(p1 ‖ p0) por sorteo. **Brier**: (q − x)²; mejora esperada (p1 − p0)². Ambas son reglas propias: el mínimo esperado se alcanza declarando la probabilidad verdadera (Brier 1950; Gneiting y Raftery 2007).
- **Diebold-Mariano (1995)**: d_t = L_uniforme − L_modelo; estadístico = media(d)/√(varianza de largo plazo/n) → N(0,1) bajo igual precisión; corrección para muestras pequeñas de Harvey, Leybourne y Newbold (1997); versión condicional de Giacomini y White (2006). n ≈ (z_α + z_β)²·Var(d)/E(d)².
- **Intervalo de confianza de la mejora**: media(d) ± z·s_d/√n en nats por sorteo; dividir por ln 2 para bits. Informar siempre el intervalo, no solo el valor p.

| δ | KL (nats/sorteo) | Bits/sorteo | Fracción de los 22,1 bits | n razón de verosimilitud (unilateral) | n Diebold-Mariano | Parada esperada del e-proceso, ln(20)/KL | Brier skill |
|---|---|---|---|---|---|---|---|
| 1 % | 8,5·10^-6 | 1,2·10^-5 | 5,6·10^-7 | 361 658 | 1 450 541 | 350 466 | 1,7·10^-5 |
| 5 % | 2,1·10^-4 | 3,1·10^-4 | 1,4·10^-5 | 14 625 | 59 274 | 14 171 | 4,1·10^-4 |
| 10 % | 8,3·10^-4 | 1,2·10^-3 | 5,5·10^-5 | 3705 | 15 199 | 3590 | 1,6·10^-3 |
| 20 % | 3,3·10^-3 | 4,7·10^-3 | 2,1·10^-4 | 949 | 3982 | 920 | 5,9·10^-3 |

**[I]** Un modelo aprendido de los datos rinde menos que el oráculo y, mientras aprende, puede rendir peor que la uniforme: con 41 parámetros estimados de n sorteos, el costo esperado de estimación es del orden de (N−1)/(2n) nats por sorteo, que supera a la ganancia KL salvo que n ≫ (N−1)/(2·KL) (unos 6000 sorteos para δ = 20 %; unos 24 000 para δ = 10 %). Esta es la razón cuantitativa por la que los modelos de aprendizaje automático sobre historias de lotería no superan la línea base fuera de muestra.

### 5.5 Anexo: juego 14 de 25

p0 = 0,56; factor de corrección (N−k)/(N−1) = 0,4583 (usar X² sin corregir es aquí gravemente erróneo). Sorteos para potencia 0,8: una bolilla prerregistrada 61 617 / 2455 / 610 / 150 (δ = 1 / 5 / 10 / 20 %); Bonferroni 25: 121 394 / 4842 / 1205 / 297; ómnibus J: 176 677 / 7068 / 1767 / 442. Es más sensible que el 6 de 41 porque cada sorteo observa 14 de 25 bolillas.

---

## 6. Fuentes verificadas

Método: cada DOI se consultó en `https://api.crossref.org/works/<DOI>` en esta sesión; los documentos de NIST se descargaron de csrc.nist.gov / nvlpubs.nist.gov y se leyeron las secciones citadas; el resto se abrió en la página del editor o del autor.
Nivel de lectura: **TC** = texto completo (secciones pertinentes leídas); **R** = resumen leído; **M** = solo metadatos confirmados (autor, título, revista, año). **Advertencia:** en las fuentes M, la columna «qué aporta» refleja conocimiento general de la obra, no una lectura en esta sesión.

### 6.1 Normas y documentos oficiales

| # | Referencia | DOI o URL | Aporta | Limitaciones | Lectura |
|---|---|---|---|---|---|
| 1 | Rukhin, Soto, Nechvatal, Smid, Barker, Leigh, Levenson, Vangel, Banks, Heckert, Dray, Vo; rev. Bassham (2010). *A Statistical Test Suite for Random and Pseudorandom Number Generators for Cryptographic Applications*. NIST SP 800-22 Rev. 1a | 10.6028/NIST.SP.800-22r1a | Las 15 pruebas, sus mínimos de n y la estrategia de §4.2 | Solo bits; mínimos inalcanzables para sorteos; en revisión desde 2022 | TC |
| 2 | Turan, Barker, Kelsey, McKay, Baish, Boyle (2018). *Recommendation for the Entropy Sources Used for Random Bit Generation*. NIST SP 800-90B | 10.6028/NIST.SP.800-90B | Min-entropía, vías IID y no IID, pruebas de permutación, estimadores, pruebas de salud | Exige 10^6 muestras; supone símbolos de alfabeto fijo; dos erratas reconocidas (nota del 29-05-2025) | TC |
| 3 | NIST CSRC (19-04-2022). «Decision to Revise NIST SP 800-22 Rev. 1a» | https://csrc.nist.gov/news/2022/decision-to-revise-nist-sp-800-22-rev-1a | Decisión de revisar; objetivos; rechazo del uso para evaluar generadores criptográficos | No fija fecha; el borrador no había comenzado | TC |
| 4 | NIST CSRC. Página de la publicación SP 800-22 Rev. 1a y noticias del proyecto Random Bit Generation | https://csrc.nist.gov/pubs/sp/800/22/r1/upd1/final ; https://csrc.nist.gov/Projects/Random-Bit-Generation/news | Estado al 2026-10-09: nota de planificación de 2022; sin noticias de 2025–2026; sin Rev. 2 | Ausencia de noticia no prueba ausencia de borrador | TC |
| 5 | Barker y otros (2024). *Bridging the Gap between Standards on Random Number Generation* (NIST IR 8446, borrador público inicial) | 10.6028/NIST.IR.8446.ipd | Comparación SP 800-90 con AIS 20/31 | Borrador; no confirmé versión final | M |
| 6 | Roginsky, Sönmez Turan, Buller, Kaufer (2023). *Discussion on the Full Entropy Assumption of the SP 800-90 Series* (NIST IR 8427) | 10.6028/NIST.IR.8427 | Contexto de la serie 90 | Tangencial a sorteos | M |
| 7 | BSI (17-09-2024). *A proposal for: Functionality classes for random number generators*, versión 3.0 (AIS 20 / AIS 31) | https://bsi.bund.de/SharedDocs/Downloads/EN/BSI/Certification/Interpretations/AIS_31_Functionality_classes_for_random_number_generators_e_2024.html | Criterios de evaluación de generadores deterministas y físicos; exigencia de modelo estocástico | La página no lista autores; no leí el PDF de 6 MB | R |

### 6.2 Críticas a las baterías

| # | Referencia | DOI o URL | Aporta | Limitaciones | Lectura |
|---|---|---|---|---|---|
| 8 | Kim, Umeno, Hasegawa (2004). «Corrections of the NIST Statistical Test Suite for Randomness». IACR ePrint 2004/018 | https://eprint.iacr.org/2004/018 | Parámetros incorrectos en la prueba espectral y en la de Lempel-Ziv; cuatro correcciones | Preimpresión; anterior a Rev. 1a (que ya no incluye Lempel-Ziv entre las 15) | R |
| 9 | Hamano (2005). «The Distribution of the Spectrum for the Discrete Fourier Transform Test Included in SP800-22». IEICE Trans. Fundamentals E88-A(1), 67–73 | 10.1093/ietfec/e88-a.1.67 | Distribución correcta del estadístico espectral | — | M |
| 10 | Pareschi, Rovatti, Setti (2012). «On Statistical Tests for Randomness Included in the NIST SP800-22 Test Suite and Based on the Binomial Distribution». IEEE TIFS 7(2), 491–505 | 10.1109/TIFS.2012.2185227 | Errores de aproximación en pruebas basadas en la binomial | — | M |
| 11 | Sýs, Říha, Matyáš, Márton, Suciu (2015). «On the interpretation of results from the NIST statistical test suite». Romanian J. Information Science and Technology 18(1), 18–32 | https://www.muni.cz/en/research/publications/1322353 | Datos aleatorios fallan al menos una prueba con probabilidad cercana a 80 %; umbrales de cuántas fallas tolerar | Calibrado con un generador cuántico concreto | R |
| 12 | Doğanaksoy, Sulak, Uğuz, Şeker, Akcengiz (2017). «Mutual correlation of NIST statistical randomness tests and comparison of their sensitivities on transformed sequences». Turkish J. Elec. Eng. & Comp. Sci. 25, 655–665 | 10.3906/elk-1503-214 | Correlación entre pruebas de la batería | — | M |
| 13 | Georgescu, Simion, Nita, Toma (2017). «A view on NIST randomness tests (In)Dependence». ECAI 2017 | 10.1109/ECAI.2017.8166460 | Dependencia entre pruebas | Actas | M |
| 14 | Sulak, Doğanaksoy, Ege, Koçak (2010). «Evaluation of Randomness Test Results for Short Sequences». LNCS (SETA 2010), 309–319 | 10.1007/978-3-642-15874-2_27 | Tratamiento de secuencias cortas | «Corto» sigue siendo cientos de bits por secuencia y muchas secuencias | M |
| 15 | Saarinen (2022). «SP 800-22 and GM/T 0005-2012 Tests: Clearly Obsolete, Possibly Harmful». IACR ePrint 2022/169; SSR 2022 | https://eprint.iacr.org/2022/169 | Los generadores más débiles pasan la batería; pide retirar 800-22; propone modelar la fuente | Posición argumentativa | R |
| 16 | Okada, Fukushima (2023). «Revisiting the DFT Test in the NIST SP 800-22 Randomness Test Suite». ICISSP 2023, 366–372 | 10.5220/0011626300003405 | La prueba espectral sigue en discusión | Actas | M |
| 17 | Zhu, Ma, Chen, Lin, Jing (2017). «Analysis and Improvement of Entropy Estimators in NIST SP 800-90B for Non-IID Entropy Sources». IACR ToSC 2017(3), 151–168 | 10.46586/tosc.v2017.i3.151-168 | Análisis de los estimadores no IID | Sobre el borrador previo a la versión final | M |
| 18 | Kelsey, McKay, Sönmez Turan (2015). «Predictive Models for Min-entropy Estimation». CHES 2015, LNCS, 373–392 | 10.1007/978-3-662-48324-4_19 | Origen de los estimadores predictores de 90B | — | M |
| 19 | Hurley-Smith, Hernandez-Castro (2018). «Certifiably Biased: An In-Depth Analysis of a Common Criteria EAL4+ Certified TRNG». IEEE TIFS 13(4), 1031–1041 | 10.1109/TIFS.2017.2777342 | Un generador certificado con sesgo detectable: pasar baterías no garantiza | Caso único | M |

### 6.3 Otras baterías

| # | Referencia | DOI o URL | Aporta | Limitaciones | Lectura |
|---|---|---|---|---|---|
| 20 | L'Ecuyer, Simard (2007). «TestU01: A C library for empirical testing of random number generators». ACM TOMS 33(4), art. 22, 1–40 | 10.1145/1268776.1268777 | Biblioteca y baterías SmallCrush, Crush, BigCrush | Crossref registra el título abreviado «TestU01»; tamaños de Crush y BigCrush no confirmados (ver §7) | M |
| 21 | Marsaglia, Tsang (2002). «Some Difficult-to-Pass Tests of Randomness». J. Statistical Software 7(3) | 10.18637/jss.v007.i03 | Pruebas posteriores a Diehard | — | M |
| 22 | Brown, R. G. (con Eddelbuettel y Bauer). *Dieharder: A Random Number Test Suite*, v. 3.31.1 | https://webhome.phy.duke.edu/~rgb/General/dieharder.php | Contenido de la batería; advertencia sobre rebobinado de archivos | Página con versiones inconsistentes | TC (página) |
| 23 | Walker, J. (2008). *ENT: A Pseudorandom Number Sequence Test Program* | https://www.fourmilab.ch/random/ | Las cinco medidas | Opera sobre bytes | TC (página) |
| 24 | *PractRand* (proyecto en SourceForge) | https://pracrand.sourceforge.net/ | Existencia y propósito | La página abierta solo tiene el índice; autor y detalles en §7 | R |
| 25 | Maurer (1992). «A universal statistical test for random bit generators». J. Cryptology 5(2), 89–105 | 10.1007/BF00193563 | Base de la prueba 9 de 800-22 | — | M |
| 26 | Good, Gover (1967). «The Generalized Serial Test and the Binary Expansion of √2». JRSS A 130(1), 102 | 10.2307/2344040 | Base de la prueba serial | — | M |

### 6.4 Sorteos sin reposición, exactas, bayesianas y secuenciales

| # | Referencia | DOI o URL | Aporta | Limitaciones | Lectura |
|---|---|---|---|---|---|
| 27 | Joe (1993). «Tests of uniformity for sets of lotto numbers». Statistics & Probability Letters 16(3), 181–188 | 10.1016/0167-7152(93)90141-5 | Estadísticos chi-cuadrado para márgenes de k-tuplas; la fórmula habitual de Pearson no es apropiada | Texto completo no accesible (403); la forma J = (N−1)X²/(N−k) la tomo de la cita en Genest y otros | R |
| 28 | Genest, Lockhart, Stephens (2002). «χ² and the lottery». The Statistician (JRSS D) 51(2), 243–257 | 10.1111/1467-9884.00315 ; https://www.sfu.ca/~lockhart/Research/Papers/GenestLockhartStephensJRSSD02.pdf | X² es suma ponderada de χ² para subconjuntos de tamaño c; pesos explícitos; aplicación a 1798 sorteos del Lotto 6/49 | No considera el orden de salida; advierte que la dependencia entre los X² de distinto c dificulta el ajuste por multiplicidad | TC |
| 29 | Mosimann (1962). «On the compound multinomial distribution, the multivariate β-distribution, and correlations among proportions». Biometrika 49(1–2), 65–82 | 10.1093/biomet/49.1-2.65 | Dirichlet-multinomial | — | M |
| 30 | Kass, Raftery (1995). «Bayes Factors». JASA 90(430), 773–795 | 10.1080/01621459.1995.10476572 | Factores de Bayes e interpretación | Sensibles al a priori | M |
| 31 | Wald (1945). «Sequential Tests of Statistical Hypotheses». Ann. Math. Statist. 16(2), 117–186 | 10.1214/aoms/1177731118 | SPRT | Alternativa simple | M |
| 32 | Shafer (2021). «Testing by Betting: A Strategy for Statistical and Scientific Communication». JRSS A 184(2), 407–431 | 10.1111/rssa.12647 | Prueba como apuesta; capital como evidencia | — | M |
| 33 | Vovk, Wang (2021). «E-values: Calibration, combination and applications». Ann. Statist. 49(3), 1736–1754 | 10.1214/20-AOS2020 | Combinación de e-valores | — | M |
| 34 | Ramdas, Grünwald, Vovk, Shafer (2023). «Game-Theoretic Statistics and Safe Anytime-Valid Inference». Statistical Science 38(4), 576–601 | 10.1214/23-STS894 | Revisión de inferencia válida en todo momento | — | M |
| 35 | Grünwald, de Heide, Koolen (2024). «Safe testing». JRSS B 86(5), 1091–1128 | 10.1093/jrsssb/qkae011 | E-variables óptimas | — | M |
| 36 | Waudby-Smith, Ramdas (2024; en línea 2023). «Estimating means of bounded random variables by betting». JRSS B 86(1), 1–27 | 10.1093/jrsssb/qkad009 | Sucesiones de confianza por apuestas | — | M |
| 37 | Phipson, Smyth (2010). «Permutation P-values Should Never Be Zero: Calculating Exact P-values When Permutations Are Randomly Drawn». Stat. Appl. Genet. Mol. Biol. 9(1) | 10.2202/1544-6115.1585 | p = (b+1)/(m+1) | — | M |

### 6.5 Comparaciones múltiples, senderos que se bifurcan, datos sustitutos

| # | Referencia | DOI o URL | Aporta | Limitaciones | Lectura |
|---|---|---|---|---|---|
| 38 | Dunn (1961). «Multiple Comparisons among Means». JASA 56(293), 52–64 | 10.1080/01621459.1961.10482090 | Uso de la desigualdad de Bonferroni | — | M |
| 39 | Holm (1979). «A Simple Sequentially Rejective Multiple Test Procedure». Scand. J. Statist. 6(2), 65–70 | JSTOR 4615733 (sin DOI) | Procedimiento escalonado | Confirmado por búsqueda, no por Crossref | M |
| 40 | Benjamini, Hochberg (1995). «Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing». JRSS B 57(1), 289–300 | 10.1111/j.2517-6161.1995.tb02031.x | Tasa de falsos descubrimientos | Supone independencia o dependencia positiva | M |
| 41 | Benjamini, Yekutieli (2001). «The control of the false discovery rate in multiple testing under dependency». Ann. Statist. 29(4) | 10.1214/aos/1013699998 | Dependencia arbitraria | Más conservador | M |
| 42 | Theiler, Eubank, Longtin, Galdrikian, Farmer (1992). «Testing for nonlinearity in time series: the method of surrogate data». Physica D 58(1–4), 77–94 | 10.1016/0167-2789(92)90102-S | Método de datos sustitutos | Diseñado para series continuas | M |
| 43 | Schreiber, Schmitz (2000). «Surrogate time series». Physica D 142(3–4), 346–382 | 10.1016/S0167-2789(00)00043-9 | Revisión y sustitutos restringidos | — | M |
| 44 | Gelman, Loken (14-11-2013). «The garden of forking paths: Why multiple comparisons can be a problem, even when there is no "fishing expedition" or "p-hacking" and the research hypothesis was posited ahead of time» | https://sites.stat.columbia.edu/gelman/research/unpublished/p_hacking.pdf | Multiplicidad sin búsqueda consciente | Manuscrito no publicado | R (texto abierto; leí resumen e introducción) |
| 45 | Gelman, Loken (2014). «The Statistical Crisis in Science». American Scientist 102(6), 460 | 10.1511/2014.111.460 | Versión publicada del argumento | Divulgación | M |
| 46 | White (2000). «A Reality Check for Data Snooping». Econometrica 68(5), 1097–1126 | 10.1111/1468-0262.00152 | Prueba del mejor modelo entre muchos | — | M |
| 47 | Hansen (2005). «A Test for Superior Predictive Ability». JBES 23(4), 365–380 | 10.1198/073500105000000063 | Refinamiento de White | — | M |
| 48 | Romano, Wolf (2005). «Stepwise Multiple Testing as Formalized Data Snooping». Econometrica 73(4), 1237–1282 | 10.1111/j.1468-0262.2005.00615.x | Versión escalonada | — | M |
| 49 | Simmons, Nelson, Simonsohn (2011). «False-Positive Psychology». Psychological Science 22(11), 1359–1366 | 10.1177/0956797611417632 | Grados de libertad del investigador | Crossref registra solo el título corto | M |
| 50 | Head, Holman, Lanfear, Kahn, Jennions (2015). «The Extent and Consequences of P-Hacking in Science». PLOS Biology 13(3), e1002106 | 10.1371/journal.pbio.1002106 | Evidencia de p-hacking | — | M |
| 51 | Nosek, Ebersole, DeHaven, Mellor (2018). «The preregistration revolution». PNAS 115(11), 2600–2606 | 10.1073/pnas.1708274114 | Prerregistro | — | M |
| 52 | Ioannidis (2005). «Why Most Published Research Findings Are False». PLoS Medicine 2(8), e124 | 10.1371/journal.pmed.0020124 | Tasa base y valor predictivo positivo | Modelo simplificado | M |

### 6.6 Predictibilidad y potencia

| # | Referencia | DOI o URL | Aporta | Limitaciones | Lectura |
|---|---|---|---|---|---|
| 53 | Gneiting, Raftery (2007). «Strictly Proper Scoring Rules, Prediction, and Estimation». JASA 102(477), 359–378 | 10.1198/016214506000001437 | Teoría de reglas propias | — | M |
| 54 | Brier (1950). «Verification of Forecasts Expressed in Terms of Probability». Monthly Weather Review 78(1), 1–3 | 10.1175/1520-0493(1950)078<0001:VOFEIT>2.0.CO;2 | Puntuación de Brier | — | M |
| 55 | Diebold, Mariano (1995). «Comparing Predictive Accuracy». JBES 13(3), 253–263 | 10.1080/07350015.1995.10524599 | Prueba de igual precisión | Asintótica; supone estacionariedad de la diferencia de pérdidas | M |
| 56 | Harvey, Leybourne, Newbold (1997). «Testing the equality of prediction mean squared errors». Int. J. Forecasting 13(2), 281–291 | 10.1016/S0169-2070(96)00719-4 | Corrección para muestras pequeñas | — | M |
| 57 | Giacomini, White (2006). «Tests of Conditional Predictive Ability». Econometrica 74(6), 1545–1578 | 10.1111/j.1468-0262.2006.00718.x | Versión condicional, válida con modelos estimados | — | M |
| 58 | Cohen (1988; reimpresión Routledge 2013). *Statistical Power Analysis for the Behavioral Sciences*, 2.ª ed. | 10.4324/9780203771587 | Efecto w y convenciones 0,1 / 0,3 / 0,5 | Convenciones pensadas para ciencias del comportamiento | M |

Total verificadas: **58** (TC: 7; R: 7; M: 44).

---

## 7. No verificadas

Afirmaciones o referencias que NO confirmé en esta sesión; no deben citarse sin comprobación.

1. **Borrador o Rev. 2 de SP 800-22.** No hallé ninguno en las páginas oficiales al 2026-10-09. No revisé el repositorio de borradores completo de CSRC ni el Federal Register; puede existir trabajo interno no anunciado.
2. **Versión final de NIST IR 8446.** Solo confirmé el borrador público inicial de septiembre de 2024.
3. **Erratas de SP 800-90B (nota del 29-05-2025).** Confirmé que existen dos; no leí el PDF de erratas ni sé a qué secciones afectan.
4. **Marsaglia, G. (1995). *The Marsaglia Random Number CDROM including the Diehard Battery of Tests of Randomness*.** Referencia original de Diehard; no localizada en fuente primaria (solo a través de Dieharder).
5. **Autoría y detalles internos de PractRand** (atribuido habitualmente a Chris Doty-Humphrey; umbrales de falla; tamaños). La búsqueda no confirmó el autor.
6. **Tamaños de muestra de Crush y BigCrush de TestU01** (se suele citar del orden de 2^35 y 2^38 números). La búsqueda no los confirmó; solo confirmé el número de pruebas (10, 96, 106) y el tamaño de SmallCrush por archivo, este último por documentación de terceros.
7. **Procedimientos de prueba de AIS 31 (T0–T8, procedimientos A y B) y sus tamaños de muestra.** No leí el PDF de la versión 3.0.
8. **Pesos de Genest, Lockhart y Stephens para c ≥ 2.** Leí el artículo y confirmo que existen y sus multiplicidades (N−1 y N(N−3)/2 para pares), pero la extracción de texto dañó las fórmulas; no las transcribo. Usar el PDF original o calibrar por Monte Carlo.
9. **Referencias citadas dentro de Genest y otros (2002) que no abrí:** Stern y Cover (1989), Bellhouse (1982), Imhof (1961), Rao y Scott (1987). Corresponden además al agente de literatura de loterías.
10. **Bonferroni (1936)**, publicación original de la desigualdad; cito a Dunn (1961) en su lugar.
11. **Ville (1939)**, origen de la desigualdad usada en la prueba 11; la tomo como resultado estándar descrito en las fuentes 32–35, que solo verifiqué por metadatos.
12. **Contenido detallado de las 44 fuentes marcadas M.** Confirmé que existen y sus datos bibliográficos; lo que digo que aportan es conocimiento general de esas obras.
13. **Texto completo de Joe (1993).** El editor devolvió 403; solo resumen y cita secundaria.
14. **Costo de estimación (N−1)/(2n) nats por sorteo** de la sección 5.4: es la aproximación asintótica habitual del exceso de log-loss de un estimador de máxima verosimilitud con N−1 parámetros; inferencia mía, no simulada en `potencia.py`.
15. **Afirmación de que Rev. 1 de 800-22 eliminó la prueba de Lempel-Ziv.** Confirmé que Rev. 1a no la incluye entre sus 15 pruebas; no abrí la versión de 2001 para confirmar que estaba.
