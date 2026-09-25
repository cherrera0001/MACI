# Resumen_Clase6_Regresion

> Material de clase de Fundamentos de Ciencia de Datos, UdeC T2-2026.
> Texto extraido de `Resumen_Clase6_Regresion (1).pdf` para busqueda e indexacion.
> 24 laminas. Las figuras no se extraen: si una lamina
> depende de un grafico, hay que abrir el PDF.

---

## Lamina 1

FundamentosenCienciadeDatos—CLASE6: Regresión
Apuntescompletos: diapositivasoficiales+transcripcióndeclase
Profesor: GuillermoCabrera-Vives(IngenieroCivilInformático;MScyPh.D.enCienciasdelaComputación,
UniversidaddeChile)·guillecabrera@inf.udec.cl UniversidaddeConcepción —FacultaddeIngeniería·IIT
UdeC·UnidaddeDataScience
Cómoleerestedocumento. Integraelcontenidodelas33diapositivasoficialescontodolo
dichoenclase,organizadosegúnelordenrealdelaexposición. Semarcancon �� � �loscontenidos
quesoloaparecenenlatranscripción (noestánenlasslides),porquesuelenserjustamentelo
queunestudianteolvidarepasar. Semarcacon �� �elcontenidomatemáticoqueenlaspropias
slidesllevaelsímbolodeadvertenciadelprofesor.
Notasobrelasfuentes. Latranscripciónesautomática(Whisper+pyannote-audio)ycontiene
errores de reconocimiento evidentes; cuando el término correcto se deduce de las slides, se
usa el de las slides y se indica el error en nota al pie de sección. Todo lo que está en este
documento proviene de las dos fuentes entregadas; las escasas aclaraciones externas están
marcadasexplícitamentecomotales.
����RESUMENEJECUTIVO
Estaclaseabrelaunidadde aprendizajeautomático(machinelearning) ,queelprofesorsitúacomola
basedel~90-95%delainteligenciaartificialactual,ycorrespondealaetapade modelamientodentrodel
ciclodelcientíficodedatosyavistoenclasesanteriores. Sedefineelaprendizajeautomáticomediantela
tripleta ⟨P,T,E ⟩(rendimiento,tarea,experiencia)ysedistinguenlosdosgrandesenfoquessegúnexistaono
etiquetas: supervisado(clasificaciónyregresión)y nosupervisado (clusteringyestimacióndedensidad). El
focodelaclaseesla regresión,esdecir,predecirunvalorreal,yenparticularla regresiónlineal,elegida
porserelmodelomássimplecapazdeilustrartodoslosconceptosquedespuésreaparecenenmodelos
arbitrariamente complejos. Se construye el modelo lineal ŷ = θ₀ + θ₁x, se define lafunción de costo
cuadrática,ysemuestraqueaprenderconsisteen minimizaresafunción igualandolasderivadasacero,lo
queenelcasolinealadmite soluciónanalíticacerrada . Luegoseextiendea regresiónlinealpolinomial ,
introduciendoelpuntoconceptualcentraldelaclase: laregresiónlinealeslineal enlosparámetrosθ,no
enlasvariablesx . Aumentarelgradodelpolinomioaumentala complejidaddelmodelo ,loqueconduce
alsobreajusteyalapérdidade generalización. Laclasecierraconlaherramientaqueelprofesorllamala
másimportantedetodalaIA:la validacióncruzada (holdout,submuestreoaleatorio,K-Foldybootstrap),
juntoconladistinciónentre parámetrosehiperparámetros ylostresconjuntosentrenamiento/validación
/test. Seilustratodoconelcasoreal Deep-Hub(conteodeárbolescondronesparaArauco).
�CONCEPTOSCLAVEDELACLASE
# Concepto Prioridad Porquéimporta
1 Aprendizajeautomático
como ⟨P,T,E ⟩
Esencial Definiciónformal,
aplicableacualquier
sistemadeIA(incluidas
lasLLM)
2 Supervisadovs.no
supervisado;las4tareas
Esencial Taxonomíabase;separa
clasificación/regresión
declustering/densidad
1

## Lamina 2

# Concepto Prioridad Porquéimporta
3 Regresión=predecirun
valorreal
Esencial Defineelobjetodetoda
laclase
4 Notacióndelgorrito: ŷ
predichovs.yreal
Esencial Convenciónusada
durantetodoelcurso
5 Modelolinealŷ=θ₀+
θ₁x
Esencial Modelodereferencia
6 Funcióndecosto
cuadrática ℒ
Esencial Esla“P”de ⟨P,T,E⟩en
regresión
7 Aprender=minimizar ℒ
(derivadas=0)
Esencial Ideaquesegeneralizaa
todoelML
8 Lineal enθ,noenx Esencial Trampaclásicade
examen
9 Complejidad↔número
deparámetros
Esencial Puentehaciasobreajuste
10 Generalizacióny
sobreajuste
Esencial Objetivorealdetodo
modelo
11 Parámetro
vs.hiperparámetro
Esencial Seconfunden
constantemente
12 Entrenamiento/
validación/test
Esencial Lostresconjuntosysu
funcióndistinta
13 Validacióncruzadaysus
4estrategias
Esencial “Larespuestaalamayor
partedelosproblemas
delML”
14 Soluciónanalíticade
mínimoscuadrados
Importante Sepideentender,no
derivar
15 Porquéelerrorvaal
cuadrado(3razones)
Importante Preguntamuynaturalde
desarrollo
16 63.2%delbootstrap Importante Datonumérico
memorizable
17 EjemploDeep-Huby
localizacióncomo
regresión
Importante Únicoejemploaplicado
completo
18 LLM,agentes,modelos
abiertos,LoRA
Complementario Digresiónrespondiendo
preguntasde
estudiantes
6.0Encuadredelaclase
Agendaoficial(slide3)
Unidad Tema
01 AprendizajeAutomático(machinelearning)
02 Regresión
03 Generalización
04 ValidaciónCruzada
2

## Lamina 3

�� � �Ubicacióndentrodelciclodelcientíficodedatos
Elprofesorabre,comoeshabitual,retomandoelciclo: pregunta/requerimiento→recoleccióndedatos→
limpieza→exploración→modelamiento→evaluaciónderesultados→comunicación→puestaen
marcha. Estaclasecorrespondealaetapade modelamiento.
�� � �Recordatorioexplícitodelanolinealidaddelciclo: “puedeserqueyoestéhoydíahaciendoel
modelamientoymedécuentadequehayalgoquenofunciona[…]yentoncestengoquevolver
atrásalafasedeexploraciónyseguramentehayalgúndatoquefuemallimpiadoomalrecopilado.”
EstorefuerzaelpuntodelaClase2sobrelasflechasbidireccionales.
�� � �Advertenciasmetodológicasdelprofesor
• El90-95%delaIAactual sedebealsubconjuntodealgoritmosdeaprendizajeautomático.
• Elsímbolo �� �enlasslides (apareceenlasláminas18,19y21)indicaquesevaaentrarenmatemáticas
yque “esimportantequeprestenatención” . Sinembargo,aclara: “sinolologranentender,porqueno
vienendeunbackgroundmatemático,noestanterrible. Loimportanteesqueaprendanlapartemás
conceptualdelcurso.”
– �� � �Implicanciaparaelexamen: elcursoevalúacomprensiónconceptual,nodestrezaalgebraica.
Ver§6.4.4.
• Anticipo: la clase termina con validación cruzada, que el profesor califica como“la técnica más
importante,yocreo,quizás,detodalainteligenciaartificial” .
• Porquéseparteconregresión: losconceptosfundamentalesquesevenenregresiónseaplican
despuésenclasificaciónysucesivamenteenmodelosdeIAmáscomplejos.
6.1AprendizajeAutomático—Esencial
6.1.1Definición(slide4)
Aprendizajeautomático: estudiodealgoritmosque mejoransurendimientoP enalguna tarea
TconexperienciaE.
Unatareadeaprendizajebiendefinidaesunatripleta ⟨P,T,E ⟩.
Componente Quées Dedóndesaleenlapráctica
E—Experiencia Loqueelalgoritmo“vive”para
aprender
�� � �Enaprendizajeautomáticola
experienciaseentregadesdelos
datos
T—Tarea Loquesequierequeelalgoritmo
haga
Clasificación,regresión,clustering,
estimacióndedensidad
P—Rendimiento Medidadequétanbienloestá
haciendo
Funcióndecosto/métricade
error
�� � �6.1.2Ejemplodesarrolladoenclase: unaLLMcomo ⟨P,T,E ⟩
Elprofesordescomponeunmodelodelenguajesegúnlatripleta,conparticipacióndelosestudiantes:
Componente ValorparaunaLLM
E(experiencia) Todoeltextoquelahumanidadhageneradoyque
sepudoextraerdeInternet
3

## Lamina 4

Componente ValorparaunaLLM
T(tarea) Predecirlasiguientepalabra(token) . Nadamás
queeso,unaalavez
P(rendimiento) Seleentregaunaoracióntruncada,elmodelo
predicelapalabrasiguienteysecomparaconla
palabrareal. Formalmentesemideconunafunción
decosto
Mecánicadescrita: seleentrega “Hola,minombreesGuillermoy…” ;elmodelodebepredecir “estoy”. Si
prediceotrapalabra,nolohizobien. Luegotomaesapalabraypredicelasiguiente,yasísucesivamente.
�� � �Adelantoparalapróximaclase: enclasificaciónlafuncióndecostoestándaresla entropíacruzada,y
eslaqueusaGPT. (Severáenlaclasedeclasificación;estaclasetrataregresión.)
�� � �Aclaracionesconceptualesimportantessurgidasdepreguntas
1. ChatGPTNOesunaLLM. ChatGPTesun sistemamultiagente quepordetrástieneunaLLM(GPTes
laLLM).Severáenlaúltimaclasedelcurso.
2. Entrenamiento≠inferencia. Sondosetapasdistintas:
• Entrenamiento: selevadiciendoalmodeloloquesequierequeprediga;elmodeloajustasus
parámetros.
• Inferencia: escuandose usaelmodelo. CuandounusuarioconversaconChatGPT,Claudeo
Gemininoestáentrenandoelmodelo ;elmodeloyaestáentrenadoysimplementeresponde.
3. ElrendimientoNOeseltiempoderespuesta. Unestudiantepropusoeltiempoderespuestacomo
medidadeP;elprofesorlodescarta: Pmide quétanbien lohaceelalgoritmo,noquétanrápido.
�� � �6.1.3Limitaciónfundamental: lamáquinasoloaprendedelosdatosquerecibe
“Lamáquinaaprendedesdelosdatos. Siesquehaydatosqueyonotengoincluidosoqueyonole
entreguéalamáquina,lamáquinanovaaaprenderesosdatos.”
Ejemplodado: siquieroclasificarentreperro,conejoyratón,perosololeentregoimágenesdeperrosy
conejos,novaaaprenderadistinguirunratón .
�� � �Estepuntoconectadirectamenteconlaunidaddecalidaddedatos: unmodelonopuedecompensarla
ausenciadeinformaciónenelconjuntodeentrenamiento.
6.1.4Diagramadelproceso(slides5y16)
┌──────────┐
│ DATOS │ ──────► [ MÁQUINA que aprende ] ──────► ✓ respuesta
└──────────┘ (experiencia E) (tarea T)
▲
│
ℒ = Σᵢ (ŷ(xᵢ) − yᵢ)²
(rendimiento P)
�� � �Elprofesorarmaestediagramaporpartesalolargodelaclase: primerolosdatos,luegolamáquina,
luegolafuncióndecosto,ysoloalfinalelmecanismodeaprendizaje(minimización).
6.1.5Ejemplomotivador: laplantadeevaporación(slide6)
“ConsidereunaplantadeevaporaciónparalacualUd. quieredeterminarlacantidaddeagua
evaporada. ParaesoUd. quiereentrenarunamáquinaqueseacapazdepredecirestevaloren
funcióndeunconjuntodeparámetrosqueUd. puedecontrolar.”
4

## Lamina 5

�� � �Contextoampliadoenclase: esun casoreal enelqueelequipodelprofesortrabajó. Laideaesque
existen“perillas”quesepuedenmoverdentrodelamáquina,ysegúncómosemuevanlaplantaevapora
másomenosagua. Conunmodelopredictivosepuede optimizarlacantidaddeaguaevaporada ,porque
sesabedeantemanocómohayquemoverlasperillasparaconseguirunresultadodado.
�� � �Quéenseñaesteejemplo: quelaregresiónnosirvesolopara“adivinar”unnúmero,sinopara habilitar
laoptimizacióndeunprocesocontrolable .
6.2Losdosenfoquesdelaprendizajeautomático—Esencial
6.2.1Lapreguntaquedividetodo(slide7)
¿Tenemosalgunosdatosyaetiquetados?
�� � �Qué significa “dato etiquetado”:tener el valor objetivo conocido junto al dato. En clasificación
perro/gato,significatenerimágenesacompañadasdelrótulo“estaimagenesunperro”,“estaesungato”.
Enlaplantadeevaporación,significatenervaloresrealesdeevaporaciónquesequierequelamáquinasiga.
SÍhayetiquetas→Aprendizaje
SUPERVISADO
NOhayetiquetas→Aprendizaje
NOSUPERVISADO
Tarea1 Clasificación —estimaruna
clase/categoría(perro,gato,
conejo)
Clustering—agruparlosdatos
porsemejanza
Algoritmos(slide) ANN(redesneuronales
artificiales),SVM,árbolesde
decisión,clasificadores
bayesianos,vecinosmáscercanos,
etc.
K-medias,agrupaciónjerárquica,
DBSCAN,etc.
Tarea2 Regresión —estimarunvalor
real/numérico(0,2;5%)
Estimacióndedensidad —ver
dóndeseubicanlosdatosenel
espaciodeparámetros
Algoritmos(slide) Regresiónlineal,randomforest
regressor,kernelregression,etc.
Histogramas,KDE(estimaciónde
densidadporkernels),mezclade
gaussianas,etc.
Notadetranscripción: WhispertranscribeDBSCANcomo“tibiscan”;eltérminocorrectoapareceen
laslide7.
�� � �6.2.2Precisionesdadasenclase
• Soncuatrotareasdistintas ,yelprofesorloenfatiza: clasificación,regresión,clusteringyestimación
dedensidad. Paracadatarea existenmúltiplesmodelosposibles.
• Clusteringexplicadointuitivamente: escomopasarlemuchosanimalesalamáquinasindecirlequé
son,yqueellasoladescubraquelosgatosvanconlosgatosylosconejosconlosconejos. Losobjetos
dentrodeungruposeparecenentresíysediferenciandelosotrosgrupos.
• Estimacióndedensidad yasevioenelcurso: los histogramasdelaclasedeanálisisexploratorioson
uncaso. Permiteobtenerprobabilidadesdequehayadatosenciertaszonasdelespacio.
• Estadodelarte: hoycadaunadelascuatrotareasseestáabordandoconredesneuronales (hay
redesneuronalesparaclasificación,pararegresión,paraclusteringyparaestimacióndedensidad).
5

## Lamina 6

6.3AprendizajeSupervisado—Esencial
6.3.1Definición(slide9)
Elaprendizajesupervisado: -Utilizaun conjuntodeentrenamiento compuestopor: -atributosxᵢ -etiquetas
yᵢ-Objetivo: determinaruna funciónquetomelosatributosypredigalaetiqueta . -Silaetiquetaa
predeciresunvalorreal,entonceslollamamosregresión.
Formalmente: sebuscaunafunciónf(x)quetomelosatributosxypredigalaetiqueta.
�� � �6.3.2Convencióndenotacióndelcurso(¡memorizar!)
Símbolo Significado
ŷ(congorrito) Valor predicho/estimado porelmodelo
y(singorrito) Valor real/verdadero deldato
θ̂(congorrito) Valor óptimoestimado delparámetro
Estaconvenciónseusa durantetodoelcurso ,nosoloenestaclase.
�� � �6.3.3Aclaracionessurgidasdepreguntasdeestudiantes
• ¿Porquésellama“supervisado”? Porqueseestásupervisandoalalgoritmo: selediceexplícitamente
quéesloquetienequepredecir. Elalgoritmoprediceunŷparacadax,yseleindicacuáleraelyreal.
“Loestoyenseñandodirectamentedesdelaetiqueta. Poresosellamasupervisado.” Sihayetiquetases
supervisado,porqueselova corrigiendoamedidaqueentrena .
• Laetiquetadentrodelatabla: engeneral,enunatabladedatoslaetiquetaes unadelascolumnas ,
es decir, es formalmente parte de los atributos. La diferencia es que unosabecuál columna es la
etiquetayqueeseeselobjetivoqueelmodelodebepredecir. (Conectaconladefinicióndeatributo=
columnadelaclasedecalidaddedatos.)
• “Losmodelosseentrenan” : entrenarsignificairpasándoledatosalmodeloparaqueaprendadesde
ellos.
6.4RegresiónyRegresiónLineal—Esencial
6.4.1Ejemplocentral: elpesodelárbol(slides10y11)
Ejemplo(slide10): “Considerelaestimacióndelpesodeunárbolenfuncióndesuradioauna
alturadefinida. Megustaríasabermasmenoscuáleselpesodelárbolsinnecesidaddecortarlo.”
• Ejex: radiodeltronco
• Ejey: pesodelárbol
�� � �Motivacióndenegocioampliadaenclase: conocerelpesopermitiría encontrarelpuntoóptimoal
cualcortarelárbol . Nosepuedencortartodoslosárbolesparapesarlos,porque “despuésnolospuedo
volverapegarconcolafría” . Entoncesseusan datoshistóricos deárbolesyacortados(radioconocido,peso
conocido)paraajustarunmodelo.
�� � �Dosobservacionesqueelprofesorextraedelgráficodedispersión: 1. Hayruido: árbolesconel
mismoradiotienenpesosdistintos, porquenotodoslosárbolessoniguales. 2. Hayunatendencia: a
medidaqueelradiodeltroncoaumenta,elpesotambiénaumenta.
6

## Lamina 7

Quéeselmodelo: lacurva(línearoja)ajustadaalosdatos. Unavezquesetiene, paracualquierXsepuede
obtenerunY .
�� � �“Sellamaregresiónsolamenteporqueestácalculandounvalorreal.”
6.4.2Elmodelolineal(slides13y14)
̂ 𝑦 = 𝜃0 + 𝜃1𝑥
• θ₀: intercepto(dóndecortaelejey)
• θ₁: pendiente(cuántosemultiplicax)
• Produceuna línearecta.
�� � �Porquéseparteconregresiónlineal: “Laregresiónlinealesunodelosmodelosmássimples,pero[…]
conestemodelotansimplepodemostocartodoslostemasqueimportanentodoslosproblemasmáscomplejos,
contodoslosmodelosmáscomplejos.”
Lapreguntaqueabretodalaclase(slide14)
Laslidemuestra tresrectasdistintas (roja,azulynaranja)sobrelosmismosdatos,ypregunta: ¿porquéesa
rectaynootra? ¿Concuálmedeberíaquedaryporqué?
�� � �Respuestadelosestudiantes: laque minimizalosmínimoscuadrados ,esdecir,laquetiene menor
error. Unestudiantedefinemínimoscuadradoscomo “unamedidadeerror” ,ymencionaqueexistenotras
medidas(nombraelMAE).Elprofesoraceptayreformulalapreguntaclave:
�� � �“Lapreguntaes: ¿lamáquinacómosabequeelrojotienemenorerror?”
Estomotivalafuncióndecosto.
6.4.3FuncióndeCosto �� �(slide15)—Esencial
ℒ = ( ̂ 𝑦(𝑥1) − 𝑦1)2 + ( ̂ 𝑦(𝑥2) − 𝑦2)2 + ⋯ + ( ̂ 𝑦(𝑥𝑛) − 𝑦𝑛)2
ℒ =
𝑛
∑
𝑖=1
( ̂ 𝑦(𝑥𝑖) − 𝑦𝑖)2
Anatomíadelerrorparaunpunto (asílodibujalaslide):
Elemento Significado
(𝑥𝑖, 𝑦𝑖) Eldatoreal observado
̂ 𝑦(𝑥𝑖) Loqueel modelopredice paraesemismoxᵢ
̂ 𝑦(𝑥𝑖) − 𝑦𝑖 Elresiduo: ladiferenciaverticalentremodeloydato
real
�� � �Notación: elprofesorusalaletracaligráfica ℒ(“estaLcomorarita” )paralafuncióndecosto— loss.
�� � �¿Porquéseelevaelerroralcuadrado? —Tresrazonesdadasenclase
Estapreguntasediscutióextensamenteyesmaterialdeexamendedesarrollomuyprobable.
7

## Lamina 8

# Razón Explicación
1 Eliminarlossignosnegativos Siunpuntotieneerror−100y
otro+100,sinelcuadrado se
cancelanyelerrortotaldaría
cero,haciendoparecerqueel
modeloesperfectocuandonolo
es
2 Penalizarmásfuerteloserrores
grandes
Adiferenciadelvalorabsoluto,el
cuadradocastiga
desproporcionadamentelas
desviacionesextremas. Unerror
queseescapamuchoproduceun
errorcuadráticomuchomayor
queunoqueseescapapoco
3 Razónprobabilística
(mencionadacomo“no
importanteparaestecurso”)
Elerrorcuadrático asume
implícitamentequeelruidode
losdatossigueunadistribución
normal. Surgedetomarel
logaritmodeladistribución
normal,loquedejalostérminos
elevadosalcuadrado
�� � �Matizsobrelaescala: unestudianteobservócorrectamentequeelefectoamplificadordelcuadrado
dependedelaescaladelosdatos : siloserroressonmayoresque1,elcuadradolosamplifica;siestánentre
0y1,elcuadradolosreduce. Elprofesorvalidólaobservaciónenelcontextodelejemplo(dondeysemueve
aproximadamenteentre0y6).
�� � �Sobrelasumatoria: elprofesorexplicaexplícitamenteelsímboloΣparaquienesnoloconocen—es
simplementelainstruccióndesumarcadaunodelostérminos,tomandoidesde1hastan.
Lostresingredientesreunidos(slide16)
Llegadoestepuntosetienen: 1. Experiencia(E) →losDATOS2. Rendimiento(P) →lafuncióndecosto
(errorcuadrático)3. Falta: lamáquinaqueaprenda(T) →¿cómohagoqueelmodeloaprenda?
6.4.4Aprender=minimizarlafuncióndecosto �� �(slides17,18y19)—Esencial
�� � �Ideacentral: “Loqueunohaceestratardeminimizaresteerror.”
Elpaisajedelafuncióndecosto
• Lafuncióndecosto dependedelosparámetrosdelmodelo ,nodelosdatoscomovariableslibres.
Enelmodelolinealsimplehay dosparámetros: θ₀yθ₁ .
• �� � �Para poder graficarlo, el profesor supone un modelo deun solo parámetro(imaginar que θ₀
noexisteyelmodeloessoloθ·x). Laslide18muestraentonces ℒenfuncióndeθcomouna curva
convexaenformadeparábola ,conunmínimoen θ̂.
• Sebuscael θ̂queminimiza ℒ,yeseθ̂eselqueseusaenelmodelofinal.
• �� � �Comentariodeescala: “engenerallosmodelostienenhoydíabillonesdeparámetros” —elcasode
unparámetroessoloparaefectosgráficos.
Condicióndeoptimalidad
Minimizarunafunciónsignifica hacerqueelgradienteseacero ,esdecir, quelasderivadasseancero .
8

## Lamina 9

�� � �Recordatoriodelprofesor: “laderivadaeslapendiente” . Enlacurvadecostolapendientebaja,baja,baja,
ydespuésempiezaasubir;enelmínimolapendienteescero.
𝜕ℒ
𝜕𝜃0
= 𝜕ℒ
𝜕𝜃1
= 0
Soluciónanalíticadelmodelolineal(slide18y19)—Importante
Enelcasoparticulardelmodelolinealsepuedederivar,igualaraceroyllegarauna solucióncerrada:
̂𝜃1 = ∑ 𝑥𝑖𝑦𝑖 − 1
𝑁 ∑ 𝑥𝑖 ∑ 𝑦𝑖
∑ 𝑥2
𝑖 − 1
𝑁 (∑ 𝑥𝑖)2 = cov[𝑥, 𝑦]
var[𝑥]
̂𝜃0 = ̄ 𝑦 − ̂𝜃1 ̄ 𝑥
Interpretación(laformaenquehayquerecordarla): -θ̂₁=covarianzaentrexey,divididaporla
varianzadex. -θ̂₀=promediodey,menosθ̂₁porelpromediodex.
�� �Advertenciasobreunaerrataenlaslide. Lalámina18/19escribeelpasointermediocomo
̂𝜃0 = 1
𝑁 ∑ 𝑦𝑖 +
̂𝜃1
𝑁 ∑ 𝑥𝑖 = ̄ 𝑦 − ̂𝜃1 ̄ 𝑥. El signo intermedio debería sermenos, no más: la
expresióndeladerecha(ȳ−θ̂₁x ̄)eslacorrectayeslaqueelprofesorleeenvozaltaenclase( “el
promediodeymenostetaunogorroporelpromediodex” ). Guiarseporlaformafinalȳ−θ̂₁x ̄.
(Observaciónderivadadecontrastarlaslideconlatranscripción.)
�� � �������Alcancedeevaluación(datoadministrativocrítico)
El profesor afirma textualmente sobre la derivación:“ustedes lo pueden hacer en su casa
si quieren, yo no se lo voy a pedir para ningún certamen; es solamente para que entiendan
conceptualmenteloqueestamoshaciendo: estamosminimizandounafuncióndecostoyqueremos
básicamentequelasderivadasseancero.”
�� � �Noseevaluaráderivarlasolución ,pero síseesperaentender : (a)queaprender=minimizarelcosto,
(b)queesoselograigualandoderivadasacero,y(c)quésignificanθ̂₁yθ̂₀conceptualmente.
�� � �Aclaraciónsobrequésederiva
Un estudiante preguntó si al derivar la función de costo se derivan los datos.No. La función de costo
dependedelmodelo,yelmodelodependedelosparámetros . Sesustituyeelmodelodentrodelafunción
decosto,sedesarrollaelcuadrado,ysederiva conrespectoalosparámetrosθ . Elprofesordestacaquees
relativamentefácilporquelaexpresiónes linealycuadráticaenθ .
�� � �Analogíaextendidadelpresupuesto(aportadaporunestudiante)
Unestudiantepropusolaanalogíadeunaempresaquepresentapresupuestos: losprimerossalenmal,se
cobrademásodemenos,yconlarepeticiónelerrorsevaacercandoacero. Elprofesorvalidólaanalogíay
larefinódescribiendoelprocesoiterativo:
1. Separteenunpuntocualquieradelacurvadecosto.
2. Secometeunerrorgrande,pero sesabeenquédirección hayquecorregir.
3. Seavanzaenesadirección;elerrorbajaperosigueexistiendo.
4. Sepuede pasaralotrolado (desobreestimarasubestimar)yentonceshayquedevolverse.
5. Seconvergeiterativamentehaciaelmínimo.
9

## Lamina 10

�� � �Estaesunadescripciónintuitivadel descensoporgradiente ,elmétodogeneralqueseusacuando no
existesoluciónanalítica (queeselcasodecasitodoslosmodelosreales). Enelmodelolinealsimpleno
hacefalta,porquesellegadirectoalóptimo.
6.5ComplejidaddelmodeloyRegresiónLinealPolinomial �� �—Esen-
cial
6.5.1Delarectaalpolinomio(slides20,21y22)
�� � �Elprofesorplantealaobjeciónnatural: “¿porquéunmodelolineal? ¿Porquénounmodelocuadrático?” ,
dadoquelosdatosdelejemplosevencurvos.
Progresiónmostrada:
̂ 𝑦 = 𝜃0 + 𝜃1𝑥 (grado1)
̂ 𝑦 = 𝜃0 + 𝜃1𝑥 + 𝜃2𝑥2 (grado2)
̂ 𝑦 = 𝜃0 + 𝜃1𝑥 + 𝜃2𝑥2 + 𝜃3𝑥3 (grado3)
̂ 𝑦 = 𝜃0 + 𝜃1𝑥 + 𝜃2𝑥2 + ⋯ + 𝜃𝑝𝑥𝑝
6.5.2 ������ELCONCEPTOMÁSEXAMINABLEDELACLASE
�� � �LaregresiónlinealsellamaLINEALporqueeslinealenlosθ(losparámetros),NOporque
sealinealenlosx.
Consecuenciasdirectas,todasafirmadasexplícitamenteenclase:
• Unpolinomiodegrado3 siguesiendo regresiónlineal: enxescúbica,pero enθeslineal .
• Sepuedereemplazarcadapotenciadexpor cualquierfuncióndex : unlogaritmo,unaexponencial,
unseno,uncoseno— “loqueyoquiera” —y elmodelosiguesiendolineal .
Formageneral(slide21):
̂ 𝑦 = 𝜃0 + 𝜃1𝑔1(𝑥) + 𝜃2𝑔2(𝑥) + ⋯ + 𝜃 𝑝𝑔𝑝(𝑥)
̂ 𝑦 =
𝑝
∑
𝑗=0
𝜃𝑗 𝑔𝑗(𝑥)
�� � �Criteriooperativoparareconocerlinealidadenθ
“Cadatetaapareceunasolavez[…]nohayuntetaalcuadrado,niunlogaritmodeteta,niuna
exponencialdeteta.”
10

## Lamina 11

Modelo ¿Esregresiónlineal? Porqué
Modelo ¿Esregresiónlineal? Porqué
ŷ=θ₀+θ₁x ��Sí Linealenθ
ŷ=θ₀+θ₁x+θ₂x²+θ₃x³ ��Sí Cúbicoenx,perolinealenθ
ŷ=θ₀+θ₁·log(x)+θ₂·sen(x) ��Sí Lasgⱼ(x)sonarbitrarias;sigue
siendolinealenθ
ŷ=θ₀+θ₁²·x �No Hayunθelevadoalcuadrado
ŷ=θ₀+log(θ₁)·x �No Hayunθdentrodeunafunción
nolineal
6.5.3Complejidaddelmodelo—Esencial
�� � �Definiciónoperativadadaenclase: “Lacomplejidaddelmodelotienerelaciónconel número
de parámetros quetieneelmodelo. Unmodeloconmenosparámetrosesmássimple[…]un
modeloconmuchosparámetrosesmuchomáscomplejoqueunoconpocosparámetros.”
�� � �Detalledeconteo: unmodelopolinomialdegrado ptieneenrealidad p+1parámetros (θ₀,θ₁,…,θₚ),
porquesecuentaelintercepto.
6.5.4Efectovisualdelgradodelpolinomio(slide22)
Laslidemuestraelmismoconjuntodedatosajustadocontrespolinomios:
Grado Comportamientoobservado
Grado1 Unarecta;captalatendenciageneralperodeja
muchospuntoslejos( subajuste/modelo
demasiadosimple)
Grado2 Unaparábolaquesiguebienlaformacurvadelos
datos(buenajuste paraestecaso)
Grado10 Unacurvacon oscilacionesviolentas quepasamuy
cercadecasitodoslospuntos( sobreajuste)
6.5.5Lademostracióndelproblema(slide23)
Conelpolinomiodegrado10ajustado,elprofesorpreguntaporunvalordex intermedio(entrepuntosde
datos). Elmodeloentregaunvalordey absurdamentealto,quenosigueenabsolutolatendenciadelos
datos.
�� � �“Esraroqueeseseaelvalordey,asícomoquenossiguelatendencia. Esoesloquesellama
sobreajuste.”
�� � �Diagnósticodeunestudiante,validadoporelprofesor: “elmejorseríaeldegradodiez,perotalvez
estásobreajustadoalosdatos[…]solofuncionaconesosdatos;siunolepasaotros,talveznoseajustatan
bien”→nogeneraliza.
�� � �Conclusiónquecierralasección: “Nonosbastaconsolamentetenerunmodeloqueminimice
elerrorsobreelconjuntodeentrenamiento.”
11

## Lamina 12

6.6Generalización—Esencial
6.6.1Definición(slide25)
GENERALIZACIÓN-Capacidaddeobtenerbuenosresultadoscondatosnuncaantesobser-
vados. -Quelamáquina noseaprendadememorialosdatos ,yqueseacapazde“entender”
datosnuncavistos.
6.6.2 �� � �Porquéeselobjetivorealdetodomodelo
Ejemplodadoenclase: sitengounmodeloquepredicecuándovaafallarunamáquina, noquieroqueme
predigacuándofalló (esoyalosé), quieroquemepredigacuándovaafallarenelfuturo . Esoexigeque
elmodelogeneraliceadatosquenohavisto.
6.6.3 �� � �Elbalancecomplejidad↔simplicidad
“Amedidaquesecomplejizaelmodelotiendeasobreajustarsemás. Perosiyotengounmodelo
muysimple,entonces[…]novaasercapazdepredecirbien,queescomoelmodelolinealque
habíamosvistoantes. Entonceshayunbalanceentretenerunmodelomuycomplejoyunmodelo
muysimple.”
Modelodemasiado simple Puntoóptimo Modelodemasiado complejo
Pocosparámetros Balance Muchosparámetros
Nocapturalaestructuradelos
datos
Capturalatendenciasin
memorizarelruido
Memorizalosdatos,incluidoel
ruido
Erroraltoenentrenamiento yen
datosnuevos
Errorbajoenambos Errormuybajoenentrenamiento,
altoendatosnuevos
Subajuste �� Sobreajuste
6.6.4Definicionesasociadas
Término Definiciónsegúnlaclase
Sobreajuste(overfitting) �� � �Situaciónenqueelmodeloseajustatanbiena
losdatosdeentrenamientoque solofuncionacon
esosdatos ypierdelacapacidaddegeneralizar
Generalizar �� � �“Queseacapazdefuncionarparadatosqueno
havistoantes”
6.7ValidaciónCruzada—Esencial(bloquemásimportantedelaclase)
6.7.1 �� � �Lafrasequehayquerecordar
Preguntadelprofesor: “¿Cómosabersiestoysobreajustado?” →Respuesta: VALIDACIÓN
CRUZADA.
�� � �“Yoledigoatodosmisalumnos: siesquenosabenlarespuestaaalgúnproblema,tienencomo
respuesta‘validacióncruzada’,porquelavalidacióncruzadaeslarespuestaalamayorpartedelos
problemasdelaprendizajeautomático.”
Estafraseserepitealfinaldelaclasecuandounaestudiantepreguntacómoelegirentrevariosmodelos. Es
lacandidatamásobviaapreguntadeexamendelaclase.
12

## Lamina 13

6.7.2Lostresconjuntos(slide26)—Esencial
┌───────────────────────────── DATOS ─────────────────────────────┐
│ │
│ ENTRENAMIENTO │ VALIDACIÓN │ TEST │
│ el modelo aprende │ ajustar hiper- │ evaluar; el │
│ (ajusta los θ) │ parámetros │ modelo NUNCA lo │
│ │ (ej. orden del │ ha visto │
│ │ polinomio) │ │
└─────────────────────────────────────────────────────────────────┘
Conjunto Funciónexacta(slide26) �� � �Ampliacióndelaclase
Entrenamiento “Seusaparaqueelmodelo
aprenda”
Esdondeseajustanlos
parámetrosθ
Validación “Seutilizaparaajustar
hiperparámetros(porej.,elorden
delpolinomio)”
Esdondese tomaunadecisión
sobreelmodelo,nodondese
ajustanlosθ
Test “Seusaparaevaluar. Elmodelo
nuncalohavisto”
�� � �“Yolotomoymeloguardoen
elbolsillo”. Sesacaalfinal,y
sobreélsereportanlasmétricas
�� � �Regladeororepetidatresvecesenclase: “Siemprepartoguardandoeltest. Esoquenose
lesolvidenunca: guardareltest.” Además,elconjuntodetestNOcambiaentreunaiteración
yotra.
6.7.3 ������Parámetrovs.Hiperparámetro—Esencial
�� � �Hiperparámetro: parámetroque sefijaANTESdeempezaraajustarelmodelo .
Parámetro Hiperparámetro
Símboloenestaclase θ(θ₀,θ₁,…) p(ordendelpolinomio)
¿Cuándosedetermina? Duranteelentrenamiento Antesdelentrenamiento
¿Cómosedetermina? Minimizandolafuncióndecosto
sobreel conjuntode
entrenamiento
Probandodistintosvaloresy
comparandosobreel conjunto
devalidación
¿Elmodelolo“aprende”? Sí No—lodecideelcientíficode
datos
�� � �“Todoslosmodelos,olagranmayoría—nosemeocurreningunoqueno—,tienenhiperparámetros.”
�� � �Elciclocompleto,talcomoelprofesorloexplicópasoapaso
1. Elijounhiperparámetro,porejemplo p=2 .
2. Ajustolosθ sobreel conjuntodeentrenamiento .
3. Evalúoelmodeloresultantesobreel conjuntodevalidación (calculolafuncióndecostoahí). Esto
midesucapacidaddegeneralizar,porqueelmodelonovioesosdatosalentrenar.
4. Cambioelhiperparámetro,porejemplo p=10 ,yrepitolospasos2y3.
5. Comparoloserroresdevalidaciónymequedoconelhiperparámetrode menorerrordevalidación .
6. Yaconelmodelofinaldecidido, sacoelconjuntodetestdelbolsillo ,evalúosobreély reportoesas
métricas. Esaeslaúltimavalidación.
13

## Lamina 14

6.7.4 �� � �¿PorquénecesitoDOSconjuntosseparados(validaciónYtest)?
Estapreguntafueformuladaporunestudianteyocupóuntramolargodelaclase. Esmaterialdeexamende
desarrollomuyprobable.
Razón: alusarelconjuntodevalidación paratomarunadecisión (quéhiperparámetroelegir),
eseconjuntodejadeser“limpio”. Podríaocurrir, porazar,queundeterminadohiperparámetro
funcioneparticularmentebiensobreeseconjuntodevalidaciónespecífico. Esdecir, sepuede
sobreajustaralconjuntodevalidación .
�� � �Elprofesorloformulaasí: “Podríaserqueescojajustoelordendelpolinomioquecalzabienconelconjunto
devalidación,peroquedespuésnogeneraliceigualadatosquenohevistoantes. Entonces,poresolamétrica
finalsemidesobreelconjuntodetest.”
Matizimportante: aunqueenelconjuntodevalidación noseajustanlosθ (esoocurresoloenentre-
namiento),sísetomaunadecisión conél,yesobastaparacontaminarlocomoestimadorinsesgadodel
rendimiento.
�� � �¿QuépasasielerrordetestNOseparecealdevalidación?
• Engeneral loserroressobrevalidaciónysobretestson muyparecidos.
• Cuandonoloson,hayqueinvestigarconcuidado. Causasposiblesmencionadas:
1. Elconjuntodetesttienealguna anomalía.
2. Elconjuntodetest noesrepresentativo delrestodelosdatos(seescogióartificialmentemal).
• �� � �Ejemploconcretodeparticiónmalhecha(seriesdetiempo): entrenarcondatoshasta2025,
validarcondatosde2025–2026,yusarcomotestdatosdelaño2008. Elconjuntodetestquedamuy
separadodeldevalidacióny norepresentaloquesequierequeelmodelohaga .
6.7.5 �� � �Distincióncrítica: “validación”≠“validacióncruzada”
“Estoqueyoleacabodemostraracánoesvalidacióncruzada,estoesvalidaciónnomás.”
Elesquemasimpledepartirentresconjuntosyevaluarunavezessolo validación(holdout). Lavalidación
cruzadapropiamentetal implicarepetirelprocedimientomúltiplesveces condistintasparticiones,lo
quepermiteobteneruna distribucióndeerrores envezdeunúniconúmero.
6.7.6Lascuatroestrategiasdevalidacióncruzada(slide27)—Esencial
A)Métododeretención— Holdout Method (slide28)
• Separarelconjuntodeentrenamientoen dosconjuntosseparados .
• Entrenarsobreunconjuntoy validarsobreelotro.
• Proporcióntípica: 2/3paraentrenamiento,1/3paravalidación .
• Calcularelerrorfinalsobreelconjuntode test.
�� � �Limitacióncentral: entregaunsolovalordeerror . Nohayformadesabersiesenúmerofuesuerte.
Estalimitacióneslaquemotivalostresmétodossiguientes.
B)Bootstrap(slide29)
• Generarmsubconjuntosdetamañon’<n ,muestreandodelosdatosalazar CONREEMPLAZO.
• Lasobservaciones noincluidas enelconjuntodeentrenamientopasanaformarpartedel conjunto
devalidación.
• ��� �Dato numérico memorizable:“En promedio, un conjunto de entrenamiento de tamaño n con
bootstrapcontieneel 63.2%delasobservacionesdelosdatosoriginales.”
14

## Lamina 15

�� � �Analogíadelsacodebolitas: sacounabolita,laanotocomopartedelconjuntodeentrenamiento, la
vuelvoameter ,sacudolabolsaysacootra. Poresopuedehaberrepeticiones.
�� � �Reglaclavesobrerepeticiones:
Conjunto ¿Puedetenerdatosrepetidos?
Entrenamiento ��Sí
Validación �No
�� � �Cuándo usarlo:“Uno lo usa cuando tengo POCOS datos.”Si hay pocos datos y “saldría muy caro”
gastarlos,serepiten.
C)Submuestreoaleatorio— Random subsampling(slide30)
• Dividiraleatoriamente losdatosenconjuntodeentrenamientoyconjuntodevalidación.
• Realizarelmétododeretenciónparacadadivisión.
• Elerrorsecalculacomoel promediodeloserroresobtenidos .
�� � �Relaciónconbootstrap: “Esbásicamentelamismaidea,peroSINreemplazo.” Porlotanto, elconjunto
deentrenamientonotienedatosrepetidos .
D)ValidaciónCruzadaconK-Fold(slide31)
• Dividirelconjuntodedatosen Ksubconjuntosdisjuntos .
• Dejarunsubconjunto comoconjuntodevalidaciónyusarlos otrosK−1 paraentrenamiento.
• RepetirKveces ,usandocadasubconjunto exactamenteunavez paralavalidación.
Esquemadelaslide(conK=4;E=entrenamiento,V=validación):
DATOS → [ E ][ E ][ E ][ V ] | TEST (siempre apartado)
[ E ][ E ][ V ][ E ] |
[ E ][ V ][ E ][ E ] |
[ V ][ E ][ E ][ E ] |
�� � �Ventajasdestacadasenclase: 1. Cadadatoseusaexactamenteunavezcomovalidación → se
obtieneunapredicciónpara cadadatodelconjunto,ysepuedevercómosecomportaelmodelosobre
todoslosdatos. 2. Sepuedeusar exactamentelamismapartición paracompararmuchosmodelos(el
profesormencionaelcasodequererprobar20modelos),asegurandounacomparaciónjusta. (Estotambién
sepuedehacerconlosotrosmétodos,muestreandoprimeroyentrenandodespués,perosesuelehacercon
K-Fold.)
�� � �Limitación: sihaypocosdatos, nohaymuchasopcionesparaK .“Siyotengo100datosnopuedohacer
K=1000. Sitengo10datosnopuedohacerK=12.”
6.7.7 �� � �Cómoelegirlaestrategia(preguntadeFrancisco)
Situación Métodorecomendadoenclase
Muchosdatos K-Fold—cadasubconjuntotendrásuficientesdatos
Muypocosdatos Bootstrap —nohabrácapacidaddegenerar
conjuntosdeentrenamientosuficientemente
grandesdeotromodo
Engeneral Dependedelatareaydequésequierahacerconella
15

## Lamina 16

�� � �Principioteóricodado: “Engeneraltodasestasconvergenalosmismosresultadosparadatosinfinitos[…]
convergebásicamentealerrorreal. Peronadietienedatosinfinitos.” Esdecir, lasdiferenciasentremétodos
sonunartefactodetenerdatosfinitos .
�� � �¿Cuántosson“muchosdatos”? “Dependedelproblema.” Ejemplodado: paraclasificarentreperro
ygato,bastaríaconquecaigandelordende50gatosy50perrosencadasubconjuntoparatenercierta
precisiónenlasmétricas.
6.7.8 �� � �Elresultadoprincipalderepetir: ladistribucióndelerror
Estefueelpuntoquemáscostóenclaseyqueelprofesorterminóexplicandoconundibujoenpizarra. Vale
lapenareproducirlo:
Construcción del gráfico:-Eje horizontal:el hiperparámetro (grado del polinomio: 1, 2, 3, …). -Eje
vertical: elerrorsobreelconjuntode validación. -Paracadagrado,serepiteelremuestreovariasveces→
seobtieneuna nubedepuntos (varioserroresdevalidaciónporgrado).
Lecturadelgráfico: 1. Secomparalanubedepuntosdecadagrado. 2. Seeligeelgradocuyanubeestá
máscercadecero (menorerrordevalidación). 3. Reciénentoncesseevalúaelconjuntode test,cuyoerror
debiesecaerdentrodeladistribución deerroresdevalidación. 4. SielerrordetestNOcaeahí ,algoraro
estápasando(ver§6.7.4).
Porquéestoessuperioralholdoutsimple: teniendo10,50,100o1000repeticiones,sepuedecalcularla
mediaomediana yla desviaciónestándarolospercentiles delerror. Esdecir,sesabe enquérangose
mueveelmodelo ,nosolounnúmeroaislado. �� � �Nótesequeestoreutilizadirectamentelasmedidasde
centralidadydispersióndelaClase5.
6.7.9 �� � �Aplicación: ¿cómoelijoentrevariosmodeloscandidatos?
Preguntafinaldelaclase: sibajotresmodelosdistintos,¿cómosécuálusar?
Respuestadelprofesor: hacervalidacióncruzadaconlostresmodelos yquedarseconelde menorerror.
�� � �Sobreapoyarseenlaliteratura (preguntadeunaestudiante): sí,escorrectoyhabitualusarlaliteratura
paraseleccionarmodelosquefuncionanbienentareassimilares. Pero siempreconvieneevaluarmásde
unmodelo,porqueavecesunmodelotomadodirectamentedeunpapernofuncionaigualdebienenel
casopropio.
6.8Ejemploaplicado: Deep-Hub(slide32)—Importante
Referenciadelaslide: Pérez-Carrascoetal.2023.
Flujogeneralmostrado
Etiquetado → Entrenamiento → Evaluación → Predicción
Etapa Quéocurre
Etiquetado Conseguirlasetiquetasdealgunaparte
Entrenamiento Ajustarelmodelo
Evaluación Verificarsobreelconjuntodetestquétanbienlo
hace
Predicción Usarelmodelosobredatosnuevos
16

## Lamina 17

�� � �Elcasorealdetrásdelsistema
• Cliente: Arauco(empresaforestal).
• Problema: teníandronesvolandosobresusprediosgenerando ortomosaicos(muchísimasimágenes
compuestas). Elobjetivoprincipalera contarlacantidaddeárboles .
• Soluciónconstruida: lasimágenessedividenen grillas;dentrodecadaceldasepuede etiquetarlo
quesequiera;luego lascelditasseseparanenconjuntodeentrenamiento,validaciónytest ;se
entrenaelmodelo,seevalúasobretestysepredicecondatosnuevos.
• Generalidad: elsistemasirveparaetiquetarcualquiercosa—elprofesormencionaquepodríausarse
paracélulasuotrosobjetos.
������ �� � �Puntoconceptualfinal: lalocalizaciónesunproblemadeREGRESIÓN
Preguntadeunestudiantesobrequéseetiqueta. Respuestaclavedelprofesor:
“Cuandounohacelocalización[…]tengounaimagenyquierohacerunacajaalrededordealgún
objeto[…]lacajasedefineengeneralpordospuntos,unaesquinayotraesquina. Las coordenadas
son valores reales,entoncesesunproblemaderegresión.”
�� � �Estocierraelcírculoconladefinicióninicial: regresión=predecirunvalorreal ,independientemente
dequeelproblema“parezca”devisióncomputacionaloclasificación. Detectarobjetoscon boundingboxes
implicaregresiónporquelascoordenadasdelasesquinassonnúmerosreales.
�� � �Comentariosobreetiquetas
“Siempreunonecesitaetiquetas,siempreunonecesitalamayorcantidaddeetiquetasquepueda;a
veceslasetiquetassoncaras. Entoncestútienesquedealgunaformagenerarmodelosquehagan
lavalidacióncruzadaconelnúmerodeetiquetasquetengas.”
6.9Digresionesypreguntasabiertas—Complementario
Estebloquesurgeíntegramentedepreguntasdeestudiantes(CristóbalyPriscila)alfinaldela
clase. Noestáenlasslides. Esútilparacontextoprofesional,peroesdebajaprioridadparael
certamen.
6.9.1 �� � �¿Cómoseimplementaestoenunaarquitecturareal?
• Sedescarganlosdatos ,se entrenaelmodelo ,yluegose subeelmodeloentrenado conectándoloa
lapipelinedeprocesamiento.
• ElmodeloNOsereentrenamientrasestáenproducción (engeneral;hayexcepciones).
• Laimplementaciónprácticadelentrenamientoseveenla clasepráctica/ayudantía .
6.9.2 �� � �Autoaprendizaje( self-supervised learning)
• Modelosqueseentrenanpara reconocerlosdatosporsímismos ,sinunaetiquetaexterna.
• Ejemplo dado: inpainting — se borra un pedazo de una imagen y se le pide al modelo que la
reconstruya. Sitengounaimagendeunperroyrecortounaparte,leenseñoalmodeloapredecirese
recorte.
• Esautoaprendizajeporque nohayunaetiquetaquediga“perro” ;seusanlospropiosatributos(los
píxeles)comoobjetivo.
17

## Lamina 18

6.9.3 �� � �¿SepuedecompetirconOpenAI/Anthropic/Google?
Respuestadirectadelprofesor: “Noexisteformadecompetirconellos.” Tienendatacentersgigantes
distribuidosportodoelmundoyrecursosenormesparaentrenar. Alternativasrealistasmencionadas:
Alternativa Descripción
Modelosabiertos Ej. DeepSeek: sedescargaelmodeloy,conunaGPU
suficientementepotente,secorre enmodo
inferencialocalmente(evitandobrechasde
seguridad). Entrenarloesmuchomásdifícil
Modelosfundacionales Modelosdeusogeneraldescargablessobrelos
cualessepuedenhacercosas
Adaptadores “Modeloschiquititos”queseconectanaunmodelo
fundacionalyaprendenunatareaespecífica contus
datos,dejandofijatodala“maquinariapesada”. El
profesorlosllama “lowresolutionadapters” /LoRA
(notaexterna: enlaliteraturalasiglaLoRA
correspondea Low-Rank Adaptation;sedeja
constanciaporquelatranscripciónregistrala
expresióndichaenclase)
Cabezasdetarea ConectaralfinaldeunaLLMunmodelodistinto,por
ejemploun clasificadordesentimiento ,envezde
predecirlasiguientepalabra
Agentes Loqueestámásdemoda;requierecapacidadde
correrlasLLM
�� � �PorquéelprofesorusaAPIspagadasenvezdehardwarepropio (razonamientoeconómicoexplícito):
1. LosagentesnecesitanquelaLLMrespondarápido ,ylasGPUtipo gamernotienensuficienteanchode
banda. 2. LasGPUdealtoanchodebanda cuestancientosdemillonesdepesos . 3.Elhardwarequeda
obsoletoenunaño ,mientrasqueGoogle/OpenAI/Anthropicactualizansusmodelosautomáticamente.
�� � � � � � � � �FORMULARIODELACLASE
# Concepto Fórmula Prioridad
1 Modelolinealsimple ̂ 𝑦 = 𝜃0 + 𝜃1𝑥 Esencial
2 Funcióndecosto(error
cuadrático)
ℒ =
∑𝑛
𝑖=1( ̂ 𝑦(𝑥𝑖) − 𝑦𝑖)2
Esencial
3 Residuodeunpunto ̂ 𝑦(𝑥𝑖) − 𝑦𝑖 Esencial
4 Condiciónde
optimalidad
𝜕ℒ
𝜕𝜃0
= 𝜕ℒ
𝜕𝜃1
= 0 Esencial
5 Pendienteóptima(forma
interpretable)
̂𝜃1 = cov[𝑥, 𝑦]
var[𝑥] Esencial
6 Pendienteóptima(forma
desarrollada)
̂𝜃1 =
∑ 𝑥𝑖𝑦𝑖 − 1
𝑁 ∑ 𝑥𝑖 ∑ 𝑦𝑖
∑ 𝑥2
𝑖 − 1
𝑁 (∑ 𝑥𝑖)2
Importante
7 Interceptoóptimo ̂𝜃0 = ̄ 𝑦 − ̂𝜃1 ̄ 𝑥 Esencial
18

## Lamina 19

# Concepto Fórmula Prioridad
8 Regresiónpolinomial ̂ 𝑦 = 𝜃0 + 𝜃1𝑥 +
𝜃2𝑥2 + ⋯ + 𝜃𝑝𝑥𝑝
Esencial
9 Regresiónlinealgeneral
(basedefunciones)
̂ 𝑦 = ∑𝑝
𝑗=0 𝜃𝑗 𝑔𝑗(𝑥) Esencial
10 Coberturapromediodel
bootstrap
≈ 63.2% delas
observacionesoriginales
Importante
11 Proporcióntípicadel
holdout
2/3entrenamiento,1/3
validación
Importante
����� �LISTADEDEFINICIONESIMPORTANTES
Término Definición(segúnslidesyclase)
Aprendizajeautomático EstudiodealgoritmosquemejoransurendimientoP
enalgunatareaTconexperienciaE
Tareadeaprendizajebiendefinida Latripleta ⟨P,T,E ⟩
Datoetiquetado �� � �Datoquevieneacompañadodelvalorobjetivo
conocido
Aprendizajesupervisado Elqueusaunconjuntodeentrenamientocon
atributosxᵢyetiquetasyᵢ,conelobjetivode
determinarunafunciónquetomelosatributosy
predigalaetiqueta
Aprendizajenosupervisado Elqueseaplicacuandonohayetiquetas(clustering
yestimacióndedensidad)
Clasificación �� � �Tareasupervisadaenqueseestimauna claseo
categoría
Regresión Tareasupervisadaenquelaetiquetaapredeciresun
valorreal
Clustering �� � �Tomarelconjuntodedatosyformargrupos,de
modoquelosobjetosdentrodecadagrupose
parezcanentresíydifierandelosotrosgrupos
Entrenar �� � �Pasarledatosalmodeloparaqueaprendadesde
ellos,ajustandosusparámetros
Inferencia �� � �Etapaenquese usaelmodeloyaentrenado;no
modificasusparámetros
Funcióndecosto( ℒ) Funciónquemidequétanmalloestáhaciendoel
modelo;enregresión,lasumadeloserroresal
cuadrado
Parámetro(θ) �� � �Valorqueelmodelo aprendeduranteel
entrenamiento
Hiperparámetro �� � �Parámetroque sefijaantes deempezaraajustar
elmodelo(ej.: elordenpdelpolinomio)
Complejidaddelmodelo �� � �Relacionadaconel númerodeparámetros : más
parámetros=máscomplejo
Generalización Capacidaddeobtenerbuenosresultadoscondatos
nuncaantesobservados;quelamáquinanose
aprendadememorialosdatos
19

## Lamina 20

Término Definición(segúnslidesyclase)
Sobreajuste �� � �Cuandoelmodeloseajustatantoalosdatosde
entrenamientoquesolofuncionaconellosyno
generaliza
Conjuntodeentrenamiento Seusaparaqueelmodeloaprenda
Conjuntodevalidación Seutilizaparaajustarhiperparámetros
Conjuntodetest Seusaparaevaluar;elmodelonuncalohavisto
Validacióncruzada Estrategiadedividirlosdatosy repetirel
procedimientodeentrenamiento/validaciónpara
estimarlacapacidaddegeneralización
Holdout Separarendosconjuntos,entrenarenunoyvalidar
enelotro(típicamente2/3–1/3)
Bootstrap Generarmsubconjuntosdetamañon’<n
muestreandoconreemplazo;lonoincluidopasaa
validación
Submuestreoaleatorio Igualquebootstrappero sinreemplazo;elerror
finaleselpromediodeloserroresobtenidos
K-Fold DividirenKsubconjuntosdisjuntos,usarunocomo
validaciónyK−1comoentrenamiento,repitiendoK
veces
Autoaprendizaje(self-supervised) �� � �Entrenarelmodeloparareconocersuspropios
atributossinunaetiquetaexterna(ej.: inpainting)
���������POSIBLESPREGUNTASDEEXAMEN(conrespuestasbreves)
Verdadero/Falsoconjustificación
# Afirmación V/F Justificación
1 Unmodeloŷ=θ₀+θ₁x
+θ₂x²NOesuna
regresiónlineal,porque
contieneuntérmino
cuadrático.
F Laregresiónlineales
linealenlosparámetros
θ,noenx. Cadaθ
apareceunasolavez,sin
potenciasnifunciones
aplicadassobreél
2 Elconjuntodevalidación
seusaparaajustarlos
parámetrosθdel
modelo.
F Losθseajustansobreel
conjuntode
entrenamiento. El
conjuntodevalidación
seusaparaelegir
hiperparámetros
3 Elerrorseelevaal
cuadradoúnicamente
paraeliminarlossignos
negativos.
F Esunadelasrazones,
perotambiénpenaliza
másfuerteloserrores
grandesyseasociaal
supuestoderuido
normal
20

## Lamina 21

# Afirmación V/F Justificación
4 Siunmodeloobtiene
errorcerosobreel
conjuntode
entrenamiento,esel
mejormodeloposible.
F Esseñaltípicade
sobreajuste:
probablemente
memorizólosdatosyno
generalizará
5 Enbootstrap,tantoel
conjuntode
entrenamientocomoel
devalidaciónpueden
tenerdatosrepetidos.
F Soloelde
entrenamientopuede
tenerrepetidos;elde
validaciónno
6 Separarlosdatosen
entrenamiento,
validaciónytestunasola
vezyaconstituye
validacióncruzada.
F Esoes validación
(holdout). Lavalidación
cruzadaimplicarepetirel
procedimientocon
distintasparticiones
7 Unmodelomás
complejosiempre
generalizamejor.
F Existeunbalance: muy
complejo→sobreajuste;
muysimple→no
capturalaestructura
8 EnK-Foldcadadatose
usaexactamenteunavez
comodatodevalidación.
V Esprecisamentela
ventajadistintivadel
método
9 Elconjuntodetest
puedecambiarentre
iteracionesdela
validacióncruzada.
F Eltestseapartaalinicio
ynocambia;soloseusa
alfinal
10 Detectarunobjetoen
unaimagenmediante
unacajadelimitadoraes
unproblemade
clasificación.
F Lascoordenadasdelas
esquinasson valores
reales,porloqueesun
problemade regresión
Preguntasdedesarrollo
P1. Expliquelatripleta ⟨P,T,E ⟩aplicándolaaunmodelodelenguaje. E=todoeltextogeneradopor
lahumanidadydisponibleeninternet; T=predecirlasiguientepalabra/token; P=compararlapalabra
predichaconlarealmedianteunafuncióndecosto(enclasificación,laentropíacruzada).
P2. ¿Porquélafuncióndecostoelevalosresiduosalcuadradoynousaelvalorabsoluto? Tresrazones:
(a)eliminalosnegativos,evitandoqueerroresdesignocontrariosecancelenydenlafalsaimpresióndeun
modeloperfecto;(b)penalizadesproporcionadamenteloserroresgrandes,adiferenciadelvalorabsoluto;
(c) razón probabilística: el error cuadrático corresponde a suponer que el ruido de los datos sigue una
distribuciónnormal(surgedellogaritmodelanormal). Sedebenotarqueelefecto(b)dependedelaescalade
losdatos.
P3. ¿Quésignifica“aprender”enunmodeloderegresiónlineal? Significaencontrarlosvaloresdelos
parámetrosθque minimizanlafuncióndecosto . Estoselograigualandolasderivadasparcialesde ℒ
respectodecadaθacero. Enelcasolinealexisteuna soluciónanalíticacerrada : θ̂₁=cov[x,y]/var[x]yθ̂₀=
ȳ−θ̂₁x̄.
P4. ¿Porquésellama“regresiónlineal”sipuedeajustarpolinomiosycurvas? Porquelalinealidadse
refierealos parámetros,noalasvariables. Mientrascadaθⱼaparezcaunasolavezymultiplicando(sin
estarelevado,nidentrodeunlogaritmooexponencial),elmodeloeslineal,aunquelasfuncionesgⱼ(x)sean
21

## Lamina 22

polinomios,logaritmos,senosoexponenciales.
P5. Explique la diferencia entre parámetro e hiperparámetro con un ejemplo de esta clase.Los
parámetros(θ₀,θ₁,…)losaprendeelmodeloduranteelentrenamientominimizandolafuncióndecosto. El
hiperparámetrosefijaantesdeentrenaryseeligecomparandoresultadossobreelconjuntodevalidación.
Ejemplo: en regresión polinomial,p (el orden del polinomio) es el hiperparámetroy los θ son los
parámetros.
P6. ¿Porquésenecesitaunconjuntodevalidación yunconjuntodetest? ¿Nobastaconuno? Porqueal
elegirelhiperparámetrocomparandoerroressobreelconjuntodevalidación,seestá tomandounadecisión
conesosdatos ,ypodríaocurrirporazarqueunhiperparámetrofuncioneespecialmentebiensobreesa
particiónparticular—esdecir,sepuede sobreajustaralconjuntodevalidación . Poresolamétricafinale
insesgadasereportasobreunconjuntode testquenuncaparticipóenningunadecisión.
P7. Describalascuatroestrategiasdevalidacióncruzadaycuándoconvienecadauna. Holdout(una
solapartición,típicamente2/3–1/3;limitación: entregaunsolovalordeerror);Submuestreoaleatorio(repetir
elholdoutconparticionesaleatoriassinreemplazoypromediarloserrores);K-Fold(Ksubconjuntosdisjuntos,
cadaunousadoexactamenteunavezcomovalidación;convieneconmuchosdatos);Bootstrap(muestreo
conreemplazo,~63.2%deobservacionesoriginalesenentrenamiento; convieneconpocosdatos). Con
datosinfinitostodasconvergenalmismoresultado.
P8. ¿Quéventajatienerepetirlavalidaciónmuchasvecesfrenteahacerlaunasolavez? Seobtiene
unadistribucióndeerrores envezdeunúniconúmero: sepuedecalcularmediaomedianaydesviación
estándaropercentiles,yasíconocerelrangoenquesemueveelerrordelmodelo. Además,permiteverificar
queelerrordetest caigadentrodeesadistribución ;sinolohace,esseñaldequeelconjuntodetesttiene
unaanomalíaonoesrepresentativo.
P9. Uncompañeroajustaunpolinomiodegrado10yobtieneerrorcasiceroenentrenamiento. ¿Qué
lediría? Queelerrordeentrenamientonoesunindicadorválidodecalidad: elmodeloprobablementeestá
sobreajustado—memorizólosdatos,incluidoelruido,yalpreguntarleporvaloresintermediosentregará
prediccionesabsurdasquenosiguenlatendencia. Hayqueevaluarsucapacidadde generalizaciónmediante
validacióncruzadaycompararelerrordevalidaciónentredistintosgrados.
P10. ¿Cómoelegiríaentretresmodeloscandidatosdistintos? Mediantevalidacióncruzada: aplicarla
mismaestrategia(idealmentelamismapartición)alostresmodelos,compararloserroresdevalidacióny
quedarseconeldemenorerror;reportarlamétricafinalsobreelconjuntodetest.
�� �ERRORESYCONFUSIONESCOMUNES
1. Creerque“regresiónlineal”significaquelarelaciónentrexeydebeserunalínearecta. Esel
errorconceptualmásprobabledeestaclase. Lalinealidades enθ,noenx.
2. Confundirparámetroconhiperparámetro. Losθseaprenden;elordenpdelpolinomiosedecide
antesdeentrenar. Unmodelono“aprende”sushiperparámetros.
3. Creerqueseajustanparámetrossobreelconjuntodevalidación. No: losθseajustan soloconel
conjuntodeentrenamiento. Lavalidaciónseusapara decidir,nopara ajustar.
4. Pensarquelaparticiónentresconjuntosyaes“validacióncruzada”. Esoesholdout/validación.
Lavalidacióncruzadarequiere repeticióncondistintasparticiones.
5. Creerquebastaconunsoloconjuntoademásdeldeentrenamiento. Usarelmismoconjunto
paraelegirhiperparámetrosyparareportarmétricasproduceunaestimaciónoptimistaysesgadadel
rendimiento.
6. Juzgarunmodeloporsuerrordeentrenamiento. Elerrordeentrenamientosiemprebajaalaumentar
lacomplejidad;nodicenadasobregeneralización.
7. Asumirque“máscomplejo=mejor”. Existeunbalance; tantoelsubajustecomoelsobreajuste
degradanlacapacidadpredictiva.
22

## Lamina 23

8. Olvidarapartarelconjuntodetestalinicio,odejarlovariarentreiteraciones. Elprofesorlorepite
tresveces: “siemprepartoguardandoeltest” ,yeltest nocambia entreiteraciones.
9. Invertirlaregladerepeticionesdelbootstrap. Elentrenamientopuedetenerrepetidos;la validación
no.
10. Confundirbootstrapconsubmuestreoaleatorio. Laúnicadiferenciaeselreemplazo: bootstrap
muestreaconreemplazo,submuestreoaleatorio sinreemplazo.
11. Creerqueelerrorseelevaalcuadradosoloporlossignos. Sontresrazones(signos,penalización
deerroresgrandes,supuestoderuidonormal).
12. Suponerquesepediráderivarlasolucióndemínimoscuadradosenelcertamen. Elprofesorlo
descartóexplícitamente;loqueseevalúaeslacomprensiónconceptual.
13. Confundirelrendimiento(P)conlavelocidaddelmodelo. Pmidequétanbienlohace,nocuánto
demora.
14. CreerqueChatGPTesunaLLM. ChatGPTesunsistemamultiagente;GPTeslaLLMquetienepor
detrás.
15. PensarquealusarChatGPT/Claude/Geminiseestáentrenandoelmodelo. Esoesinferencia;el
modeloyaestáentrenado.
16. Asumirqueladeteccióndeobjetosconcajasesclasificación. Predecircoordenadasdeesquinases
regresión,porquesonvaloresreales.
17. Pensarquetodaslasestrategiasdevalidacióncruzadadanlomismo. Convergensolocondatos
infinitos;condatosfinitoslaelecciónimportaydependedelvolumendisponible.
18. Olvidarqueunmodelonopuedeaprenderloquenoestáenlosdatos. Sinoseleentreganratones,
noaprenderáareconocerratones.
��CONEXIONESCONCLASESANTERIORES
Conceptodeestaclase Seapoyaen…
Etapademodelamiento Elciclodelcientíficodedatos(Clase2)ysucarácter
bidireccional
Atributos=columnas;etiqueta=unadelas
columnas
Datostabuladosytiposdevariables(Clase4)
Estimacióndedensidadehistogramas Distribucionesyvisualización(Clase5)
Media/medianaydesviaciónestándar/percentiles
delerrordevalidación
Medidasdecentralidadydispersión(Clase5)
Covarianzayvarianzaenθ̂₁ Varianzaymatrizdecorrelación(Clase5)
“Elmodelonopuedeaprenderloquenoestáenlos
datos”
Calidaddedatos(Clase4)
Entropíacruzadacomofuncióndecostoen
clasificación
Anticipodela próximaclase
������MAPAMENTALDELACLASEENUNAPÁGINA
APRENDIZAJE AUTOMÁTICO ⟨P, T, E ⟩
│
├── ¿Hay etiquetas?
│ ├── SÍ → SUPERVISADO ── Clasificación (categoría)
│ │ └── REGRESIÓN (valor real) ◄── foco de la clase
│ └── NO → NO SUPERVISADO ── Clustering
23

## Lamina 24

│ └── Estimación de densidad
│
└── REGRESIÓN LINEAL
│
├── MODELO: ŷ = θ₀ + θ₁x → generaliza a ŷ = Σⱼ θⱼ gⱼ(x)
│ (lineal EN θ, no en x)
├── COSTO: ℒ = Σᵢ (ŷ(xᵢ) − yᵢ)²
│
├── APRENDER: minimizar ℒ ⇒ ∂ℒ/∂θ = 0
│ ⇒ θ̂ ₁ = cov[x,y]/var[x] , θ̂ ₀ = ȳ − θ̂ ₁x ̄
│
├── PROBLEMA: más parámetros → más complejo → SOBREAJUSTE
│ ⇒ pierde GENERALIZACIÓN
│
└── SOLUCIÓN: VALIDACIÓN CRUZADA
├── Entrenamiento → ajusta θ
├── Validación → elige hiperparámetros (p)
└── Test → métrica final (guardado desde el inicio)
Estrategias: Holdout · Submuestreo aleatorio
K-Fold · Bootstrap (63.2%)
24
