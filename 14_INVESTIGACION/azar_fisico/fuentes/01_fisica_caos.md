# 01 — Física experimental y dinámica no lineal: sistemas mecánicos «aleatorios», sesgo y límites de la predicción

Fecha de la búsqueda: 2026-10-09. Autor: agente físico experimental del concilio.
Alcance: monedas, dados, ruleta, tablero de Galton, billares, péndulo doble, esferas duras y flujo granular; conceptos de aleatoriedad, caos y entropía. Fuera de alcance (lo cubren otros agentes): lotería y sesgos de sorteo, NIST y baterías de pruebas, aprendizaje automático e instrumentación, caso chileno.

Cómo se verificó: cada referencia de la sección 2 se confirmó en esta sesión contra la API de Crossref (metadatos) y, cuando fue posible, contra OpenAlex (resumen) o el texto completo en arXiv o en un PDF abierto. La columna «Leído» dice hasta dónde llegó la lectura. Lo que afirmo de una fuente de la que solo vi metadatos va marcado como «no leído» y no debe citarse como resultado sin abrir el original.

Convención de etiquetas en el texto:
- **[HECHO]** dato documentado en la fuente leída.
- **[EXP]** resultado experimental medido por los autores.
- **[INF]** inferencia mía a partir de las fuentes (cálculo o lectura propia).
- **[HIP]** hipótesis no contrastada.

---

## 1. Síntesis

1. Ningún dispositivo mecánico de azar estudiado con rigor (moneda, dado, ruleta, tablero de Galton) es «intrínsecamente aleatorio»: todos son deterministas y su azar aparente proviene de la incertidumbre sobre las condiciones iniciales, amplificada por la dinámica [HECHO: F1, F2, F5, F8, F9, F10].
2. Hay que separar dos fenómenos que la literatura popular confunde: **sesgo estadístico** (la distribución de resultados no es uniforme) y **predictibilidad de la tirada individual** (se anticipa un resultado concreto midiendo el estado inicial). El primero se detecta con muchas repeticiones; el segundo exige instrumentación en tiempo real.
3. Sesgo medido en moneda: la probabilidad de caer del mismo lado del que partió es 0,508 (IC 95 % 0,506–0,509) en 350.757 lanzamientos de 48 personas [EXP: F3], coincidente con la predicción de 0,51 del modelo con precesión [F2]. No hay sesgo cara/sello (0,500). El efecto varía mucho entre personas y decae con la práctica.
4. Sesgo medido en dados: 12 dados de plástico corrientes, 26.306 tiradas automatizadas (315.672 resultados), frecuencias entre 0,1651 y 0,1688 por cara, χ² = 25,0, p = 0,00014; la causa medida es geométrica (eje 1–6 un 0,2 % más corto), no el peso de las marcas [EXP: F13].
5. Los sesgos reales son pequeños (del orden de 0,2 a 0,8 puntos porcentuales) y requieren del orden de 10⁵ repeticiones para detectarse: 250.000 lanzamientos estimados para la moneda [F2], 270.939 tiradas para el dado [F13].
6. Predicción de tirada individual lograda: ruleta. Con una cámara a 90 cuadros/s sobre una rueda de casino, 700 ensayos muestran desviaciones significativas respecto del azar en la casilla predicha [EXP: F6]; con cronometraje manual, 13 aciertos de mitad de rueda en 22 ensayos (p < 0,15, evidencia débil) [EXP: F6]. Thorp y Shannon declararon +44 % de ganancia esperada con su computador de 1961 [relato del autor: F7].
7. La ruleta es predecible porque tiene una fase larga, lenta y casi regular (bola en el riel) y solo una fase corta de dispersión (deflectores y separadores). La predicción termina donde empiezan las colisiones [HECHO: F6].
8. En dados y monedas que rebotan, las fronteras entre cuencas de atracción se afinan con cada rebote; con disipación el número de rebotes es finito, de modo que el sistema es pseudoaleatorio y no caótico en sentido estricto [F8, F9, F10, F11]. La cara inicialmente más baja del dado es la más probable [modelo y experimento con cámara a 1.500 cuadros/s: F9].
9. Para la moneda sin rebote las fronteras entre cuencas son suaves (no fractales) y no hay divergencia exponencial; la impredecibilidad práctica viene de que las bandas son estrechas frente a la precisión de la mano [F5, F10]. Una máquina lanzadora produce 100 % de caras [HECHO: F2].
10. En sistemas de muchas esferas duras la situación es cualitativamente distinta: cada colisión entre superficies convexas multiplica el error por un factor del orden de (1 + 2ℓ/r) [F17], el exponente de Lyapunov máximo escala con la frecuencia de colisión [F20, F21] y el horizonte de predicción crece solo con el logaritmo de la precisión inicial [F23, F24].
11. Límite físico duro: para bolas de billar reales la incertidumbre cuántica domina tras unas 8 colisiones según una estimación [teoría: F17], con un antecedente de 1967 [F18]. Es un argumento de plausibilidad, no una medición.
12. Ejemplo medido de horizonte corto: péndulo doble con λ = 7,5 ± 1,5 s⁻¹ [EXP: F25]; mejorar diez veces la medición inicial añade solo 0,3 s de predicción [INF].
13. Los materiales granulares no se mezclan «hacia el azar» sin más: diferencias pequeñas de tamaño o densidad producen segregación sistemática [F28, F29]. Esto es la vía física por la que una bolilla distinta podría tener una probabilidad distinta [HIP: no encontré medición en máquinas de sorteo].
14. Vacío central: no encontré ningún trabajo revisado por pares que mida exponentes de Lyapunov, horizonte de predicción o sensibilidad a masa y restitución en una máquina de extracción de bolillas. Todo lo que se diga de esas máquinas desde esta literatura es extrapolación.
15. Conclusión operativa [INF]: en un sistema de muchas esferas agitadas, la vía realista para detectar desviaciones es estadística (sesgo por propiedades físicas de las bolillas o del mecanismo), no la predicción de la extracción individual, salvo que exista una fase final lenta y regular comparable al riel de la ruleta.

---

## 2. Tabla de fuentes verificadas

Niveles de evidencia: **ER** experimento replicado de forma independiente; **EU** experimento único; **SIM** simulación; **TEO** teoría o modelo analítico; **REV** revisión; **REL** relato.
Lectura: **TC** texto completo; **RES** solo resumen; **MET** solo metadatos (Crossref/OpenAlex); **SEC** contenido conocido por fuente secundaria leída en esta sesión.

### 2.1 Moneda

| # | Referencia | DOI / URL | Método | Resultado principal | Limitaciones | Ev. | Leído |
|---|---|---|---|---|---|---|---|
| F1 | Keller, J. B. (1986). «The Probability of Heads». *The American Mathematical Monthly* 93(3), 191–197. | 10.1080/00029890.1986.11971784 | Teoría (moneda que gira sobre un eje en su plano, sin rebote) | En el límite de velocidad y giro grandes, la probabilidad de cara tiende a 1/2 (según lo resume F2). | Sin precesión, sin rebote, sin aire. | TEO | MET + SEC (descrito en F2) |
| F2 | Diaconis, P., Holmes, S., Montgomery, R. (2007). «Dynamical Bias in the Coin Toss». *SIAM Review* 49(2), 211–235. | 10.1137/S0036144504446436; PDF: stat.berkeley.edu/~aldous/157/Papers/diaconis_coinbias.pdf | Teoría + experimento (cinta adherida a la moneda; cámara rápida, filmado a unos 600 cuadros/s) | La moneda atrapada en la mano tiende a caer como partió; la probabilidad depende de un solo parámetro, el ángulo ψ entre la normal y el momento angular. De 50 lanzamientos filmados, 27 útiles: probabilidades entre 0,500 y 0,545, mediana 0,5027, desviación 0,0125, media 0,508 (redondeada a 0,51). Una máquina lanzadora da 100 % de caras. Detectar el sesgo requeriría 250.000 lanzamientos. | Solo 27 lanzamientos medidos; supone inicio exactamente «cara arriba» y captura sin rebote; los autores señalan que con rebote el análisis no aplica. | TEO + EU | TC |
| F3 | Bartoš, F. et al. (50 autores; último: Wagenmakers, E.-J.) (2025). «Fair Coins Tend to Land on the Same Side They Started: Evidence from 350,757 Flips». *Journal of the American Statistical Association* 120(552), 2118–2127. | 10.1080/01621459.2025.2516210; arXiv:2310.04153 (v4, 2025) | Experimento masivo; 48 personas, 44 combinaciones de moneda y denominación; análisis bayesiano jerárquico | 178.079 de 350.757 caen del mismo lado: 0,5077 (IC 95 % 0,5060–0,5094); modelo jerárquico: 0,508 [0,506–0,509], BF = 2359. Cara/sello: 0,500 [0,498–0,502]. Fuerte heterogeneidad entre personas (de 0,487 a 0,601 por persona). El sesgo decae con la práctica. Sin los cuatro valores extremos: 0,5060. | Registro manual por los propios lanzadores (con filmación y auditoría); procedimiento «autocorrelacionado» (cada lanzamiento parte del lado en que cayó el anterior); no mide ψ; moneda atrapada en la mano, no rebota. | EU de gran tamaño; confirma la predicción de F2 | TC (preimpresión v4) |
| F4 | Vulović, V. Z., Prange, R. E. (1986). «Randomness of a true coin toss». *Physical Review A* 33(1), 576. | 10.1103/PhysRevA.33.576 | Modelo numérico con rebote | El azar de la moneda lo fija la estructura de las cuencas de atracción de cara y sello; la moneda no es intrínsecamente aleatoria: su azar efectivo depende de la escala de variación de las cuencas frente a la precisión del mecanismo de lanzamiento. | Modelo bidimensional; sin validación experimental en el resumen. | SIM | RES |
| F5 | Strzałko, J., Grabski, J., Stefański, A., Perlikowski, P., Kapitaniak, T. (2008). «Dynamics of coin tossing is predictable». *Physics Reports* 469(2), 59–92. | 10.1016/j.physrep.2008.08.003 | Modelo mecánico tridimensional + simulación | El resultado queda fijado por las condiciones iniciales; sin divergencia exponencial ni fronteras fractales; las fronteras entre cuencas son suaves, pero una condición típica queda tan cerca de una frontera que un error pequeño cambia el resultado. | Resumen conocido por el anuncio de un seminario del autor (Univ. de Aberdeen, 6-feb-2009), no por la página del editor. | SIM + TEO | MET + SEC |
| F5b | Strzałko, J. et al. (2010). «Understanding Coin-Tossing». *The Mathematical Intelligencer* 32(4), 54–58. | 10.1007/s00283-010-9143-x | Divulgación técnica del mismo grupo | No leído. | — | TEO | MET |
| F5c | Strzałko, J., Grabski, J., Perlikowski, P., Stefański, A., Kapitaniak, T. (2009). *Dynamics of Gambling: Origins of Randomness in Mechanical Systems*. Lecture Notes in Physics 792, Springer. | 10.1007/978-3-642-03960-7 | Monografía (moneda, dado, ruleta) | Según la ficha del catálogo: los resultados son predecibles si las condiciones iniciales pueden reproducirse con incertidumbre pequeña. F6 la cita como modelo «independiente y mucho más detallado» de la ruleta. | No leído el libro. | TEO + SIM | MET + SEC |
| F12 | Murray, D. B., Teare, S. W. (1993). «Probability of a tossed coin landing on edge». *Physical Review E* 48(4), 2547–2552. | 10.1103/PhysRevE.48.2547 | Experimento (cilindros de distinta forma) + simulación | Buen acuerdo entre experimento y modelo; extrapolación: una moneda de cinco centavos estadounidense cae de canto aproximadamente 1 vez en 6.000. | La cifra 1/6.000 es extrapolación del modelo, no conteo directo. | EU + SIM | RES |
| F14 | Yong, E. H., Mahadevan, L. (2011). «Probability, geometry, and dynamics in the toss of a thick coin». *American Journal of Physics* 79(12), 1195–1201. | 10.1119/1.3630934; arXiv:1008.4559 | Teoría + experimento de mesa | La relación de aspecto que da 1/3 de probabilidad a cara, sello y canto es h/D = 1/√3 con criterio dinámico, frente a 1/(2√2) ≈ 0,354 con criterio geométrico (von Neumann). El experimento se ajusta mejor al criterio dinámico (suma de errores cuadráticos 0,01 frente a 0,20). | Sin rebote; experimento sencillo. | TEO + EU | TC parcial |
| F14b | Mahadevan, L., Yong, E. H. (2011). «Probability, physics, and the coin toss». *Physics Today* 64(7), 66–67. | 10.1063/PT.3.1178 | Divulgación | No leído. | — | REV | MET |
| F15 | Clark, M. P. A., Westerberg, B. D. (2009). «How random is the toss of a coin?». *CMAJ* 181(12), E306–E308. | 10.1503/cmaj.091733 | Experimento: 13 residentes, 300 lanzamientos cada uno intentando sacar cara | Todos sacaron más caras que sellos; 7 de 13 con p ≤ 0,05; máximo 0,68 (IC 95 % 0,62–0,73). | Muestra pequeña; sin control del método de lanzamiento. | EU | RES |
| F16 | Ford, J. (1983). «How random is a coin toss?». *Physics Today* 36(4), 40–47. | 10.1063/1.2915570 | Ensayo conceptual | Convivencia histórica de descripciones determinista y probabilista; caos y complejidad algorítmica. | Ensayo, no resultado. | REV | RES (solo inicio) |

### 2.2 Dados

| # | Referencia | DOI / URL | Método | Resultado principal | Limitaciones | Ev. | Leído |
|---|---|---|---|---|---|---|---|
| F8 | Nagler, J., Richter, P. (2008). «How random is dice tossing?». *Physical Review E* 78(3), 036207. | 10.1103/PhysRevE.78.036207 | Modelo simplificado (barra con dos masas, dos estados finales) | Según condiciones iniciales y disipación en los rebotes, el resultado es más o menos impredecible: el sistema es pseudoaleatorio, no aleatorio. | Modelo reducido, no un cubo. | SIM + TEO | RES |
| F9 | Kapitaniak, M., Strzałko, J., Grabski, J., Kapitaniak, T. (2012). «The three-dimensional dynamics of the die throw». *Chaos* 22(4), 047504. | 10.1063/1.4746038 | Modelo tridimensional con rebote y disipación, mesa fija y oscilante; comparación con cámara rápida (1.500 cuadros/s según nota de AIP Inside Science) | Para energías iniciales realistas, la cara inicialmente más baja es más probable que cualquier otra. La no suavidad del sistema explica la incertidumbre dinámica. Más fricción en la mesa produce más rebotes y menos predictibilidad; sería caótico solo con infinitos rebotes. | El resumen no da probabilidades numéricas; no es un conteo estadístico de tiradas reales. | SIM + EU | RES + SEC |
| F10 | Strzałko, J., Grabski, J., Stefański, A., Kapitaniak, T. (2010). «Can the dice be fair by dynamics?». *International Journal of Bifurcation and Chaos* 20(4), 1175–1184. | 10.1142/S021812741002637X | Modelo tridimensional con rebote | Mismo resultado que F9 sobre la cara más baja. | Mismo grupo; no es réplica independiente. | SIM | RES |
| F11 | Grebogi, C., McDonald, S. W., Ott, E., Yorke, J. A. (1983). «Final state sensitivity: An obstruction to predictability». *Physics Letters A* 99(9), 415–418. | 10.1016/0375-9601(83)90945-3 | Teoría (fronteras fractales de cuencas) | No leído; fuente canónica del concepto de sensibilidad del estado final. | — | TEO | MET |
| F13 | Labby, Z. (2009). «Weldon's Dice, Automated». *CHANCE* 22(4), 6–13. | 10.1080/09332480.2009.10722977 | Experimento automatizado: caja con solenoides, cámara web y conteo de puntos por análisis de imagen; 12 dados de plástico con marcas huecas | 26.306 tiradas de 12 dados (315.672 resultados). Frecuencias: 0,1686; 0,1651; 0,1662; 0,1658; 0,1655; 0,1688. χ² = 25,0, p = 0,00014. Se rechaza la tendencia lineal por peso de las marcas (p = 0,00005). Micrómetro: eje 1–6 más corto en torno a 0,2 %. Dato histórico de Weldon (1894): cinco o seis en 33,77 %. Detectar 16,88 % frente a 16,67 % requiere 270.939 tiradas (potencia 90 %, α = 5 %). | Un solo juego de dados baratos; 4 % de imágenes con error corregidas a mano (27 incontables); no prueba dados de casino. | EU (réplica moderna de Weldon con resultado distinto en la causa) | TC |
| F13b | Riemer, W., Stoyan, D., Obreschkow, D. (2014). «Cuboidal dice and Gibbs distributions». *Metrika* 77(2), 247–256. | 10.1007/s00184-013-0435-y | Modelo estadístico de dados no cúbicos | No leído. | — | TEO + EU | MET |

### 2.3 Ruleta

| # | Referencia | DOI / URL | Método | Resultado principal | Limitaciones | Ev. | Leído |
|---|---|---|---|---|---|---|---|
| F6 | Small, M., Tse, C. K. (2012). «Predicting the outcome of roulette». *Chaos* 22(3), 033150. | 10.1063/1.4753920; arXiv:1204.6412 | Modelo dinámico sencillo + dos experimentos en una rueda de casino europea (Matsui «President Revolution», 37 casillas) | (a) Cronometraje manual de pasos de bola y rueda: mitad de rueda acertada en 13 de 22 ensayos (p < 0,15), ganancia esperada +18 % frente a −2,7 %; casilla exacta 3 veces (p < 0,02). (b) Cámara Prosilica EC650C, 659×493 píxeles, 90 cuadros/s: 700 ensayos; la casilla predicha y otra a un cuarto de rueda quedan fuera del intervalo de 99 %; 30 de 37 casillas dentro del de 90 %. Una inclinación leve de la mesa produce un sesgo muy marcado. El trayecto posterior a los deflectores se trata como estocástico. | 22 ensayos manuales es muy poco; sin ensayo en casino; modelo con desaceleración constante y deflectores idealizados; la dispersión final depende de cada rueda. | EU | TC (preimpresión) |
| F7 | Thorp, E. O. (1998). «The invention of the first wearable computer». *Digest of Papers, 2nd Int. Symposium on Wearable Computers*, 4–8. IEEE. | 10.1109/ISWC.1998.729523 | Relato en primera persona | Dispositivo analógico de 1960–61 con Shannon; ganancia esperada de +44 % apostando al octante favorecido; pruebas en Las Vegas en 1961 coherentes con el laboratorio; un problema de hardware impidió apuestas sostenidas. | Sin datos brutos; autoinforme décadas después. | REL | RES |
| F7b | Thorp, E. O. (1969). «Optimal Gambling Systems for Favorable Games». *Review of the International Statistical Institute* 37(3), 273–293. | 10.2307/1402118 | Artículo matemático con sección sobre ruleta | Según F6: describe dos esquemas; inclinación de 0,2° suficiente; cerca de un tercio de las ruedas observadas la cumplían; +15 % sin computador y +44 % con él. F6 advierte que no contiene ecuaciones sobre la ruleta. | No leído el original. | REL + TEO | MET + SEC |
| F7c | Bass, T. A. (1985). *The Eudaemonic Pie*. Houghton Mifflin (ed. británica: *The Newtonian Casino*, Penguin, 1990). | Open Library: primera publicación 1985; ISBN 0395353351 | Libro periodístico | Según F6: Farmer, Packard y colegas (1977–1978) usaron un microprocesador 6502 oculto en un zapato en casinos de Las Vegas. | Relato sin datos verificables. | REL | MET + SEC |
| F7d | Ethier, S. N. (1982). «Testing for Favorable Numbers on a Roulette Wheel». *Journal of the American Statistical Association* 77(379), 660–665. | 10.1080/01621459.1982.10477869 | Estadística (prueba de números favorables) | Marco estadístico para detectar irregularidades de una rueda (así lo describe F6). | No leído. | TEO | MET + SEC |
| F7e | Ethier, S. N. (2010). *The Doctrine of Chances: Probabilistic Aspects of Gambling*. Springer. | 10.1007/978-3-540-78783-9 | Monografía | No leído. | — | REV | MET |
| F7f | Farmer, J. D., Sidorowich, J. J. (1987). «Predicting chaotic time series». *Physical Review Letters* 59(8), 845–848. | 10.1103/PhysRevLett.59.845 | Método de predicción por aproximación local en espacio de fases reconstruido | Predicción a corto plazo de series caóticas (Mackey-Glass, Rayleigh-Bénard, Taylor-Couette). F6 señala que los autores atribuyen su inspiración a la ruleta. | No trata la ruleta. | SIM + TEO | RES |

### 2.4 Tablero de Galton, billares y péndulo doble

| # | Referencia | DOI / URL | Método | Resultado principal | Limitaciones | Ev. | Leído |
|---|---|---|---|---|---|---|---|
| F30 | Lue, A., Brenner, H. (1993). «Phase flow and statistical structure of Galton-board systems». *Physical Review E* 47(5), 3128–3144. | 10.1103/PhysRevE.47.3128 | Teoría + simulación (colisiones inelásticas, red periódica) | Atractores extraños, atractores periódicos y repulsores extraños según la geometría; las estadísticas dependen críticamente de los detalles y, en ciertas condiciones, no reproducen las «leyes de la probabilidad». | Modelo idealizado. | SIM + TEO | RES |
| F31 | Kozlov, V. V., Mitrofanova, M. Yu. (2003). «Galton board». *Regular and Chaotic Dynamics* 8(4), 431. | 10.1070/RD2003v008n04ABEH000255; arXiv:nlin/0503024 | Simulación (masa puntual, coeficiente de restitución e, radio del clavo R, varianza inicial) | La distribución final no siempre es gaussiana: aparecen huecos y picos periféricos que dependen de e y R; la varianza no es monótona en e. Hasta 10⁶ bolas simuladas. | Sin experimento; bola puntual. | SIM | TC |
| F32 | Judd, K. (2007). «Galton's quincunx: random walk or chaos?». *International Journal of Bifurcation and Chaos* 17(12), 4463–4469. | 10.1142/S0218127407020129 | Modelo dinámico y análisis | El supuesto de «eventos aleatorios independientes» casi con certeza no es válido; el dispositivo tiene las cualidades, más predecibles, de un sistema determinista de baja dimensión. | El resumen no detalla la evidencia. | TEO + SIM | RES |
| F33 | Chernov, N., Dolgopyat, D. (2009). «The Galton board: Limit theorems and recurrence». *Journal of the AMS* 22(3), 821–858. | 10.1090/S0894-0347-08-00626-7 | Demostración matemática (gas de Lorentz periódico con fuerza constante, horizonte finito, colisiones elásticas) | v(t) crece como t^(1/3) y x(t) como t^(2/3); el movimiento es recurrente. | Idealizado: sin disipación. | TEO | RES |
| F34 | Sinai, Ya. G. (1970). «Dynamical systems with elastic reflections». *Russian Mathematical Surveys* 25(2), 137–189. | 10.1070/RM1970v025n02ABEH003794 | Matemática (billares dispersivos) | No leído; fuente canónica de la ergodicidad de billares con obstáculos convexos. | — | TEO | MET |
| F25 | Shinbrot, T., Grebogi, C., Wisdom, J., Yorke, J. A. (1992). «Chaos in a double pendulum». *American Journal of Physics* 60(6), 491–499. | 10.1119/1.16860 | Experimento + simulación | Crecimiento exponencial de la incertidumbre con λ = 7,5 ± 1,5 s⁻¹ (experimento) y 7,9 ± 0,4 s⁻¹ (modelo idealizado). | Un aparato; condiciones iniciales «típicas». | EU + SIM | RES |
| F26 | Levien, R. B., Tan, S. M. (1993). «Double pendulum: An experiment in chaos». *American Journal of Physics* 61(11), 1038–1044. | 10.1119/1.17335 | Experimento docente con codificadores ópticos | La sensibilidad a condiciones iniciales se demuestra y cuantifica directamente. | El resumen no da el exponente. | EU | RES |

### 2.5 Esferas duras, amplificación de errores y límite cuántico

| # | Referencia | DOI / URL | Método | Resultado principal | Limitaciones | Ev. | Leído |
|---|---|---|---|---|---|---|---|
| F17 | Albrecht, A., Phillips, D. (2014). «Origin of probabilities and their application to the multiverse». *Physical Review D* 90(12), 123514. | 10.1103/PhysRevD.90.123514; arXiv:1212.0953 | Teoría (estimación de orden de magnitud) | Incertidumbre del parámetro de impacto tras n colisiones: Δbₙ = Δb·(1 + 2ℓ/r)ⁿ. Número de colisiones hasta que domina la incertidumbre cuántica: aire −0,3; agua 0,6; billar (r = 0,029 m, ℓ = 1 m, m = 0,16 kg, v = 1 m/s, Δb = 5,1×10⁻¹⁷ m) 8; autos chocadores 25. Moneda: 1 ms de fluctuación neuronal cambia en 0,5 el número de vueltas. | Argumento de plausibilidad; ignora decoherencia detallada, inelasticidad y fricción; los autores reconocen que omiten factores. | TEO | TC |
| F18 | Raymond, D. J. (1967). «How Determinate is the "Billiard Ball Universe"?». *American Journal of Physics* 35(2), 102–103. | 10.1119/1.1973895 | Teoría | El principio de incertidumbre impone un límite drástico a la predictibilidad del movimiento detallado de esferas duras que colisionan. F17 dice que presenta un resultado similar al suyo. | Nota breve; cifras no vistas. | TEO | RES |
| F19 | Berry, M. V. (1978). «Regular and irregular motion». *AIP Conference Proceedings* 46, 16–120. | 10.1063/1.31417 | Curso de revisión | No leído (el PDF del autor es una imagen escaneada sin texto extraíble). La cifra popular sobre el electrón en el borde del universo queda sin verificar: ver sección 4. | — | REV | MET |
| F19b | Zeh, H. D. (1970). «On the interpretation of measurement in quantum theory». *Foundations of Physics* 1(1), 69–76. | 10.1007/BF00708656 | Teoría | No leído. La atribución del argumento de Borel a este artículo queda sin verificar: ver sección 4. | — | TEO | MET |
| F19c | Zurek, W. H. (1998). «Decoherence, Chaos, Quantum-Classical Correspondence, and the Algorithmic Arrow of Time». *Physica Scripta* T76, 186. | 10.1238/Physica.Topical.076a00186 | Teoría | Un sistema macroscópico caótico deja de ser determinista en principio, por la indeterminación de Heisenberg, tras un tiempo solo logarítmico en ℏ; la tasa de producción de entropía es la suma de los exponentes de Lyapunov positivos. Ejemplo: Hiperión, con tiempo de Lyapunov de poco más de un mes. | Teórico. | TEO | RES |
| F19d | Zurek, W. H., Paz, J. P. (1994). «Decoherence, chaos, and the second law». *Physical Review Letters* 72(16), 2508–2511. | 10.1103/PhysRevLett.72.2508 | Teoría | No leído (citado por F17). | — | TEO | MET |
| F20 | Dellago, Ch., Posch, H. A., Hoover, W. G. (1996). «Lyapunov instability in a system of hard disks in equilibrium and nonequilibrium steady states». *Physical Review E* 53(2), 1485–1501. | 10.1103/PhysRevE.53.1485 | Simulación (64 y 144 discos duros) | Espectros de Lyapunov completos; el exponente máximo y la entropía de Kolmogorov-Sinai siguen muy de cerca la frecuencia de colisión; a baja densidad λ₁ ∝ −ρ ln ρ (conjetura de Krylov). | Discos elásticos sin fricción ni gravedad. | SIM | RES |
| F21 | van Zon, R., van Beijeren, H., Dellago, Ch. (1998). «Largest Lyapunov Exponent for Many Particle Systems at Low Densities». *Physical Review Letters* 80(10), 2035–2038. | 10.1103/PhysRevLett.80.2035 | Teoría cinética + simulación (esferas y discos duros) | Dependencia con la densidad predicha por Krylov, con prefactor mayor; convergencia lenta con el número de partículas. | Gas diluido elástico. | TEO + SIM | RES |
| F22 | Gaspard, P. et al. (1998). «Experimental evidence for microscopic chaos». *Nature* 394, 865–868. | 10.1038/29721 | Experimento (movimiento browniano) | No leído. | Interpretación discutida en la literatura posterior (lo afirmo de memoria, no verificado). | EU | MET |
| F22b | Dorfman, J. R. (1999). *An Introduction to Chaos in Nonequilibrium Statistical Mechanics*. Cambridge University Press. | 10.1017/CBO9780511628870 | Monografía | No leído. | — | REV | MET |
| F27 | Lighthill, J. (1986). «The recently recognized failure of predictability in Newtonian dynamics». *Proceedings of the Royal Society A* 407(1832), 35–50. | 10.1098/rspa.1986.0082 | Ensayo de revisión | En clases amplias de sistemas newtonianos simples la predicción es imposible más allá de un horizonte temporal definido. | Ensayo. | REV | RES |
| F27b | Lorenz, E. N. (1969). «The predictability of a flow which possesses many scales of motion». *Tellus* 21(3), 289–307. | 10.1111/j.2153-3490.1969.tb00444.x | Teoría y modelo | No leído. | — | TEO | MET |

### 2.6 Predictibilidad, entropía y conceptos

| # | Referencia | DOI / URL | Método | Resultado principal | Limitaciones | Ev. | Leído |
|---|---|---|---|---|---|---|---|
| F23 | Boffetta, G., Cencini, M., Falcioni, M., Vulpiani, A. (2002). «Predictability: a way to characterize complexity». *Physics Reports* 356(6), 367–474. | 10.1016/S0370-1573(01)00025-4; arXiv:nlin/0101029 | Revisión | Relación entre exponentes de Lyapunov, entropía de Kolmogorov-Sinai, entropía de Shannon y complejidad algorítmica; efectos de tiempo y resolución finitos; cómo distinguir caos de ruido. | La fórmula del horizonte la atribuyo a esta revisión por conocimiento previo; en esta sesión solo leí el resumen. | REV | RES |
| F24 | Eckmann, J.-P., Ruelle, D. (1985). «Ergodic theory of chaos and strange attractors». *Reviews of Modern Physics* 57(3), 617–656. | 10.1103/RevModPhys.57.617 | Revisión | No leído; fuente canónica de exponentes, entropía y dimensiones. | — | REV | MET |
| F24b | Pesin, Ya. B. (1977). «Characteristic Lyapunov exponents and smooth ergodic theory». *Russian Mathematical Surveys* 32(4), 55–114. | 10.1070/RM1977v032n04ABEH001639 | Matemática | No leído; fuente de la identidad entre entropía KS y suma de exponentes positivos. | — | TEO | MET |
| F35 | Kolmogorov, A. N. (1968, reimpresión en inglés). «Three approaches to the quantitative definition of information». *International Journal of Computer Mathematics* 2(1–4), 157–168. | 10.1080/00207166808803030 | Teoría | No leído; fuente de la complejidad algorítmica. El original ruso es de 1965. | — | TEO | MET |
| F36 | Martin-Löf, P. (1966). «The definition of random sequences». *Information and Control* 9(6), 602–619. | 10.1016/S0019-9958(66)80018-9 | Teoría | No leído; definición de secuencia aleatoria por pruebas efectivas. | — | TEO | MET |
| F37 | Shannon, C. E. (1948). «A Mathematical Theory of Communication». *Bell System Technical Journal* 27(3), 379–423. | 10.1002/j.1538-7305.1948.tb01338.x | Teoría | No leído en esta sesión; fuente de la entropía de Shannon. | — | TEO | MET |
| F38 | Li, M., Vitányi, P. (1997). *An Introduction to Kolmogorov Complexity and Its Applications* (2.ª ed.). Springer. | 10.1007/978-1-4757-2606-0 | Monografía | No leído. | — | REV | MET |
| F39 | Blum, M., Micali, S. (1984). «How to Generate Cryptographically Strong Sequences of Pseudorandom Bits». *SIAM Journal on Computing* 13(4), 850–864. | 10.1137/0213053 | Teoría | No leído; fuente de la pseudoaleatoriedad como impredecibilidad computacional. | — | TEO | MET |
| F40 | Chor, B., Goldreich, O. (1988). «Unbiased Bits from Sources of Weak Randomness and Probabilistic Communication Complexity». *SIAM Journal on Computing* 17(2), 230–261. | 10.1137/0217015 | Teoría | No leído; fuente habitual de la min-entropía como medida de fuentes débiles. | — | TEO | MET |
| F41 | Atmanspacher, H. (2000). «Ontic and epistemic descriptions of chaotic systems». *AIP Conference Proceedings* 517, 465–478. | 10.1063/1.1291283 | Filosofía de la física | La distinción entre estado óntico y epistémico es especialmente importante en sistemas con caos determinista y aclara las relaciones entre determinismo, causalidad, predictibilidad, aleatoriedad y estocasticidad. | Conceptual. | TEO | RES |
| F42 | Der Kiureghian, A., Ditlevsen, O. (2009). «Aleatory or epistemic? Does it matter?». *Structural Safety* 31(2), 105–112. | 10.1016/j.strusafe.2008.06.020 | Ensayo metodológico | No leído. | — | TEO | MET |
| F43 | Bricmont, J. (1995). «Science of chaos or chaos in science?». *Annals of the New York Academy of Sciences* 775, 131–175. | 10.1111/j.1749-6632.1996.tb23135.x | Ensayo crítico | Aclara confusiones sobre caos, determinismo, entropía y el papel de la probabilidad en física. | Ensayo. | REV | RES |
| F44 | Engel, E. M. R. A. (1992). *A Road to Randomness in Physical Systems*. Lecture Notes in Statistics 71, Springer. | 10.1007/978-1-4419-8684-9 | Monografía (método de funciones arbitrarias) | No leído. | — | TEO | MET |
| F44b | von Plato, J. (1983). «The Method of Arbitrary Functions». *British Journal for the Philosophy of Science* 34(1), 37–47. | 10.1093/bjps/34.1.37 | Historia y filosofía | No leído. | — | TEO | MET |
| F44c | Hopf, E. (1934). «On Causality, Statistics and Probability». *Journal of Mathematics and Physics* 13, 51–102. | 10.1002/sapm193413151 | Teoría | No leído. | — | TEO | MET |
| F45 | Crutchfield, J. P., Farmer, J. D., Packard, N. H., Shaw, R. S. (1986). «Chaos». *Scientific American* 255(6), 46–57. | 10.1038/scientificamerican1286-46 | Divulgación | No leído. | — | REV | MET |

### 2.7 Flujo granular

| # | Referencia | DOI / URL | Método | Resultado principal | Limitaciones | Ev. | Leído |
|---|---|---|---|---|---|---|---|
| F28 | Ottino, J. M., Khakhar, D. V. (2000). «Mixing and Segregation of Granular Materials». *Annual Review of Fluid Mechanics* 32, 55–91. | 10.1146/annurev.fluid.32.1.55 | Revisión | Los materiales granulares se segregan: diferencias pequeñas de tamaño o densidad producen segregación inducida por el flujo; la advección caótica aparece en tambores no circulares e interactúa con la segregación. | Tambores con muchas partículas pequeñas, no decenas de esferas grandes con aire. | REV | RES |
| F29 | Rosato, A., Strandburg, K. J., Prinz, F., Swendsen, R. H. (1987). «Why the Brazil nuts are on top: Size segregation of particulate matter by shaking». *Physical Review Letters* 58(10), 1038–1040. | 10.1103/PhysRevLett.58.1038 | Simulación Monte Carlo | Al agitar, la bola grande sube aunque sea más densa; el mecanismo es local y geométrico. | Simulación; agitación vertical. | SIM | RES |

Recuento: 62 referencias con metadatos confirmados en Crossref (y Open Library para el libro de Bass). De ellas, 6 con texto completo leído (F2, F3, F6, F13, F17, F31), 1 con lectura parcial (F14), 24 con resumen leído y 31 solo con metadatos (6 de estas con contenido conocido por una fuente secundaria leída).

---

## 3. Respuestas

### 3.1 Diferencias conceptuales

Advertencia: de las fuentes primarias de este apartado (F35–F40, F24, F24b) solo confirmé metadatos. Las definiciones que siguen son conocimiento estándar que expongo por mi cuenta [INF]; antes de citarlas textualmente hay que abrir los originales.

| Concepto | Qué dice | Fuente citable |
|---|---|---|
| Aleatoriedad algorítmica (Kolmogorov) | Una cadena finita es aleatoria si no admite descripción sustancialmente más corta que ella misma. Es propiedad de la secuencia, no del proceso. No es computable. | F35, F38 |
| Aleatoriedad de Martin-Löf | Una secuencia infinita es aleatoria si pasa todas las pruebas estadísticas efectivas. | F36 |
| Pseudoaleatoriedad | Secuencia generada por un algoritmo determinista corto que ningún observador con recursos acotados distingue del azar ni predice. Su complejidad de Kolmogorov es baja. | F39 |
| Caos determinista | Dinámica determinista con al menos un exponente de Lyapunov positivo: errores iniciales crecen como e^(λt). | F24, F23, F27 |
| Entropía de Shannon | Incertidumbre media de una fuente; mide el promedio. | F37 |
| Min-entropía | −log₂ de la probabilidad del resultado más probable; mide el peor caso y es la que importa frente a un adversario. | F40 |
| Entropía de Kolmogorov-Sinai | Tasa a la que la dinámica genera información; en sistemas suaves es la suma de los exponentes positivos (identidad de Pesin). | F24, F24b, F23 |
| Incertidumbre epistémica vs. óntica (o aleatoria) | Epistémica: reducible con más información. Óntica: propia del sistema. | F41, F42 |

Puntos con respaldo leído:
- F23 [HECHO, resumen] trata como un solo problema la relación entre exponentes de Lyapunov, entropía KS, entropía de Shannon y complejidad algorítmica, e incluye el problema de distinguir caos de ruido.
- F41 [HECHO, resumen] sostiene que la distinción óntico/epistémico es particularmente importante en sistemas caóticos.
- F4, F5, F8 y F9 [HECHO, resúmenes] coinciden en que moneda y dado son deterministas; F8 usa literalmente el término «pseudoaleatorio» para el dado.
- F19c [HECHO, resumen] y F17 [HECHO, texto completo] argumentan que en sistemas caóticos macroscópicos la incertidumbre cuántica se amplifica hasta escala macroscópica. Si eso es correcto, la incertidumbre de un sistema de muchas colisiones deja de ser puramente epistémica tras pocas colisiones.

Consecuencia para el caso de estudio [INF]: una secuencia de resultados de un dispositivo mecánico puede pasar pruebas estadísticas (parecer aleatoria en el sentido de Martin-Löf hasta donde alcancen las pruebas) y, a la vez, provenir de un proceso con sesgo físico pequeño o con una fase predecible. Las pruebas sobre la secuencia y la física del proceso responden preguntas distintas. Una min-entropía por extracción ligeramente inferior a la ideal es compatible con una entropía de Shannon casi máxima.

### 3.2 Qué sistemas resultaron predecibles o sesgados, y con qué instrumentación

| Sistema | Qué se logró | Instrumentación | Fuente | Solidez |
|---|---|---|---|---|
| Moneda, lanzamiento a máquina | 100 % de caras con ajuste cuidadoso | Resorte y trinquete, moneda cae en una copa | F2 | Descrito por los autores, sin conteo publicado en el pasaje leído |
| Moneda, lanzamiento humano | Sesgo de 0,8 puntos hacia el lado inicial | 48 personas, registro manual, filmación y auditoría | F3 | Alta para el promedio; es el único estudio de este tamaño |
| Moneda, parámetro físico del sesgo | Medición de ψ en 27 lanzamientos | Cámara rápida a unos 600 cuadros/s; cinta adherida | F2 | Muestra pequeña |
| Moneda, manipulación deliberada | Hasta 68 % de caras | Ninguna (habilidad manual) | F15 | Muestra pequeña |
| Dado, sesgo de fabricación | Desviaciones de hasta 0,2 puntos por cara | Máquina con solenoides, cámara web, análisis de imagen, micrómetro digital | F13 | Alta para ese juego de dados |
| Dado, dependencia de la orientación inicial | Cara inicialmente más baja más probable | Modelo tridimensional y cámara a 1.500 cuadros/s | F9, F10 | Modelo validado cualitativamente; sin estadística de tiradas |
| Ruleta, predicción de tirada | Ganancia esperada positiva | Cronometraje manual; cámara a 90 cuadros/s sobre la rueda | F6 | Moderada con cámara (700 ensayos); débil a mano (22 ensayos) |
| Ruleta, computador portátil | +44 % declarado | Computador analógico del tamaño de una cajetilla | F7, F7b | Relato |
| Ruleta, inclinación | Sesgo marcado con 0,2° | Observación | F6, F7b (vía F6) | Modelo y verificación cualitativa de F6 |
| Tablero de Galton | Distribuciones no gaussianas según restitución y geometría | Simulación | F30, F31, F32 | Solo simulación y teoría |
| Péndulo doble | Medición del exponente, no predicción a largo plazo | Estroboscopía y codificadores ópticos | F25, F26 | Dos experimentos independientes del mismo fenómeno |

Patrón común [INF]: en todos los casos donde hubo predicción de tirada individual, el sistema tenía pocos grados de libertad y una fase de vuelo o rodadura regular antes de pocas colisiones (o ninguna). Donde hay muchos rebotes (dado sobre mesa con fricción, bola de ruleta tras los deflectores) los autores abandonan la predicción determinista y pasan a una descripción probabilística [HECHO: F6, F9].

Influencia medida o modelada de parámetros físicos:
- **Geometría**: 0,2 % de diferencia en un eje del dado produce un sesgo detectable [EXP: F13]. La relación de aspecto de una moneda gruesa fija la probabilidad de canto [TEO + EXP: F14, F12].
- **Masa y distribución de masa**: la hipótesis de Pearson (marcas huecas aligeran la cara del seis) fue rechazada para los dados de F13 (p = 0,00005) [EXP]. F2 recoge argumentos de que la inhomogeneidad no importa en monedas atrapadas en la mano [HECHO de F2, que cita a otros; no verifiqué esas fuentes].
- **Restitución**: en el tablero de Galton simulado, la forma de la distribución y su varianza cambian de modo no monótono con el coeficiente de restitución [SIM: F31]. En el modelo de dado, la disipación en los rebotes regula cuán impredecible es el resultado [SIM: F8].
- **Fricción**: más fricción en la mesa produce más rebotes y menos predictibilidad del dado [F9 vía nota de prensa de AIP; SEC].
- **Condiciones iniciales**: orientación inicial del dado [F9, F10]; lado inicial y ángulo ψ de la moneda [F2, F3]; velocidad angular relativa de bola y rueda en la ruleta [F6].
- **Nivelación**: inclinación de la mesa de ruleta [F6].
- **Tamaño y densidad en medios granulares**: segregación sistemática [F28, F29].

Contradicciones entre fuentes y su explicación:

1. **Keller (F1) frente a Diaconis et al. (F2).** F1 concluye probabilidad 1/2 en el límite de lanzamiento vigoroso; F2 concluye 0,51. Diferencia metodológica: F1 supone que el eje de giro está en el plano de la moneda; F2 permite precesión (eje inclinado), y entonces la moneda pasa más tiempo con el lado inicial hacia arriba. F2 no refuta a F1: lo generaliza y dice expresamente que el análisis de Keller es buena aproximación.
2. **Diaconis et al. (F2) frente a Bartoš et al. (F3).** Coinciden en la media (0,508 en ambos), pero F2 la obtiene de 27 lanzamientos de pocos lanzadores midiendo ψ, y F3 de 350.757 resultados sin medir ψ. F3 añade lo que F2 no podía ver: heterogeneidad entre personas (algunas sin sesgo) y decaimiento con la práctica. F3 cita además un antecedente de 40.000 lanzamientos (Larwood y Ku) con evidencia ambigua: 10.231 de 20.000 en una lanzadora y 10.014 de 20.000 en la otra, lo que es coherente con la heterogeneidad.
3. **Strzałko et al. (F5) frente a la imagen de «caos» en la moneda.** F5 afirma que no hay divergencia exponencial ni fronteras fractales en la moneda; F4 habla de la estructura de las cuencas con rebote. No es contradicción estricta: F5 y F4 coinciden en que el azar efectivo depende de la escala de las cuencas frente a la precisión del lanzador. La diferencia está en el vocabulario y en cuántos rebotes se modelan.
4. **Weldon/Pearson (histórico) frente a Labby (F13).** Ambos encuentran sesgo, con causas distintas: Pearson lo atribuyó al peso de las marcas; F13 mide cara por cara, rechaza esa tendencia y encuentra una causa geométrica. Diferencia metodológica: Weldon registró solo «cinco o seis» frente al resto; F13 registró cada cara y midió los dados. Son además dados de material y época distintos.
5. **Thorp (F7, F7b) frente a Small y Tse (F6).** +44 % declarado frente a +18 % medido. No son comparables: la cifra de Thorp es un autoinforme de laboratorio sobre el octante favorecido; la de F6 proviene de 22 ensayos manuales sobre media rueda. Con 13 de 22, el intervalo de Wilson al 95 % para la tasa de acierto es aproximadamente 0,39–0,77, es decir, una ganancia esperada entre −23 % y +54 % [INF: cálculo mío]. F6 observa que el artículo de 1969 no contiene ecuaciones sobre la ruleta.
6. **Tablero de Galton: Chernov y Dolgopyat (F33) frente a Lue y Brenner (F30), Kozlov y Mitrofanova (F31) y Judd (F32).** F33 demuestra teoremas límite para el tablero idealizado elástico; F30, F31 y F32 encuentran comportamiento regular o distribuciones no gaussianas. Diferencia: F33 no tiene disipación y exige horizonte finito; los otros incluyen colisiones inelásticas y geometrías concretas, donde aparecen atractores periódicos.
7. **Albrecht y Phillips (F17) frente a la lectura epistémica clásica (F43, F5).** F17 afirma que toda probabilidad útil tiene origen cuántico; la tradición de Laplace que defiende F43 trata la probabilidad en sistemas clásicos como ignorancia. F17 es un argumento de orden de magnitud sin contraste experimental; no invalida el uso práctico de modelos clásicos, pero pone un techo a la precisión alcanzable.

### 3.3 Qué precisión se requiere

Relación general [conocimiento estándar; F23, F24, F27 como referencias, no leídas en detalle]:

  T ≈ (1/λ) · ln(Δ/δ₀)

donde λ es el exponente de Lyapunov máximo, δ₀ el error inicial y Δ la tolerancia. Cada mejora de un factor 10 en la medición inicial añade un tiempo fijo ln(10)/λ ≈ 2,3/λ.

Versión por colisiones para esferas duras [HECHO: F17]: Δbₙ = Δb·(1 + 2ℓ/r)ⁿ, de donde

  n ≈ ln(r/Δb) / ln(1 + 2ℓ/r)

con r el radio, ℓ el camino libre medio y Δb el error en el parámetro de impacto.

Cuantificaciones disponibles:

| Sistema | Dato | Consecuencia | Tipo |
|---|---|---|---|
| Péndulo doble | λ = 7,5 ± 1,5 s⁻¹ (F25) | Cada factor 10 de precisión añade 0,31 s. Pasar de error 10⁻³ rad a 1 rad toma 0,92 s. Predecir 10 s con tolerancia de 1 rad exigiría un error inicial del orden de e⁻⁷⁵ ≈ 3×10⁻³³ rad. | EXP (λ) + INF (cálculos) |
| Bolas de billar | r = 0,029 m, ℓ = 1 m: factor ≈ 70 por colisión; desde 5,1×10⁻¹⁷ m se llega al radio en 8 colisiones (F17) | Con error inicial de 1 µm: ln(0,029/10⁻⁶)/ln(70) ≈ 2,4 colisiones. | TEO (F17) + INF (segunda cifra) |
| Gas de discos o esferas duras | λ₁ del orden de la frecuencia de colisión; λ₁ ∝ −ρ ln ρ a baja densidad (F20, F21) | El horizonte se mide en unos pocos tiempos de colisión por cada década de precisión. | SIM + INF |
| Ruleta | 90 cuadros/s bastan para la fase de riel; la salida depende de las estimaciones iniciales solo de forma lineal o cuadrática (F6) | Precisión modesta porque la fase predicha no es caótica. | EXP |
| Moneda | Detección estadística del sesgo: 250.000 lanzamientos (F2); medición del parámetro: 600 cuadros/s, y 60 cuadros/s es insuficiente (F2) | — | EXP |
| Dado | Detección estadística: 270.939 tiradas para 16,88 % frente a 16,67 % (F13); seguimiento de trayectoria: 1.500 cuadros/s (F9) | — | EXP |
| Moneda, mano humana | 1 ms de incertidumbre temporal cambia 0,5 vueltas (F17, con v = 5 m/s y d = 0,01 m) | La mano no puede controlar el resultado de un lanzamiento vigoroso. | TEO |

Extrapolación ilustrativa a esferas agitadas en un recinto [INF con parámetros supuestos, no medidos]: con r = 0,025 m y ℓ = 0,1 m el factor por colisión sería 1 + 2·0,1/0,025 = 9. Con error inicial de 1 µm se alcanzaría el radio en ln(2,5×10⁴)/ln 9 ≈ 4,6 colisiones entre bolas; con error de 10⁻¹⁷ m, en unas 16. Esto supone colisiones elásticas entre esferas lisas sin rotación ni aire; la inelasticidad, la fricción, las paredes y el flujo de aire cambian la cifra, y no hay medición que la respalde. Sirve solo para fijar el orden de magnitud: unidades o decenas de colisiones, no centenares.

No encontré ningún trabajo que cuantifique el horizonte de predicción para dados reales ni para un sistema de decenas de esferas macroscópicas agitadas.

### 3.4 Qué límites impiden predecir aunque el sistema sea determinista

1. **Amplificación exponencial en colisiones convexas** [HECHO: F17; marco matemático F34, no leído]. El horizonte crece con el logaritmo de la precisión: ninguna mejora instrumental realista compra más que unas pocas colisiones adicionales.
2. **Límite cuántico** [TEO: F17, F18, F19c]. Para billar, unas 8 colisiones; para moléculas de aire o agua, menos de una. Más allá no existe una condición inicial clásica que medir. Es una estimación teórica sin verificación experimental directa.
3. **Perturbaciones externas no modelables** [HIP en cuanto a cifras]. El argumento clásico sobre el efecto gravitatorio de masas lejanas sobre un gas o un billar (Borel, Berry) apunta en la misma dirección; no pude verificar sus cifras en la fuente (sección 4).
4. **No suavidad** [HECHO: F9]. Los impactos, el paso de deslizar a rodar y los contactos con aristas introducen discontinuidades; los autores de F9 las señalan como el origen de la incertidumbre dinámica del dado.
5. **Estructura fina de las cuencas de atracción** [HECHO: F4, F5, F8; concepto en F11, no leído]. Aunque las fronteras sean suaves, pueden estar tan juntas que cualquier error realista las cruza. Con disipación el número de rebotes es finito y la estructura no llega a ser fractal: pseudoaleatoriedad, no caos estricto.
6. **Ventana temporal y de observación** [HECHO: F6]. En la ruleta la predicción debe hacerse antes del cierre de apuestas y solo cubre hasta los deflectores. Un sistema sin fase regular observable no ofrece esa ventana [INF].
7. **Incertidumbre de parámetros, no solo del estado** [HECHO: F6; F13]. Hay que estimar dimensiones, inclinación, fricción y restitución de cada aparato concreto; F6 advierte que la distribución final depende de cada rueda.
8. **Ruido del actuador** [HECHO: F17, que cita fluctuaciones neuronales de 1 ms; F3: heterogeneidad entre personas].
9. **Dimensión alta** [SIM: F20, F21]. En muchos cuerpos hay tantos exponentes positivos como grados de libertad inestables; la entropía KS, que es la tasa de pérdida de información, crece con el tamaño del sistema.
10. **Costo estadístico de detectar sesgos pequeños** [EXP: F2, F3, F13]. Un sesgo de 0,2 a 0,8 puntos requiere del orden de 10⁵ observaciones, y un sesgo detectado en el agregado apenas mejora la predicción de un resultado individual.

Lo que estos límites **no** impiden [INF]: detectar un sesgo estacionario del mecanismo o de las piezas si se dispone de suficientes repeticiones con el mismo equipo, ni predecir una fase final regular si existe y es observable. La segregación granular (F28, F29) muestra que diferencias físicas pequeñas entre partículas pueden producir efectos sistemáticos y no solo ruido.

---

## 4. No verificadas

Afirmaciones o referencias que no pude confirmar en la fuente primaria en esta sesión. No deben citarse como hechos.

1. **Berry y el «electrón en el borde del universo».** La referencia F19 existe (metadatos confirmados), pero no pude leer el texto. Las fuentes secundarias que encontré se contradicen: una nota de prensa habla de unas 60 colisiones entre moléculas; reseñas de lectores hablan de 9 colisiones de billar para la gravedad de una persona junto a la mesa. Mi recuerdo era «unas 56 colisiones». Ninguna cifra queda verificada.
2. **Borel (1914), *Le Hasard*, Alcan, París.** La existencia del libro está confirmada por fuentes secundarias (reseña en *Bulletin of the AMS* 21, 1915, 361–362). El pasaje sobre desplazar un gramo de materia en Sirio y su efecto sobre las moléculas de un gas no lo encontré en ninguna fuente consultada.
3. **«Raymond-Zeh».** No existe como pareja. Raymond es F18 (verificado). Que Zeh (F19b) discuta el argumento de Borel lo recuerdo, pero no lo verifiqué.
4. **García-Pelayo y Jagger (sesgo de rueda).** Solo encontré prensa y sitios de divulgación, con cifras inconsistentes entre sí (65.000 libras o 325.000 dólares para Jagger en 1873; entre 600.000 euros en un día y más de un millón en total para García-Pelayo). Ninguna fuente académica. La referencia seria sobre sesgo de rueda es F7d (Ethier 1982), que no leí. F6 menciona como antecedentes a Hibbs y Walford (1947) y un reportaje de *Time* de 1951 sobre el casino de Mar del Plata; no verifiqué esas fuentes.
5. **Caso del casino Ritz de Londres (2004).** F6 lo relata citando a la BBC (1,3 millones de libras, escáner láser y teléfonos). No abrí las notas de la BBC.
6. **Epstein, R. A. (1967), *The Theory of Gambling and Statistical Logic*.** Citado por F6 por experimentos con una rueda privada; no verificado.
7. **Thorp, E. O. (1985), *The Mathematics of Gambling*.** Citado por F6; no verificado.
8. **Iversen, Longcor, Mosteller, Gilbert y Youtz (1971), «Bias and runs in dice throwing and recording: A few million throws», *Psychometrika* 36(1), 1–19.** Citado en la lista de lecturas de F13; no lo confirmé en Crossref ni lo leí. Sería la mayor base de tiradas de dados publicada.
9. **Kemp y Kemp (1991), «Weldon's dice data revisited», *The American Statistician* 45(3), 216–222.** Citado por F13; no verificado.
10. **Larwood y Ku, 40.000 lanzamientos.** Los datos constan en F3 y en una página de D. Aldous (Berkeley) que apareció en la búsqueda; no abrí la página ni hay publicación revisada.
11. **Kolmogorov (1958) y Sinai (1959), artículos originales de la entropía KS; Rényi (1961), «On measures of entropy and information».** Crossref no devolvió registro; uso F24 y F24b como sustitutos.
12. **Faisal, Selen y Wolpert (2008), «Noise in the nervous system», *Nature Reviews Neuroscience* 9, 292–303 (10.1038/nrn2258).** Metadatos confirmados; la cifra de 1 ms la tomo de F17, no del original.
13. **Krylov, conjetura λ ∝ −ρ ln ρ.** Conocida solo por los resúmenes de F20 y F21.
14. **Cifras numéricas de probabilidad por cara en F9 y F10.** Los resúmenes no las dan; no accedí al texto completo.
15. **Resumen de F5.** Lo conozco por el anuncio de un seminario del autor, no por el editor.
16. **Estudio de mezcla granular por «corte y barajado» (EPL, 2010).** Apareció en la búsqueda; no confirmé sus metadatos.

---

## 5. Vacíos detectados

1. **No hay física publicada de máquinas de extracción de bolillas.** La búsqueda no devolvió ningún estudio revisado por pares con exponentes de Lyapunov, simulación por elementos discretos validada o medición de sensibilidad a masa, diámetro, restitución o rugosidad en esas máquinas. (La búsqueda fue acotada; el agente de lotería puede tener más.)
2. **Falta el puente entre billar ideal y esferas reales.** Los resultados de Lyapunov (F20, F21) son para esferas elásticas sin fricción, gravedad ni aire. No encontré exponentes medidos o simulados para decenas de esferas inelásticas con rotación, paredes curvas y agitación por aire o paletas.
3. **Horizonte de predicción de dados sin cuantificar.** F8, F9 y F10 son cualitativos. No hay un trabajo que diga «con error δ en orientación y velocidad se predice la cara con probabilidad p tras n rebotes».
4. **Un solo experimento grande por sistema.** F3 (moneda) y F13 (dado) no tienen réplica independiente de tamaño comparable. F6 (ruleta) no tiene réplica publicada; los propios autores mencionan ensayos de campo solo por comunicación privada.
5. **Sin medición directa del mecanismo en F3.** El sesgo del mismo lado se atribuye a la precesión, pero el estudio grande no midió ψ; el vínculo causal descansa en 27 lanzamientos de F2.
6. **El límite cuántico es solo teórico.** F17, F18 y F19c son estimaciones; no hay experimento que muestre la pérdida de predictibilidad clásica en un sistema macroscópico de colisiones por esa causa.
7. **Segregación en sistemas de pocas esferas grandes.** F28 y F29 tratan muchos granos pequeños. No encontré datos sobre si diferencias de fracciones de gramo o décimas de milímetro entre unas decenas de esferas producen sesgos de posición medibles bajo agitación por aire.
8. **Relación entre sesgo físico y pruebas estadísticas.** Ninguna de las fuentes leídas conecta un sesgo físico medido con el tamaño de muestra necesario para que una batería estándar de pruebas lo detecte, más allá de los cálculos de potencia puntuales de F2 y F13.
9. **Lecturas pendientes que cambiarían la solidez del informe:** el texto completo de F5, F5c, F9 y F19 (para cifras), F7b (para el método de Thorp) y F7d (para la estadística de ruedas sesgadas), y la referencia de Iversen et al. (1971).
10. **Efecto del rebote en la moneda.** F2 conjetura que una moneda que rebota en el suelo puede ser menos justa que una atrapada en la mano; no encontré un experimento que lo mida.
