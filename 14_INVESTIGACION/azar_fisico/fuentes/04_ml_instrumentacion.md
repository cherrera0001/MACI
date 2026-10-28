# 04 · Aprendizaje automático, instrumentación y simulación en sistemas físicos caóticos

Agente: especialista en ML, visión computacional y sistemas ciberfísicos.
Fecha de verificación de todas las fuentes y URL: 2026-10-09.
Alcance: qué se ha logrado con ML e instrumentación en sistemas caóticos o estocásticos y qué herramientas abiertas existen. Quedan fuera (los cubren otros agentes): física del caos de monedas, dados y ruleta, literatura de loterías y fraudes, NIST y pruebas estadísticas, caso chileno.

Convenciones de este documento:

- **[H]** hecho documentado en la fuente. **[E]** resultado experimental o numérico reportado por la fuente. **[I]** inferencia mía. **[Hip]** hipótesis sin respaldo directo.
- Nivel de lectura: **TC** texto completo, **R** resumen, **M** solo metadatos (Crossref, arXiv o API del repositorio).
- «Tiempo de Lyapunov» (T_L) = 1/λ_max, el tiempo medio en que un error crece por un factor e.
- Método de verificación: DOI contra `https://api.crossref.org/works/<DOI>`, arXiv contra `export.arxiv.org/api/query`, repositorios contra `api.github.com/repos/...`, `gitlab.com/api/v4`, `api.bitbucket.org` y `api.osf.io`.

---

## 1. Síntesis

1. **[E]** El mejor horizonte de predicción publicado para caos espaciotemporal con ML puro es del orden de unidades de T_L: unos 8 T_L en Kuramoto-Sivashinsky con reservorios en paralelo (Pathak et al. 2018, texto completo leído), y entre 0,5 y 4,8 T_L según modelo y observabilidad en la comparación sistemática de Vlachas et al. (2020).
2. **[E]** Con estado parcialmente observado el horizonte cae a menos de 1–1,2 T_L (Vlachas 2020, Lorenz-96 con 35 de 40 variables). Un bombo filmado es, por construcción, un sistema parcialmente observado (oclusiones, giro de las bolillas no visible).
3. **[E]** En sistemas de baja dimensión (3 a 6 variables, sin ruido, simulados) los métodos de gran escala alcanzan «hasta dos docenas» de T_L (Gilpin 2023, resumen); los modelos fundacionales sin entrenamiento específico llegan a cerca de 1 T_L y luego conservan la geometría del atractor, no la trayectoria (Zhang y Gilpin 2025).
4. **[H]** Todos esos resultados son sobre sistemas **suaves, disipativos, simulados y con atractor estacionario**. Ninguno trata dinámica no suave con colisiones entre muchos cuerpos rígidos.
5. **[E]** Las PINN fallan incluso en problemas no caóticos de convección, reacción y difusión (Krishnapriyan 2021), necesitan reformulación causal para Lorenz o Kuramoto-Sivashinsky (Wang 2022/2024) y en el péndulo doble convergen a una trayectoria distinta de la real (Steger 2022).
6. **[E]** Los operadores neuronales y los simuladores aprendidos de partículas reproducen **estadísticas** de largo plazo (medida invariante, distancia de escurrimiento, perfiles) y no trayectorias individuales (Li 2021/2022; Sanchez-Gonzalez 2020; Choi y Kumar 2024; NeuralDEM 2024).
7. **[E]** El antecedente más cercano a un dado con ML es el lanzamiento de un cubo real de 10 cm seguido con tres cámaras a 148 Hz (ContactNets, 570 lanzamientos); los autores atribuyen el error residual a «comportamiento de contacto estocástico y datos ruidosos». No evalúan la cara final.
8. **Vacío [H de búsqueda]**: no encontré ningún trabajo revisado por pares que use ML sobre vídeo o sensores para predecir el resultado de una máquina de bolillas de lotería. Para dados hay un único grupo (Dimitriadis, Koutsoyiannis, Tzouka 2013/2016) con vídeo a 120 Hz y modelo estadístico; para ruleta, Small y Tse (2012) usan física y cámara, no ML; el único intento con redes profundas hallado es un repositorio de aficionado que declara que no funcionó.
9. **[E]** La instrumentación para medir el estado existe: seguimiento lagrangiano 3D denso (Shake-The-Box), PEPT (0,5 mm a unas 250 localizaciones por segundo para un trazador a 1 m/s), seguimiento magnético, esferas instrumentadas con acelerómetro y giróscopo (36 mm de diámetro, 1 kHz y 8 kHz).
10. **[E]** La inestabilidad de N cuerpos en DEM de esfera blanda está medida: Fullmer et al. (2022) estiman el mayor exponente de Lyapunov y muestran que crece con la rigidez del contacto y con la concentración por encima del 30 %.
11. **[I]** De 9 y 10 se sigue que la pregunta útil no es «qué red neuronal», sino cuántos T_L dura la agitación antes de la extracción y con qué error se puede medir el estado inicial. El horizonte predecible escala como T_L · ln(tolerancia / error inicial): mejorar la medición diez veces solo añade unos 2,3 T_L.
12. **[Hip]** Si un sorteo dura decenas o cientos de T_L del conjunto de bolillas, la predicción de la bolilla concreta desde vídeo queda fuera del alcance de cualquiera de los métodos revisados. **Nadie ha medido el T_L de un bombo de lotería**, así que esto es hipótesis, no resultado.
13. **[I]** Lo que sí es abordable con las herramientas abiertas listadas: (a) detectar **sesgos estadísticos** (bolillas más pesadas, asimetrías de flujo) con CFD-DEM calibrado; (b) estimar el T_L del bombo por simulación con el protocolo de Fullmer; (c) medir trayectorias reales para validar (a) y (b).
14. **[H]** Que un método prediga Lorenz o Kuramoto-Sivashinsky algunos T_L **no dice** que prediga un bombo de bolillas. Ninguna fuente aquí reunida hace esa extrapolación y este documento tampoco la hace.
15. Recuento: 49 publicaciones y 34 repositorios o conjuntos de datos confirmados en esta sesión; lo no confirmado está en la sección 7.

---

## 2. ML en sistemas caóticos: fuentes verificadas

| # | Referencia | Método y sistema | Resultado principal (cifras) | Limitaciones | Evidencia / lectura |
|---|---|---|---|---|---|
| 1 | Pathak J., Hunt B., Girvan M., Lu Z., Ott E. (2018). «Model-Free Prediction of Large Spatiotemporally Chaotic Systems from Data: A Reservoir Computing Approach». *Phys. Rev. Lett.* 120, 024102. DOI 10.1103/PhysRevLett.120.024102 | Reservoir computing; reservorios en paralelo por regiones espaciales. Kuramoto-Sivashinsky simulada, L = 200, Q = 512 puntos, 64 reservorios de 5000 nodos | **[E]** «low prediction error is obtained for about 8 Lyapunov times». El esquema escala a L = 400, 800, 1600 manteniendo L/g | Datos simulados sin ruido, estado completo observado, sistema suave con interacción local | Numérico, un grupo. **TC** (manuscrito aceptado en link.aps.org/accepted) |
| 2 | Pathak J., Lu Z., Hunt B., Girvan M., Ott E. (2017). «Using machine learning to replicate chaotic attractors and calculate Lyapunov exponents from data». *Chaos* 27, 121102. DOI 10.1063/1.5010300 | Reservoir computing en Lorenz y Kuramoto-Sivashinsky | **[H]** el reservorio autónomo reproduce el «clima» del atractor y permite estimar exponentes de Lyapunov. Sin cifra de horizonte extraída | Simulado | **M** |
| 3 | Vlachas P., Byeon W., Wan Z., Sapsis T., Koumoutsakos P. (2018). «Data-driven forecasting of high-dimensional chaotic systems with long short-term memory networks». *Proc. R. Soc. A* 474, 20170844. DOI 10.1098/rspa.2017.0844 | LSTM en espacio reducido; Lorenz-96, Kuramoto-Sivashinsky, modelo climático prototipo | **[E]** LSTM supera a procesos gaussianos en corto plazo; se necesita un híbrido (MSM-LSTM) para converger a la medida invariante | El resumen no da horizonte en T_L | **R** |
| 4 | Vlachas P., Pathak J., Hunt B., Sapsis T., Girvan M., Ott E., Koumoutsakos P. (2020). «Backpropagation algorithms and Reservoir Computing in Recurrent Neural Networks for the forecasting of complex spatiotemporal dynamics». *Neural Networks* 126, 191–217. DOI 10.1016/j.neunet.2020.02.016; arXiv 1910.05266 | Comparación RC, LSTM, GRU. Tiempo de predicción válido (VPT) en T_L | **[E]** Lorenz-96 estado completo (40 var.): RC ≈ 2,31, GRU ≈ 1,34, LSTM ≈ 0,97. **Estado reducido (35 var.)**: RC ≈ 0,55, LSTM ≈ 0,74, GRU ≈ 0,98. Kuramoto-Sivashinsky en paralelo (512 var.): LSTM ≈ 4, GRU ≈ 3,5, RC ≈ 3,2 a 4,8 según tamaño | Simulado; el VPT es el máximo sobre hiperparámetros | Numérico. **TC parcial** (ar5iv, primeros 100 000 caracteres) |
| 5 | Platt J., Penny S., Smith T., Chen T., Abarbanel H. (2022). «A systematic exploration of reservoir computing for forecasting complex spatiotemporal dynamics». *Neural Networks* 153, 530–552. DOI 10.1016/j.neunet.2022.06.025 | Estudio sistemático de diseño de reservorios | Existencia confirmada; cifras no extraídas | — | **M** |
| 6 | Raissi M., Perdikaris P., Karniadakis G. (2019). «Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations». *J. Comput. Phys.* 378, 686–707. DOI 10.1016/j.jcp.2018.10.045 | PINN: el residuo de la EDP entra en la función de pérdida | Referencia fundacional (19 741 citas en Crossref). No es un trabajo sobre caos | No reporta horizonte en T_L | **M** |
| 7 | Krishnapriyan A., Gholami A., Zhe S., Kirby R., Mahoney M. (2021). «Characterizing possible failure modes in physics-informed neural networks». NeurIPS 2021. arXiv 2109.01050 | Análisis de fallos de PINN en convección, reacción y difusión | **[E]** las PINN «can easily fail to learn relevant physical phenomena for even slightly more complex problems»; el fallo es de optimización, no de expresividad. Currículo y seq2seq reducen el error «1–2 orders of magnitude» | No trata sistemas caóticos de muchos cuerpos | **R** |
| 8 | Wang S., Sankaran S., Perdikaris P. (2022/2024). «Respecting causality for training physics-informed neural networks» (arXiv: «Respecting causality is all you need…»). *Comput. Methods Appl. Mech. Eng.* 421, 116813. DOI 10.1016/j.cma.2024.116813; arXiv 2203.07404 | Reponderación causal de la pérdida temporal | **[H]** atribuye el fallo a no respetar la causalidad espaciotemporal; afirma ser la primera vez que una PINN resuelve Lorenz, Kuramoto-Sivashinsky caótica y Navier-Stokes turbulento | La PINN resuelve una EDP conocida con condición inicial exacta; no es pronóstico desde datos medidos | **R** |
| 9 | Steger S., Rohrhofer F. M., Geiger B. (2022). «How PINNs cheat: Predicting chaotic motion of a double pendulum». Taller de NeurIPS 2022. https://neurips.cc/virtual/2022/59901 | PINN sobre péndulo doble | **[E]** la PINN no responde a cambios pequeños de condición inicial y converge a otra trayectoria físicamente válida más fácil de ajustar | Trabajo de taller, experimentos iniciales | **R** (página del congreso) |
| 10 | Li Z., Kovachki N., Azizzadenesheli K., Liu B., Bhattacharya K., Stuart A., Anandkumar A. (2020). «Fourier Neural Operator for Parametric Partial Differential Equations». arXiv 2010.08895 | Operador neuronal en espacio de Fourier; Burgers, Darcy, Navier-Stokes | **[E]** «up to three orders of magnitude faster» que solvers clásicos; superresolución sin reentrenar | Aprende un operador de EDP en malla, no partículas discretas con contacto | **R** |
| 11 | Li Z., Liu-Schiaffini M., Kovachki N., Liu B., Azizzadenesheli K., Bhattacharya K., Stuart A., Anandkumar A. (2021). «Learning Dissipative Dynamics in Chaotic Systems». arXiv 2106.06898 | Operador de solución markoviano con disipación impuesta | **[E]** predice **estadísticas de la medida invariante** del flujo de Kolmogorov hasta Re = 5000; trayectorias solo a corto plazo | Requiere sistema disipativo con atractor | **R** |
| 12 | Brunton S., Proctor J., Kutz J. N. (2016). «Discovering governing equations from data by sparse identification of nonlinear dynamical systems». *PNAS* 113(15), 3932–3937. DOI 10.1073/pnas.1517384113 | SINDy: regresión dispersa sobre biblioteca de funciones candidatas | **[H]** recupera ecuaciones parsimoniosas desde datos. No da horizonte en T_L (cifras no extraídas) | Necesita derivadas limpias y una base en la que la dinámica sea dispersa; el contacto no suave no cumple lo segundo | **M + declaración de relevancia** |
| 13 | Gilpin W. (2021). «Chaos as an interpretable benchmark for forecasting and data-driven modelling». NeurIPS 2021. arXiv 2110.05266 | Base de 131 sistemas caóticos; 16 modelos de pronóstico | **[E]** Transformer y NBEATS con el menor error mediano; «a high degree of correlation between the largest Lyapunov exponent and the forecast error» | No expresa el horizonte en T_L | **TC** (ar5iv) |
| 14 | Gilpin W. (2023). «Model scale versus domain knowledge in statistical forecasting of chaotic systems». *Phys. Rev. Research* 5, 043252. DOI 10.1103/PhysRevResearch.5.043252; arXiv 2303.08011 | 24 métodos, 135 sistemas de baja dimensión, 17 métricas | **[E]** los métodos de gran escala agnósticos del dominio «remain accurate up to two dozen Lyapunov times» | Sistemas de 3 a 6 dimensiones, simulados, entrenamiento por sistema | **R** |
| 15 | Zhang Y., Gilpin W. (2025). «Zero-shot forecasting of chaotic systems». ICLR 2025. arXiv 2409.15771 | Chronos (8M a 710M parámetros) sin ajuste; 135 sistemas, 20 condiciones iniciales, contexto de 512 puntos, 30 puntos por T_L | **[E]** VPT de hasta ≈ 1 T_L sin entrenamiento; VPT casi exponencialmente distribuido entre condiciones iniciales; mecanismo de «context parroting»; se conserva la dimensión de correlación del atractor tras fallar el pronóstico puntual; la no estacionariedad degrada el resultado | Depende de un atractor estacionario y recurrente en el contexto | **TC** (arxiv.org/html, primeros 100 000 caracteres) |
| 16 | Ansari A. F., Stella L., Turkmen C., et al. (2024). «Chronos: Learning the Language of Time Series». arXiv 2403.07815 | Series tokenizadas sobre T5, 20M a 710M parámetros, 42 conjuntos de prueba | **[E]** rendimiento sin ajuste comparable a modelos entrenados por conjunto | No es un trabajo de caos | **R** |
| 17 | Lai J., Bao A., Gilpin W. (2025). «Panda: A pretrained forecast model for chaotic dynamics». arXiv 2505.13755 | Preentrenado en 2 × 10⁴ sistemas caóticos sintéticos | **[H]** afirma pronóstico sin ajuste de sistemas no vistos, series experimentales y EDP | El resumen no da cifras; el repositorio lo anuncia como ICLR 2026 (sede no confirmada en arXiv) | **R** |
| 18 | Sanchez-Gonzalez A., Godwin J., Pfaff T., Ying R., Leskovec J., Battaglia P. (2020). «Learning to Simulate Complex Physics with Graph Networks». ICML 2020. arXiv 2002.09405 | Simulador de red de grafos (GNS) entrenado a un paso | **[E]** generaliza de miles de partículas a «at least an order of magnitude more» y a despliegues de miles de pasos; fluidos, sólidos rígidos, materiales deformables | Evalúa plausibilidad y error agregado; no reporta T_L | **R** |
| 19 | Choi Y., Kumar K. (2024). «Graph Neural Network-based surrogate model for granular flows». *Comput. Geotech.* 166, 106015. DOI 10.1016/j.compgeo.2023.106015; arXiv 2305.05218 | GNS sobre colapso de columna granular | **[E]** predice razones de aspecto no vistas, dominios con más del doble de partículas, «hundreds of times faster» que el simulador de alta fidelidad | Sustituto de un simulador continuo; mide escurrimiento, no trayectoria de un grano | **R** |
| 20 | Allen K., Rubanova Y., Lopez-Guevara T., Whitney W., Sanchez-Gonzalez A., Battaglia P., Pfaff T. (2022). «Learning rigid dynamics with face interaction graph networks». arXiv 2212.03574 | FIGNet: interacción entre caras de malla para colisiones rígidas | **[H]** los GNN basados en nodos o partículas son imprecisos o caros en cuerpo rígido | — | **R** |
| 21 | Alkin B., Kronlachner T., Papa S., Pirker S., Lichtenegger T., Brandstetter J. (2024). «NeuralDEM – Real-time Simulation of Industrial Particulate Flows». arXiv 2411.09678 | Operadores neuronales multirrama que sustituyen a DEM y CFD-DEM (tolvas, lechos fluidizados) | **[H]** modela transporte de largo plazo «using macroscopic observables without any reference to microscopic model parameters» | Deliberadamente macroscópico: no sigue partículas individuales | **R** |

### Lección para un bombo de muchas esferas en colisión

- **[H]** Las fuentes 1, 4, 13–17 miden su éxito en sistemas suaves y disipativos con atractor. Un bombo agitado es no suave (impactos), de alta dimensión (6 grados de libertad por bolilla más el aire) y transitorio (se extrae una bolilla y el sistema cambia).
- **[E]** La observación parcial reduce el horizonte a menos de la mitad (fuente 4).
- **[E]** Los métodos que escalan a muchas partículas (18, 19, 21) lo logran renunciando a la trayectoria individual.
- **[I]** El resultado de un sorteo es una función de una trayectoria individual (qué bolilla entra al canal), justo la magnitud que estos métodos no conservan.
- **[I]** Los modelos fundacionales (15, 17) dependen de que el contexto contenga recurrencias del atractor; un sorteo de decenas de segundos no ofrece esa estadística por bolilla.
- **No extrapolar**: ninguna cifra de esta tabla es una cota para el bombo. Lo único transferible es el orden de magnitud «unidades de T_L» como techo empírico en las condiciones más favorables.

---

## 3. Trabajos directos sobre juegos de azar físicos

### 3.1 Lo que existe

| Referencia | Qué hace | Resultado | ¿Usa ML? | Lectura |
|---|---|---|---|---|
| Dimitriadis P., Tzouka K., Koutsoyiannis D. (2013). «Windows of predictability in dice motion». *Facets of Uncertainty: 5th EGU Leonardo Conference*, Kos. DOI 10.13140/RG.2.2.19417.52322. https://www.itia.ntua.gr/en/docinfo/1394/ | Vídeo a 120 Hz de lanzamientos de dado; modelo estadístico que predice el estado unos cuadros después | **[E]** «there is some predictability for short horizons». Sin cifra de ventana en la ficha | Modelo estadístico, no red profunda | **R** (ficha del repositorio; PDF disponible, no leído) |
| Dimitriadis P., Koutsoyiannis D., Tzouka K. (2016). «Predictability in dice motion: how does it differ from hydro-meteorological processes?». *Hydrol. Sci. J.* 61, 1611–1622. DOI 10.1080/02626667.2015.1034128 | Versión en revista del anterior | Existencia confirmada; cifras no extraídas (resumen no disponible por API) | Ídem | **M** |
| Kapitaniak M., Strzalko J., Grabski J., Kapitaniak T. (2012). «The three-dimensional dynamics of the die throw». *Chaos* 22, 047504. DOI 10.1063/1.4746038 | Modelo 3D con rebotes disipativos, comparado con cámara de alta velocidad | **[E]** la cara inicialmente más baja es la más probable para energías realistas; la no suavidad explica la incertidumbre práctica | No. Física y cámara | **R** (lo desarrolla el agente de caos) |
| Small M., Tse C. K. (2012). «Predicting the outcome of roulette». *Chaos* 22, 033150. DOI 10.1063/1.4753920; arXiv 1204.6412 | Modelo simple de rueda y bola; posición, velocidad y aceleración iniciales medidas con conteo manual o cámara | **[E]** retorno esperado positivo; la versión en revista reporta 18 % con el sistema sin cámara (cifra tomada de un resumen de búsqueda, no del texto) | No. Física y cámara | **R** (lo desarrolla el agente de caos) |
| Pfrommer S., Halm M., Posa M. (2020). «ContactNets: Learning Discontinuous Contact Dynamics with Smooth, Implicit Representations». CoRL 2020. arXiv 2009.11193 | **Cubo acrílico de 10 cm lanzado sobre madera**; 750 lanzamientos, 570 útiles; pose con AprilTags y tres cámaras PointGrey a 148 Hz (TagSLAM) | **[E]** con 32 lanzamientos iguala al mejor modelo extremo a extremo entrenado con 256; penetración media bajo 2 % del ancho frente a más de 20 %. Error residual «primarily limited by stochastic contact behavior and noisy data» | Sí | **TC** (ar5iv). No evalúa la cara final ni discute caos |
| Allen K. et al. (2022/2023). «Graph network simulators can learn discontinuous, rigid contact dynamics». CoRL 2022, PMLR 205:1157–1167. https://proceedings.mlr.press/v205/allen23a.html | GNS sobre los mismos lanzamientos reales de cubo | **[E]** supera a simuladores de robótica con 8–16 trayectorias; aprende la discontinuidad cerca de 45° de ángulo inicial | Sí | **R** (página PMLR y resumen de búsqueda) |
| Bartoš F. et al. (2025). «Fair Coins Tend to Land on the Same Side They Started: Evidence from 350,757 Flips». *J. Am. Stat. Assoc.* 120(552), 2118–2127. DOI 10.1080/01621459.2025.2516210; arXiv 2310.04153 | 350 757 lanzamientos humanos registrados | Lo desarrolla el agente de monedas; aquí interesa como conjunto de datos (sección 6) | No | **M** |

### 3.2 Lo que no es evidencia

- `mpcodingdev/RouletteVision` (GitHub, sin licencia, último cambio 2025-01-27): aficionado, 1703 pares de vídeos; el autor declara que la red no funcionó. No revisado por pares.
- Birk A. (2024). «SmileyNet – Towards the Prediction of the Lottery by Reading Tea Leaves with AI». arXiv 2407.21385. **Es sátira declarada** por el autor («a satirical accumulation of misconceptions, mistakes, and flawed reasoning»). Se lista para que nadie la cite como resultado: su «72 %» es un chiste sobre mala práctica.
- Patentes de máquinas de sorteo y de simulación de bombos (US20040063491A1, US10019874, US5380007): describen aparatos, no miden predictibilidad. No verificadas una a una.
- Aplicaciones comerciales de «predicción de lotería»: trabajan sobre frecuencias históricas, fuera de este encargo.

### 3.3 Constancia del vacío

Búsquedas hechas (WebSearch, 2026-10-09), todas sin hallar un trabajo revisado por pares de ML sobre vídeo o sensores aplicado a una máquina de bolillas:

1. `machine learning predict dice roll outcome from high-speed video before it lands neural network`
2. `lottery ball machine computer vision tracking balls predict drawn number physical simulation DEM "lottery machine"`
3. `roulette outcome prediction deep learning video ball tracking wheel paper`
4. `"lottery" machine balls "discrete element" OR "CFD-DEM" OR "simulation" air mix randomness study paper`
5. `coin toss outcome prediction from video neural network high-speed camera initial conditions machine learning paper`
6. `arXiv dice throw final face prediction learned simulator OR "neural network" trajectory video "die" outcome predictability bounce chaotic`

**[H de búsqueda]** Resultado: cero trabajos sobre bombos de lotería (ni ML, ni DEM, ni seguimiento por visión); un grupo sobre dados con modelo estadístico; física clásica para ruleta; CNN que **leen** dados ya detenidos (no predicen). **[I]** La ausencia en seis búsquedas generales no prueba inexistencia: no se consultaron Scopus, Web of Science, IEEE Xplore ni literatura en chino, ruso o español, ni informes internos de fabricantes y laboratorios de certificación.

---

## 4. Instrumentación

### 4.1 Seguimiento óptico 3D de muchas partículas

| Fuente | Técnica | Cifras confirmadas | Lectura |
|---|---|---|---|
| Schanz D., Gesemann S., Schröder A. (2016). «Shake-The-Box: Lagrangian particle tracking at high particle image densities». *Exp. Fluids* 57, 70. DOI 10.1007/s00348-016-2157-1 | Seguimiento lagrangiano 3D denso con predicción temporal y corrección iterativa de posición | Existencia y título confirmados (622 citas). **Cifras de densidad de imagen y exactitud no confirmadas** (artículo cerrado; ver sección 7) | **M** |
| Schröder A., Schanz D. (2023). «3D Lagrangian Particle Tracking in Fluid Mechanics». *Annu. Rev. Fluid Mech.* 55, 511–540. DOI 10.1146/annurev-fluid-031822-041721 | Revisión | **[H]** el seguimiento 3D entrega posición, velocidad y aceleración de «a large number of individual particle tracks» y alimenta asimilación de datos con Navier-Stokes | **R** |
| Dijksman J., Rietz F., Lőrincz K., van Hecke M., Losert W. (2012). «Invited Article: Refractive index matched scanning of dense granular materials». *Rev. Sci. Instrum.* 83, 011301. DOI 10.1063/1.3674173 | Medio granular sumergido en fluido de índice igualado, barrido por láminas con fluorescencia | **[H]** reconstruye la estructura 3D dependiente del tiempo por reconocimiento de partículas | **R**. Exige fluido: no aplicable a un bombo con aire |
| Pfrommer et al. (2020), ya citado | AprilTags en cada cara, tres cámaras a 148 Hz | 1 cuerpo, pose completa con orientación | **TC** |
| Dimitriadis et al. (2013), ya citado | Una cámara a 120 Hz | 1 dado | **R** |

**[I]** Diferencia clave con velocimetría de fluidos: en un bombo las partículas son pocas (decenas), grandes (centímetros) y opacas entre sí. El problema no es la densidad de imagen sino la **oclusión mutua** y la **identidad** (qué número lleva cada bolilla) más la **orientación y el giro**, que el centroide no entrega. Las bolillas llevan números impresos, lo que en principio permite identificarlas y estimar orientación; no encontré ninguna fuente que lo haya hecho.

### 4.2 Técnicas no ópticas

| Fuente | Técnica | Cifras confirmadas | Lectura |
|---|---|---|---|
| Parker D., Broadbent C., Fowles P., Hawkesworth M., McNeil P. (1993). «Positron emission particle tracking – a technique for studying flow within engineering equipment». *Nucl. Instrum. Methods A* 326, 592–607. DOI 10.1016/0168-9002(93)90864-E | PEPT, Universidad de Birmingham | Referencia fundacional | **M** |
| Positron Imaging Centre, Univ. de Birmingham, «PEPT overview». https://www.birmingham.ac.uk/research/centres-institutes/research-in-physics-and-astronomy/particle-and-nuclear-physics/positron-imaging-centre/positron-emission-particle-tracking-pept-overview | Cámara Forte | **[H]** trazador a 1 m/s localizado a ≈ 0,5 mm unas 250 veces por segundo; trazadores de 100 µm a 10 mm; la mitad de los rayos gamma atraviesa 11 mm de acero; **un solo trazador** en la configuración descrita | **TC** (página institucional) |
| Windows-Yule C., Herald M., Nicuşan A., Wiggins C., Pratx G., Manger S., Odo A., Leadbeater T. (2022). «Recent advances in positron emission particle tracking: a comparative review». *Rep. Prog. Phys.* 85, 016101. DOI 10.1088/1361-6633/ac3c4c | Comparación cuantitativa de algoritmos PEPT con código abierto | **[H]** primera evaluación directa de todas las metodologías vigentes; batería de pruebas publicada | **R** |
| Nicuşan A., Windows-Yule C. (2020). «Positron emission particle tracking using machine learning». *Rev. Sci. Instrum.* 91, 013329. DOI 10.1063/1.5129251 | PEPT-ML: agrupamiento para localizar y separar trayectorias | **[E]** distingue trazadores separados **2 mm**; resolución espacial invariante con el número de trazadores; no necesita conocer cuántos hay | **R** |
| Buist K., van der Gaag A., Deen N., Kuipers J. (2014). «Improved magnetic particle tracking technique in dense gas fluidized beds». *AIChE J.* 60(9), 3133–3142. DOI 10.1002/aic.14512 | Seguimiento de un marcador magnético en lecho fluidizado | Existencia confirmada; entrega posición **y orientación** de un marcador (según trabajo posterior del mismo grupo) | **M** |
| Zimmermann R., Fiabane L., Gasteuil Y., Volk R., Pinton J.-F. (2012). «Measuring Lagrangian accelerations using an instrumented particle». arXiv 1206.1617 | Partícula instrumentada con acelerómetro de tres ejes y transmisión inalámbrica | **[H]** pensada para flujos opacos o granulares y mezcladores industriales | **R** |
| Cabrera F., Cobelli P. (2021). «Design, construction and validation of an instrumented particle for the lagrangian characterization of flows. Application to gravity wave turbulence». *Exp. Fluids*. DOI 10.1007/s00348-020-03121-3; arXiv 2101.01482 | Esfera hueca impresa en ABS con acelerómetro y giróscopo | **[E]** **36 mm de diámetro**, masa ≈ 19,6 g, 16 bits por eje, **1 kHz** en aceleración y **8 kHz** en velocidad angular, hasta 8 h de autonomía, componentes comerciales | **R** |

**[I]** La esfera de Cabrera y Cobelli tiene un tamaño del orden de una bolilla de sorteo, pero su masa (≈ 19,6 g) habría que contrastarla con la masa reglamentaria de la bolilla (dato del agente de loterías): una bolilla instrumentada que pese distinto altera justo lo que se quiere medir. **[Hip]** Una bolilla instrumentada con masa e inercia igualadas daría giro y aceleración a kHz sin problema de oclusión; no hay fuente que lo haya hecho en un bombo.

### 4.3 Sincronización multicámara y calibración

| Fuente | Contenido | Lectura |
|---|---|---|
| Zhang Z. (2000). «A flexible new technique for camera calibration». *IEEE Trans. Pattern Anal. Mach. Intell.* 22(11), 1330–1334. DOI 10.1109/34.888718 | Calibración con patrón plano en varias poses | **M** |
| Tsai R. (1987). «A versatile camera calibration technique for high-accuracy 3D machine vision metrology using off-the-shelf TV cameras and lenses». *IEEE J. Robot. Autom.* 3(4), 323–344. DOI 10.1109/JRA.1987.1087109 | Calibración en dos etapas con distorsión radial | **M** |
| IEEE Std 1588-2019. «IEEE Standard for a Precision Clock Synchronization Protocol for Networked Measurement and Control Systems». DOI 10.1109/IEEESTD.2020.9120376 | Protocolo PTP | **M** |
| Notas de fabricantes (LUCID Vision Labs, SVS-Vistek), vía resumen de búsqueda | **[H, fuente comercial]** PTP (IEEE 1588-2008) está integrado en GigE Vision; SVS-Vistek cita una desviación máxima de 10 µs; los comandos por software dejan desfases de milisegundos | Resumen de búsqueda, **no leídas directamente** |

**[I]** Requisito derivado, no medido: para acotar el error de posición por desincronización a una fracción δ del diámetro, el desfase entre cámaras debe ser menor que δ·D/v. Con v = 5 m/s, D = 40 mm y δ = 1 %, el desfase admisible es 80 µs; los valores de v y D son **supuestos ilustrativos**, no datos de un bombo real. El disparo por hardware cumple ese orden con holgura; PTP a 10 µs también, según la cifra comercial citada. El refractado en la pared curva del bombo transparente exige un modelo de cámara que la calibración de Zhang o Tsai no incluye: **vacío**, no encontré fuente específica.

---

## 5. Simulación y gemelos digitales

### 5.1 Método y herramientas

| Fuente | Contenido | Lectura |
|---|---|---|
| Cundall P., Strack O. (1979). «A discrete numerical model for granular assemblies». *Géotechnique* 29(1), 47–65. DOI 10.1680/geot.1979.29.1.47 | Origen del método de elementos discretos (15 928 citas en Crossref) | **M** |
| Kloss C., Goniva C., Hager A., Amberger S., Pirker S. (2012). «Models, algorithms and validation for opensource DEM and CFD-DEM». *Prog. Comput. Fluid Dyn.* 12(2/3), 140. DOI 10.1504/PCFD.2012.047457 | Artículo de referencia de LIGGGHTS y CFDEMcoupling | **M** |
| Goniva C., Kloss C., Deen N., Kuipers J., Pirker S. (2012). «Influence of rolling friction on single spout fluidized bed simulation». *Particuology* 10(5), 582–591. DOI 10.1016/j.partic.2012.05.002 | CFD-DEM de lecho de chorro: esferas agitadas por aire | **M** |
| Weinhart T., Orefice L., Post M., et al. (2020). «Fast, flexible particle simulations – An introduction to MercuryDPM». *Comput. Phys. Commun.* 249, 107129. DOI 10.1016/j.cpc.2019.107129 | Artículo de referencia de MercuryDPM | **M** |

### 5.2 Sensibilidad a condiciones iniciales en DEM

- Fullmer W., Porcu R., Musser J., Almgren A., Srivastava I. (2022). «The divergence of nearby trajectories in soft-sphere DEM». *Particuology* 63, 1–8. DOI 10.1016/j.partic.2021.06.008. Ficha: https://mfix.netl.doe.gov/citation-post/2022-fullmer-william-d-journal/ . Lectura: **R**.
  - **[E]** Mide la divergencia de trayectorias cercanas con el «tiempo de memoria dinámica» y lo invierte para estimar el mayor exponente de Lyapunov.
  - **[E]** Buen acuerdo con dinámica molecular de esfera dura a baja concentración; por encima del 30 % de concentración el exponente de la esfera blanda crece más rápido; la inestabilidad aumenta de forma asintótica con la rigidez del resorte.
  - **[H]** Los autores proponen el caso como prueba de regresión para verificar códigos.
  - **[I]** Es el protocolo que habría que repetir con la geometría, el número de bolillas y el flujo de aire de un bombo para obtener su T_L. Es la única fuente hallada que cuantifica el caos en DEM; es un gas granular homogéneo, **no** un bombo.
  - **[I]** Consecuencia práctica: dos ejecuciones DEM con distinto orden de sumas en coma flotante o distinto número de hilos divergen a nivel de trayectoria. Un gemelo digital no puede reproducir «el» sorteo; puede reproducir su distribución.

### 5.3 Validación de DEM contra experimento en tambores

| Fuente | Contenido | Lectura |
|---|---|---|
| Yang R., Zou R., Yu A. (2003). «Microdynamic analysis of particle flow in a horizontal rotating drum». *Powder Technol.* 130, 138–146. DOI 10.1016/S0032-5910(02)00257-7 | **[E, según resumen de búsqueda]** DEM ajustado a condiciones de PEPT (tambor de 100 mm, llenado 35 %, 10–65 rpm); acuerdo en ángulo dinámico de reposo y campos de velocidad | **M** + resumen de búsqueda |
| Alizadeh E., Bertrand F., Chaouki J. (2014). «Comparison of DEM results and Lagrangian experimental data for the flow and mixing of granules in a rotating drum». *AIChE J.* 60, 60–75. DOI 10.1002/aic.14259 | Comparación de DEM con seguimiento lagrangiano experimental | **M** |

**[H]** En ambos la validación es de **magnitudes promediadas** (ángulo de reposo, perfiles de velocidad, mezcla), no de trayectorias partícula a partícula. **[I]** Es coherente con 5.2: lo validable en un sistema caótico es la estadística.

### 5.4 Gemelos digitales y sustitutos aprendidos

- NeuralDEM (fuente 21 de la sección 2) y GNS granular (fuente 19) son el estado del arte verificado de sustitutos aprendidos de DEM. Ambos son macroscópicos.
- **Vacío**: no encontré un gemelo digital de sistema granular con asimilación de datos en tiempo real desde cámaras a nivel de partícula. La búsqueda `digital twin granular DEM real-time data assimilation rotating drum OR mixer calibrated machine learning surrogate paper 2023 2024` solo devolvió NeuralDEM, una ficha de NETL sobre DEM acelerado con CNN (sin autores ni año en el resumen; no verificada) y anuncios de congresos.

---

## 6. Repositorios y conjuntos de datos

Licencia y «última actividad» (`pushed_at`, `last_activity_at` o `updated_on`) leídas de la API del alojamiento el 2026-10-09. «NOASSERTION» de GitHub se resolvió leyendo el archivo de licencia cuando se indica.

### 6.1 Baterías de aleatoriedad

| Nombre | URL | Licencia | Última actividad | Para qué sirve |
|---|---|---|---|---|
| SP800-90B_EntropyAssessment (usnistgov) | https://github.com/usnistgov/SP800-90B_EntropyAssessment | Aviso de software NIST en el README (uso, copia y modificación permitidos conservando el aviso); sin archivo LICENSE | 2026-08-04 | Estimación de min-entropía de una fuente de ruido según SP 800-90B |
| sp800_22_tests (dj-on-github) | https://github.com/dj-on-github/sp800_22_tests | GPL-2.0 | 2026-06-13 | Implementación en Python de SP 800-22 Rev. 1a |
| dieharder (página del autor, R. G. Brown) | https://webhome.phy.duke.edu/~rgb/General/dieharder.php | GPL «versión 2b» (GPL con cláusula «Beverage») | versión 3.31.1; archivos fechados 2024-06-27 | Batería de pruebas de generadores |
| dieharder (espejo de D. Eddelbuettel) | https://github.com/eddelbuettel/dieharder | GPL con la modificación «Beverage» (archivo COPYING leído) | 2024-04-30 | Mismo código, empaquetado |
| TestU01-2009 (umontreal-simul) | https://github.com/umontreal-simul/TestU01-2009 | Apache-2.0 | 2026-04-12 | SmallCrush, Crush, BigCrush. Artículo: L'Ecuyer y Simard (2007), *ACM TOMS* 33, DOI 10.1145/1268776.1268777 |
| NIST CSRC, documentación y software | https://csrc.nist.gov/projects/random-bit-generation/documentation-and-software | Sitio gubernamental de EE. UU. | responde 200 | Distribución oficial de la batería SP 800-22 |

### 6.2 Datos

| Nombre | URL | Licencia | Última actividad | Para qué sirve |
|---|---|---|---|---|
| «How fair is a fair coin flip?» (Bartoš et al.) | https://osf.io/pxu6r/ | CC-BY 4.0 (API de OSF) | 2025-09-27 | 350 757 lanzamientos de moneda con lado inicial y lanzador |
| dysts (GilpinLab; redirige desde williamgilpin/dysts) | https://github.com/GilpinLab/dysts | Apache-2.0 | 2026-04-15 | Más de un centenar de sistemas caóticos con exponentes de Lyapunov anotados |
| dysts_data | https://github.com/GilpinLab/dysts_data | **sin licencia declarada** | 2025-09-23 | Series precalculadas de dysts |
| Lottery Powerball Winning Numbers: Beginning 2010 | https://data.ny.gov/Government-Finance/Lottery-Powerball-Winning-Numbers-Beginning-2010/d6yy-54nr | **Campo de licencia vacío** en los metadatos; atribución: New York State Gaming Commission | conjunto vivo (actualizado en octubre de 2026) | Registro histórico público. Solo resultados, sin datos físicos del sorteo |

**[H]** No encontré ningún conjunto de datos público con vídeo o trayectorias de bolillas de un sorteo real. **[H]** No encontré un registro histórico de lotería con licencia abierta explícita; el de Nueva York es público pero no declara licencia en sus metadatos.

### 6.3 Bibliotecas de ML para dinámica

| Nombre | URL | Licencia | Última actividad | Para qué sirve |
|---|---|---|---|---|
| pysindy | https://github.com/dynamicslab/pysindy | MIT (archivo leído) | 2026-06-10 | SINDy |
| reservoirpy | https://github.com/reservoirpy/reservoirpy | MIT | 2026-10-08 | Redes de estado de eco |
| DeepXDE | https://github.com/lululxvi/deepxde | LGPL-2.1 | 2026-08-18 | PINN y operadores |
| PhysicsNeMo (antes Modulus) | https://github.com/NVIDIA/physicsnemo | Apache-2.0 | 2026-10-09 | Marco de aprendizaje profundo para física |
| PINNs (código original de Raissi) | https://github.com/maziarraissi/PINNs | MIT | 2026-02-11 | Reproducir el artículo de 2019 |
| neuraloperator | https://github.com/neuraloperator/neuraloperator | MIT | 2026-08-06 | FNO y afines |
| chronos-forecasting | https://github.com/amazon-science/chronos-forecasting | Apache-2.0 | 2026-10-05 | Modelo fundacional de series |
| panda | https://github.com/abao1999/panda | MIT | 2026-02-24 | Modelo preentrenado para caos |
| gns (geoelements) | https://github.com/geoelements/gns | MIT (archivo leído) | 2026-03-27 | Simulador de red de grafos, flujo granular |
| deepmind-research | https://github.com/google-deepmind/deepmind-research | Apache-2.0 | 2026-06-17 | Contiene `learning_to_simulate` |

### 6.4 Visión y seguimiento

| Nombre | URL | Licencia | Última actividad | Para qué sirve |
|---|---|---|---|---|
| trackpy | https://github.com/soft-matter/trackpy | BSD de 3 cláusulas (archivo leído) | 2026-06-29 | Localización y enlace de partículas 2D y 3D |
| OpenPTV | https://github.com/OpenPTV/openptv (sitio https://www.openptv.net/) | LGPL-3.0 | 2026-10-09 | Velocimetría por seguimiento de partículas 3D multicámara |
| OpenCV | https://github.com/opencv/opencv | Apache-2.0 | 2026-10-09 | Calibración (Zhang), estéreo, detección |
| DeepLabCut | https://github.com/DeepLabCut/DeepLabCut | LGPL-3.0 | 2026-10-06 | Estimación de pose sin marcadores. **[I]** aplicable a seguir los números impresos de una bolilla; no hay precedente |
| pept (Univ. de Birmingham) | https://github.com/uob-positron-imaging-centre/pept | GPL-3.0 | 2026-02-12 | Algoritmos PEPT, incluido PEPT-ML |

### 6.5 Simulación

| Nombre | URL | Licencia | Última actividad | Para qué sirve |
|---|---|---|---|---|
| LIGGGHTS-PUBLIC | https://github.com/CFDEMproject/LIGGGHTS-PUBLIC | GPL-2.0 | 2026-05-18 | DEM |
| CFDEMcoupling-PUBLIC | https://github.com/CFDEMproject/CFDEMcoupling-PUBLIC | GPL-3.0 | 2025-07-03 | Acoplamiento CFD-DEM con OpenFOAM: esferas agitadas por aire |
| Yade | https://gitlab.com/yade-dev/trunk | GPL-2.0 o posterior | 2026-10-09 | DEM con interfaz Python |
| MercuryDPM | https://bitbucket.org/mercurydpm/mercurydpm (sitio https://www.mercurydpm.org/) | BSD de 3 cláusulas (según artículo de los desarrolladores y resumen de búsqueda; archivo no leído) | 2026-10-09 | DEM con herramientas de promediado |
| MFiX (NETL) | https://mfix.netl.doe.gov/ | **Sin licencia formal**; registro gratuito con revisión manual; el catálogo EDX dice «No License Restrictions» y el foro pide no redistribuir (resumen de búsqueda) | versión 26.1 | CFD-DEM y modelos de dos fluidos |
| Project Chrono | https://github.com/projectchrono/chrono | BSD-3-Clause | 2026-10-09 | Multicuerpo con contacto, módulo granular en GPU |
| MuJoCo | https://github.com/google-deepmind/mujoco | Apache-2.0 | 2026-10-09 | Cuerpo rígido con contacto, diferenciable |
| NVIDIA Warp | https://github.com/NVIDIA/warp | Apache-2.0 | 2026-10-09 | Simulación diferenciable en GPU desde Python |
| PhysX | https://github.com/NVIDIA-Omniverse/PhysX | BSD-3-Clause | 2026-10-09 | Cuerpo rígido en tiempo real |
| Taichi | https://github.com/taichi-dev/taichi | Apache-2.0 | 2026-10-05 | Cómputo en GPU desde Python; base para DEM propio |

**[I]** Para un bombo de aire lo directamente aplicable es CFDEMcoupling + LIGGGHTS o MFiX; para uno de paletas, Yade, MercuryDPM o Chrono. MuJoCo, PhysX y Warp priorizan velocidad y estabilidad sobre fidelidad del contacto: sirven para explorar, no para validar.

---

## 7. No verificadas

Afirmaciones que conozco de memoria o por resumen de buscador y que **no** confirmé contra la fuente primaria en esta sesión. No citar como hecho.

1. Shake-The-Box sigue partículas a densidades de imagen de ≈ 0,125 partículas por píxel con fracción despreciable de partículas fantasma: recuerdo de memoria; el artículo es cerrado y la búsqueda dirigida no devolvió el resumen.
2. Sedes de publicación: FNO en ICLR 2021, «Learning Dissipative Dynamics» en NeurIPS 2022, Chronos en TMLR 2024, Panda en ICLR 2026 (esto último lo dice la descripción del repositorio, no arXiv).
3. Cifras cuantitativas de Choi y Kumar (2024): error de escurrimiento y factor de aceleración exacto.
4. Horizonte en T_L de las PINN causales en Lorenz (Wang et al.): el resumen no lo da.
5. Cifras de Small y Tse (retorno del 18 % en la revista, 40 % en el congreso de 2008, cámara a 90 cuadros por segundo): vienen de un resumen de búsqueda.
6. Cámara de 1500 cuadros por segundo en el experimento de Kapitaniak et al.: nota de prensa en un resumen de búsqueda.
7. Detalle de Yang, Zou y Yu (2003): tambor de 100 mm, 35 %, 10–65 rpm, tomado de un resumen de búsqueda.
8. Exactitud de PTP en cámaras GigE (10 µs) y desfases de milisegundos por software: fuentes comerciales no abiertas directamente.
9. Ficha de NETL sobre DEM acelerado con CNN en tambor rotatorio y tolva (https://mfix.netl.doe.gov/?p=10005): sin autores ni año confirmados.
10. Flapper et al. (2025), «Multi-camera orientation tracking method for anisotropic particles in particle-laden flows», arXiv 2503.08694: aparece en una búsqueda; metadatos no leídos.
11. Trabajos de seguimiento con sedimento instrumentado («Smart Sediment Particle», Xie et al. 2023; registro IAHR con 200–1000 Hz): solo resumen de búsqueda.
12. Kantzas et al. (2001), hasta cinco partículas radiactivas con dos cámaras gamma en lecho fluidizado; Buist et al. (2017), orientación por seguimiento magnético: solo resumen de búsqueda.
13. Seguimiento por tomografía de rayos X de medios granulares (número de partículas, tasa de volúmenes): **no hallé ni verifiqué ninguna fuente**.
14. `https://www.yade-dem.org/` no respondió (código 000) y `simul.iro.umontreal.ca/testu01/tu01.html` devolvió 404; los proyectos se verificaron por GitLab y por el espejo de GitHub respectivamente.
15. `github.com/fbartos/CoinTosses` y `github.com/MercuryDPM/MercuryDPM` **no existen** (404): eran suposiciones mías. Los datos de moneda están solo en OSF; MercuryDPM está en Bitbucket.
16. Patentes US20040063491A1, US10019874 y US5380007: solo resumen de búsqueda.
17. Cualquier dato físico de un bombo real (masa y diámetro de la bolilla, velocidades, duración de la agitación): no es de este encargo y no lo verifiqué; los valores usados en 4.3 son supuestos ilustrativos.

---

## 8. Vacíos

1. **No hay medición del tiempo de Lyapunov de una máquina de sorteo**, ni experimental ni por simulación. Sin ese número no se puede decir cuántos T_L dura un sorteo ni, por tanto, si la predicción de la bolilla es imposible en la práctica o solo difícil.
2. **No hay ningún trabajo de ML sobre vídeo o sensores de un bombo de lotería** (seis búsquedas, sección 3.3), ni un conjunto de datos público de trayectorias de bolillas.
3. **No hay simulación CFD-DEM publicada de un bombo de lotería**; solo patentes que mencionan la idea.
4. Toda la literatura de pronóstico de caos con ML usa **sistemas suaves simulados**. El caso no suave con muchos cuerpos solo aparece en simuladores aprendidos que se evalúan por estadística agregada.
5. Los resultados con cuerpo rígido real (cubo de ContactNets) son de **un cuerpo, un segundo y sin evaluación del resultado discreto** (cara final). Falta el paso de «error de pose» a «probabilidad de acertar la cara», y de uno a muchos cuerpos.
6. **Observación parcial**: no hay método verificado para estimar el giro de decenas de esferas opacas que se ocluyen entre sí. PEPT y seguimiento magnético siguen uno o pocos trazadores; las esferas instrumentadas alteran masa e inercia si no se igualan.
7. **Calibración a través de una pared curva transparente**: sin fuente específica.
8. **Validación de DEM**: se hace sobre promedios. No hay protocolo aceptado para validar un gemelo digital en la magnitud que importa aquí (frecuencia de extracción por bolilla en función de masa, diámetro, coeficiente de restitución y posición de carga).
9. **Sesgo frente a predicción**: la literatura revisada no separa las dos preguntas. Detectar que una bolilla más pesada sale con frecuencia distinta es un problema estadístico abordable con simulación; predecir la bolilla de un sorteo dado es un problema de trayectoria. Este documento no encontró evidencia de que lo segundo se haya logrado en ningún sistema de muchos cuerpos en colisión.
10. **Cobertura de la búsqueda**: no se consultaron bases de pago, literatura no inglesa, ni documentos de fabricantes de máquinas de sorteo y laboratorios de certificación, donde podría existir trabajo no publicado.
