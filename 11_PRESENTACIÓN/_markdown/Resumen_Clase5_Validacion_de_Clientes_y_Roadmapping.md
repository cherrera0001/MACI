# Resumen_Clase5_Validacion_de_Clientes_y_Roadmapping

> Material de clase de Fundamentos de Ciencia de Datos, UdeC T2-2026.
> Texto extraido de `Resumen_Clase5_Validacion_de_Clientes_y_Roadmapping (1).pdf` para busqueda e indexacion.
> 35 laminas. Las figuras no se extraen: si una lamina
> depende de un grafico, hay que abrir el PDF.

---

## Lamina 1

Prototipos y Creatividad — CLASE 5 (S05): Validación de clientes y Roadmap-
ping
Apuntes completos: diapositivas oficiales + transcripción de clase
Profesor: MartínMelladoGuerrero Curso: 2026G605—Prototiposycreatividad·Sesión05
Cómo leer este documento. Integraelcontenidodelas 32 diapositivas oficiales conlodichoenclase,
organizadosegúnelordenrealdelaexposición. Semarcancon �� � �loscontenidosque solo aparecen
en la transcripción (noestánenlasslides),porquesuelenserjustamenteloqueunestudianteolvida
repasar. Lostemasadministrativosestánconcentradosenlasección §0,alinicio.
Nota sobre las fuentes. Latranscripciónesautomática(Whisper+pyannote-audio)ycontieneerrores
dereconocimientoevidentes,sobretodoennombresdemodelosdeIA,marcasyherramientas. Cuando
eltérminocorrectosededucedelasslidesodelcontexto,seusaelcorrectoyseindicalareconstrucción
entreparéntesisoenel Anexofinal. Loscasosdonde nosepudoreconstruireltérminosemarcan
explícitamentecomo [término no reconstruible].
�� �Advertencia sobre los hablantes. La diarización asignó al profesor varias etiquetas distintas
(SPEAKER_02 mayoritariamente, pero también SPEAKER_03 y SPEAKER_05 durante la demo en vivo,
cuandohablamientrasdictainstruccionesaunagente). Todoelcontenidodocentedeestedocumento
seatribuyealprofesorconesasalvedad;lasintervencionesdealumnos(SPEAKER_00,SPEAKER_01)se
identificancomotalescuandoaportancontenido.
Alcance. Seexcluyeronanécdotaspersonales,digresionessincontenidodocente,interrupcionesde
audio/logísticaycomentariosdeactualidadnorelacionadosconlamateria.
���� RESUMEN EJECUTIVO
Estaquintasesióncierralaparteconceptualdelramocon roadmapping: elinstrumentoquepermiteproyectar
cómo se llega desdeelestadoactualhastaunavisióndeproducto,coordinandoeneltiempoperspectivas técnicas
y comerciales. La definición formal (slide 2) es la de ungráfico temporal por capas — Mercado, Producto,
Tecnología,ProgramaI+D,Recursos—quevinculaambasperspectivas. Laclaserecorreprimeroel catálogo de
Robert Phaal conochotiposderoadmaptecnológico(producto,estratégico,servicios/capacidades,largoplazo,
conocimiento/activo,proceso,programáticoeintegración),señalandocuálsirveparaquécaso: elde integración
eselmáscomúnensoftwareyelde conocimiento/activoelmásútilenDataScience. Luegoseestructurael
método entres pasos: (1) definir la visión de producto con la plantillaProduct Vision de Lombardo (Para /
Quién/El/Esun/Que/Adiferenciade/Nuestroproducto), quedebeserambiciosaporqueelroadmapes
justamenteloquelava“cazando”;(2) priorizar el desarrollo,comparandocincoframeworks(CriticalPath,Kano,
Deseabilidad-Factibilidad-Viabilidad,ROIScorecard,MoSCoW),ybajándoloauna fórmula de priorizaciónoperativa
—Valor/Esfuerzo×Confianza=Prioridad—yauna ficha de 13 campos por funcionalidad queincluyetamaño
dehistoria,incertidumbrederequerimientos,incertidumbretécnica,dependenciasyrequisitosdeaceptación;(3)
considerar matices,esdecir,entenderqueexiste un roadmap distinto por audiencia: ingeniería/procesosinternos,
ventasymarketing,ejecutivosyclientes. Seintegraademásel ciclo de vida del producto encincofases(Nuevo
producto→Crecimiento→Expansión→Explotación→Findeciclodevida)yselosuperponeconel Customer
Development de Steve Blank (Descubrimiento→Validación→Creación→Construccióndecompañía),dondela
fasede Nuevo producto correspondealazonade BÚSQUEDAconpivoteo,yelrestoa EJECUCIÓN.Elmensaje
transversal,repetidovariasveces: el producto por sí solo no vale nada; lo que importa es conseguir clientes ,y
conIAgenerativaesosevolvióaúnmásevidenteporqueterminarelsoftwaredejódeserlodifícil. Laclasecierra
conuna demostración en vivo decómoarmarunroadmaprealcon GitHub Issues → Milestones → Projects ,
operadoporunagentevía GitHub CLI.
� CONCEPTOS CLAVE DE LA CLASE
1

## Lamina 2

# Concepto Prioridad Porquéimporta
1 Definiciónde
roadmappingyestructura
porcapas
Esencial Slide2;definiciónformal
exigible
2 Lostrespasosdelmétodo:
visión→priorización→
matices
Esencial Estructuracompletadela
clase(slides6,9,25)
3 ProductVision(plantillade
7campos)
Esencial Slide7;esplantilla
“rellenable”enexamen
4 Tabladeframeworksde
priorización(5
frameworks)
Esencial Slide11;usos,cuándo
elegir,debilidades
5 ModeloKano(3curvas) Esencial Slide12;muycitable
6 ModeloMoSCoW
(M/S/C/W+criterios)
Esencial Slide13;elmásusadoen
lapráctica
7 Fórmuladepriorización:
(Valor/Esfuerzo)×
Confianza
Esencial Slide14;únicafórmula
matemáticadelramo
8 Fichade13camposde
unafuncionalidad/historia
Esencial Slide15;basedela
entrega
9 Cincofasesdelciclode
vidadelproducto
Esencial Slide19;marcotemporal
general
10 CustomerDevelopment:
Búsquedavs.Ejecución,
pivoteo
Esencial Slides20–21;paradigma
recomendadopara
innovación
11 Los4roadmapssegún
audiencia(ingeniería,
ventas,ejecutivos,clientes)
Esencial Slides24,27,28,29
12 Ochotiposderoadmap
tecnológicodePhaal
Importante Slides3–4;catálogode
referencia
13 Objetivosuniversales/
resultadoclave(OKR)
Importante Slide18;focodeadopción
comercial
14 Condicionesdelogroy
estrategiasdeDescubrim-
iento/Validación
Importante Slides22–23;pasadas
rápidoenclase
15 Ejemplointegradodel
smartwatch(roadmap
completoporfases)
Importante Slide26;ejemplomodelo
16 Implementaciónreal:
GitHubIssues→
Milestones→Projects
Importante �� � �Casitodooral;demo
envivo
17 Criteriosparaelegirentre
proyectosdeinnovación
Importante �� � �Soloentranscripción
18 CartaGanttyrutacrítica:
paradigmadegestión
vs.innovación
Importante �� � �Soloentranscripción
19 “Performanceasafeature”
comodriverdemercado
Complementario �� � �Soloentranscripción
20 Roadmapspúblicosreales
(GitHub,Slack,Microsoft
365)
Complementario Slides30–32;referencias
2

## Lamina 3

��� �§0. INFORMACIÓN ADMINISTRATIVA DEL RAMO
Todalainformaciónoperativaestáconcentradaaquí. Elrestodeldocumentoescontenidoconceptual.
0.1 �� � �Entrega final (presentada en esta clase)
Elprofesormostróenclaselapautadela entrega final,disponibleen Canvas. Ladescribecomo “muy simple”,
peroadvierteexplícitamenteque hay un desafío / “una trampa” .
Formato: un video de 20 minutos (mismoformatodelasentregasanteriores)+un demo presencial elsábado
siguiente.
Contenido exigido en el video:
# Requisito Detalledadoenclase
1 Definir la historia seleccionada Explicarelfocofinaldelprototipo
queseestámostrando,siemprecon
sucontexto
2 Demo de la solución en los temas
principales
Nofocalizarseenadministraciónni
accesossinoesloimportante.
Mostrar “el filete” delasolución: las
partesqueelequipocreequeson
las ganadoras
3 Concluir hasta dónde se llegó Conelprototipoyconel
entendimientodecómoresolverla
historiadeusuario. Seacepta
explícitamente nohabercumplido
todalahistoriapropuesta
4 Autoevaluación de UX de 0 a 100 Ojalá segmentada en varios
ámbitosy relativa a los objetivos
que el propio equipo se puso .
Ejemplodado: “en cobertura
logramos quizás 70 de 100; en
facilidad de uso quizás 100 de 100,
porque quizás hicimos poco pero lo
hicimos muy bien hecho”
5 �� �EL DESAFÍO (“la trampa”) Demostrar, con argumentos
propios, que en algún ámbito de
UX la solución es fundamental /
excepcional. Algunapartedela
solucióntienequeser muy buena,
alpuntodequeunodiga “esta
cuestión es muy buena”. Seespera
usarloyaaprendido: testeo,
entrevistasapersonas,preguntas,y
demostrarlo con algún tipo de
variación(comparación)
6 Conclusiones sobre testeabilidad Cuálessonlostemas más difíciles
de testear yquerequieren
implementación real parapoder
servalidados;yquétemasse
pensaron más fáciles y no lo
fueron
Demo presencial: “no requiere presentación de todo el caso, sino solo el prototipo” . El sábadosolo se verán
soluciones. Sielequipoquierecontaralgoadicional,puedehacerloenlapresentaciónfinal.
3

## Lamina 4

�� � �Lectura estratégica: elpunto5esladiferenciaentreunaentregacorrectayunabuena. Nobastaconcobertura
niconmedición(esofueDemo1yDemo2): hayque demostrar excelencia en un punto concreto y probarlo
empíricamente.
0.2 �� � �Vínculo con la clase: la entrega exige priorizar historias
Elprofesorconectaexplícitamenteelcontenidoconlaentrega:
“Por eso les he dicho en esta entrega: ya, prioricen historias. En un caso más real uno tendría hartas más
historias, pero en lo práctico uno toma pocas historias por fase.”
Ejemplodado: un sprint de dos semanas trabajando full focalizado en resolver dos historias . Justificación:
“hacer un buen producto toma tiempo” .
�� � �Recomendación transversal repetida sobre los proyectos del ramo: “traten de simplificar el scope del proyecto,
traten de quizá atender a un cliente, a un segmento de clientes primero” ,porqueanivelderoadmappingesoevita
“tomar mucha incertidumbre dentro del plato” .
0.3 �� � �Logística
• Materialypautadelaentregafinal: Canvas.
• Próximasesión: sábado, después del almuerzo;sededicaaverlassoluciones.
• Elprofesorsugiereaprovechareltiempointermediotrabajandoenelproyecto(mencionalaideademeterse
“unahackatón”).
• El GitHub CLI queusaenlademoquedarádisponible;indicaqueestádocumentado en la wiki del proyecto
delrepositoriodelcurso.
5.0 Encuadre de la sesión — Esencial
5.0.1 �� � �Por qué esta clase existe
“Cuando uno hace un producto, hay que tener una noción clara de cuál es el paso a paso de cómo uno
llega a terminarlo.”
Elargumentocentralesque un prototipo es solo un momento de un proyecto :
“El de un prototipo es un momento nomás de un proyecto, y como ya se han dado cuenta, se va avanzando
bien rápido, y entonces uno tiene un prototipo un día, el otro tiene otro prototipo, y así, y así, y así.”
�� � �Calificaciónexplícitadeladificultaddeltema: “esta rama, a pesar de todo, es súper tranqui” —elroadmapping
esconceptualmentesimple; lo complejo es la implementación práctica ,enparticularelavancetecnológicoque
hayqueirpersiguiendo.
�� � �El roadmapping es un tema muy antiguo: seusa “desde tiempos inmemorables”endesarrollodeproductos. No
hayunsoloroadmapping;existenvariantestécnicas,aeronáuticas,etc.,y cada empresa tiene su propio formato .
5.0.2 �� � �Qué aporta el roadmapping como metodología
“Es una metodología que nos permite establecer que hay etapas en el desarrollo de algo, y esas etapas
están condicionadas por distintos ámbitos que uno quiera analizar.”
Dosideasquesederivandeestoyqueserepitentodalaclase:
1. Hay etapas→eldesarrolloessecuencialyacumulativo,nounbigbang.
2. Las etapas se cruzan con ámbitos (capas) →mercado,producto,tecnología,recursos…Cadacapaavanzaen
paralelo.
4

## Lamina 5

5.0.3 �� � �La lógica de dependencias técnicas
Ensoftwareconagentes,elroadmapsematerializaen milestones e issues de GitHub (vistoenlostalleres):
“Normalmente uno tiene una lista de tareas que la gente [los agentes] va estableciendo, y eso lo ordena en
milestones en GitHub, que es como una lista de hitos que uno va cumpliendo. Eso en general lo hace bajo
una lógica de dependencias técnicas.”
Ejemplo dado: “si necesito una capa de conversación en tiempo real, tengo que armar una capa en WebSockets” y
todoloqueesoimplique.
Secuencia clásica del desarrollo de software:
1. Pensarlo muy bien ARQUITECTÓNICAMENTE ← "la jugada grande"
2. Establecer cuáles son los MÓDULOS
3. Definir el ROADMAP para llegar a ese punto técnico
▲
└── ese punto técnico se inspira en la VISIÓN DEL PRODUCTO
�� � �Estacadena(visión→arquitectura→módulos→roadmap)eslaquejustificaqueelPaso01delmétodoseala
visióndeproductoynolalistadetareas.
5.1 Qué es el roadmapping — Esencial
5.1.1 Definición formal (slide 2)
ROADMAPPING “Instrumento que facilita la evolución de mercados, productos y tecnologías en conjunto,
estableciendo vínculos entre ambas perspectivas.”
“El roadmap genérico es un gráfico temporal que comprende un diverso número de capas que normal-
mente incluyen perspectivas técnicas y comerciales .”
������ Desglose exigible: 1. Esun instrumento(noundocumentodecorativo): facilitala evolución conjunta. 2.
Integra tres objetos: mercados,productosytecnologías. 3. Sufunciónes establecer vínculos entrelaperspectiva
técnicaylacomercial. 4. Suformaesun gráfico temporal por capas.
5.1.2 Estructura del roadmap genérico (slide 2)
tx1 tx2 tx3 ──► TIEMPO
Mercado [ ] [ ] [ ] ┐
Producto [ ] [ ] [ ] │ perspectiva
Tecnología [ ] [ ] [ ] │ COMERCIAL
Programa I+D [ ] [ ] [ ] │ ↕
Recursos [ ] [ ] [ ] ┘ perspectiva TÉCNICA
Las cinco capas canónicasson: Mercado · Producto · Tecnología · Programa I+D · Recursos. Loscortestemporales
sedenotantx1,tx2,tx3.
5.1.3 �� � �Cómo se rellena en la práctica: ejemplo del profesor
Ejemplodesarrolladoenclaseconunproyectode entrenamiento de pitches (unodelosproyectosdelcurso):
5

## Lamina 6

Capa Fase1 Fase2
Producto Cuentadeusuariodondese
guardanlasdistintascosasquese
quierenpracticar;poderhacer
pitchesyrecibir recomendaciones
básicastipo scorecardgeneral
Poder elegir patrones comunes de
pitch;embarcarseenunformatode
entregayrecibirrecomendaciones
según distintos formatos
Tecnología Backendconinterfazdeiniciode
sesión;modelo speech-to-text;
capturadevideoenelfrontendy
conversiónaaudio
(se construye sobre lo anterior)
�� � �Regla operativa que se deriva: “siempre es bueno pensar mucho en el producto […] el producto manda. El
producto normalmente está inspirado en el cliente. Entonces la verdad es que uno siempre está priorizando al cliente.”
5.2 Tipos comunes de roadmaps tecnológicos — Importante
Fuente citada: Technology Roadmapping(2014), Robert Phaal (transcrito“RoadPal”). �� � �Elprofesorlodescribe
como “una especie de revisión del estado del arte” ;mencionaquees del MIT(transcrito“MyT”)conlasalvedad “si no
me equivoco”.
5.2.1 Los ocho tipos (slides 3 y 4)
# Tipo Paraquésirve Capaspropias
1 Planificación de
producto
Relacionalainserciónde
tecnología en la
manufactura de
productos
Productos·Tecnologías
2 Planificación de servicios
/ capacidades
Igualqueeldeproductos
pero ajustado a servicios;
seenfocaencómola
tecnología soporta
capacidades
organizacionales
Gatillos/Asuntos·Drivers
denegocioymercado·
Capacidadesparaabordar
drivers·Desarrollos
tecnológicos
3 Planificación estratégica Desarrollodeuna visión
futura del negocio con
brechas
Mercado·Negocio·
Producto·Tecnología·
Habilidades·Organización
4 Planificación de largo
plazo
Extiende el horizonte de
tiempo;generalmentede
alcance sectorial o
nacional;seenfocaen
desarrollostecnológicos
para converger
Desarrollostecnológicos
(convergentes)
5 Planificación de
conocimiento / activo
Alinea objetivos de
negocio y demandas del
mercadoconiniciativasy
activos de gestión de
conocimiento
Objetivosdenegocio·
Accionesyproyectos
líderes·Habilitadoresde
conocimiento·Procesos
deconocimiento·Activos
deconocimiento
6

## Lamina 7

# Tipo Paraquésirve Capaspropias
6 Planificación de proceso Administracióndel
conocimientoenun área
específica de proceso,
necesariapara incorporar
e integrar la parte
técnica y comercial
Perspectivacomercial·
Procesosdenegocio·
Perspectivatécnica
7 Planificación
programática
Implementaciónde
estrategia directamente
atada al flujo de
proyecto;seenfocaenla
administración
Flujodeproyecto·Hitos
delproyecto·Puntosclave
dedecisión·Desarrollos
tecnológicos
8 Planificación de
integración
Integración y/o
evolución de tecnología:
cómodistintastecnologías
secombinanenproductos
ysistemas,oforman
nuevastecnologías
Componentes/Subsis-
temas→
Prototipos/Sistemasde
prueba→
Sistema/Tecnologías
demostrativas→Sistemas
enproducción
5.2.2 �� � �Precisiones dadas en clase sobre cada tipo
Planificación de producto — el más natural para el curso. > “Una común que podrían hacer es ponerse a pensar
en los productos que necesitan lograr, es decir, en un software ver cuáles son todos los features principales.”
Procedimientooral: listarfeatures→agruparlosporfase→ debajoircolocandolastecnologíasqueserequierenen
cadaplazo. Ejemplo: “necesitamos una interfaz conversacional” (fase1),después “conectores de datos para tener
integraciones con Google Cloud” (fase2).
Planificación estratégica — saltos mucho más grandes. -Elproducto no se elige porque sí : “si yo tengo un
producto más generalista, normalmente voy a un mercado más generalista” . Poresosepuedever por fases de
mercado, pero muy a nivel macro. -�� � �Recomendaciónconcreta: enesteformato “la fase de producto la colocaría
como un saco de features ”,agrupando varias fases deunaplanificacióndeproductodentrode una sola fase
estratégica. Motivo:“las estrategias en general son saltos mucho más grandes” .
Planificación de servicios/capacidades — se toca con la arquitectura. - �� � �Traducciónalenguajedesoftware:
los gatillos/asuntos “normalmente uno lo vería como issues que uno tiene que resolver”,ocomocondicionesque
gatillanelarmadodeunproducto. - �� � �Los driversson “cosas que te van haciendo que vayas” moviendoelroadmap.
Ejemploactualdado: laaparicióndeIAgenerativaconmuchamejor capacidad matemática y científica;esose
leeríacomo driver de mercado — “hay un salto interesante en la capacidad de inferencia de estos modelos […] quizás
deberíamos considerarlo en el roadmap”.
Planificación de conocimiento/activo — el roadmap de Data Science. > �� � �“En Data Science es un roadmap
muy útil.”
Casodeusodado: desarrollar un dataset científico pararesolverunproblemaoalimentarunmodelo. Searma
cuandoelequipoesmástécnico,ylapreguntaqueorganizaelroadmapes:
“Si necesito en seis meses más, o en un año más, tener este activo, ¿cuáles son los pasos que hay antes
para poder lograr ese activo?”
Selollamaexplícitamente activo intelectual.
Planificación de integración — el más común en software. > �� � �“Quizá el más común, diría, de software es la
planificación de integración.”
Se usa cuando hay que llegar a“un sistema más consolidado o robusto, un software que hace muchas cosas” .
Procedimientodescrito:
1. Atacar los MODELOS / componentes INDIVIDUALES
7

## Lamina 8

2. Agruparlos en SUBMÓDULOS / subsistemas
3. Recién entonces encarar UNIDADES MAYORES
▲
└── condición en cada paso: nivel de CONFIANZA alto
("el 90 y tanto por ciento de las veces, ojalá el 100%,
sale con el output esperado")
�� � �Ejemplo desarrollado — automatización de licitaciones. Sisequiereautomatizarelprocesocompletode
licitaciones,hayque “ir cazando primero los temas individuales, las tareas que están entre medio” ,porquenose
puedepretenderqueunmodeloprocesedeunavez un documento de mil páginas enunprocesoquetiene “como
veintitantos pasos” (otrasempresastienen~15). Conclusióntextual:
“No es como que le pedí a Fable: ‘Fable, resuelva este problema’ y te lo va a resolver. Hay altos testeos
entre medio.”
5.2.3 �� � �El costo real del testeo en sistemas con IA
Datoconcretoqueelprofesorentregacomoreferenciademagnitud:
“En un software de licitaciones, el mes pasado, solo en pruebas, nos echamos como trescientos cincuenta
dólares en Gemini probando cosas […] y ni siquiera con modelos grandes: eran modelos Flash, ni siquiera
modelos Pro.”
Conclusión: “son realmente decenas de miles de pruebas ”lasquehayquehacerparamedirelrendimientocon
consistencia.
�� � �Consecuencia para el roadmap — la deprecación de modelos: > “Los modelos los publican y después los van
deprecando […] cuando hay un modelo nuevo hay que tener mecanismos rápidos para [verificar que] ese modelo
nuevo se desempeña bien y hace la tarea con el mismo nivel de certeza. Porque a veces hay modelos que son menos
capaces pero en algunas tareas lo hacen muy bien.”
Estosedefinecomo “parte de hacer software agéntico: estar revisando el estado de esos catálogos de modelos” .
5.3 PASO 01 — Definir la visión de producto — Esencial
Slide de transición (slide 5): “Puede existir cierto nivel de certeza respecto a la visión que se tiene en relación al
producto/servicio.”
5.3.1 Product Vision (slide 7)
Fuente: Product Roadmaps Relaunched (2018), C. Todd Lombardo.
Product Vision: “Clarifica por qué se trae un producto al mercado y por qué su éxito va a significar
algo para el mundo o la empresa.”
Generalmente se asocia a la propuesta de valor.
������ Plantilla de siete campos (memorizable y “rellenable” en un examen):
Campo Quésecompleta
Para [Clienteobjetivo]
Quién [Necesidadesdelclienteobjetivo]
El [Nombredelproducto]
Es un [Categoríadeproducto]
Que [Beneficiodelproducto/razóndecompra]
A diferencia de [Competidores]
Nuestro producto [Diferenciación]
8

## Lamina 9

5.3.2 �� �� � � �Ejemplo desarrollado: ChatGPT (slide 8)
Campo Contenido
Para Profesionales,estudiantesyempresas
Quién Necesitangenerarcontenido,obtenerrespuestas
rápidasomejorarsuproductividad
El ChatGPT
Es un AsistentevirtualdeIA
Que Ofrecerespuestasconversacionalesprecisasy
personalizadas
A diferencia de Otrosasistentesoherramientasdebúsqueda
Nuestro producto Sedestacaporsucapacidadavanzadadeentendimiento
contextualygeneracióncreativaenmúltiplesidiomas
Qué enseña este ejemplo: queladiferenciaciónnoseenunciacomo“somosmejores”,sinocomouna capacidad
concreta y contrastable frenteaunacategoríacompetidoraexplícita.
5.3.3 �� � �La visión debe ser ambiciosa
Puntoinsistidoenclaseyque no aparece en las slides:
“Hay que tener una visión de producto, y una visión en general ambiciosa, para que después esa visión
ambiciosa uno la va cazando obviamente en el roadmap. Eso es como la forma de trabajo.”
�� � �Relación clave: lavisióneselpuntodellegada;elroadmapeselmecanismoquelapersigueporpartes. Una
visiónpocoambiciosaproduceunroadmaptrivial.
5.4 PASO 02 — Priorizar nuestro desarrollo — Esencial
Pregunta disparadora (slide 10): “¿Cómo decidirían qué funcionalidad de la solución implementar primero?”
�� � �Advertenciapreviadelprofesor: “el roadmapping no es solo una grilla de temas que uno va viendo” . Existenotras
herramientasquetambiéncuentancomoroadmapping—porejemplo una carta Gantt.
5.4.1 �� � �Carta Gantt y ruta crítica: cuándo sí y cuándo no
Contenido exclusivamente oralymuyprobableenexamenconceptual,porqueestablece la frontera entre gestión
e innovación:
Carta Gantt / Ruta crítica
Lógica de trabajo La ruta crítica: haymomentosdelaplanificaciónquete
dicensilohicistebienono
Paradigma Gestión : “problemas conocidos, soluciones conocidas”
Supuesto Sepuedeplanificarygestionar “de una forma
relativamente perfecta”
Cuándo aplica Negocios predecibles. Ejemplodado: construcción,
cuando “solo te toca la parte constructiva, no pensar en el
producto que estás vendiendo, sino simplemente construir
la cuestión”
Por qué funciona ahí “No hay mucha incertidumbre respecto a cómo hay que
hacer las cosas”
9

## Lamina 10

�� �Corolario implícito y central del ramo: eninnovación nohayproblemasconocidosnisolucionesconocidas,
porloquelaGanttpuraeselinstrumentoequivocado. Estoconectadirectamenteconelconceptode incertidumbre
delaClase1.
�� � �Matiz posterior en la demo (min 1:13): ensoftwareseprefiere notrabajarconfechasexactas. “Uno coloca
metas más en rango de fechas : ‘ya, en este mes deberíamos tener validado un sistema, el testeo de alguna capa’.” El
roadmapresultante “es como una especie de carta Gantt, no es de precisión , pero sí es referencial”.
5.4.2 Frameworks de priorización (slide 11)
Pregunta que responde la tabla: ¿Qué se hace primero en el plan de desarrollo de un producto/servicio?
Framework Usadopara Elegidocuando Debilidades
Critical Path Identificar “lo único”que
llevaaqueunproductose
leentregueauncliente
(dependenciasycuellosde
botella)
Diseñandoun MVPo
haciendouna expansión
mayordelalcancedel
producto
Noconsideraesfuerzo,
riesgoniobjetivosdel
negocio; no rankea
necesidadesmásalláde
‘crítico’y‘nocrítico’
Kano Model Entender cómo los
clientes perciben el valor
(funcionalidad
vs.satisfacción)
Identificarposibles
extensiones o mejoras
Noconsideraelesfuerzo,
riesgoniobjetivosdel
negocio
Deseabilidad,
factibilidad y viabilidad
Identificar oportunidades
que cumplen con los
criterios de éxito
Sepriorizauna cantidad
pequeñadeiniciativaso
soluciones
Categorías no están
claramente definidas en
términosdenecesidades,
objetivosnitiposde
esfuerzo
ROI Scorecard Rankearideasenbaseaun
criteriode retorno sobre
la inversión (fórmulade
productividad=i/c)
Pesar múltiples factores
y/olistariniciativas,
problemas,featureso
soluciones
Modelo más complejo;
requierealineaciónen
distintoscomponentesde
valoryesfuerzo
MoSCoW Criterio de comunicación
delanzamiento(must,
should,could,willnot
have)
Hay incertidumbre
respectoaquésedebe
incluirenelproducto,
servicioo
lanzamiento/versión
No ayuda a establecer
prioridades, solo a
comunicarlas
�� �Trampa clásica de examen: ladebilidadde MoSCoWesque no prioriza, solo comunica. Eselerrordelectura
másprobabledeestatabla.
5.4.3 Modelo Kano (slide 12) — Esencial
Modelode dos ejes: -Eje horizontal: Noimplementado←→Totalmenteimplementado- Eje vertical: Insatisfacción
←→Satisfacción
Las tres curvas:
Curva Nombresalternativosenlaslide Comportamiento
Necesidades básicas Insatisfacción·“Debenestar”·
Calidad esperada
Curvainferior: sinoestá,genera
insatisfacción;siestá,apenas
alcanzaelpuntoneutro.
Implementarlamás nogenera
satisfacciónadicional
10

## Lamina 11

Curva Nombresalternativosenlaslide Comportamiento
Performance Satisfacción· Calidad deseada Recta diagonal: lasatisfaccióncrece
proporcionalmenteconelnivelde
implementación
Experiencia atractiva Impresionadores · Calidad
excitante
Curvasuperior: sinoestá,nogenera
insatisfacción;siestá,genera
satisfacción desproporcionada
�� � �Descripciónoral: elKano “establece distintas criticidades respecto a las cosas en base a dónde estén ubicadas: si
son necesidades básicas, si son experiencias atractivas” .
�� � �Uso práctico: elKanodice dónde invertir esfuerzo marginal. Sobre-invertirennecesidadesbásicasnocompra
satisfacción;invertiren“impresionadores”sí. Estoconectadirectamenteconel desafío de la entrega final (§0.1,
punto5): demostrarquealgunapartedelasoluciónesexcepcionalequivaleaconstruirun impresionador.
5.4.4 Modelo MoSCoW (slide 13) — Esencial
M — Must
haveDebetener
S — Should
haveDeberíatener
C — Could
havePodríatener
W — Will not
haveNovaatener
Definición Requerimientos
necesarios para
que el proyecto sea
exitoso
Requerimientos
importantesparala
completacióndel
proyectopero no
necesarios/críticos
Requerimientosque
sería bueno tener,
perodemucho
menorimpactosise
dejanfuera
Requerimientos no
prioritariosparael
espaciodetiempo
delproyecto
Criterios • No negociable•
Producto mínimo
viable•Nosepuede
entregaratiempo
sinesto• No es legal
sinesto• No es
segurosinesto•Sin
estoelproyectono
esviable
•Importantepero
no vital• Doloroso
dedejarfuerapero
lasoluciónaúnes
viable•Necesita
algúntipo[de
solución]
•Deseableperono
tantocomoloque
“deberíatener”•
Solo hacer si hay
tiempo o
presupuesto extra
•Fuerade
presupuesto•Fuera
deplazos•Sería
buenotenerpero no
tiene real impacto
�� � �Precisiones de clase: - “Esto se utiliza harto, no tan estructurado, pero sí en el mundo de la gestión.” Enstartupses
comúncategorizarfeaturescomo nice to have vs. must have : “siempre les van a preguntar esas cosas” . -Los must
haveson no negociables yson parte de la estrategia;sinoestá,enpalabrasdelprofesor, “vale hongo la solución
para el cliente”. -�� � �Uso con IA: sepuedepedirlealaIAqueclasifiquelosfeaturesdelproyectoenMoSCoW,
“pero ustedes obviamente lo revisan si no coinciden con lo que está diciendo la IA” .Sirveparatenerrápidamenteuna
nocióndeprioridades.
�� � ��� �� � � �Caso desarrollado: legalidad como must have — GDPR y reclutamiento
Ejemploconcretodeporquéelcriterio “no es legal sin esto” esdeterminante:
• ParavendersoftwareenEuropahayquecumplirel GDPR(transcrito“GDRP”).
• Reglaconcretacitada: una persona no puede ser descartada por la IA ; “una persona siempre tiene que ser el
último que tome la decisión”.
• Consecuenciasinosetratacomo must have: “la solución te la revisan y te la bajan. Literalmente te bloquean
los servidores”.
Qué enseña:lasrestriccionesregulatorias noson“requisitosnofuncionalesquesevendespués”;entrandirectamente
enlacategoríamásaltadeMoSCoWycondicionanlaarquitecturadelproductodesdeelinicio.
11

## Lamina 12

5.4.5 Fórmula de priorización (slide 14) — ������ NÚCLEO CUANTITATIVO DE LA CLASE
(𝑁 𝐶1 + 𝑁 𝐶2 + 𝑂𝑁1 + 𝑂𝑁2)
(𝐸1 + 𝐸2) × 𝐶 = 𝑃
((NC1 + NC2 + ON01 + ON02) / (E1 + E2)) × C = P
└────── V A L O R ──────┘ └ESFUERZO┘ CONFIANZA PRIORIDAD
Símbolo Significado
NC NecesidaddelCliente
ON Objetivodenegocios
E Esfuerzo
C Confianza
P Prioridad
Tabla de ejemplo de la slide (columnas: CN=necesidaddecliente,BO1/BO2= business objectives,E=esfuerzo,
RAW=valor/esfuerzoantesdeconfianza,C=confianza,PTS=puntajefinal):
Feature CN BO1 BO2 E RAW C PTS
A 2 1 1 2 2 75% 1.5
B 1 1 0 2 1 90% 0.9
C 1 2 −1 1 2 40% 0.8
Verificación del cálculo (útil para reproducirlo en una prueba): -A:(2+1+1)/2= 2(RAW)→2×0.75= 1.5-B:
(1+1+0)/2= 1(RAW)→1×0.90= 0.9-C:(1+2−1)/1= 2(RAW)→2×0.40= 0.8
������ Lecciones que la tabla enseña deliberadamente: 1. Los objetivos de negocio pueden ser negativos (BO2=
−1enelfeatureC):unfeaturepuede dañarunobjetivodenegocio,yesoserestadelvalor. 2. A y C tienen el
mismo RAW (2) pero terminan muy separados (1.5vs.0.8): la confianzaeselfactorquedesempata. Unfeature
valiosoybaratopero inciertocaealfinaldelacola. 3. Laconfianzaoperacomo multiplicador,nocomosumando:
castigaproporcionalmente.
�� �Nota de fuentes: lafórmuladeclara dostérminosdenecesidaddecliente(NC1+NC2),perolatabladeejemplo
muestra una sola columnaCN.Lafórmuladebeentendersecomo genérica: nnecesidadesdecliente+ mobjetivos
denegocio,divididosporlasumadeloscomponentesdeesfuerzo.
5.4.6 �� � �De dónde salen los componentes de la fórmula (desarrollo oral)
Elprofesordesarmacadatérminoconcriteriosprácticos:
Necesidad del cliente (NC). -Seponderapor criticidad. “Si algo es muy crítico, obviamente es muy importante.” -
Ejemplodado: enunbacklogde100issues,untemacrítico “va a ser probablemente el primer issue que uno va a
estar tomando, porque si no lo tomas puede que el cliente te corte el agua” . Casotípico: unbug levantado por el
clienteque,sinoseresuelve,hacequesecambieaotrosoftware. Setrata “casi como soporte extremadamente
importante”.
Objetivo de negocio (ON). > “Puede que algo sea importante para el cliente, pero puede que no tenga nada que ver
con lo que uno está haciendo a nivel de producto. Entonces, si no es importante, también hay que ir descartándolo.”
Esfuerzo (E). �� � �Aquíhayunadistinciónconceptualrelevante:
Unidad Descripción Opinióndelprofesor
Tamaño del issue / ticket Seleasignauntamañoalatarea
concreta
Alternativahabitual
12

## Lamina 13

Unidad Descripción Opinióndelprofesor
Tamaño de la historia Unidaddeesfuerzoasignadaala
historia(lenguajede Scrum):
historiapequeñavs.historiagrande.
“Una historia grande a veces es una
historia que hay que armar cinco
features distintos para poder
resolverla”
�� Preferida: “a mí me gusta el
tamaño de la historia […] en la
práctica hay una unidad de software,
pero no sirve de nada si no está
cohesionada; al final lo que importa
es que retorne la historia ”
�� � �Comentarioadicionalsobreelesfuerzoconagentes: hoyhaymuchosissuescuyoesfuerzoes “extremadamente
bajo”— “cosas que a mí me toman literal minutos” —yenesoscasosconviene tomarlos al tiro,porqueesfuerzo
bajonormalmentevadelamanocon complejidad baja.
Confianza (C). �� � �Elprofesorlatraducecomo claridad de los requerimientos ylallama “el problema más común
que yo tengo en el día a día” :
“Hay algo que se define teóricamente, así con sus características, está súper claro, así como las cosas de
rendimiento, pero no hay muestras . No hay muestras de nada, ni del output ni del input. Y eso […]
te podés poner a armar algo, pero ¿cómo después valido que está bien si no tengo muestras para hacer
testeo?”
�� � �Regla derivada: sinmuestrasdeentradaysalida no hay testeo posible,ysintesteolaconfianzaesbaja,por
loqueelfeature baja de prioridad aunqueparezcavalioso. Estovinculadirectamenteestaclaseconlaclasede
métricasytesteo.
5.4.7 �� � �Criterios para elegir entre proyectos (no entre features)
Contenidooral,traídodelramoanterior,aplicablecuandohay varios proyectos candidatos. Buencandidatoa
preguntadedesarrollo.
# Criterio Explicación/ejemplodado
1 Criticidad de la necesidad del
cliente
EjemploCOVID:entrehacer
mascarillasovendercomidaa
domicilio, “el tema de las máscaras
era mucho más crítico en ese
momento”,yporeso ponderaba
muy alto
2 Facilidad de hacer un primer PMV Sielproductotardamucho, “te
afecta en tu capacidad de tener
capital de trabajo”. Escenariode
fracasodescrito: “a los cinco meses
seguís armando un producto, no lo
terminaste, te quedaste sin plata y no
tenés ni producto ni nada”
3 Tamaño del mercado “De las cosas muy relevantes de
innovación”,ponderadopor la
capacidad propia de absorberlo
4 Cercanía con el segmento de
cliente/usuario
“Podés armar un producto, pero si no
puedes llegar al cliente, no sirve
mucho”
5 Que te guste el proyecto Recomendaciónestándaren
innovación: comohaymuchos
cambiosy “el producto va teniendo
remesones”,sinotegustael
proyecto, “al primer remesón vas a
dejar el proyecto botado”
13

## Lamina 14

������ Regla que se enuncia explícitamente combinando (2) y (4): > “Si para ti las dos son fáciles [construirlo y llegar
al cliente], es un buen proyecto para hacer, porque lo podés construir rápido, llegar rápido con el producto y tener
rápidamente retroalimentación.”
Justificación: losproyectosinnovadoresson súper iterativos; “no es como que lo hiciste a la primera y salió bien” .
5.4.8 Ficha de funcionalidad: los 13 campos (slide 15) — Esencial
Principio rector de la slide: “El desarrollo ágil se trata de separar el desarrollo en fracciones menores
e implementar lo más importante .”
# Campo �� � �Comentariodelprofesor
1 ID de funcionalidad EnGitHub,losissuestienen índice
secuencial creciente;elprimeroes
el1. “Si vamos en el issue 200 y
tantos, es porque han tomado 200 y
tantos issues históricos”
2 Nombre de funcionalidad —
3 Descripción —
4 Tipo de funcionalidad —
5 Tiempo estimado de desarrollo en
días
�� �“No sé si el tiempo en días sea
relevante hoy día, porque las cuesta y
las termina mucho menos” (con
agentes,lostiemposse
comprimieron)
6 Tamaño de historia �� “El tamaño de la historia sí creo
que es importante”
7 Valor para el cliente/usuario
(crítico,alto,medio,bajo)
—
8 Usuario/cliente Sepuede separar por rol. Un
proyectonormaltiene 3–4 perfiles
de usuario;proyectosgrandes,
hasta 8. “Créanme que se vuelven
confusas las listas de issues cuando
hay muchos tipos de usuarios”
9 Frecuencia de uso (diario,semanal,
mensual…)
—
10 Incertidumbre de requerimientos
(alto/medio/bajo)
Esel“quétanclarotengoloquehay
quehacer”de§5.4.6
11 Incertidumbre técnica
(alto/medio/bajo)
Verrecuadroabajo
12 Dependencias con otras
funcionalidades
EnGitHubseexplicitaenelissue,o
con sub-issues(unissuegrande
como feature,ylossub-issuescomo
loquevaadentro),oseparandopor
fasecon milestones
13 Requisitos de aceptación con
pruebas
Verrecuadroabajo—elmás
enfatizado
�� � �Recuadro: incertidumbre técnica en Data Science y Deep Learning
“En especial en temas de Data Science, deep learning: del dicho al hecho hay harto tiempo. […] En machine
learning es más fácil , pero en deep learning es tinkering: es ponerse a jugar a ser como el alquimista.”
Eltrabajo,ademásdearquitectónico, “tiene que ver mucho con estudio” : “no es como que sacás el resultado al tiro;
más o menos proyectás qué podés lograr con ciertas características” . Poresolaincertidumbretécnicaenestoscasos
es muy alta.
14

## Lamina 15

�� � �Esto matizalodichoenlaClase1(dondelaincertidumbretécnicasedescribíacomoalgoque “pasa rara vez”,
propiodeDeep/HardTech): enproyectosdelMACIcondeeplearning, sí es un factor esperable.
�� � �Recuadro: la regla más enfática de la clase — requisitos de aceptación
“Nunca hagan un issue si no tiene requisitos de aceptación. Tienen que tener claro cuál es la prueba
que se hace.”
Instrucción operativa concreta: - Al escribir unskill (instrucción reutilizable para el agente), incluir queestén
declaradas las pruebas quesetienenquehacery cuáles son los requisitos para que la prueba sea aceptada . -
Motivo: “si no, se les va a volver muy desordenado el proceso” . -Beneficioadicional: integrarlametodologíade
testeogenera sinergia entre proyectos. Ejemplodelprofesor: “estoy trabajando en un proyecto y digo ‘oye, revisá
este otro proyecto, traé esta cuestión para acá y usá la misma metodología de testeo’, y casi no le tengo que explicar
nada, ni el deploy ni nada” . -Estoseenmarcaenalgodelramoanterior: estandarizar procesos, empaquetar
cosas, estandarizar activos comoactivointelectual.
5.4.9 �� �� � � �Ejemplos de fichas completas (slide 16)
“Es común ver sistemas de priorización de features e historias.”
Campo Ejemplo 1 — Software (LMS)
Ejemplo 2 — Servicio
(gastronomía)
ID 1 10
Nombre Sistemadeanálisis Menúdiariodealmuerzo
Descripción Sistemadeanálisisdeindicadores
parahacerseguimientoa
desempeñocomparativode
actividadesyparticipantesdeLMS
Serviciodealmuerzoquevaríaensu
menúdiariamente
Tipo Clienteadministrador Productosconsumidor
Tiempo estimado 10días 25días
Tamaño de historia 2puntos 5puntos
Valor Crítico Alto
Usuario/cliente Analistayadministrador Comensal
Frecuencia de uso Semanal Diaria
Incert. requerimientos Bajo Media
Incert. técnica Bajo Alta
Dependencias Teneroperativounsistemade
registroparaeventosimportantes
Desarrollodecocina;sistematización
depackagingparallevar;
sistematizacióndeselección,prueba
ypreparaciónderecetas
Aceptación Unusuariopuedevereldesempeño
comparativodedistintosalumnos
endiferentesactividadesdela
plataforma;tambiénpuedehacerlo
mismoconpuntodereferenciade
loscontenidos
Elclientevisitaellocalypuede
comerunalmuerzodiferentetodos
losdías
������ Qué enseñan estos dos ejemplos puestos lado a lado (muy probable en examen): 1. La metodología es
agnóstica al tipo de negocio: lamismafichadescribeunmódulodesoftwareyunserviciogastronómico. 2. Valor
alto ≠ prioridad alta. Elejemplo2tienemenorvalor(Altovs.Crítico), más esfuerzo (25días/5puntos), mayor
incertidumbrederequerimientosytécnica,y más dependencias. Aplicandolafórmulade§5.4.5,elejemplo1
ganaclaramente. 3. Los requisitos de aceptación están escritos como comportamiento observable del usuario ,
nocomoespecificacióntécnica. Eseeselformatocorrecto.
15

## Lamina 16

5.5 Focos de adopción comercial — objetivos y resultados clave — Impor-
tante
Slide de transición (slide 17): “Debemos integrar en nuestra planificación focos de adopción comercial .”
5.5.1 Tabla de objetivos universales (slide 18)
Estructuradetrescolumnas: Objetivo universal → Tema → Resultado clave (formatotipoOKR).
Grupo 1 — Valor sostenible
Objetivo Tema Resultadoclave
Soportealnúcleodelproducto Propiedadesmateriales Chasisdetitanioenprimeraversión
Crearbarrerasparalacompetencia Canalesdedistribución Acuerdodeexclusividadcon
Walmart
Grupo 2 — Crecimiento
Objetivo Tema Resultadoclave
Aumentarparticipacióndemercado Programatrade-incompetitivo 5%departicipaciónaño1
Responderamayordemanda Aumentodeproveedores Reducirquiebredestocken2%
Desarrollarnuevosmercados Versiónparaproveedores Ventaappcontractores200kprimer
año
Mejorarelvalorrecurrente Extensionescomprables 65%tasaderecompra
Grupo 3 — Utilidad
Objetivo Tema Resultadoclave
Soportarmayoresprecios 10añosdegarantía +20%deprecionoreducevolumen
deventasen+5%
Mejorarvalordeciclodevida Conectorespropietarios LTVpromedio+30%ensegundo
producto
Costosbajos Packaginginhouse Reduccióndecostovariabledirecto
en15%en12meses
Equilibraractivosexistentes Marketplacewhitelabel Utilidad+1men12mesesen
capacidaddeservidorociosa*
* La slide corta la frase en “sin”; por contexto, se refiere a capacidad de servidor no utilizada.
������ Qué enseña esta tabla: cada objetivo comercial abstracto seaterrizaenun tema concreto de producto (una
decisióndediseño,materialidad,canalomodelodenegocio)yluegoenun resultado clave medible. Elpatrónes:
objetivo → decisión de producto → métrica . Esexactamentelalógicaquehayquellevaralroadmapparaquela
capacomercialnoquedecomodeclaracióndeintenciones.
�� �Nota de fuentes: elprofesor no desarrolló esta slide en detalle durantelaclase; pasódelapriorización
directamentealasfasesdelciclodevida. Elcontenidoesdeslidey es evaluable.
16

## Lamina 17

5.6 Fases de roadmapping de productos — Esencial
5.6.1 Las cinco fases (slide 19)
Fuente: Product Roadmaps Relaunched (2018),C.ToddLombardo.
Fase Motivación Contenidocaracterístico
1. Nuevo producto Creacióndela primera versión de
unproducto. Startupsyproyectos
deinnovacióncorporativos
Validacióndehipótesis; prototipaje
rápido;testeoyvalidaciones; alto
riesgo comercial
2. Crecimiento Conseguirla mayor cantidad de
clientes posibles
Escalamiento; reorganización de
features; eliminación de features;
mejoracontinua; bajo riesgo
comercial
3. Expansión Expandirel producto núcleo o
expandir líneas de productos y
nuevas áreas
Oportunidadesdelproductocore;
desarrollodenuevosfeatures
4. Explotación Mantenerla “vaca lechera”. Seha
hechountrabajoperfecto
entregandovalor
Market fit + permanencia +
expansión de clientes;usuarios
felices;mantenerelproducto
relevante
5. Fin de ciclo de vida La “puesta de sol” / “ocaso” del
producto
Decadenciademercado; gestión de
stakeholders; dignidad
�� �Detalle fino y muy citable: el riesgo comercial es ALTO en “Nuevo producto” y BAJO en “Crecimiento” . Es
contraintuitivosiunopiensaen“crecer”comoriesgoso;laslidelodicealrevésporqueenCrecimientoyaexiste
evidenciadequealguiencompra.
5.6.2 �� � �Cómo se recorren las fases en un proyecto realmente nuevo
Secuenciadescritaoralmente,aplicableasoluciones “realmente nuevas” (aniveldeUXodetecnología):
1. TECNOLOGÍA / UX NUEVA
· Si es UX nueva (ej. un juego con interacción distinta usando
Unreal Engine como todos): "tratar de dar con esa UX"
· Si es tecnología dura / académica: verificar que el índice o
modelo que se está trabajando "sea confiable y sea bueno"
2. PRODUCTO
· Requiere una VICTORIA EN DISEÑO: "tiene que ser realmente
mucho mejor que la competencia"
· REGLA: "uno entra a competencia con otro NO cuando tiene
tecnología, sino cuando tiene un PRODUCTO"
3. MERCADO / MASIVIDAD
· "Proliferación de aplicaciones": el servicio debe conectar con
muchos estándares existentes y volverse fácilmente consumible
�� � �Corolario sobre software masivo (aplicablealdiseñodelassolucionesdelcurso): cuandoseabordaalusuario
comúnycorriente,lasaplicaciones “normalmente son muy, muy, muy simples, muy generalistas, poco paramétricas”,
yconIAgenerativason “muy customizables sin requerir mucha demanda cognitiva de tener que manejar interfaces,
parámetros y cosas por el estilo” .
5.6.3 �� � �No hagas roadmaps de largo plazo en una startup
Advertenciaexplícitayrepetida:
“No se lo recomiendo por ningún motivo: hacer un roadmap a muy largo plazo en una startup. Uno no
sabe lo que va a pasar en tres meses.”
17

## Lamina 18

Quiénes sí pueden planificar a varios años: - Commodities- Monopolios(ejemplodado: “empresas como el
metro, gas, cosas por el estilo” )-Empresascon condiciones de mercado cuasi-monopólicas (mencionaAmazon)-
Empresasqueplanifican temas centrales específicos(ejemplo: Appleconplanificacióndechips)
“Pero la mayoría del común y silvestre de la empresa no sabemos lo que va a pasar en dos años; sabemos
lo que va a pasar en los próximos meses.”
�� � ��� �� � � �Ejemplo de por qué: líneas de negocio que desaparecieron
Casodadoparamostrarlavolatilidadactual: empresasdedicadascasiexclusivamentea desarrollar paneles de BI
vierondesapareceresalíneadenegocio, “porque ahora armar un dashboard es fácil” .
Matiz importante que agrega: que sea fácilno significa que no haya metodología. Su propio método para
implementarpanelesysistemasdeanalíticasiguelovistoenlaclasedemétricas:
1. Partir con métricas de REPORTERÍA (cosas que uno sabe que están pasando)
2. Después armar LEADING METRICS → tratar de hacer forecasting
3. Hoy, además: bajarlo a DECISIONES, no solo a mirar paneles
("mirar paneles no es muy útil")
5.7 Customer Development (Steve Blank) — Esencial
5.7.1 El proceso de cuatro etapas (slide 20)
Fuente: Customer Development Process, Steve Blank.
┌─────────── BÚSQUEDA ───────────┐ ┌────────── EJECUCIÓN ──────────┐
│ Descubrimiento Validación │ │ Creación Construcción │
│ de clientes de clientes │──►│ de clientes de compañía │
│ (○) PARE (○) PARE │ │ (○) PARE (○) PARE │
│ └──── PIVOTEO ────┘ │ │ │
└────────────────────────────────┘ └───────────────────────────────┘
Etapa Quéocurre
Descubrimiento de clientes Visión a hipótesis : testeoconceptual;presentaciónde
MVP
Validación de clientes Pruebade capacidad de escalar y vender a muchos
clientes
Creación de clientes Escalamiento del primer éxito de ventas atravésde
marketingyventasrobustas
Construcción de compañía Secrean departamentos estructurados y
tradicionalesparaescalarlacompañía
������ Elementos del diagrama que hay que saber leer: 1. Las dos macro-fases: BÚSQUEDA (lasdosprimeras
etapas)y EJECUCIÓN(lasdosúltimas). Búsqueda=todavíanosesabecuáleselnegocio;Ejecución=yasesabey
seescala. 2. Los “PARE”alfinaldecadaetapa: son puertas de decisión. Noseavanzasincumplirlacondición
delogro. 3. El PIVOTEOsoloexistedentrodelazonade BÚSQUEDA:laflechavadesdeValidacióndevueltaa
Descubrimiento. PivotearenEjecuciónnoestácontempladoenelmodelo. 4. Cada etapa es circular (iterativa),no
lineal.
5.7.2 Superposición con las fases de roadmapping (slide 21)
Nuevo producto │ Crecimiento │ Expansión │ Explotación │ Fin ciclo de vida
◄─ BÚSQUEDA ──►│◄──────────────── EJECUCIÓN ─────────────────────────────►
Descubrimiento│ Creación de clientes · Construcción de compañía
18

## Lamina 19

+ Validación │
+ PIVOTEO │
������ Esta es la síntesis conceptual de la clase. Lafasede Nuevo productodelciclodevidaesexactamentelazona
de BÚSQUEDAdelCustomerDevelopment,esdecir: Descubrimiento + Validación + posibilidad de pivotear.
TodolodemásyaesEjecución.
�� � �Implicancia directa para el ramo: losproyectosdelcursoestán todosenlafasedeNuevoproducto/Búsqueda.
Poresosepermitecambiardeproyecto,seesperapivoteo,yseevalúalacapacidaddevalidarynodeescalar.
5.7.3 �� � �Por qué el Customer Development es el paradigma recomendado
“En general el motivo principal es que uno está haciendo algo nuevo. Y en algo nuevo, yo creo que un buen
paradigma de cómo gestionar el trabajo es el customer development. Ciertamente es súper estricto […]
yo creo que es la forma más estricta de ponerse a trabajar en una startup.”
������ La tesis más repetida de toda la sesión:
“El producto no significa nada. Al final del día uno necesita clientes, que es como lo único que importa.
[…] Terminar algo en sí tiene un valor creativo para uno, como personal, pero a nivel de empresa no tiene
ningún valor.”
�� � �YsuconexiónconlaIAgenerativa:
“Lo genial a la hora de la IA generativa es que a veces eso sea mucho más latente: tú puedes terminar algo
pero no sirve de nada . Igual tenés que conseguir clientes, tenés que hacer toda la pega comercial. […]
Ahora el software no es tan importante — era difícil, sigue siendo difícil en algunos casos, pero no es lo
único importante.”
�� � �EstoescoherenteconlodichoenlaClase1sobreporquéelramocambióatresprototipos: terminarelprototipo
yanoeslovalioso.
5.7.4 Condiciones de logro (slide 22)
Loquehayquetener para poder cerrar cada etapa (los“PARE”deldiagrama):
Descubrimiento de clientes Validación de clientes
–Entendimientototaldeproblemasdeclientes,sus
necesidadesypasiones
– Validar por qué el cliente paga. Vender primero.
– Propuesta de valor confirmada –Saberconcertezala utilidad objetivo
– Tamaño de mercado considerable – MVP de alta fidelidad
– Plan de adquisición listo: correos,publicidad,
banners
– Plan de activación listo: landing,capacidadde
compra,procesodecompra
– Dashboard de comportamiento de clientes
�� �Detalle exigible: “Vender primero” aparececomocondicióndelogrode Validación,nodeDescubrimiento.
Conectadirectamenteconla“leydelaevidencia”delaClase1( si te pagan, es la evidencia más alta ).
5.7.5 Estrategias (slide 23)
Descubrimiento de clientes —estrategiasdeentrada
almercado Validación de clientes —palancas
– Mercado existente: venceralacompetenciay
posicionamiento
– Volumen:adquirirlamayorcantidaddeclientes
potencialesparallevarlosalproducto
19

## Lamina 20

Descubrimiento de clientes —estrategiasdeentrada
almercado Validación de clientes —palancas
– Resegmentar mercado: partirdébilyatacaralosmás
débiles,abordandoa) nicho,b) bajo costo,oc) bajo
costo y diferenciación (océano azul)
– Costo: mejorarprogresivamenteelcostode activaral
cliente
– Nuevo mercado: productoradicalmentediferente;es
el más caro en creación de demanda yes de largo
plazo
– Conversión: incrementarelnúmerodepotenciales
clientesquese activan y se vuelven clientes
– Clonar mercado
������ Lo más citable de esta slide: el nuevo mercadoeslaestrategia más cara (porlacreacióndedemanda)y de
largo plazo. Eslaadvertenciacontraelreflejode“inventarunacategoría”.
�� �Nota de fuentes: lasslides22y23fueron mencionadas muy brevemente enlaclase;elprofesorpasórápido
deellasalarecomendaciónprácticaderoadmap. Sucontenidoesdeslideyesevaluable.
5.8 PASO 03 — Considerar matices: un roadmap por audiencia — Esencial
Idea central: noexiste elroadmap. Existeun roadmap por cada audiencia ,concapasdistintas,porquecada
audienciatomadecisionesdistintas.
5.8.1 Roadmap para ingeniería / procesos internos (slide 24)
A quién orienta: alequipoque construye e implementaelproducto—ingenieros,diseñadores,equipo
deoperaciones. Qué le da: uncontextotemáticodealtocontexto,incluyendocaracterísticas,etapasde
desarrollo,expectativasdeescalabilidad,dependenciasyriesgos.
Capa Contenido
Features y soluciones Quésevaadesarrollarparaejecutarelplan
Etapa del desarrollo Denominaciónquedictaprioridadesycontexto
Áreas del producto Equiposinternosasociadosaentregas
Escala Volúmenesdeinput/outputesperados
Tecnología e infraestructura Elementostécnicossubyacentesalosfeatures
Dependencias y riesgos Dependenciasquesonunfactordelasecuencia
Calendario y recursos Recursosdeorganizaciónpersonalizados
�� � �Este es el roadmap que el profesor recomienda explícitamente para los proyectos del curso:
“Este es un roadmap que les recomiendo: roadmap de producto de ingeniería / procesos internos. Que
ustedes puedan ir definiendo los features que necesitan para una solución; en el caso de los prototipos,
establecerlos por capas.”
�� � �Recuadro: la importancia de la capa “Escala” (volumetría)
Puntodesarrolladoconinsistencia:
“Un buen roadmap siempre tiene escalas : que hay que testearlo con 10 clientes, que hay que probarlo
con 10 conectores, los 10 conectores más comunes.”
“Hay que tener una volumetría. El volumen de acción te da perspectiva y te da como objetivo.”
Ejemplodesupropiapráctica: altrabajareltemadeconectores, “nos ponemos metas: vamos a trabajar ahora en 10
conectores distintos para ver estos temas” .
20

## Lamina 21

�� � �Regla práctica exigible: unametaderoadmapsinnúmeronoesunameta. “Probarlosconectores”nosirve;
“probarlos10conectoresmáscomunes”sí.
5.8.2 �� �� � � �Ejemplo integrado: roadmap de un smartwatch (slide 26)
Ejemplomodeloquemuestralascapasdelroadmapdeingenieríadesplegadasalolargodelascincofases. Es el
ejemplo más completo de la clase.
Capa Descubrimiento Validación Expansión Explotación Fin ciclo de vida
Features y
soluciones
Diseñoindustrial
yconceptual;
materialidadde
prueba
demostrativa
Campañade
crowdfunding
(video,RRSS);UI
completa;
materialidad
terminada;specs
deproducción
masiva
Ventadirecta;
API;bundlescon
smartphones
Marketplaces;
integracióncon
otrosservicios
(Strava,Nike
Run,Garmin
Connect,
MyFitnessPal)
Liquidaciones;
incompatibilidad
defeaturesenUI
Etapa de
desarrollo
Financiamiento
gubernamental
Financiamiento
colectivoy
primera
producción
masiva
Escalamientoy
comienzode
proliferaciónde
apps
Integración
horizontaly
retenciónde
usuarios
Transicióna
nuevaversión
Áreas del
producto
Diseñográfico;
desarrollode
software;diseño
industrial
ÍDEM+
Producción;
Comunicaciones
ÍDEM+Supply
chain;Soporte
ÍDEM+Ventas;
Distribución
ÍDEM
Escala 3prototipos;
producción1
unidad;
validacióncon
1.000usuarios
deprueba
Desarrollode3
estudios;
producción
20.000unidades;
basedeusuarios
+10.000
Producción
200.000
unidades;base
deusuarios
+130.000
Producción
300.000
unidades;base
deusuarios
+400.000
Basedeusuarios
−300.000
Tecnología e
infraestructura
Modelosdemo
(maqueta)/
Arduino/
impresión3D;
Ionic(cliente
mobile)
Manufactura
industrializada;
Kickstarter
Cadenade
proveedores
completa;
cadenade
distribución
pequeña
Cadenade
distribuidores
grandes
Kickstarter
Métricas •Financiamiento
obtenido•%de
avancedepro-
ducto/tiempo
•Métricasde
usode
funciones•
Cantidadde
unidades
terminadas
producidas
•Ventas
segmentadas
porcanales•
Métricasdeuso
defunciones•%
decumplimiento
deentrega
producto/fi-
nancistasde
crowdfunding
������ Qué enseña este ejemplo (muy probable en examen): 1. Las capas avanzan en paralelo, no en serie.
Enlamismafasehaydiseñoindustrial,financiamiento,producciónymétricas. 2. La capa “Áreas del producto”
es acumulativa (ÍDEM +): los equipos se van sumando, no se reemplazan. 3.La capa Escala tiene número
siempre,inclusoenelocaso—dondeelnúmeroes negativo(−300.000usuarios). Elfindeciclodevidatambién
seplanificaysemide. 4. Las métricas cambian con la fase : enDescubrimientosondefinanciamientoyavance;
enValidación,deusoyunidadesproducidas;enExpansión,deventasporcanalycumplimientodecompromisos.
21

## Lamina 22

5. El crowdfunding aparece como capa de tecnología/infraestructura , no como marketing: Kickstarter es
infraestructuradefinanciamiento.
�� � �Comentario en clase sobre este ejemplo: “Si estuvieran trabajando en una aplicación en un smartwatch, en
features colocarían el diseño industrial conceptual, la materia de prueba demostrativa para hacer pruebas con los
clientes; después estarían viendo el desarrollo de la UI; si tuvieran que levantar plata estarían trabajando en un
crowdfunding.”
�� � �La lección explícita: hayqueponerenparalelolos distintos desafíos,porque “no solo son desafíos técnicos” :
“Tienen que armar la aplicación que le van a meter al reloj, pero ¿cómo consiguen plata? Esa es la
cuestión. No solo lanzar la aplicación: también llegar a clientes.”
Mencionaqueelmercadoyaestápoblado( Coros, Garmin, “un millón más”),loquerefuerzaqueeldesafíonoes
soloconstruir.
5.8.3 Roadmap para ventas y marketing (slide 27)
A quién orienta: al equipo comercial,acercadela generación de utilidades. Qué le da: contexto
sobrelasventajasqueelproductogeneraentérminosdevalor,asociadoaun calendario de fechas y
plazos críticos.
Capa Contenido
Características y soluciones Quésevaadesarrollarparaejecutarelplan
Clientes objetivos Elgrupoobjetivoasociadoalaresolucióndelproblema
Confianza Porcentaje dequétanprobableesquelosproductos
seanentregadoseneserangodetiempo
Drivers externos Eventosexternosquepodríantenerinjerenciaenel
proyecto(entradaenvigenciaderegulaciones,
convenciones,etc.)
�� �Detalle exigible: lacapa Confianzaaquíesun porcentaje de probabilidad de entrega a tiempo —esdistinta
(aunqueemparentada)dela“confianza”delafórmuladepriorización,queesclaridadderequerimientos. Larazón
dequeexistaestacapaesqueelequipocomercial promete cosas a clientes.
�� � �Justificacióndadaenclaseparateneresteroadmapenparalelo: > “Hay dos flancos en la empresa: el flanco
de producir, como la parte interna de la creación de valor , y otra que es la distribución de valor , que es que el
producto llegue al cliente. Y eso también hay que tenerlo súper claro.”
5.8.4 Roadmap para ejecutivos (slide 28)
A quién orienta: al equipo ejecutivo / dirección,generalmenteenfocadaenla inversióndelaempresa.
Qué le da: contextosobre visión, estrategia y resolución de problemas .
Capa Contenido
Oportunidad de mercado Descripcióndecómoselograexitosamentelacaptura
demercado,larentabilidadylageneracióndeutilidades
Utilidades y costos Indicadoresfinancierosquedimensionen magnitud y
timingdeunesfuerzo,expresadoen resultados
monetarios
�� � �Comentariodeclase: estosroadmapsdeusointerno “uno los ve como implícitos en los pitch deck para efectos
de inversión”: quéoportunidaddemercadoseestácazandoyquéseesperaobtener.
22

## Lamina 23

5.8.5 Roadmap para clientes (slide 29)
Para qué sirve: “Entrega certeza a clientes y usuarios de lo que obtendrán. Esto permite reducir la
incertidumbre del cliente y evitar acciones no deseadas, como evitar que se renueven contratos, servicios,
o perder el cliente.”
Pregunta que plantea la slide: “¿Es comprometerse con una función/producto? ¿Con una fecha? ¿Que
están siendo escuchados?”
Capa Contenido
Espacios de tiempo Separacióntemporalycronológicadeentrega
Features Soluciones/productosqueobtendrán
������ La tensión que plantea esta slide (buenapreguntadedesarrollo): publicarunroadmapalcliente crea una
expectativa. Lapreguntaabiertaes con qué te estás comprometiendo: ¿conlafunción,conlafecha,osimplemente
condemostrarqueestásescuchando? Poresolosroadmapspúblicosreales(§5.9)usanrangosampliosycategorías
como“Future”.
5.8.6 Cuadro comparativo de los cuatro roadmaps — ������ RESUMEN EXIGIBLE
Ingeniería /
procesos Ventas y marketing Ejecutivos Clientes
Audiencia Ingenieros,
diseñadores,
operaciones
Equipocomercial Dirección/inversión Clientesyusuarios
Pregunta que
responde
¿Cómolo
construimos?
¿Cómolovendemos
ycuándo
prometemos?
¿Cuántoinvertimosy
quéretorna?
¿Quévoyarecibiry
cuándo?
Nº de capas 7 4 2 2
Capa distintiva Escala(volumetría),
dependenciasy
riesgos
Confianza (% de
entrega a tiempo) y
driversexternos
Utilidadesycostos
monetarios
Espaciosdetiempo
Nivel de detalle Máximo Medio Mínimo,financiero Mínimo,sin
compromisoduro
5.9 Ejemplos de roadmaps públicos reales — Complementario
Tresreferenciasmostradasalcierredelasslides,todasejemplosde roadmap para clientes:
Fuente Slide Quémuestra
GitHub public roadmap (Beta) 30 TablerotipoKanbanconcolumnas
por trimestre (Q42021·Q12022·
Q22022·Q32022· Future),cada
tarjetaconun roadmap #IDy
etiquetas(beta,ga,shipped,
cloud,server,security &
compliance,in design,
planning…). Tienevistas
alternativas: Board,Table,yfiltros
porproducto
23

## Lamina 24

Fuente Slide Quémuestra
Slack Platform Roadmap (Trello) 31 https://trello.com/b/ZnTQyumQ/slack-
platform-roadmap
Microsoft 365 Roadmap 32 https://www.microsoft.com/en-
us/microsoft-
365/roadmap?filters=
������ Qué enseñan como conjunto: losroadmapspúblicosreales(a)usan rangos temporales amplios (trimestres)
envezdefechas,(b)incluyenunacategoría “Future”sinfecha,y(c)marcan estado de madurez conetiquetas
(beta/GA/shipped)—exactamentelasdenominacionesalfa/beta/releasecandidatedelaClase1. Eslarespuesta
prácticaalatensiónde§5.8.5.
5.10 �� � �Implementación práctica: el roadmap en GitHub — Importante
Estasecciónes casi enteramente oral (demoenvivo). Lasslidessolomuestranelroadmappúblicode
GitHubcomoreferenciavisual. Esdealtovalorprácticoparalasentregasdelramo.
5.10.1 La jerarquía de tres niveles
ISSUES ──agrupados en──► MILESTONES ──asignados a──► PROJECT
(tareas) (fases/hitos) (vista roadmap)
│ │
├── sub-issues (subtareas dentro de un feature grande) ├── vista Board / Kanban
├── etiquetas (labels) ├── vista Table
└── custom fields (prioridad, importancia cliente, status) └── vista Roadmap (temporal)
�� � �El nombre de la funcionalidad,preguntadoexplícitamenteporunalumno: GitHub Projects. Seaccededesde
elrepositorio,yaunProjectsepuede invitar personas.
�� � �Custom fields: en SettingsdelProjectsepuedencrearcampospersonalizados— prioridad, importancia para
el cliente, status, campos de progreso (elprofesornotaesteúltimocomonovedadquenoconocía). Unalumno
(SPEAKER_00)preguntasisirvecomo tiqueteradebugs;elprofesorconfirmaquesí.
�� � �GitHub Actions: mencionadocomocomplemento— “una forma fácil de después tomar pedidos o gestionar
cosas: cuando pasen ciertas cosas en GitHub, uno gatilla cierto flujo de trabajo” .
�� � �Alternativas mencionadas: GitLab (aunque “en GitLab no está todo tan acabado a nivel de proyecto” ), GitKraken.
“Hay harto software para hacer esto mismo […] pero todos son gratis.”
5.10.2 �� � �GitHub CLI, no el MCP
Recomendacióntécnicaexplícitaytransferibleaotrasherramientas:
“GitHub tiene un MCP, pero el MCP es muy pobre: no tiene muchas habilidades. Y todas las empresas,
cuando uno trabaja en software a escala corporativa, tienen el CLI.”
Regla general que enuncia: > “Cada vez que trabajen con un software técnico” ,buscarsuCLI.Ejemplosdados: AWS
CLI(“todo lo que podés hacer en Amazon lo podés hacer vía terminal” ), Vultr CLI(transcrito“vulture”), Google Cloud.
Por qué existe el CLI: automatización. Ejemplodado: unnegociodehostingnopuedeteneraalguienentrando
manualmentealaconsola “cada vez que alguien inicia un servidor” —todosehaceautomático.
Por qué importa hoy: > “La verdad, no se tienen que aprender esto: los agentes ya saben esto de memoria. Le decís
lo que necesitás y te lo resuelven. Hasta montar servidores: te aprovisionan solo las cosas.”
• Cobertura: “todas las funciones de GitHub tienen cobertura con el GitHub CLI” .
• Instalaciónydocumentación: enla wiki del proyecto delrepositoriodelcurso.
24

## Lamina 25

5.10.3 �� � �Qué se hizo en la demo en vivo
Secuenciaobservada(elprofesorledictaaunagenteconcapacidadde computer use):
1. Partirdeunrepositoriocon 16 issues cerrados (ajusteshechosaunaaplicación).
2. Pediralagente: “con el GitHub CLI, arma los milestones” →losmilestonessecrean.
3. Pedir: “organiza los issues en los milestones, crea un proyecto con roadmap” .
4. Después,paraefectoseducativos: “ponle fechas a los milestones y agrégalos” .
5. Resultado: unavista de roadmap temporal organizadapormilestones.
Resultado evaluado por el profesor: “Hay un roadmap hecho en un par de minutos […] bien impresionante. Trabajó
bien rápido.” Ycomentaquelegustaríacomparareldesempeñocon Fable(modelodeClaude).
�� �Nota de fuentes: elmodelousadoenlademosetranscribecomo “ Astra”yselodescribecomoreciénpublicado
(“salió ayer”),muyrápidoengeneracióndetokens,yusadoenmodo fast. Tambiénsemenciona “la solución de
computer use de OpenAI”.Latranscripciónesdemasiadofragmentariaparareconstruirconseguridadquéproducto
escadacosa;verelAnexo.
5.10.4 �� � �Convenciones de versionado y milestones
Convención Detalle
Fase 0 “Normalmente uno coloca en la fase 0 […] una
convención: la fase 0 es tu desarrollo ”. Reciéncuando
elproductoestáterminadovienela versión 1
Lanzar en 0.x “Hay empresas que a veces hacen lanzamiento con
versión 0.algo, como para decir aún no está terminado ,
a pesar de que igual es un producto que uno puede
consumir y usar”
Tamaño de un bloque de milestone “Un bloque de software normalmente no es como un día:
son bloques de este tamaño, como siete días, diez días ”,
cuandosonissuescomplejos
5.10.5 �� � �Volumetría de issues y observabilidad
Referenciasnuméricasdadascomocriteriodesaluddelproyecto:
Dato Cifra
Issuesactivosenunproductodesoftware sano y activo “al menos siempre como 100 issues activos ”
Issuesal iniciarunproyecto “tenés como 70, 80 issues ”
Issuesenelproyectodelademo 16( “es una lista de 16 issues” —localificadepoco
ambicioso)
“Si su proyecto no tiene 100 issues, la verdad no están haciendo nada […] probablemente no hay mucho
que estén trabajando.”
�� � �Matiz importante: “los issues uno no los toma todos . Hay unos que son especulativos, como propuestas de ‘ahí
podríamos hacer’. También implica que hay conversaciones dando vuelta de temas que todavía no se resuelven si se
van a hacer o no.”
�� � �Discusión con alumnos: ¿esto no es solo para empresas grandes?
Dosalumnos(SPEAKER_00)planteanlaobjeción: todaestacapadegestiónexistiríaporprocesoscorporativos,
KPIsydespliegues,yparaunastartuppequeña “sumar todas estas integraciones igual suma costo en el proceso de
fabricar un software”.
Respuesta del profesor (contenidoconceptualrelevante):
25

## Lamina 26

1. Observabilidad con agentes. Silepidesaunagente “resolvamos issues”,elagente “se va a tener que leer los
100 issues, pero ¿cómo va a saber cuáles son los temas críticos?” . Darlemetadata a los issues permiteque
tantoelagentecomolaspersonassepanquéesurgenteyporqué. Ejemplo: “puede que haya 10 issues fáciles,
pero acá hay uno crítico, y es crítico porque el cliente lo levantó como un bug” .
2. Product management con agentes. Mencionaqueunsociosuyo,noprogramador, “tiene un agente que es
su jefe de operaciones, su cabeza de operaciones” ,yconélgestionaadiariolosproyectosde tres empresas.
3. El costo cambió. “Muchas cosas que para personas no muy técnicas, o con equipos no muy grandes, antigua-
mente era muy difícil de hacer, ahora se pueden hacer fácil con los agentes.” Poresovalelapenatenerlas
capasdemetadatayobservabilidad: “te dan una operación más consistente” .
4. Cuándo se vuelve indispensable. “Cuando ya un equipo empieza a crecer […] necesitás más observabilidad
de cómo se van [tomando] decisiones, porque hay muchos flancos corriendo en paralelo.” Trabajandosoloes
menosnecesario,pero “con agentes yo siempre lo usaría” .
5. No es nuevo. “Para la gente que está en entornos corporativos y trabaja con metodología ágil, esto es la forma
de trabajar; no le estoy diciendo nada nuevo.”
5.10.6 �� � �“Performance as a feature”: el rendimiento como driver de roadmap
Digresiónconcontenidoconceptualaprovechable,dichaapropósitodelos drivers de mercado:
“Hace algunos meses se empezó a hablar de performance as a feature : el rendimiento como una
funcionalidad de estos modelos. Porque además de que ya se están logrando niveles altos de resolutividad
y asertividad haciendo tareas, ciertamente el peldaño que sigue es hacerlo más rápido .”
Por qué la velocidad no es solo comodidad — habilita casos de uso nuevos: - “Se deben dar otras interacciones
que no son posibles si el modelo no funciona muy rápido.” - Ejemplo dado: un sistema de cámaras conunmodelo
“mirando y tomando decisiones en tiempo real” ,en stream continuo. “Necesita esa velocidad de generación […] para
ese caso de uso.” Seseñalacomomuyútilpara aplicaciones empresariales.
������ Recomendación explícita para el roadmap: > “Uno hoy día, si va a hacer un roadmap, es cauto ponerse a
pensar que en seis meses más la velocidad de estos modelos va a ser mucho más rápida […] y eso te abre hartos
otros casos de uso. Hay que tenerlo detectado, porque van a aparecer en los negocios.”
�� � �Cómo se usa esto en un roadmap: esun driver externo (capadelroadmapdeventasymarketing,slide27)y
alavezunsupuestodelacapadetecnología: sepuedeplanificarfeaturesque hoy no son viables peroquelo
seránenelhorizontedelroadmap.
��� ���� ����� LISTA DE DEFINICIONES IMPORTANTES
Término Definición
Roadmapping Instrumentoquefacilitalaevolucióndemercados,
productosytecnologíasenconjunto,estableciendo
vínculosentreambasperspectivas. (slide 2)
Roadmap genérico Gráficotemporalquecomprendeundiversonúmerode
capasquenormalmenteincluyenperspectivastécnicasy
comerciales. (slide 2)
Product Vision Clarificaporquésetraeunproductoalmercadoypor
quésuéxitovaasignificaralgoparaelmundoola
empresa;seasociaalapropuestadevalor. (slide 7)
Critical Path Frameworkparaidentificar“loúnico”quellevaaqueun
productoseentregueauncliente: dependenciasy
cuellosdebotella. (slide 11)
Modelo Kano Modeloquerelacionaniveldeimplementacióndeuna
funcionalidadconsatisfacción/insatisfaccióndelcliente,
distinguiendonecesidadesbásicas,performancey
experienciaatractiva. (slides 11–12)
26

## Lamina 27

Término Definición
Necesidades básicas (Kano) “Debenestar”; calidad esperada. Suausenciagenera
insatisfacción;supresencianogenerasatisfacción. (slide
12)
Performance (Kano) Calidaddeseada;lasatisfaccióncrecelinealmenteconel
niveldeimplementación. (slide 12)
Experiencia atractiva (Kano) “Impresionadores”; calidad excitante. Suausenciano
molesta;supresenciagenerasatisfacción
desproporcionada. (slide 12)
MoSCoW Criteriode comunicacióndelanzamiento: Must/
Should/Could/Willnothave. (slides 11, 13)
Must have Requerimientonecesarioparaqueelproyectosea
exitoso;nonegociable;eselPMV;sinestonoeslegal,
noessegurooelproyectonoesviable. (slide 13)
Should have Importanteperonovital;dolorosodedejarfuera,pero
lasoluciónsiguesiendoviable. (slide 13)
Could have Deseable,perodemuchomenorimpactosisedeja
fuera;solosihaytiempoopresupuestoextra. (slide 13)
Will not have Noprioritarioparaelespaciodetiempodelproyecto:
fueradepresupuesto,fueradeplazos,sinrealimpacto.
(slide 13)
Confianza (C) (fórmula) Multiplicadordelaprioridad;enclaseseexplicacomoel
nivelde claridad de los requerimientos ylacapacidad
delograrelresultado. (slide 14 + clase)
Confianza (roadmap de ventas) Porcentajedequétanprobableesquelosproductos
seanentregadoseneserangodetiempo. (slide 27)
Tamaño de historia Unidaddeesfuerzoasignadaaunahistoria(Scrum);una
historiagrandepuederequerirarmarvariosfeatures
distintos. (slide 15 + clase)
Requisitos de aceptación Condicionesypruebasquedefinencuándouna
funcionalidadseconsideraterminadaycorrecta. (slide
15)
Fase “Nuevo producto” Fasemotivadaporlacreacióndelaprimeraversiónde
unproducto;validacióndehipótesis,prototipajerápido,
testeo, alto riesgo comercial. (slide 19)
Fase “Explotación” Mantenerla“vacalechera”;marketfit+permanencia+
expansióndeclientes. (slide 19)
Fin de ciclo de vida La“puestadesol”/“ocaso”delproducto: decadenciade
mercado,gestióndestakeholders,dignidad. (slide 19)
Customer Development ProcesodeSteveBlankencuatroetapas—
Descubrimiento,Validación,Creacióndeclientesy
Construccióndecompañía—divididoen Búsqueday
Ejecución. (slide 20)
Pivoteo RetornodesdeValidacióndeclienteshacia
Descubrimientodeclientes;soloexistedentrodela
zonadeBúsqueda. (slide 20)
Descubrimiento de clientes Visiónahipótesis: testeoconceptual;presentaciónde
MVP. (slide 20)
Validación de clientes Pruebadecapacidaddeescalaryvenderamuchos
clientes. (slide 20)
Resegmentar mercado Estrategiadepartirdébilyatacaralosmásdébilesvía
nicho,bajocosto,obajocostoydiferenciación(océano
azul). (slide 23)
Escala (capa de roadmap) Volúmenesdeinput/outputesperados. (slide 24)
Drivers externos Eventosexternosconinjerenciaenelproyecto: entrada
envigenciaderegulaciones,convenciones,etc. (slide 27)
27

## Lamina 28

Término Definición
Milestone (GitHub) �� � �Agrupacióndeissuesquerepresentaunhitoofase
deldesarrollo
GitHub Projects �� � �FuncionalidaddeGitHubquepermitegenerarvistas
(board,tabla,roadmaptemporal)sobreissuesy
milestones
Performance as a feature �� � �Conceptosegúnelcualelrendimiento/velocidadde
unmodeloesensíunafuncionalidad,porquehabilita
casosdeusoimposiblesamenorvelocidad
������ FÓRMULAS Y PROCEDIMIENTOS
F1 — Fórmula de priorización (única fórmula matemática del ramo)
(NC₁ + NC₂ + ON₁ + ON₂)
P = ───────────────────────── × C
(E₁ + E₂)
└──────── RAW ────────┘
NC = Necesidad de Cliente ON = Objetivo de negocio
E = Esfuerzo C = Confianza (0–1)
P = Prioridad
Lectura: Prioridad = (Valor / Esfuerzo) × Confianza Advertencias: los ON pueden sernegativos; la
confianzaes multiplicativa,noaditiva.
P1 — Procedimiento general de roadmapping (los tres pasos)
PASO 01 — DEFINIR VISIÓN DE PRODUCTO
Plantilla: Para / Quién / El / Es un / Que / A diferencia de / Nuestro producto
Condición: la visión debe ser AMBICIOSA
PASO 02 — PRIORIZAR EL DESARROLLO
a) elegir framework (Critical Path · Kano · D-F-V · ROI Scorecard · MoSCoW)
b) fichar cada funcionalidad (13 campos)
c) calcular P = (Valor/Esfuerzo) × Confianza
d) ordenar
PASO 03 — CONSIDERAR MATICES
Construir un roadmap POR AUDIENCIA:
ingeniería/procesos (7 capas) · ventas y marketing (4) ·
ejecutivos (2) · clientes (2)
P2 — �� � �Procedimiento de construcción por integración (software)
1. Atacar componentes / modelos INDIVIDUALES
2. Agrupar en SUBMÓDULOS / subsistemas → prototipos y sistemas de prueba
3. Encarar UNIDADES MAYORES → tecnologías demostrativas
4. Sistemas EN PRODUCCIÓN
Condición en cada paso: nivel de confianza alto
("el 90 y tanto %, ojalá el 100%, sale con el output esperado")
28

## Lamina 29

P3 — �� � �Procedimiento de implementación en GitHub
1. Crear ISSUES (con requisitos de aceptación SIEMPRE)
2. Agrupar issues en MILESTONES (fases; bloques de ~7–10 días)
3. Asignar a un PROJECT
4. Añadir CUSTOM FIELDS (prioridad, importancia cliente, status, progreso)
5. Generar vista ROADMAP (opcionalmente con fechas en los milestones)
Herramienta: GitHub CLI (no el MCP, que es "muy pobre")
R1 — �� � �Regla de la volumetría
Toda meta de roadmap debe tener NÚMERO.
✗ "probar los conectores"
✓ "probar los 10 conectores más comunes"
✓ "testear con 10 clientes" · "validar con 1.000 usuarios de prueba"
R2 — �� � �Regla del horizonte
Startup / proyecto de innovación → roadmap de MESES (no años)
Roadmap de varios años → solo commodities, monopolios, o
temas centrales muy específicos
R3 — �� � �Regla de la aceptación
NUNCA crear un issue sin requisitos de aceptación.
Debe estar declarado: (a) qué prueba se hace,
(b) qué requisitos hacen que la prueba se acepte.
��� POSIBLES PREGUNTAS DE EXAMEN CON RESPUESTAS BREVES
P1. Defina roadmapping y describa la estructura de un roadmap genérico. Esuninstrumentoquefacilitala
evolución conjuntademercados,productosytecnologías,estableciendovínculosentrelaperspectiva técnicayla
comercial. Elroadmapgenéricoesun gráfico temporal por capas;lascapascanónicasson Mercado, Producto,
Tecnología, Programa I+D y Recursos,desplegadassobrecortestemporales(tx1,tx2,tx3).
P2. Enumere los tres pasos del método de roadmapping visto en clase. (1) Definir la visión de producto;(2)
priorizar nuestro desarrollo;(3) considerar matices,esdecir,construirunroadmapdistintoporaudiencia.
P3. Complete la plantilla de Product Vision para un producto a elección. Lossietecamposson: Para[cliente
objetivo]/ Quién[necesidadesdelclienteobjetivo]/ El[nombredelproducto]/ Es un[categoríadeproducto]/ Que
[beneficioorazóndecompra]/ A diferencia de [competidores]/ Nuestro producto[diferenciación]. Ejemplodela
slide: ChatGPT,paraprofesionales/estudiantes/empresasquenecesitangenerarcontenidoymejorarproductividad,
esunasistentevirtualdeIAqueofrecerespuestasconversacionalesprecisasypersonalizadas,adiferenciadeotros
asistentesobuscadores,destacándoseporsuentendimientocontextualavanzadoygeneracióncreativaenmúltiples
idiomas.
P4. ¿Cuál es la debilidad principal de MoSCoW y por qué es relevante? Que no ayuda a establecer prioridades,
solo a comunicarlas. Esrelevanteporqueseusamuchísimoenlaprácticayseloconfundeconunmétodode
priorización: MoSCoWordenala conversaciónsobreelalcance,peronodicequéconstruirprimerodentrodelos
must have. Paraesohacefaltaunmétodoconesfuerzoyconfianza,comolafórmuladepriorización.
P5. Explique el modelo Kano y sus tres curvas. Cruza nivel de implementación (horizontal)con satisfacción/in-
satisfacción(vertical). Lasnecesidades básicas(“debenestar”,calidadesperada)generaninsatisfacciónsifaltan
peronosatisfacciónsiestán;la performance(calidaddeseada)hacecrecerlasatisfacciónproporcionalmenteal
niveldeimplementación;la experiencia atractiva(“impresionadores”,calidadexcitante)nomolestasifalta,pero
generasatisfaccióndesproporcionadasiestá. Suutilidadesdecidir dónde poner el esfuerzo marginal.
29

## Lamina 30

P6. Escriba la fórmula de priorización y explique el rol de cada componente. ¿Qué pasa si un objetivo de
negocio es negativo? P = ((NC₁+NC₂+ON₁+ON₂) / (E₁+E₂)) × C.Elnumeradoresel valor(necesidadesde
cliente+objetivosdenegocio),eldenominadoresel esfuerzo,yla confianzamultiplicaelcociente. Unobjetivode
negocionegativo resta valor: significaqueelfeatureperjudicaeseobjetivo(enlatabladelaslide,elfeatureC
tieneBO2=−1). Quelaconfianzaseamultiplicativahacequedosfeaturesconelmismococientevalor/esfuerzo
terminenmuyseparados: AyCtienenRAW=2,perocon75%y40%deconfianzadan1,5y0,8respectivamente.
P7. Enumere los 13 campos de la ficha de una funcionalidad. ID,nombre,descripción,tipodefuncionalidad,
tiempo estimado en días, tamaño de historia, valor para el cliente/usuario, usuario/cliente, frecuencia de uso,
incertidumbrederequerimientos,incertidumbretécnica,dependenciasconotrasfuncionalidadesyrequisitosde
aceptaciónconpruebas.
P8. Compare los dos ejemplos de ficha de la slide 16 y decida cuál priorizaría. El“Sistemadeanálisis”(valor
crítico,2puntosdehistoria,incertidumbrederequerimientosytécnica bajas,unasoladependencia)dominaal
“Menúdiariodealmuerzo”(valoraltopero5puntos,incertidumbrederequerimientosmedia,incertidumbretécnica
altay tresdependencias). Aplicandolafórmula: másvalor,menosesfuerzoymásconfianza→prioridadmayor.
Además,elpardeejemplosmuestraquelametodologíaes agnóstica al tipo de negocio: sirveigualparasoftware
queparaunserviciogastronómico.
P9. Enumere las cinco fases de roadmapping de productos y diga en cuál el riesgo comercial es alto. Nuevo
producto → Crecimiento → Expansión → Explotación → Fin de ciclo de vida. Elriesgo comercial es alto en
“Nuevo producto”(validacióndehipótesis,prototipajerápido,testeo)y bajo en “Crecimiento”(escalamiento,
reorganizaciónyeliminacióndefeatures,mejoracontinua).
P10. Describa el proceso de Customer Development y explique dónde puede ocurrir el pivoteo. Cuatroetapas:
Descubrimiento de clientes (visiónahipótesis,testeoconceptual,presentacióndeMVP), Validación de clientes
(probarcapacidaddeescalaryvenderamuchosclientes), Creación de clientes (escalarelprimeréxitodeventas
conmarketingyventasrobustas)y Construcción de compañía (departamentosestructuradosparaescalar). Las
dosprimerassonlafasede BÚSQUEDAylasdosúltimasde EJECUCIÓN;entreetapashaypuertasdedecisión
(“PARE”).El pivoteo solo ocurre dentro de la Búsqueda ,volviendodeValidaciónaDescubrimiento.
P11. ¿Cómo se superponen las fases de roadmapping con el Customer Development? La fase deNuevo
productodelciclodevidacoincideconlazonade BÚSQUEDA(Descubrimiento+Validación+pivoteo);lasfases
de Crecimiento, Expansión, Explotación y Fin de ciclo de vida caendentrode EJECUCIÓN(Creacióndeclientesy
Construccióndecompañía).
P12. Mencione tres condiciones de logro de la Validación de clientes. Entreotras: validar por qué el cliente
paga —“vender primero”,saberconcertezala utilidad objetivo,tenerun MVP de alta fidelidad,un plan de
adquisiciónlisto(correos,publicidad,banners),un plan de activación listo(landing,capacidaddecompra,proceso
decompra)yun dashboard de comportamiento de clientes.
P13. ¿Cuál de las estrategias de entrada al mercado es la más cara y por qué? El nuevo mercado: producto
radicalmentediferente. Eselmáscaro en creación de demanda yesde largo plazo,porquehayqueeducaraun
mercadoqueaúnnoexiste. Lasalternativassonmercadoexistente(venceralacompetencia),resegmentar(nicho/
bajocosto/bajocosto+diferenciación=océanoazul)yclonarmercado.
P14. Nombre los cuatro tipos de roadmap por audiencia e indique la capa distintiva de cada uno. Inge-
niería/procesos internos (7capas;distintiva: Escalay dependencias y riesgos); ventas y marketing (4capas;
distintiva: Confianzacomo % de probabilidad de entrega a tiempo, ydrivers externos); ejecutivos(2 capas:
oportunidaddemercado,y utilidades y costos entérminosmonetarios); clientes(2capas: espaciosdetiempoy
features).
P15. ¿Para qué sirve un roadmap de producto para clientes y qué tensión plantea? Sirvepara entregar certeza
alclientesobreloqueobtendrá,reduciendosuincertidumbreyevitandoaccionesnodeseadascomonorenovar
contratososervicios. Latensiónqueplantealaslidees con qué se está comprometiendo la empresa : ¿conuna
función/producto,conunafecha,osolocondemostrarqueelclienteestásiendoescuchado? Poresolosroadmaps
públicosrealesusantrimestresycategoríastipo“Future”envezdefechasexactas.
P16. Describa el roadmap de “planificación de integración” y por qué es el más común en software. Suscapas
son Componentes/Subsistemas → Prototipos/Sistemas de prueba → Sistema/Tecnologías demostrativas →
Sistemas en producción,ydescribecómodiferentestecnologíassecombinanenproductosysistemasoforman
30

## Lamina 31

nuevastecnologías. Eselmáscomúnensoftwareporquellegaraunsistemarobustoexigeresolver subsistema
por subsistema,contesteoentremedioyunniveldeconfianzaaltoencadapasoantesdeagruparenunidades
mayores.
P17. �� � �¿Por qué la carta Gantt no es el instrumento adecuado para un proyecto de innovación? Porquelacarta
Ganttoperabajoel paradigma de gestión: “problemasconocidos,solucionesconocidas”,dondesepuedeplanificar
yejecutardeformarelativamenteperfecta. Funcionaennegociospredecibles(ejemplodado: laparteconstructiva
deunaobra)porque no hay incertidumbre sobre cómo hacer las cosas . Eninnovaciónlaincertidumbreesel
rasgodefinitorio,porloqueseprefierenrangosdefechasymilestonesreferencialesporsobrefechasdeprecisión.
P18. �� � �¿Qué criterios usaría para elegir entre varios proyectos de innovación? Criticidaddelanecesidaddel
cliente(ejemplo: mascarillasduranteelCOVID), facilidad de construir un primer PMV (porsuimpactoenelcapital
detrabajo),tamañodemercadoponderadoporlacapacidadpropiadeabsorberlo, cercanía con el segmento
de cliente/usuario,yqueelproyecto te guste (porquealprimerremesónseabandonaloquenointeresa). La
reglacombinada: siconstruirlo yllegaralclientesonfáciles,esunbuenproyecto,porquepermiteretroalimentación
rápidaenunprocesoqueesintrínsecamenteiterativo.
P19. �� � �¿Por qué no se recomienda hacer un roadmap de largo plazo en una startup? Porquenosesabequéva
apasarnientresmeses. Solopuedenplanificaravariosañoslos commodities,los monopoliosocuasi-monopolios,
ylasempresasqueplanifican temas centrales muy específicos (ejemplo: Appleconchips). Elcasoilustrativodado
esladesaparicióndelíneasdenegociocompletasdedicadasaconstruirpanelesdeBI,porquearmarundashboard
sevolviófácil.
P20. �� � �¿Qué es “performance as a feature” y cómo afecta a un roadmap? Eslaideadequeel rendimiento/ve-
locidadde un modelo es en sí una funcionalidad, porque habilita interacciones imposibles a menor velocidad
(ejemplo: unsistemadecámarasconunmodelotomandodecisionesentiemporealsobreunstreamcontinuo).
Afectaalroadmapcomo driver externo: convieneplanificarasumiendoqueenseismeseslosmodelosseránmucho
másrápidos,loqueabrecasosdeusoquehoynosonviables.
P21. �� � �¿Cuál es la regla sobre requisitos de aceptación y por qué importa? Nunca crear un issue sin requisitos
de aceptación: debeestardeclaradoquépruebasehaceyquérequisitoshacenquelapruebaseacepte. Importa
porquesinesoelprocesosevuelvedesordenado,yporquelaconfianza(componentemultiplicativodelaprioridad)
dependedepodertestear—sinmuestrasdeinputyoutputnohaytesteoposible,aunqueelrequerimientoesté
descritoconprecisiónteórica.
�� �ERRORES Y CONFUSIONES COMUNES
1. Creer que MoSCoW prioriza. No: solo comunica prioridadesyaestablecidas. Esladebilidadquelapropia
slide11declara.
2. Confundir las dos “confianzas”. Enla fórmula de priorización (slide14)laconfianzaeslacertezadepoder
lograrelresultado/claridadderequerimientos. Enel roadmap de ventas y marketing (slide27)laconfianza
esel porcentaje de probabilidad de entregar a tiempo . Sonconceptosdistintosconelmismonombre.
3. Sumar la confianza en vez de multiplicarla. Laconfianzaesun multiplicador;poresodosfeaturesconel
mismococientevalor/esfuerzopuedenquedarmuyseparadosenprioridad.
4. Asumir que los objetivos de negocio solo suman. Puedenser negativos(BO2=−1enelejemplo): un
featurepuededañarunobjetivodenegocio.
5. Pensar que el riesgo comercial crece con las fases. Alrevés: laslide19lodeclara alto en “Nuevo producto”
y bajo en “Crecimiento”.
6. Creer que se puede pivotear en cualquier momento. EnelmodelodeBlankel pivoteo solo existe dentro
de la fase de BÚSQUEDA (Validación→Descubrimiento). UnavezenEjecución,elmodelonolocontempla.
7. Confundir Descubrimiento con Validación de clientes. Descubrimientoes visión a hipótesis,testeoconcep-
tualypresentacióndeMVP;Validaciónesprobarla capacidad de escalar y vender a muchos clientes ,yahí
aparecelacondición “vender primero”.
8. Creer que hay un solo roadmap por proyecto. Hay uno por audiencia,concapasyniveldedetalledistintos:
ingeniería(7capas),ventas(4),ejecutivos(2),clientes(2).
9. Confundir “planificación de producto” con “planificación de integración”. Laprimerarelacionatecnología
conmanufacturadeproductos(capas: Productos/Tecnologías);lasegundadescribecómodistintastecnologías
31

## Lamina 32

se combinan parallegarasistemasenproducción,pasandoporsubsistemas,prototiposydemostradores.
10. Confundir “planificación estratégica” con “planificación programática”. Laestratégicaesuna visión
futura del negocio con brechas (Mercado,Negocio,Producto,Tecnología,Habilidades,Organización);la
programática es laimplementaciónatada al flujo de proyecto, enfocada en administración (Flujo, Hitos,
Puntosclavededecisión,Desarrollostecnológicos).
11. Poner metas sin volumetría. Unroadmapsin escala(10clientes,10conectores,1.000usuariosdeprueba,
20.000unidades)nodaniperspectivaniobjetivo.
12. Creer que las capas del roadmap se recorren en serie. Elejemplodelsmartwatchmuestraqueenuna
mismafaseavanzan en paralelofeatures,financiamiento,producción,áreasinvolucradasymétricas.
13. Asumir que “Áreas del producto” cambia de fase en fase. Es acumulativa(ÍDEM+): losequipossevan
sumando.
14. Pensar que la fase de fin de ciclo de vida no se planifica. Síseplanificaysemide: laslide26leasignauna
escalaexplícita( −300.000 usuarios)ylaslide19leasignacontenido(decadenciademercado,gestiónde
stakeholders, dignidad).
15. Creer que “tiempo estimado en días” sigue siendo el mejor estimador de esfuerzo. Elprofesorlocuestiona
explícitamente con agentes; prefiere eltamaño de historia, porque la unidad que importa es la historia
cohesionada,nolatareaaislada.
16. Confundir tamaño de issue con tamaño de historia. Unahistoriagrande “a veces es una historia que hay
que armar cinco features distintos para poder resolverla” .
17. Tratar los requisitos regulatorios como algo posterior. Elcriterio “no es legal sin esto” losponedirectamente
en must have(casoGDPR:unapersonanopuedeserdescartadaporlaIA).
18. Creer que un backlog corto es señal de orden. Segúnelprofesor, unproyectosanotiene~100issues
activos,ymuchosson especulativos—reflejanconversacionesabiertas,nocompromisos.
19. Confundir la visión de producto con el roadmap. Lavisiónesel punto de llegada ambicioso;elroadmap
eselmecanismoquelava“cazando”porpartes.
20. Creer que terminar el producto es el logro. Latesisrepetidaeslaopuesta: “el producto no significa nada; al
final del día uno necesita clientes” . Terminaralgotienevalorcreativopersonal,peroaniveldeempresano
tieneninguno.
21. Suponer que toda esta gestión es solo para empresas grandes. Elargumentodelprofesoresquecon
agenteselcostodemantenermetadatayobservabilidadbajótantoqueconvieneinclusotrabajandosolo,
porque el agente necesita esa metadata parasaberquéescrítico.
22. Usar el MCP de GitHub en vez del CLI. ElMCP “es muy pobre, no tiene muchas habilidades” ;el CLI cubre
todas las funciones deGitHubyeselestándarcorporativo.
�� CONEXIONES CON EL RESTO DEL RAMO
Conceptodeestaclase Seapoyaen/anticipa
Incertidumbretécnicaeincertidumbrede
requerimientos(campos10y11delaficha)
Clase 1 —losdostiposdeincertidumbre. Aquíse
operacionalizancomo campos evaluables por feature
“Venderprimero”comocondicióndelogrode
Validación
Clase 1—leydelaevidencia: si te pagan, es la evidencia
más alta
MVP/ Must have =productomínimoviable Clase 1 —definicióndePMV.MoSCoWdefineel must
have comoelPMV
MVPdealtafidelidad(condicióndelogro) Clase 1 —matizde precisióndelprototipo
Fases: prototipajerápido,testeoyvalidacionesen
“Nuevoproducto”
Clase 1 —herramientasdeprototipoyPMV
CrowdfundingyKickstarterenelejemplodel
smartwatch
Clase 1 —crowdfundingcomoherramientadePMV,
consusesgodeperfildecomprador
Etiquetasbeta/ga/shippeddelroadmappúblicode
GitHub
Clase 1 —alfa/beta/releasecandidate
Requisitosdeaceptaciónconpruebas;testeoentre
subsistemas
Clase 2 —pruebasfuncionalesynofuncionales,testeo
deintegraciónydeaceptación
32

## Lamina 33

Conceptodeestaclase Seapoyaen/anticipa
Métricasporfaseenelejemplodelsmartwatch;leading
metricsyforecasting
Clase 3 —métricas,mediciónyplanificación
Fichadefuncionalidadypriorizacióndehistorias Clase 3 —planificacióndeprototipos; Clase 4 —
prototipajeconceptual
Curvadevalor/benchmarkingimplícitosenla
diferenciacióndelaProductVision
Ramo anterior —benchmarkingycurvadevalor
Estandarizarprocesos,empaquetaryestandarizar
activosintelectuales
Ramo anterior —mencionadoexplícitamentecomo
continuidad
Criteriosdeselecciónentreproyectosdeinnovación Ramo anterior — “como lo habíamos conversado con
los que participaron”
Priorizacióndehistoriasydemostracióndeexcelencia
enunámbitodeUX
Entrega final (S06) —esliteralmenteeldesafío
evaluado
������ MAPA MENTAL DE LA CLASE EN UNA PÁGINA
ROADMAPPING = instrumento que hace evolucionar MERCADOS + PRODUCTOS + TECNOLOGÍAS
vinculando perspectiva TÉCNICA ↔ COMERCIAL
forma: GRÁFICO TEMPORAL POR CAPAS
capas canónicas: Mercado · Producto · Tecnología · Programa I+D · Recursos
CATÁLOGO DE PHAAL (8 tipos)
Producto · Servicios/capacidades · Estratégico · Largo plazo
Conocimiento/activo (← Data Science) · Proceso · Programático
INTEGRACIÓN (← el más común en software)
Componentes → Prototipos/pruebas → Demostradores → Producción
╔══════════════════════ EL MÉTODO EN 3 PASOS ══════════════════════╗
║ ║
║ PASO 01 · VISIÓN DE PRODUCTO (debe ser AMBICIOSA) ║
║ Para / Quién / El / Es un / Que / A diferencia de / ║
║ Nuestro producto ║
║ ▼ ║
║ PASO 02 · PRIORIZAR ║
║ frameworks: Critical Path · KANO · D-F-V · ROI · MoSCoW ║
║ KANO: básicas (esperada) · performance (deseada) · ║
║ atractiva (excitante / impresionadores) ║
║ MoSCoW: Must (=PMV, no negociable) / Should / Could / ║
║ Will not ⚠ no prioriza, solo COMUNICA ║
║ ║
║ FÓRMULA: P = (ΣNC + ΣON) / ΣE × C ║
║ └─valor─┘ └esfuerzo┘ confianza (multiplica) ║
║ ⚠ los ON pueden ser NEGATIVOS ║
║ ║
║ FICHA DE 13 CAMPOS por funcionalidad ║
║ ID · nombre · descripción · tipo · tiempo · TAMAÑO DE ║
║ HISTORIA · valor · usuario · frecuencia · incert. ║
║ requerimientos · incert. técnica · dependencias · ║
║ REQUISITOS DE ACEPTACIÓN ← nunca omitir ║
║ ▼ ║
║ PASO 03 · MATICES → UN ROADMAP POR AUDIENCIA ║
║ Ingeniería (7 capas) · Ventas y mkt (4) · Ejecutivos (2) · ║
║ Clientes (2) ║
33

## Lamina 34

╚══════════════════════════════════════════════════════════════════╝
CICLO DE VIDA Nuevo producto → Crecimiento → Expansión → Explotación → Fin
riesgo comercial ALTO BAJO
└──────────┘ └────────────────────────────────────────┘
CUSTOMER DEV B Ú S Q U E D A E J E C U C I Ó N
Descubrimiento ⇄ Validación Creación → Compañía
└── PIVOTEO ──┘ (aquí NO hay pivoteo)
PARE PARE PARE PARE
⚖ TESIS CENTRAL: "El producto no significa nada.
Al final del día uno necesita CLIENTES."
🛠 IMPLEMENTACIÓN REAL (GitHub)
ISSUES → MILESTONES → PROJECT → vista ROADMAP
vía GitHub CLI (el MCP es pobre) · custom fields · Actions
fase 0 = desarrollo · bloques de 7–10 días · ~100 issues = proyecto sano
📏 REGLAS OPERATIVAS
· Toda meta lleva NÚMERO (volumetría)
· Roadmap de startup = MESES, no años
· Ningún issue sin requisitos de aceptación
· Simplificar scope: un cliente, un segmento primero
��������� ANEXO — Errores de transcripción identificados
Reconstruccioneshechasapartirdelcontextoylasslides. Semarcanexplícitamenteporqueson inferencias,no
certezas.
TranscritoporWhisper Términoprobable Confianza
“RoadPal”(autorde Technology
Roadmapping)
Robert Phaal (apareceenlaslide) Alta
“MyT”(institucióndelartículo) MIT Media-alta
“Yamina”/“yeminas”(repetido) Gemini(Google) Alta—confirmadoporelcontexto
“modelos Flash,nisiquieramodelos
Pro”
“YaminayFlash,el3.8” probablemente Gemini 3 Flash Media
“Fable” Claude Fable(modelode
Anthropic);enelresumendelaClase
1elmismotérminosereconstruyó
como“unmodelodeClaude”
Media-alta
“CloudCode” Claude Code Alta
“MosQ”/“MosCow” MoSCoW Alta
“Skullcar” scorecard Media-alta
“Gira” Jira(Atlassian) Alta
“lagente”(enfrasescomo “una de
las gracias de la gente es que
además de ser hiperinteligente no se
cansan”, “pedirle a la gente que te lo
arme”)
los agentes Alta—elsentidosolocierracon
“agentes”
“bytecoding”/“bitframes” vibecoding Media
“cartagans” carta Gantt Alta
“GDRP” GDPR Alta
34

## Lamina 35

TranscritoporWhisper Términoprobable Confianza
“vulture”(proveedordeservidores
conCLI)
Vultr Alta
“teclit” tech lead Media-alta
“SoundRelaunch” Product Roadmaps Relaunched
(librodelabibliografía)
Media
“estrelladeprototipaje” esta era de prototipaje Media
“uncoladerodeagentes” probablemente caladero/conjunto
deagentes
Baja
“laHH”(procesocorporativo
mencionadoporunalumno)
probablemente RR.HH.o HHcomo
horas-hombre
Baja
“elINE-Tiempo”(vistadeKanban) probablemente “en el tiempo” Baja
“unaARIE” probablemente una API Baja
“Astra”(modelousadoenlademo,
“salióayer”,muyrápido)
[término no reconstruible con
certeza]—seloasociaa“lasolución
de computer use deOpenAI”
—
“Mythic”( “en el caso de Mythic
nosotros también el testeo lo vemos
así”)
[término no reconstruible] —
presumiblementeuna
empresa/proyectodelprofesor
—
“parkingmanagementmv”(nombre
delproyectodelademo)
[término no reconstruible] —
“servidores.cl” plausibletalcual;noverificable —
“Priscila”/“Cristóbal”/“Matías” nombresdeparticipantes;sin
contenidodocente
—
Términos correctamente transcritos que conviene no “corregir”: Kickstarter,Ionic,Arduino,Strava,NikeRun,
GarminConnect,MyFitnessPal,Coros,Garmin,Walmart,UnrealEngine,GitKraken,GitLab,GitHubActions,AWS,
GoogleCloud,Trello,Scrum,SteveBlank,C.ToddLombardo.
35
