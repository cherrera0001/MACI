# 02 · Loterías: sesgos mecánicos y estadísticos en sorteos, y sus controles

Fecha de la búsqueda: 2026-10-09. Autor de la ficha: agente estadístico de loterías del concilio.
Alcance: sorteos con bolillas, análisis estadísticos de sorteos reales, fraudes y fallos documentados, estándares y tolerancias. Quedan fuera (otros agentes): física del caos, baterías NIST, aprendizaje automático e instrumentación, caso chileno.

Convención de lectura usada en todo el documento:

- **TC** = leí el texto completo. **RES** = leí el resumen del editor o de un repositorio. **META** = solo confirmé metadatos (Crossref, RePEc). **SEC** = lo conozco por una fuente secundaria que sí leí.
- «Cálculo propio» marca una cifra que calculé yo a partir de los datos publicados; no la afirman los autores.

---

## 1. Síntesis

1. Existe un único experimento controlado publicado sobre masa de bolillas en una máquina de sorteo que pude localizar: Pinitsoontorn, Buathong y Srisodaphol (KKU Research Journal 19(6), 2014). Es una máquina casera de aire con 10 bolas de espuma de 0,28 g; no es una máquina comercial.
2. Su resultado central: una bola 1 % o 5 % más liviana sale más (12,8 % y 13,6 % frente al 10 % esperado, n = 1000 por condición); una bola 1 % o 5 % más pesada no se distingue del azar. El efecto es asimétrico y no crece en proporción a la dosis.
3. Ese sesgo equivale a acertar un dígito con probabilidad 0,13 en vez de 0,10. Sigue fallando el 87 % de las veces: es un sesgo detectable con mil extracciones, no una predicción de la extracción siguiente.
4. El mismo artículo muestra el problema del tamaño de muestra: su grupo de control (masas iguales) da p = 0,076 con 200 extracciones y p = 0,544 con 1000. Con pocas extracciones se «detectan» sesgos que no existen.
5. Los análisis de sorteos reales con más datos no encuentran desviación: Lotto 6/49 de Canadá, 1798 sorteos en casi 20 años, p = 0,104 para números individuales (Genest, Lockhart y Stephens 2002); Reino Unido, primeros 96 sorteos, compatible con azar (Haigh 1997); Sportka checa, 1957–2010, ningún año rechaza la uniformidad (Rozkovec 2012).
6. Hay hallazgos en sentido contrario: Melate de México con N = 51 (211 sorteos, p = 0,0056) y lotto italiano de la rueda de Roma en un período (p < 10⁻⁵) (Coronel-Brizio et al. 2008); Tris de México, 500 sorteos (Gutiérrez-Pulido y García 2010). Ninguno identifica la causa física ni cuantifica ventaja para un apostador.
7. La diferencia entre unos y otros es metodológica: los que rechazan parten el historial en varios períodos y prueban cada uno (comparaciones múltiples), usan muestras de 200 a 500 sorteos y estadísticos distintos (vector ordenado frente a frecuencias).
8. El estadístico de Pearson habitual está mal calibrado para lotos k/N porque se extrae sin reposición. Hay que escalarlo por (N−1)/(N−k) (Joe 1993) o usar la suma ponderada de χ² (Genest et al. 2002). Un análisis casero que no lo haga no es comparable.
9. Potencia real, cálculo propio: en 1798 sorteos de un 6/49 cada número sale unas 220 veces con desvío estándar de 13,9, o sea 6,3 % relativo. Un sesgo de un par de puntos porcentuales por bola no se ve ni en veinte años, y la rotación de juegos de bolas y máquinas lo diluye más.
10. El caso clásico de mezcla física insuficiente no es una lotería de premios: es el sorteo militar de EE. UU. de 1969 para 1970. Correlación entre día del año y orden de sorteo de −0,226, p ≈ 0 (Fienberg 1971; Starr 1997). Causa: cápsulas cargadas mes a mes y mal mezcladas. Corregido en 1971 (Rosenblatt y Filliben 1971).
11. Todos los casos documentados de resultado alterado en loterías que pude confirmar son manipulación deliberada o error de software, no sesgo natural de una máquina certificada.
12. Manipulación física: Pensilvania 1980 (bolas lastradas con pintura látex, salió 666) y Milán 1995–1999 (bolas barnizadas, calentadas o enfriadas para que las reconocieran niños vendados).
13. Manipulación electrónica: Eddie Tipton, código en el generador de números de MUSL que hacía predecible el resultado en tres fechas del año; condena de 25 años en 2017.
14. Fallos sin dolo: Tennessee 2007 (el generador no repetía dígitos, 28 de julio a 20 de agosto), Arizona 2017 (números duplicados entre juegos), visas de diversidad 2012 (más del 90 % de seleccionados de los dos primeros días).
15. Los fallos de software se detectaron con pocas semanas de datos porque el defecto era estructural (un tipo de resultado imposible), no una leve desviación de frecuencias.
16. El estándar sectorial WLA-SCS:2020 exige inspección de máquinas y juegos de bolas con una autoridad independiente, mantenimiento documentado al menos anual y bolas con tolerancias compatibles con la máquina (controles L.2.3.1 a L.2.3.5). No fija ninguna cifra de tolerancia.
17. Las cifras de tolerancia que encontré vienen de reguladores y operadores: Texas, ±0,095 g del promedio del juego en bolas tipo ping-pong y ±1 g en bolas de caucho; Nueva Zelanda, 11–13 g, 49,0–51,5 mm y máximo 0,45 g entre la más pesada y la más liviana; Washington, de 2 g a 1 g en 1999.
18. Esas tolerancias relativas (del orden de 1–4 % de la masa) son del mismo orden que el 1 % que en la máquina tailandesa bastó para un sesgo medible. No hay estudio publicado que mida el efecto en una máquina comercial.
19. No encontré ningún trabajo revisado por pares que prediga extracciones de lotería con frecuencias históricas o redes neuronales y que supere una línea base de azar. Lo que circula son repositorios, notas de prensa y una sátira en arXiv.
20. El sesgo de los jugadores (números populares) es otro fenómeno: no cambia la probabilidad de ganar, cambia cuánto se cobra al ganar (Stern y Cover 1989; Farrell et al. 2000; Baker y McHale 2009; Cook y Clotfelter 1993).
21. Vacío principal: no hay experimento publicado con máquina comercial (Smartplay, WinTV, Ryo-Catteau), bolas reales y miles de extracciones con masa controlada.

---

## 2. Ficha detallada: Pinitsoontorn, Buathong y Srisodaphol

### 2.1 Referencia confirmada

- **Autores:** Supree Pinitsoontorn y Suwat Buathong (Departamento de Física, Facultad de Ciencias, Universidad de Khon Kaen) y Wuttichai Srisodaphol (Departamento de Estadística, misma facultad). Autor de correspondencia: psupree@kku.ac.th.
- **Título:** «Is it possible to cheat the lottery draw by weighing?» (título en tailandés: ผลการออกรางวัลสามารถล็อกได้ด้วยการถ่วงน้ำหนักจริงหรือ?).
- **Revista:** KKU Research Journal, hoy Asia-Pacific Journal of Science and Technology (APST). Volumen 19, número 6, páginas 804–818, diciembre de 2014. El encabezado del PDF dice «KKU Res. J. 2014; 19(6): 804-818».
- **Año:** 2014. La plataforma ThaiJO muestra «publicado 13 abr 2017» y sugiere citar «(2017)»; esa es la fecha de carga al sitio, no la de la revista. Citar 2014.
- **DOI:** **no tiene**. No aparece en la página del artículo ni en el PDF, y la búsqueda bibliográfica en Crossref no lo devuelve. Identificador estable: https://so01.tci-thaijo.org/index.php/APST/article/view/83061 (PDF: `.../article/view/83061/66039`).
- **Idioma:** cuerpo en tailandés, resumen y palabras clave en inglés.
- **Nivel de lectura:** TC. Descargué el PDF (15 páginas), extraje el texto y leí todas las tablas.
- **Nivel de evidencia:** experimento controlado de laboratorio, una sola corrida por condición.

### 2.2 Contexto y motivación

El 16 de marzo de 2014 (2557 en calendario tailandés) el primer premio de la lotería estatal tailandesa (531404, terminación de dos cifras 79) coincidió con las patentes de dos autos oficiales de la primera ministra Yingluck Shinawatra, y la prensa habló de «lotería amarrada» (หวยล็อก). La Oficina de Lotería del Gobierno hizo demostraciones públicas con su máquina «Lat Krabang 6» y su diseñador sostuvo que no se podía amarrar lastrando bolas. Los autores objetan que demostrar con 5 o 6 extracciones no prueba nada y se proponen (a) medir si lastrar cambia el resultado y (b) medir cuánto influye el número de sorteos en el veredicto estadístico.

El artículo reseña trabajos tailandeses previos que no pude consultar (ver sección 6): análisis de Veerathaworn con 257 sorteos de la Lat Krabang 6 (16 jun 2002 a 16 feb 2013) que rechaza la uniformidad del primer premio a p < 0,05; y Panichkitkosolkul y Lertsuwansri, que no la rechazan para 2001–2003.

### 2.3 Máquina

- **No usaron la máquina oficial.** No pudieron conseguir una Lat Krabang 6, y además la descartan porque es manual: una persona hace girar el tambor y otra levanta la palanca que recoge la bola, lo que introduce factores humanos.
- Construyeron una máquina propia de **mezcla por aire**, «parecida a las europeas» según ellos: tambor cilíndrico cerrado de acrílico de 50,0 cm de diámetro y 7,0 cm de espesor, montado de canto; abertura inferior de 5,0 × 7,0 cm conectada a un soplador de 60 W; abertura superior de 4,0 × 4,0 cm con un tubo de captura apenas más ancho que una bola, de modo que entra una sola.
- **Bolas:** esferas de espuma de unos 3,8 cm de diámetro y unos 280 mg cada una. Eligieron espuma para poder ajustar la masa rebanando material. Se registró la masa de cada bola en cada ensayo.

### 2.4 Procedimiento

- Diez bolas numeradas 0–9. Se enciende el soplador; tras 5 a 10 segundos una bola queda atrapada en el tubo; se anota; el operador golpea el tubo para devolverla al tambor y se repite. Es extracción de una bola **con reposición**.
- **1000 extracciones por condición**, con análisis intermedios a 50, 200, 500 y 1000.
- Siete condiciones, 7000 extracciones en total.
- Pruebas: χ² de bondad de ajuste para las condiciones 1, 6 y 7; prueba binomial de una proporción, unilateral, sobre la bola 9 en las condiciones 2 a 5 (H₁: p > 0,1 si es liviana, p < 0,1 si es pesada).

### 2.5 Resultados (tablas 1 a 8 del artículo)

Frecuencias a n = 1000 por número de bola:

| Condición | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | Estadístico | p |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1. Diez bolas iguales (279,6–280,4 mg; diferencia máx. 0,30 %) | 105 | 92 | 105 | 98 | 101 | 111 | 105 | 110 | 92 | 81 | χ² = 7,900 | 0,544 |
| 2. Bola 9 un 1,0 % más liviana | 91 | 93 | 100 | 91 | 111 | 87 | 105 | 104 | 90 | **128** | binomial | 0,003 |
| 3. Bola 9 un 1,0 % más pesada | 107 | 98 | 99 | 111 | 101 | 91 | 111 | 100 | 96 | **86** | binomial | 0,075 |
| 4. Bola 9 un 5,0 % más liviana | 100 | 107 | 108 | 96 | 83 | 100 | 100 | 85 | 85 | **136** | binomial | < 0,001 |
| 5. Bola 9 un 5,0 % más pesada | 103 | 110 | 90 | 107 | 111 | 92 | 95 | 108 | 88 | **96** | binomial | 0,361 |
| 6. Diez bolas escalonadas de 1 % (bola 0 = 278 mg … bola 9 = 250 mg) | 70 | 115 | 95 | 109 | 115 | 107 | 89 | 117 | 75 | 108 | χ² = 26,040 | 0,002 |
| 7. Siete bolas escalonadas de 2 % (bola 0 = 286 mg … bola 6 = 250 mg) | 114 | 140 | 141 | 161 | 141 | 149 | 154 | — | — | — | χ² = 9,372 | 0,154 |

Valor p según el número de extracciones analizadas (tabla 8):

| Condición | n = 50 | n = 200 | n = 500 | n = 1000 |
|---|---|---|---|---|
| 1. Masas iguales | 0,350 | 0,076 | 0,798 | 0,544 |
| 2. Una bola 1 % más liviana | 0,384 | 0,067 | 0,001 | 0,003 |
| 3. Una bola 1 % más pesada | 0,112 | 0,143 | 0,131 | 0,075 |
| 4. Una bola 5 % más liviana | 0,384 | 0,033 | 0,013 | < 0,001 |
| 5. Una bola 5 % más pesada | 0,122 | 0,559 | 0,255 | 0,361 |
| 6. Diez bolas, pasos de 1 % | 0,779 | 0,172 | 0,010 | 0,002 |
| 7. Siete bolas, pasos de 2 % | 0,596 | 0,040 | 0,059 | 0,154 |

Otros resultados que informan:

- **Correlación masa–frecuencia (Spearman):** −0,039 con diez bolas en pasos de 1 % (sin relación); −0,704 con siete bolas en pasos de 2 % (las livianas salen más).
- **Independencia serial:** grafican número extraído contra orden de extracción en el control y no ven que la bola recién devuelta, que cae encima, tienda a repetirse. Es una inspección visual; no informan prueba de rachas ni autocorrelación.
- Nota menor: el texto dice que la bola 9 salió 127 veces en la condición 2 y la tabla dice 128.

### 2.6 Qué concluyen los autores

1. Con masas iguales el sorteo es justo (p > 0,05).
2. El número de extracciones cambia el veredicto: 50, 200 o 500 pueden contradecir a 1000. De ahí deducen que los estudios previos con 40 a 257 sorteos reales no permiten concluir que la lotería tailandesa sea injusta.
3. Una bola más pesada (1 % o 5 %) no altera el resultado.
4. Una bola más liviana (1 % o 5 %) sí lo altera y su probabilidad de salir aumenta.
5. Diez bolas en pasos de 1 % dan resultado injusto, pero sin relación masa–frecuencia.
6. Siete bolas en pasos de 2 % dan resultado «justo» por χ², pero con correlación negativa masa–frecuencia.
7. Explicación propuesta para la asimetría: en un sistema de aire el flujo afecta más a la bola liviana.
8. Recomiendan a la Oficina de Lotería ensayar la Lat Krabang 6 con al menos 1000 extracciones, publicar el resultado y pesar las bolas en público en el lugar del sorteo (el autor principal asistió al sorteo del 16 de junio de 2014 y observó que el pesaje no es público).

### 2.7 Ventaja predictiva que implica

Los autores no la cuantifican como ganancia esperada. Lo que dicen es que lastrar «no hace salir el número todas las veces» pero sube su probabilidad, y eso basta para que sea injusto. Con sus cifras:

- Bola 1 % más liviana: 0,128 frente a 0,100, es decir +28 % relativo. Bola 5 % más liviana: 0,136, +36 % relativo.
- Quien apueste a ese dígito acierta 13 de cada 100 veces en vez de 10. No hay predicción de una extracción concreta.
- Cálculo propio: intervalo de 95 % aproximado para 0,128 con n = 1000 es 0,107 a 0,149; para 0,136 es 0,115 a 0,157. Los dos intervalos se traslapan casi por completo: el experimento no distingue el efecto de 1 % del de 5 %.

### 2.8 Limitaciones

Reconocidas por los autores:

- No es la máquina oficial; no se puede trasladar el resultado a la Lat Krabang 6.
- En la condición 7 solo siete bolas, porque con diez la diferencia de tamaño entre la más pesada y la más liviana se notaba a simple vista.
- Al quitar espuma cambia también el tamaño y la superficie de la bola, que es otro factor distinto de la masa.

No reconocidas, a mi juicio:

- **Una sola corrida por condición.** No hay réplicas ni se reconstruyó la máquina. No se puede separar el efecto de la masa del efecto de la bola concreta (forma, rugosidad, posición del número pintado).
- **El control ya muestra a la bola 9 como la menos frecuente** (81 de 1000). Las condiciones 2 a 5 modifican justamente la bola 9, de modo que 86 con 1 % más pesada no es menos que su propio control. La comparación correcta sería contra el control de la misma bola, no contra 0,1.
- **Comparaciones múltiples sin corrección:** siete condiciones por cuatro tamaños de muestra, 28 pruebas. Que el control dé p = 0,076 a n = 200 es lo esperable por azar, no una demostración de que 200 sea insuficiente en general.
- **Pruebas distintas según la condición.** Cálculo propio con sus tablas: el χ² global de la condición 2 (una bola 1 % más liviana) da 14,26 con 9 grados de libertad, p ≈ 0,113, es decir, **no** rechaza; el rechazo viene de la prueba dirigida a la bola 9. En la condición 4 el χ² global da 21,64, p ≈ 0,010. Un auditor que no supiera cuál bola está alterada no habría detectado el 1 % con mil extracciones.
- **Resultados internamente incoherentes:** la condición 6 rechaza la uniformidad sin relación con la masa (las dos bolas menos frecuentes, 0 y 8, están en extremos opuestos de la escala de masa). Eso apunta a diferencias entre bolas ajenas a la masa, probablemente introducidas al rebanar.
- **Spearman con n = 7.** Cálculo propio suponiendo masas estrictamente decrecientes de la bola 0 a la 6: ρ ≈ −0,76, p ≈ 0,049, valor que no coincide con el −0,704 publicado (no tengo las masas exactas para reconciliarlo). En cualquier caso, con siete puntos es evidencia débil.
- **Escala no representativa:** bolas de 0,28 g y diferencias de 2,8 mg (1 %) o 14 mg (5 %). Las bolas reales pesan entre 2,7 g (tipo ping-pong) y 11–13 g o más (espuma, caucho). La dinámica en el flujo de aire no escala linealmente.
- **Diez bolas y una extracción con reposición.** No reproduce un loto 6/49 sin reposición ni una máquina de gravedad con paletas.
- Sin cegamiento del operador ni control de humedad, carga estática o desgaste a lo largo de 7000 extracciones.
- Potencia, cálculo propio: con n = 1000 y p₀ = 0,1 el error estándar es 0,0095; el experimento solo detecta con fiabilidad desvíos absolutos de unos 2,5 puntos porcentuales en una bola.

### 2.9 Valor para la revisión

Es la única medición directa publicada que encontré del efecto de la masa en una máquina de aire, con datos completos y reproducibles. Sirve como cota de orden de magnitud (1 % de masa puede mover la probabilidad de una bola de 10 % a 13 % en un sistema de aire con bolas muy livianas) y como ilustración del problema de muestra. No sirve para afirmar nada sobre máquinas comerciales ni sobre predicción de extracciones.

---

## 3. Tabla de fuentes verificadas

### 3.1 Experimento controlado

| # | Referencia | DOI o URL | Método | Resultado principal | Limitaciones | Lectura |
|---|---|---|---|---|---|---|
| 1 | Pinitsoontorn, Buathong y Srisodaphol (2014). «Is it possible to cheat the lottery draw by weighing?». KKU Res. J. 19(6): 804–818 | Sin DOI. https://so01.tci-thaijo.org/index.php/APST/article/view/83061 | Máquina de aire propia, 10 bolas de espuma, 7 condiciones × 1000 extracciones | Bola 1 % o 5 % más liviana: 0,128 y 0,136 frente a 0,100 (p = 0,003 y < 0,001). Más pesada: sin efecto (p = 0,075 y 0,361). Control p = 0,544 | Ver 2.8 | TC |

### 3.2 Análisis estadísticos de sorteos reales

| # | Referencia | DOI o URL | Datos y método | Resultado | Ventaja predictiva | Limitaciones | Lectura |
|---|---|---|---|---|---|---|---|
| 2 | Genest, Lockhart y Stephens (2002). «χ² and the lottery». J. R. Stat. Soc. D (The Statistician) 51(2): 243–257 | 10.1111/1467-9884.00315 | Lotto 6/49 de Canadá, primeros 1798 sorteos (12 jun 1982 a 14 abr 2001). Pearson para subconjuntos de tamaño c = 1…6 con distribución asintótica de suma ponderada de χ² | c = 1: X² = 54,34, p = 0,104; c = 2: p = 0,300; c = 3: p = 0,476; c = 4: p = 0,479. Con el número adicional (7 bolas), c = 1: X² = 57,64, p = 0,044. Frecuencias extremas: bola 48 con 193 y bola 31 con 269. Concluyen que no hay base seria para sospechar falta de uniformidad | Ninguna; no rechazan | El p = 0,044 no está corregido por comparaciones múltiples, lo dicen ellos. No detecta dependencia serial. Si cambian máquina o bolas, la potencia calculada no vale | TC |
| 3 | Joe (1993). «Tests of uniformity for sets of lotto numbers». Stat. Probab. Lett. 16(3): 181–188 | 10.1016/0167-7152(93)90141-5 | Deriva estadísticos χ² para uniformidad de marginales de k-tuplas; muestra que Σ(O−E)²/E no es apropiado sin corrección | Corrección para números individuales: J = (N−1)·X²/(N−k), con límite χ² de N−1 grados de libertad (según Genest et al.) | No aplica | No pude leer la aplicación a datos | RES + SEC |
| 4 | Johnson y Klotz (1993). «Estimating Hot Numbers and Testing Uniformity for the Lottery». J. Am. Stat. Assoc. 88(422): 662–668 | 10.1080/01621459.1993.10476320 (JSTOR 10.2307/2290349) | Modelo de extracción secuencial sin reposición con probabilidad propia por bola; máxima verosimilitud y razón de verosimilitud generalizada; datos de Lotto America; simulación | No pude leer el valor del estadístico ni el veredicto | No la conozco | Solo resumen. **La pista «The atom bomb and the Lotto» no corresponde a este título; ver sección 6** | RES |
| 5 | Haigh (1997). «The Statistics of the National Lottery». J. R. Stat. Soc. A 160(2): 187–206 | 10.1111/1467-985X.00056 | Lotería Nacional del Reino Unido, primeros 96 sorteos; frecuencias individuales y tiempos de espera entre apariciones | Compatible con azar en ambas medidas. Las combinaciones elegidas por los jugadores están lejos de ser aleatorias | Ninguna por la máquina; sí mejora el retorno medio evitar combinaciones populares | 96 sorteos es poca potencia. Sin detalle de máquinas ni juegos de bolas en lo que leí | RES |
| 6 | Coronel-Brizio, Hernández-Montoya, Rapallo y Scalas (2008). «Statistical auditing and randomness test of lotto k/N-type games». Physica A 387(25): 6385–6390 | 10.1016/j.physa.2008.07.017; arXiv:0806.4595 | Melate de México (6/N con N = 39, 44, 47, 51) y lotto italiano 5/90, rueda de Roma. Estadístico Q sobre el vector ordenado contra media y covarianza hipergeométricas; χ² con k grados de libertad y Monte Carlo de 5000 réplicas | Melate: N = 39, 555 sorteos, p = 0,41; N = 44, 992 sorteos, p = 0,87; N = 47, 330 sorteos, p = 0,94; **N = 51, 211 sorteos, Q = 18,25, p = 0,0056**. Italia: **P1, 450 sorteos, Q = 31,17, p < 10⁻⁵**; P2 p = 0,84; P3 p = 0,90; P4 p = 0,15 | No la cuantifican; no identifican qué números ni la causa | Ocho pruebas sin corrección. 211 sorteos en el período que rechaza. Fechas italianas incoherentes entre texto y tabla. No describen máquina ni bolas | TC (ar5iv) |
| 7 | Gutiérrez-Pulido y García (2010). «Verificación y monitoreo de la aleatoriedad de los juegos de números de d dígitos». Rev. Colomb. Estad. 33(2): 167–190 | https://emis.muni.cz/journals/RCE/V33/v33n2a01.html (sin DOI en la página) | Prueba bayesiana multinomial y carta de control geométrica; 500 sorteos del Tris de México | Informan problemas de falta de aleatoriedad en el Tris, detectados por ambos métodos | No la conozco | Solo resumen: sin cifras ni mecanismo físico | RES |
| 8 | Rozkovec (2012). «Probability Distributions in Lottery Games». 6th Int. Days of Statistics and Economics, Praga, pp. 973 y ss. | https://msed.vse.cz/files/2012/Rozkovec_2012.pdf | Sportka checa (6 o 7 de 49), 1957–2010, χ² por año y por sorteo, valor crítico 65,17 con 48 g. l. | Ningún año rechaza la uniformidad; máximos 64,88 (Sorteo I, 1993) y 61,65 (Sorteo II, 1981). En cambio la distribución del mínimo sí se rechaza (χ² = 180,57 frente a crítico 58,12) | Ninguna | No aplica la corrección por extracción sin reposición. El rechazo del mínimo queda sin explicar y puede ser un artefacto de datos. Leí la primera mitad | TC parcial |
| 9 | Souza (2017). «Considerações sobre a aleatoriedade dos concursos da Mega Sena». Holos 8: 65–75 | 10.15628/holos.2017.5647 | Prueba de hipótesis de equiprobabilidad sobre los concursos de la Mega-Sena de Brasil | No pude leer cifras | — | Solo metadatos y descripción del resumen en buscador | META |
| 10 | Vahaplar y Berberler (2020). «Analysis of Turkish 6/49 lottery results». MANAS J. Eng. 8(1): 55–58 | https://dergipark.org.tr/tr/pub/mjen/article/712154 | Todos los sorteos del 6/49 turco, pruebas de confianza estadística | Sin cifras en el resumen; sostienen que las estrategias populares carecen de base | — | Solo resumen | RES |
| 11 | Hassler y Pohle (2022). «Unlucky Number 13? Manipulating Evidence Subject to Snooping». Int. Stat. Rev. 90: 397–410 | arXiv:2009.02198 | Usan el loto alemán 6/49 para mostrar cómo mirar los datos antes de elegir la hipótesis fabrica un «13 desafortunado» | Advertencia metodológica: elegir el número a probar después de ver las frecuencias invalida el valor p | Ninguna | Solo resumen | RES |

### 3.3 Mezcla física insuficiente: sorteo militar de EE. UU.

| # | Referencia | DOI o URL | Resultado | Lectura |
|---|---|---|---|---|
| 12 | Fienberg (1971). «Randomization and Social Affairs: The 1970 Draft Lottery». Science 171(3968): 255–261 | 10.1126/science.171.3968.255 | Subtítulo del propio artículo: la aleatorización no se logra fácilmente mezclando cápsulas en un recipiente. Promedios mensuales del número de sorteo decrecientes, de 201,2 en enero a 121,5 en diciembre (p. 260, según cita secundaria). Las cápsulas se cargaron mes a mes; las de enero se mezclaron once veces y las de diciembre una; se volcaron a un bol y no se revolvieron | META + SEC |
| 13 | Rosenblatt y Filliben (1971). «Randomization and the Draft Lottery». Science 171(3968): 306–308 | 10.1126/science.171.3968.306 | Analizan el sorteo de 1971 y concluyen que el proceso fue efectivamente aleatorio (según Starr) | META + SEC |
| 14 | Starr (1997). «Nonrandom Risk: The 1970 Draft Lottery». J. Stat. Educ. 5(2) | 10.1080/10691898.1997.11910534; https://jse.amstat.org/v5n2/datasets.starr.html | 366 cápsulas, sorteo del 1 dic 1969. Pendiente y correlación entre día del año y orden = −0,226, p ≈ 0 a cuatro decimales. χ² de mitades del año contra mediana = 13,388, 1 g. l., p < 0,0005. Sorteo de 1971: χ² = 0,463, p = 0,50 | TC |

Ventaja predictiva en este caso: sí existía en sentido estadístico (un nacido en diciembre tenía un número medio de 121,5 frente a 183,5 esperado), pero se conoce a posteriori; nadie podía predecir el orden de una cápsula concreta.

### 3.4 Sesgo de selección de los jugadores (fenómeno distinto)

| # | Referencia | DOI o URL | Qué establece | Lectura |
|---|---|---|---|---|
| 15 | Stern y Cover (1989). «Maximum Entropy and the Lottery». J. Am. Stat. Assoc. 84(408): 980–985 | 10.1080/01621459.1989.10478862 | Estiman la distribución de los boletos comprados en el Lotto 6/49 de Canadá; usan el ajuste por extracción sin reposición (según Genest et al.). Trata de qué eligen los jugadores, no de la máquina | META + SEC |
| 16 | Farrell, Hartley, Lanot y Walker (2000). «The Demand for Lotto: The Role of Conscious Selection». J. Bus. Econ. Stat. 18(2): 228–241 | 10.1080/07350015.2000.10524865 | Selección consciente de números en la demanda de lotto | META |
| 17 | Cook y Clotfelter (1993). «The Peculiar Scale Economies of Lotto». Am. Econ. Rev. 83(3): 634–643 | https://ideas.repec.org/a/aea/aecrev/v83y1993i3p634-43.html (documento de trabajo NBER 10.3386/w3766) | Las ventas por habitante de lotto crecen con la población; los jugadores juzgan la probabilidad por la frecuencia con que alguien gana | RES |
| 18 | Clotfelter y Cook (1993). «The "Gambler's Fallacy" in Lottery Play». Manage. Sci. 39(12): 1521–1525 | 10.1287/mnsc.39.12.1521 | Falacia del jugador en juegos de números | META |
| 19 | Baker y McHale (2009). «Modelling the Probability Distribution of Prize Winnings in the UK National Lottery: Consequences of Conscious Selection». J. R. Stat. Soc. A 172(4): 813–834 | 10.1111/j.1467-985X.2009.00599.x | La selección consciente vuelve sobredispersos y correlacionados los conteos de ganadores; elegir números impopulares sube el valor esperado del boleto | RES |
| 20 | Baker y McHale (2011). «Investigating the Behavioural Characteristics of Lottery Players by Using a Combination Preference Model for Conscious Selection». J. R. Stat. Soc. A 174(4): 1071–1086 | 10.1111/j.1467-985X.2011.00693.x | Modelo de preferencia por combinaciones; Reino Unido y El Gordo de la Primitiva de España | RES |
| 21 | Finkelstein (1995). «Estimating the frequency distribution of the numbers bet on the California lottery». Appl. Math. Comput. 69(2–3): 195–207 | 10.1016/0096-3003(94)00126-O | Distribución de números apostados en California | META |

Regla para no confundirlos: el sesgo del jugador no altera qué bola sale; altera entre cuántos se reparte el pozo. La «ventaja» que da es de pago esperado, nunca de probabilidad de acierto.

### 3.5 Aprendizaje automático y frecuencias históricas

| # | Fuente | Qué es | Línea base | Lectura |
|---|---|---|---|---|
| 22 | Birk (2024). «SmileyNet – Towards the Prediction of the Lottery by Reading Tea Leaves with AI». arXiv:2407.21385 | **Sátira declarada** por el autor: acumula errores metodológicos típicos; «72 % de acierto» en lanzamientos de moneda | Deliberadamente defectuosa; material docente | RES |

No encontré ningún artículo revisado por pares que prediga extracciones de lotería y supere el azar. Las búsquedas (buscador general y OpenAlex) devolvieron repositorios de código, notas de prensa comerciales y textos de divulgación. Un análisis informal publicado en Medium compara una estrategia de «IA» con selección al azar y obtiene 0,7359 frente a 0,7352 aciertos medios por sorteo; es divulgación, no evidencia.

---

## 4. Fraudes y fallos documentados

Distinción que mantengo: **(A)** manipulación deliberada del mecanismo físico; **(B)** manipulación deliberada del mecanismo electrónico; **(C)** fallo sin dolo; **(D)** incidente de transmisión o avería sin efecto probado en el resultado. No encontré ningún caso documentado de sesgo natural de una máquina certificada que alguien haya explotado.

### 4.1 (A) Manipulación física

**Pensilvania, «Triple Six Fix», 24 de abril de 1980.**
- Juego: The Daily Number, tres máquinas de aire con 10 bolas tipo ping-pong cada una.
- Mecanismo: se fabricaron réplicas de las bolas oficiales y se lastraron todas menos las 4 y las 6, inyectando pintura látex blanca con jeringa. Solo podían salir ocho combinaciones (444, 446, 464, 466, 644, 646, 664, 666). Salió 666. Las bolas se cambiaron antes y después del sorteo y se quemaron media hora después.
- Participantes: Nick Perry (locutor del sorteo, WTAE), Joseph Bock (director de arte), Edward Plevel (funcionario de la lotería que dejó las máquinas sin custodia), hermanos Maragos (compra de boletos).
- Montos: pago récord de 3,5 millones de dólares; unos 1,18 millones a los conspiradores según una fuente, 1,8 millones «en juego» según otra.
- Detección: no por estadística de sorteos, sino por el patrón anómalo de apuestas sobre las ocho combinaciones y una pista anónima.
- Resultado judicial: Perry y Plevel condenados en mayo de 1981 (las fuentes difieren: 11 o 20 de mayo). Perry: conspiración, daño, hurto por engaño, amaño de concurso público y perjurio; 7 años, cumplió 2 más 1 en régimen intermedio. Plevel: 2 años.
- Fuentes leídas: Wikipedia «1980 Pennsylvania Lottery scandal» (cita Pittsburgh Post-Gazette 24-04-2003, TribLIVE 27-04-2008, LA Times 29-04-2003, Altoona Mirror 16-05-1981); LotteryUSA (25-12-2024). Nivel: prensa y enciclopedia. **No localicé la sentencia ni su cita oficial.**
- Enseñanza para la revisión: el lastre necesario para «amarrar» fue grosero (solo dos dígitos podían subir), muy lejos del 1–5 % del experimento tailandés.

**Milán, lotto italiano, 1995–1999.**
- Mecanismo: los números los extraían niños vendados de un bombo. Las bolas «ganadoras» se barnizaban para dejarlas más lisas, se hacían algo más grandes o se calentaban o enfriaban para que los niños las reconocieran al tacto; las vendas se aflojaban; a los niños se les pagaba con dinero y juguetes.
- Cronología: primer sorteo amañado declarado, 15 de abril de 1995; tiroteos en Milán en noviembre de 1998; nueve detenidos en enero de 1999 (funcionarios del Ministerio de Finanzas, un policía, inspectores de impuestos).
- Alcance: 112 sospechosos identificados según Codacons; daños estimados en 200 mil millones de liras; penas de más de tres años para Aliberti y Curatoli.
- Fuente leída: LotteryUSA (20-07-2025), que cita BBC, The Guardian, La Stampa, Corriere della Sera y Codacons. Nivel: prensa secundaria. No leí las fuentes italianas originales.
- Es manipulación del extractor humano, no de una máquina.

### 4.2 (B) Manipulación electrónica

**Eddie Tipton, Multi-State Lottery Association (MUSL), sorteos de 2005 a 2011.**
- Cargo: director de seguridad de la información de MUSL; mantenía el software de los generadores de números aleatorios.
- Mecanismo: código instalado en el computador del generador (según la fiscalía, mediante memoria USB y con autoborrado). El peritaje del generador usado en Wisconsin en 2007 mostró que producía resultados conocibles el 27 de mayo, el 23 de noviembre y el 29 de diciembre, si caían en miércoles o sábado y el sorteo era después de las 20:00.
- Sorteos: Colorado 23-11-2005 (568.990 dólares); Wisconsin 29-12-2007 (783.257); Iowa, Hot Lotto 29-12-2010 (14,3 millones, nunca cobrado); Oklahoma 23-11-2011 (1,2 millones); también Kansas.
- Detección: intento de cobro anónimo del boleto de Iowa en 2011 y video de la compra; no hubo detección estadística.
- Resultado judicial: condena en julio de 2015 y 10 años en septiembre de 2015; *State v. Tipton*, 897 N.W.2d 653 (Iowa, 23-06-2017) anuló parte por prescripción; confesión en junio de 2017 y 25 años en agosto de 2017; libertad condicional en julio de 2022.
- Fuentes leídas: Wikipedia «Hot Lotto fraud scandal» (cita el fallo y Des Moines Register); CNN 22-08-2017 vía buscador. Nivel: expediente judicial citado por fuente secundaria. No leí el fallo.
- Enseñanza: un generador certificado puede ser determinista en condiciones raras sin que ninguna batería estadística sobre el historial lo note, porque afecta a tres fechas por año.

### 4.3 (C) Fallos sin dolo

- **Tennessee, Cash 3 y Cash 4, 28 de julio a 20 de agosto de 2007.** Un error de programación impedía que un dígito se repitiera dentro de un sorteo; boletos como 2-2-1 o 7-7-7-7 no podían ganar. Lo notó la propia lotería al ver que no había repetidos en tres semanas. Atribuido a un proveedor externo. La lotería había pasado de bolas a sorteo computarizado el mes anterior. Fuente: AP en Action News 5 (TC).
- **Arizona, 28 de septiembre a 3 de octubre de 2017.** Un generador produjo los mismos números en juegos sucesivos (Fantasy 5, Pick 3, All or Nothing, 5 Card Cash); la lotería retiró la máquina. Fuente: resultados de buscador (Arizona Republic, KGUN 9); no leí el artículo.
- **Lotería de visas de diversidad de EE. UU., DV-2012 (mayo de 2011).** Un programa nuevo generó un ordenamiento no aleatorio: más del 90 % de los seleccionados venía de los dos primeros días de inscripción según el Departamento de Estado (98 % según la reseña del informe del Inspector General en IEEE Spectrum). Se anuló el resultado; 22.000 personas ya lo habían visto. Causa: cambio de programa sin pruebas adecuadas. Fuente: IEEE Spectrum, R. Charette, 02-11-2011 (TC); fallo del Circuito de D. C. vía buscador.
- **Sorteo militar de 1969:** ver 3.3. Es el caso más limpio de sesgo físico sin dolo.

### 4.4 (D) Incidentes de transmisión o avería

- **Serbia, julio de 2015.** En el sorteo televisado apareció en pantalla el número 21 cuando la máquina había soltado el 27; el 21 salió a continuación. La lotería estatal lo atribuyó a un error de quien cargaba el gráfico. La policía interrogó a seis personas con polígrafo e incautó equipos; el director, Aleksandar Vulović, renunció. No encontré resultado de la investigación. Fuentes: The Register 03-08-2015 (TC, cita a AP); OCCRP y Reuters vía buscador.
- **Reino Unido.** 30-11-1996: la máquina no arrancó en vivo. 07-11-2015: la máquina de Lotto no liberó todas las bolas; el sorteo se hizo después fuera del aire. Fuente: Wikipedia «National Lottery (United Kingdom)». Sin efecto alegado en la aleatoriedad.
- El control L.2.3.6 de WLA-SCS:2020 existe precisamente para este tipo de incidente (errores de gráfica que hacen creer al público que el sorteo está comprometido).

### 4.5 Pistas que no se confirmaron como manipulación de bolas

- **China:** no encontré ningún caso con fuente seria de bolas o máquinas alteradas. Lo documentado es otra cosa: Xi'an 2004 (boleto ganador declarado falso), Anshan 2007–2008 (un agente explotó una falla del sistema «3D» para comprar tras conocerse el resultado; cadena perpetua), Shenzhen 2009 (un ingeniero falsificó registros de boletos).

---

## 5. Estándares y tolerancias con cifras

### 5.1 Estándar sectorial: WLA-SCS:2020

Fuente: World Lottery Association, *WLA Security Control Standard* WLA-SCS:2020, versión 1.1 revisada el 10-12-2020 (PDF en inglés, 29 páginas; leí el anexo B, sección L.2, en texto completo). https://world-lotteries.org/volumes/downloads/Download_Center/Security/WLA_SCS_2020/202012_EN_WLA-SCS-2020_Standard_V1-2.pdf

Estructura: anexos A (controles G, generales), B (controles L, operadores), C (controles S, proveedores), D (controles M, juegos multijurisdiccionales); 120 controles.

Controles sobre sorteos físicos (L.2.3, «Physical drawing appliances and ball sets»):

| Control | Qué exige |
|---|---|
| L.2.3.1 | Procedimiento de inspección de máquinas y juegos de bolas a la entrega y después, periódicamente, en consulta con una autoridad independiente |
| L.2.3.2 | Inspección y mantenimiento de las máquinas documentados **al menos una vez al año** |
| L.2.3.3 | Uso de juegos de bolas fabricados con medidas y tolerancias de peso compatibles con la máquina |
| L.2.3.4 | Máquina y juego de bolas de reemplazo disponibles si el sorteo se transmite en vivo |
| L.2.3.5 | Almacenamiento, traslado y manipulación seguros de máquinas y bolas |
| L.2.3.6 | Procedimiento para minimizar errores de gráfica, retardo o corrupción en la transmisión |

Además: L.2.1 (el sorteo como evento planificado, equipo de sorteo, reservas, observadores independientes) y L.2.2 (procedimiento paso a paso, asistencia de auditor u oficial de cumplimiento, seguridad del equipo, emergencias).

**El estándar no fija ninguna tolerancia numérica** de peso ni de diámetro, ni un número de sorteos de prueba, ni una prueba estadística. Remite a las especificaciones del fabricante y del regulador.

### 5.2 Cifras de operadores y reguladores

| Jurisdicción | Fuente (tipo) | Bolas | Tolerancia de peso | Diámetro | Frecuencia y control | Lectura |
|---|---|---|---|---|---|---|
| Texas (EE. UU.) | Texas Lottery, «Drawing Procedures» (documento del operador) | Tipo ping-pong (Cash Five, Pick 3, Daily 4, Two Step, All or Nothing); caucho natural (Lotto Texas). Máquinas Smartplay y Garron | Ping-pong: cada bola **dentro de 0,095 g del promedio del juego**. Caucho: **dentro de 1 g del promedio del juego** | No indica | Rotación mensual de máquinas; el juego de bolas se designa según el resultado del día anterior; firma contable independiente observa el pesaje; un estadístico independiente revisa pesos, pruebas previas y resultados | TC |
| Nueva Zelanda | Lotto NZ, respuesta a solicitud de información oficial, 08-04-2019 (documento del operador) | Espuma plástica, macizas, sin metal ni material magnético | **11 g a 13 g** por bola; **variación máxima de 0,45 g** entre la más pesada y la más liviana del juego | Diseño 50 mm; **49,0 a 51,5 mm** | Inspección visual antes de cada sorteo; cada 10 sorteos como máximo se revisan, limpian y pesan una a una ante Audit NZ; cuatro juegos (Lotto A y B, Powerball A y B); el juego se elige por lanzamiento de moneda; si una bola falla se retira todo el juego. A la fecha ninguna había fallado | TC |
| Washington (EE. UU.) | Washington State Register, WSR 00-04-042, 26-01-2000 (norma) | Juego Lucky for Life | Rango de tolerancia reducido **de 2 g a 1 g** (políticas 110.552 y 110.554, nov. de 1999) | No indica | Auditor externo decide el reemplazo de juegos rechazados | TC |
| Florida (EE. UU.) | Regla de emergencia 53ER10-6, «Draw Procedures», vigente 01-03-2010 (norma) | Máquinas de aire; la bola vale solo si queda atrapada arriba | Remite al rango del fabricante, sin cifra. Según resumen de otra versión de la regla que no leí, un juego que varíe más de 1 g respecto de su peso previo se retira e investiga | No indica | Máquina y juego elegidos al azar, con primario y secundario. **Sorteos de prueba:** Lotto 6 (si un mismo dígito sale 4 veces, 4 más; se rechaza si sale 2 veces más); Fantasy 5: 7; Mega Money: 6; Play 4 y Cash 3: 5 (si sale 3 veces, 3 más; se rechaza con 2 más). Contador público independiente certifica | TC |
| Irlanda | NSAI, laboratorio nacional de metrología (documento institucional) | — | «Similares y dentro de las tolerancias permitidas», sin cifras | Sin cifras; también esfericidad, textura y tamaño de fuente | Comparadores de masa de precisión; ensayos de repetibilidad y muestreo de la máquina; KPMG observa los sorteos | TC |

Lectura conjunta, cálculo propio: 0,095 g sobre una bola tipo ping-pong de 2,7 g es alrededor de ±3,5 %; 0,45 g de rango sobre 12 g es 3,75 %; 1 g sobre una bola de caucho de unos 80 g (masa no verificada) sería del orden de ±1,2 %. Las tolerancias públicas admiten diferencias relativas del mismo orden que las que produjeron un sesgo medible en la máquina tailandesa. Esto no demuestra sesgo en máquinas reales, porque la dinámica es otra, pero tampoco hay un estudio publicado que lo descarte.

### 5.3 Fabricantes

**Smartplay International** (Nueva Jersey; páginas del fabricante, leídas en TC; son material comercial):

- Bolas: espuma de celda cerrada de 40 o 50 mm (máquinas de gravedad y algunas de aire); grado tenis de mesa de 38 o 40 mm (máquinas de aire); «SmartBall» de espuma con etiqueta RFID. No publican masas ni tolerancias numéricas; hablan de «juegos emparejados» con tolerancias muy estrechas.
- Sistema de validación DBVS: balanza de 0,001 g y micrómetro opcional de 0,01 mm; calibre pasa/no pasa para diámetro.
- Afirmación del fabricante, sin datos: la diferencia entre un sorteo aleatorio y uno sesgado puede ser de milésimas de gramo. Es publicidad de un instrumento de medición; no hay estudio que la respalde.
- Control de calidad declarado: lista de 59 ítems y 100 juegos simulados por máquina con la configuración del cliente (LotteryUSA, 25-12-2024, citando al fabricante).
- Modelo Magnum: mezcla por gravedad con paletas horizontales, 300 bolas de capacidad, extrae hasta 12, bolas de espuma de 50 mm; cliente declarado: Lotería Nacional del Reino Unido.
- Historial británico (Wikipedia): 1994, máquinas Criterion de Beitel; 2003, Magnum I; 2009, Magnum II para Lotto; Halogen II para Thunderball.

**GLI:** la hoja institucional de GLI dice que la empresa ensaya sistemas de sorteo automatizado (ADM), generadores y juegos de loto. Que GLI-11 sea el estándar aplicable a máquinas de bolas lo afirma solo un artículo comercial de Smartplay (10-09-2026); GLI-11 es el estándar de dispositivos de juego. No lo doy por verificado (sección 6).

### 5.4 Tipos de máquina

| Tipo | Funcionamiento | Bolas | Dónde se usa | Fuente |
|---|---|---|---|---|
| Gravedad con paletas («gravity pick» o «gravity mix») | Las bolas caen a una cámara con paletas que giran en sentidos opuestos; salen de a una por una compuerta o por un eje que sube; un sensor óptico confirma la cantidad | Espuma o caucho, 50 mm | Lotto del Reino Unido, Mega Millions, Powerball, EuroMillions | LotteryUSA 25-12-2024; Wikipedia «Lottery machine» (una sola referencia de divulgación); Smartplay |
| Aire («air mix») | Un ventilador o chorros de aire agitan las bolas; una válvula abre paso a un tubo y la bola empujada es la ganadora | Livianas, tipo ping-pong | Juegos diarios de dígitos en EE. UU., Eurojackpot | Ídem; regla 53ER10-6 de Florida describe el mecanismo |
| Manual con bombo | Una persona gira el tambor y otra recoge la bola | — | Lat Krabang 6 de Tailandia según Pinitsoontorn et al.; lotto italiano histórico | Pinitsoontorn et al. 2014 |

Consecuencia para la revisión: el único experimento sobre masa es de una máquina de aire. En una de gravedad con paletas el mecanismo de selección es distinto y el sentido del efecto de la masa no está medido.

---

## 6. No verificadas

Cosas que no pude confirmar en esta sesión. No deben citarse como hechos.

1. **«The atom bomb and the Lotto» de Johnson y Klotz.** No existe con ese título en Crossref ni en buscadores. El artículo real de esos autores es «Estimating Hot Numbers and Testing Uniformity for the Lottery» (JASA 1993), con datos de Lotto America según su resumen. No confirmé que trate de la lotería de Wisconsin ni que encuentre sesgo.
2. **Resultado numérico de Johnson y Klotz, Joe y Haigh** más allá de sus resúmenes: no accedí al texto completo (de pago).
3. **Informes de la Royal Statistical Society o del Centre for the Study of Gambling de Salford** para la National Lottery Commission sobre aleatoriedad de los sorteos. Solo hallé una mención secundaria (lottery.co.uk) a un estudio de Salford de 2010 sobre los boletos automáticos de EuroMillions, no sobre las máquinas.
4. **Masa y tolerancia de las bolas del Reino Unido, Powerball, EuroMillions y Loterías y Apuestas del Estado.** Para Powerball circula «unos 80 g, diferencia media de 0,3 g, pesadas, medidas y radiografiadas», pero solo en sitios de baja calidad. Sin documento oficial.
5. **GLI-11 o GLI-19 como norma aplicable a máquinas de bolas.** Solo lo afirma el fabricante. No consulté el texto de GLI.
6. **Especificaciones de WinTV/Editec (Venus) y Ryo-Catteau (Stresa, Topaze).** Las búsquedas no devolvieron nada utilizable.
7. **Tolerancia de ±0,065 g en Florida, 1992** (Tampa Bay Times, «Nothing random about Lotto balls», 01-12-1992). Apareció en un resumen de buscador; el artículo no se dejó leer.
8. **Sudáfrica, 2009** (Sowetan, ensayo de bolas con calibre y peso objetivo ante auditores y regulador). Solo resumen de buscador.
9. **Manipulación de bolas en China.** Sin fuente.
10. **Arizona 1998, Pick 3 sin nueves.** No apareció; lo que hay en Arizona es de 2017.
11. **Sentencias originales** de Pensilvania (no hallé la cita; el nombre «Commonwealth v. Perry» o «v. Katsafanas» no está confirmado) y el texto de *State v. Tipton*, que conozco por cita.
12. **Estudios tailandeses citados por Pinitsoontorn et al.:** Veerathaworn (1985 y libro electrónico de 2014, 257 sorteos, rechaza uniformidad del primer premio); Panichkitkosolkul y Lertsuwansri (2004); Ruangpraphan et al., KKU Res. J. 2008; 13(2): 214–224 (Tailandia frente a Laos). Los conozco solo por la cita.
13. **Bellhouse (1982), «Fair is fair: new rules for Canadian lotteries», Can. Public Policy 8: 311–320.** Solo por la lista de referencias de Genest et al.
14. **Cox, Daniell y Nicole (1998),** máxima entropía sobre la Lotería Nacional británica (113 sorteos). Solo resumen de buscador.
15. **Cifras exactas de Fienberg (1971)** (promedios mensuales, relato de las once mezclas): vienen de citas secundarias, no del artículo de Science.
16. **Análisis publicados de la Primitiva española, EuroMillions o Powerball** con pruebas de uniformidad: no encontré ninguno.
17. **Souza (2017), Mega-Sena:** existencia y DOI confirmados por buscador; no leí el resultado.

---

## 7. Vacíos

1. **No hay experimento publicado con máquina comercial.** Falta un ensayo con una máquina certificada (aire y gravedad), bolas reales, masa controlada dentro y fuera de tolerancia, réplicas y al menos 10⁴ extracciones por condición.
2. **No hay curva dosis–respuesta.** El único dato da el mismo efecto para 1 % y 5 %, sin réplicas. No se sabe a partir de qué diferencia de masa aparece un sesgo.
3. **No se han estudiado otras variables físicas:** diámetro, esfericidad, rugosidad, masa de la tinta del número, carga estática, humedad, desgaste. El artículo tailandés sugiere que pesan tanto como la masa.
4. **Los datos de control de los operadores no son públicos:** pesos por bola y por fecha, resultados de los sorteos de prueba, identidad de la máquina y del juego de bolas usados en cada sorteo. Sin eso no se puede estratificar un análisis histórico, y agrupar todo diluye cualquier sesgo de un juego concreto.
5. **Ningún análisis publicado estratifica por máquina y juego de bolas.** Genest et al. lo advierten: si cambian mecanismo o bolas, sus pruebas ya no aplican.
6. **Falta potencia declarada.** Casi ningún estudio dice qué tamaño de sesgo habría podido detectar. Con 6,3 % de desvío relativo por número en veinte años de un 6/49, «no se rechaza» dice poco sobre sesgos chicos.
7. **Dependencia serial y orden de extracción** casi no se prueban; los estadísticos de frecuencia no los ven.
8. **Los hallazgos de no aleatoriedad en México e Italia no tienen seguimiento:** no hay réplica con datos posteriores ni causa física identificada.
9. **Del sesgo a la apuesta:** nadie cuantifica cuánto sesgo haría falta para que un apostador supere la ventaja de la casa. No verifiqué en esta sesión el porcentaje de retorno de ningún juego, así que no afirmo si un sesgo de 3 puntos en una bola alcanzaría o no.
10. **Los estándares no fijan cifras.** WLA-SCS exige procedimientos; las tolerancias quedan en contratos y manuales de fabricante que no son públicos.
11. **No hay literatura revisada por pares sobre predicción con aprendizaje automático** que use una línea base de azar; el campo está ocupado por material comercial.
12. **Generadores electrónicos:** los casos de Tipton, Tennessee y Arizona muestran fallos estructurales que una prueba de frecuencias no detecta. La transición de bolas a generadores cambia el tipo de riesgo y cae fuera de este encargo.
