# Resumen_Clase8_DL_LLMs_Agentes

> Material de clase de Fundamentos de Ciencia de Datos, UdeC T2-2026.
> Texto extraido de `Resumen_Clase8_DL_LLMs_Agentes.pdf` para busqueda e indexacion.
> 42 laminas. Las figuras no se extraen: si una lamina
> depende de un grafico, hay que abrir el PDF.

---

## Lamina 1

FundamentosenCienciadeDatos—CLASE8: ÚltimosAvancesenInteligen-
ciaArtificial(DeepLearning,LLMsyAgentes)
Apuntescompletos: diapositivasoficiales+transcripcióndeclase
Profesor: Guillermo Cabrera-Vives (Ingeniero Civil Informático; MSc y Ph.D. en Ciencias de la Computación,
UniversidaddeChile)·guillecabrera@inf.udec.cl UniversidaddeConcepción —FacultaddeIngeniería·IITUdeC·
UnidaddeDataScience Modalidad: clasedictadaporZoom,conanotacionesenvivosobrelasdiapositivasymuy
altaparticipacióndeestudiantes(laclaseseextendió~1h49m;elpropioprofesorreconocealfinalque“sepasó”del
horarioporlacantidaddepreguntas). Audiencia: mixta—estudiantesdel magíster(MACI) ydel diploma.
Cómoleerestedocumento. Integraelcontenidodelas 66diapositivasoficiales contodolodicho
enclase,organizadosegúnelordenrealdelaexposición. Semarcancon �� � �loscontenidosque solo
aparecenenlatranscripción (noestánenlasslides),porquesuelenserjustamenteloqueunestudiante
olvidarepasar—yenestaclaseson muchísimos,yaquegranpartedelvalorestuvoenlasrespuestas
apreguntas. Semarcacon �� �elcontenidomatemáticoqueenlaspropiasslidesllevaelsímbolode
advertenciadelprofesor(enestaclaseapareceenlas slides18,19y43 ). Semarcacon ������loquetiene
mayorprobabilidaddeserevaluado.
Notasobreelarchivodeslides. Elarchivoentregadocomo FCD20262_08_DL_LLMs_Agents.pdfno
esunPDFsinouncontenedorcon66imágenesdediapositiva. Buenapartedelcontenidomatemático
(slides 13 a 31) estásolo como imagen, por lo que las fórmulas de este documento fueron leídas
visualmentedecadalámina.
Notasobrelasfuentes. Latranscripciónesautomáticaycontienenumerososerroresdereconocimiento
denombrespropios. Cuandoeltérminocorrectoapareceenlasslidesseusaeldelasslides;cuando
no,seproponeunareconstrucciónmarcadaexplícitamente. Verlatablacompletadecorreccionesal
finaldela§8.0. Todoloqueestáenestedocumentoprovienedelasdosfuentesentregadas;lasescasas
aclaracionesexternasestánmarcadascomo (nota externa).
Naturalezadelaclase. �� � �El profesor la presenta como una clasedepanorama, nodemétodo :
“yo la llamo los últimos avances de inteligencia artificial, pero cada vez los últimos avances son más,
entonces tengo que ir actualizándola cada vez que dicto esta clase… seguramente ya mañana va a estar
desactualizada esta clase”. Estotieneunaimplicanciadeestudiodirecta: loevaluablesonlosconceptos
ymecanismos,nolascifrascoyunturales .
����RESUMENEJECUTIVO
Estaclasecierraelbloquedemodelamientomostrando cómosepasódelosmodelosclásicosvistosenlasclases
6y7(regresión,SVM,árboles,RandomForest)aloquehoyllamamosDeepLearning,IAgenerativayagentes .
Elhiloconductoresunúnicomecanismorepetidoadistintasescalas: la neuronaartificialoperceptrón ,quetoma
entradas,lasmultiplicaporpesos,lassumaylaspasaporuna funcióndeactivaciónnolineal ;alconectarmuchos
perceptronesencapasseobtieneuna redneuronal,quemodelalosdatosen múltiplesnivelesdeabstracción y—
adiferenciadelMLclásico— extraelascaracterísticasautomáticamentedesdelosdatoscrudos ,siningeniería
manualdeatributos. Elentrenamientoreutilizaexactamentelalógicadelaclasederegresión: sedefineuna función
decosto (elerrorcuadráticopromedio),ycomolasredessonnolinealesnosepuededespejaranalíticamente,por
loqueseminimizaiterativamentecon descensodegradiente ,dondecadapasosemueveendireccióncontrariaa
laderivada,escaladoporla tasadeaprendizajeη (elhiperparámetromásimportantedeunared). Enlapráctica
estoseimplementacomounciclo forward(propagarlosdatoshaciaadelanteparapredecirycalcularelcosto)
ybackward(retropropagacióndelerrorparacalculargradientesyajustarpesos). Lasegundamitaddelaclase
muestraquéseconstruyósobreesabase: el mecanismodeatención (Attention is all you need,2017),quegenera
representacionescontextualesdecadapalabraponderandocuántaatenciónprestaralasdemás—yque,porser
altamenteparalelizable,permitióentrenarconvolúmenesdedatosantesimposibles;deahísalenlos modelos
fundacionales(BERT,consu masked language model queenmascarael15%delostokens)ylos transformers
autorregresivos,quealenmascararsiemprelaúltimapalabraseconviertenengeneradoresdetexto: los LLM.
ElprofesorinsisteenqueunLLM,porsísolo, solopredicelasiguientepalabra ,yporeso alucina,noaccedea
1

## Lamina 2

informaciónposteriorasuentrenamientoynorazonaniplanifica. Lasoluciónprácticasonlos agentes: unLLM
másmemoria,herramientas,objetivosycapacidaddepercibirelentorno ,capacesdeinvocarAPIs,buscaren
documentosycolaborarconotrosagentes—asífuncionarealmenteChatGPT,queesun sistemamultiagente,no
unLLMsuelto. Enparaleloseexplicala IAgenerativadeimágenes mediantemodelosdedifusión : agregarruido
progresivamenteaundatoyentrenarunaredpararevertireseproceso,demodoquepartiendodepuroruidose
genereunaimagennueva, condicionadaporeltextodelusuario. Laclasecierraconelpanoramadeindustriay
sociedad: elPremioTuring2018aBengio,HintonyLeCuntras~80añosdetrabajosobreredesneuronales;lacarta
de2023pidiendopausarlosexperimentos;lairrupcióndelopensource;ydatosdel AIIndex quemuestranquela
IAgenerativaes latecnologíadeadopciónmásrápidaenlahistoriadelahumanidad (53%en3años).
�CONCEPTOSCLAVEDELACLASE
# Concepto Prioridad Porquéimporta
1 DeepLearning=modelar
datosen múltiples
nivelesdeabstracción
concapasjerárquicas
Esencial Definiciónliteraldelaslide
10
2 DLextraecaracterísticas
automáticamente;elML
clásicorequierecalcularlas
amano
Esencial Es ladiferenciaconceptual
conlasclases6–7
3 DLganacuandohay
muchosdatos;conpocos
datosgananlos
algoritmosclásicos
Esencial Slide8;pregunta
conceptualmuyprobable
4 Perceptrón: ŷ=g(w₀+
x₁w₁+…+xₙwₙ)
Esencial Unidadbasedetodolo
demás
5 ������Lafunciónde
activacióngesNOlineal
—sinellatodocolapsaen
unmodelolineal
Esencial Correcciónexplícitadel
profesoraunalumnoen
clase
6 Funcióndecosto L=
(1/N)·Σ(ŷ(xᵢ)−yᵢ)²
Esencial Idénticaalerrordelaclase
deregresión
7 Descensodegradiente :
w^(t+1)=w^t−η·dL/dw
�� �
Esencial Slides18–19,marcadas
con �� �
8 Tasadeaprendizajeη
comohiperparámetro
clave
Esencial “Unodelos
hiperparámetrosmás
importantes”
9 Forwardpass (predecir+
calcularcosto)y backward
pass(retropropagación
delerror)
Esencial Slides26y31;elparmás
examinabledelbloqueDL
10 2012=añodela
revolución(ImageNet+
GPUs)
Esencial Hitohistóricoqueel
profesorrepiteyusacomo
ancla
11 2015=laIAalcanzael
niveldevisiónhumana
Esencial Elprofesorpide
explícitamenterecordarlo
ylopreguntadespués
12 Mecanismodeatención :
representacióncontextual
decadapalabra
Esencial Núcleoconceptualdela
segundamitad
2

## Lamina 3

# Concepto Prioridad Porquéimporta
13 ������Laatenciónes
altamenteparalelizable
⇒permiteentrenarcon
muchosmásdatos
Esencial Eslarazón técnicadepor
quélostransformers
ganaron
14 Transformer=modelo
basadosoloen
mecanismosdeatención
(Attention is all you need,
2017)
Esencial OrigendeGPTyBERT
15 Modelosfundacionales:
entrenadosconmuchos
datos,adaptablesa
muchastareasposteriores
Esencial Definiciónliteraldelaslide
36
16 BERTyel Masked
Language Model:
enmascarael 15%delos
tokensalazar
Esencial Cifraconcretay
memorizabledelaslide38
17 ������Enmascararlaúltima
palabra ⇒modelo
autorregresivo
generativo ⇒LLM
Esencial Elpuentelógicomás
eleganteymás
preguntabledelaclase
18 LLM=modeloquesolo
predicelasiguiente
palabra,agranescala
Esencial Basedetodaladiscusión
posterior
19 ������LosLLM alucinan,no
usaninfoposteriorasu
entrenamiento,no
razonanniplanifican
Esencial Slide45;contracara
obligatoriadelentusiasmo
20 ������GPT≠ChatGPT :GPT
eselmodelodelenguaje;
ChatGPTesun sistema
multiagente
Esencial �� � �Distinciónhecha
explícitamenteenclase,no
estáenslides
21 Agente=LLM+memoria
+herramientas+objetivos
+percepcióndelentorno
Esencial Slides46–47
22 Losagentesusan
herramientas(APIs,
intérpretesdecódigo,
internet,basesdedatos)
Esencial Esloqueresuelvelas
limitacionesdelpunto19
23 Modelosdedifusión :
procesohaciaadelante
(añadirruido)+proceso
inverso(denoising)
Esencial Slide42;basedela
generacióndeimágenes
24 Condicionamientopor
texto: asíChatGPT
convierteunprompten
imagen
Importante �� � �Explicadoenclase
sobrelaslide43
25 Premio Turing2018:
Bengio,Hinton,LeCun
Importante Datodurofácilde
preguntar
26 LosLLMtienendelorden
de10⁹–10¹¹parámetros
(GPT-3: 175B)
Importante Slide45
3

## Lamina 4

# Concepto Prioridad Porquéimporta
27 �� � �Elcostorealestáenla
inferencia(forwardpass),
nosoloenel
entrenamiento
Importante Discusiónlargay
sustantivaenclase
28 �� � �Destilación: enseñar
unmodelopequeño
desdeunogrande
Complementario Respuestaapreguntade
estudiante
29 �� � �Sistemasmultiagente
conagenteauditor para
bajarlatasadealucinación
Importante Muycitablecomobuena
práctica
30 IAgenerativa=
tecnologíadeadopción
másrápidadelahistoria
(53%en3años)
Importante Slide57
31 LatentSpaceDiffusion �� �Complementario Slide43,marcadacon �� �
32 Aprendizaje no
supervisadonoesparte
obligatoriadeestecurso
Complementario �� � �Aclaración
administrativadelinicio
8.0Informaciónadministrativayencuadredelaclase
�� � �8.0.1Informaciónadministrativa(todajunta,comopidióelformato)
Todaestasecciónproviene solodelatranscripción ;nadadeestoestáenlasslides.
Tema Detalle
Notasdelaprimeraprueba Alcierredelaclaseunestudianteconsultaporellas. El
profesorreconoceque aúnnoestán (“Tienes toda la
razón. No están”)ysecomprometeatenerlas amás
tardarelpróximoviernes ,intentandoadelantarlas.
Horariodeconsulta Lunesalas18:00. Elprofesorpideque avisenpor
correosivanaasistir : ellunespreviollegóynoasistió
nadie.
Hito2deltrabajo Antelapreguntadecómomostrarlosavancesdelhito2
(yaterminadoelhito1),larespuestaes: enloshorarios
deconsultadeloslunes .
Aprendizajenosupervisado Preguntadeunestudiantealminuto2. Respuesta: no
escontenidoobligatoriodeestecurso . Enel
programadel magíster(MACI) seveenun curso
posterior;enelprogramadel diplomaelprofesordicta
unaclaseespecialnoobligatoriaalfinaldelcurso
paraquienesquieranverlo.
Composicióndelcurso �� � �Seconfirmaqueenlasalahay alumnosdel
magísterydeldiploma simultáneamente.
Charlaprevia �� � �Semencionadepasadaunacharlaanteriorconun
invitado(“Felipe”)sobreregulación/datos,usadacomo
referenciaalhablardelalentitudlegislativafrenteala
IA.
4

## Lamina 5

8.0.2Repaso: aprendizajesupervisado(slide2)
Elprofesorabreexactamenteconelmismoesquemadelasclases6y7:
Aprendizaje supervisado. Utiliza unconjunto de entrenamientocompuesto poratributos xᵢy
etiquetas yᵢ. Objetivo: determinar una función que tome los atributos y prediga la etiqueta. - Si
la etiqueta a predecir es unvalorreal →regresión. - Si la etiqueta a predecir es unacategoría→
clasificación.
Formalmente: ŷ=f(x) .
�� � �Ejemplosdadosenvivoparaconectarconelrestodelaclase: - Losatributospuedenserlospíxelesdeuna
imagen,oeltamañodeunárbol. ←EstafraseeselpuentehaciaDeepLearning: porprimeravezlosatributosson
datos crudos. -Laetiquetapuedeserunaclasificación(perro/gato)o,enregresión,elvolumendelárbol.
�� � �“Hoy día vamos a ver cómo esto pasó de estos modelos como clásicos que yo les mostré, a lo que hoy
llamamos Deep Learning, que es básicamente redes neuronales artificiales.”
8.0.3Agendaoficial(slide3)
Unidad Tema
01 DeepLearning
02 I.A.Generativa: LargeLanguageModels(LLMs)ydifusión
03 Agentes
04 Últimosavances
�� � �Elprofesorañadequealfinalhablará “de la gente y de cómo el mundo está cambiando gracias a todo esto” —y
aclaraquecuandodice inteligenciaartificialgenerativa serefierea inteligenciaartificialquegeneradatos .
8.0.4Elsímbolo �� �
�� � �“Hay algunas partes matemáticas en las cuales aparece este símbolo, quiere decir que se requiere
conocimiento avanzado de matemáticas. Las paso igual; si no tienen conocimiento, no importa, igual
pueden seguir el resto de la clase.”
En esta clase el símbolo aparece en lasslides 18 (Minimización de funciones de costo), 19 (Descenso de
gradiente)y43(LatentSpaceDiffusion) .
8.0.5 ������Tabladecorreccionesdelatranscripciónautomática
Estatablaesútilporquevariosdeestosnombres sísonevaluables ylatranscripciónlosdeforma:
Apareceenlatranscripción Términocorrecto Basedelacorrección
“AndrewN.G.” AndrewNg Apareceescritoenlaslide5
“JoshuaBenyo” YoshuaBengio Slide51(TuringAward)yslide52
“JeanLecun”/“JanLecun” YannLeCun Slide51
“SupportVectorMachine” ✓ (correcto) Slide12
“funciónTg” funcióng Laslide13rotulalaactivacióncomo
g
“algoritmodesensorgradiente”/
“gradienteestocástico”
descensodegradiente
(estocástico)
Slide19: “DescensodeGradiente”
“masslanguagemodel” MaskedLanguageModel(MLM) Slide38
“Verenmascarael15%” BERTenmascarael15% Slide38
5

## Lamina 6

Apareceenlatranscripción Términocorrecto Basedelacorrección
“Celebras” Cerebras (reconstrucción) Slide53loescribe“Celebras”,pero
elhitodescrito—“OpenSource
GPT-3”,28demarzode2023—
correspondea Cerebras. Semarca
comoreconstrucciónporquela
propiaslidecontienelaerrata.
“Bart” Bard (reconstrucción) Slide53: “A13Bmodelachieves
paritywithBard”
“Antropic” Anthropic (reconstrucción) Mencionadooralmente;coherente
con“ClaudeCode”enlaslide64
“Cloud”/“CloudCode”/“Cloud.md” Claude/ClaudeCode /
CLAUDE.md (reconstrucción)
Laslide64muestraellogode
ClaudeCode;elarchivode
configuracióncompartidoen
repositorioses CLAUDE.md
“elvectorVíctor” elvector Contexto
“ladrón”(repetido) ladró Laslide35escribelaoración: “El
perro café se puso feliz y me ladró”
“DALI” DALL·E2 Slide44
“el2013Googledijo…nola
podemosdetener”
2023 Laslide53fechatodalacronología
en2023
“1.200imágenesdeentrenamiento” 1,2millones(1.2M) Slide6
“LatinoaméricaAIreport/LatamAI
report”
nombre incierto Elpropioprofesordudadelnombre
exactoenclase
“CornerShop” Cornershop Nombredelaempresa
“Bilton” nombre de un estudiante, incierto Vocativo
8.1InteligenciaArtificial: definiciónycontextohistórico(slides4a9)—
Importante
8.1.1DefinicióndeIA(slide4)
InteligenciaArtificial: áreaquetrabajaensistemasquepuedan: - Razonar: procesardatosycrear
nuevoconocimientoapartirdelexistente. - Actuar: tomardecisionesymodificarelmedioambiente.
������Nótesequeestadefinicióndedosverbos( razonaryactuar)esexactamentelaquereaparecealfinaldelaclase
enladefiniciónde agente—unagentees,literalmente,unsistemaquerazona yactúa. Esunasimetríadeliberada
yunbuencandidatoapreguntaconceptual.
8.1.2“LaIAeslanuevaelectricidad”(slide5)
Fraseatribuidaa AndrewNg. �� � �Elprofesorprecisaque ladijohaceunos10años .
Argumento: laelectricidadcambiósignificativamentelaindustria—transporte,manufactura,salud,comunicaciones.
Antesdelaelectricidadtodosehacíadistinto;después,todocambió. LaIAestáhaciendolomismohoy.
8.1.3 ������ImageNetyelaño2012(slides6y7)—Esencial
ImageNetLargeScaleVisualRecognitionChallenge: -1,2millonesdeimágenes deentrenamiento- 1.000
categoríasdeobjetos
�� � �Descripcióndelatareadadaenclase: dadaunaimagen, localizarlosobjetosquehaydentro deella(unauto,
unapersona,uncasco,unperro,unasilla…)entreesas1.000categorías.
6

## Lamina 7

�� � �Contrasteconhoy: “es un problema que hoy en día está resueltísimo” —cualquierasacaunafotoconelcelular,
elcelularledicequées,einclusoselepuedepedir“eliminaelperrodelafoto”ylohace. Peroantesde2012era
unproblemamuydifícil.
������LacurvadeerrordeImageNet(slide7)—memorizarlaforma
ElgráficomuestraenelejeYel errorhistórico sobreeldesafío:
Momento Error Comentariodelprofesor
Antesde2012 ~28%→25% Estancado
2012 ~16% �� � �“Bajar el error en un desafío así
de importante, en 10% en un año, es
lo que uno llama una revolución.”
2013 ~5puntosmenos Siguebajando
2014 ~5puntosmenos Siguebajando
2015 — ������Sellegaalniveldevisión
humana
�� � ������� “Y recuerden esto porque lo vamos a conversar después. El año 2015, la inteligencia artificial fue
capaz de llegar al nivel de visión del ser humano.”
�� � �Elprofesor efectivamentevuelveapreguntaresteaño unahoramástarde,almostrarelgráfico
delAIIndex(§8.10.5). Eseldatomásseñalizadodetodalaclase.
8.1.4 ������¿Quépasóen2012? LasGPUs
Loqueocurriófuequeseaplicó demanerasignificativa,porprimeravez,loquehoyllamamosDeepLearning .
�� � �Elprofesormatiza: “No por primera vez, pero se aplicó de manera, digamos, significativa” .
Lacausahabilitantefueelusode GPUs(unidadesdeprocesamientográfico) ,que antiguamenteseusabanpara
videojuegos,paraajustarmodelosdeIAdemaneramuyrápida.
�� � �Laestadísticaquelodemuestra (númerodesolucionesdeldesafíoqueusabanGPU):
Año SolucionesconGPU
2010 0
2011 0
2012 4
2013 60
2014 110
�� � �Mecanismodecontagio: albajarcasi10puntoselerrorenunaño, “todos los investigadores del mundo fueron
a mirar cómo lo hicieron, y se dieron cuenta que usaban GPU” .
8.1.5 ������DeepLearningvs.algoritmosclásicossegúncantidaddedatos(slide8)—Esencial
Laslidemuestraunesquema(elprofesoraclara �� � �queesundibujoilustrativo,nodatosreales ):
• EjeX: cantidaddedatos· EjeY: desempeño
• Conpocosdatos: losalgoritmosclásicosfuncionanmejor queDeepLearning. �� � �“Los algoritmos clásicos
son como los que hemos estado viendo en este curso” (SVM,RandomForest,regresión).
• Conmuchosdatos: DeepLearningfuncionamejor.
�� � �Conexiónconlarealidad: estovadelamanoconque “nosotros como humanidad hemos generado muchos
datos”. Senecesitanmásymásdatosparaentrenarcorrectamenteestosalgoritmos.
7

## Lamina 8

������Porquéimportaparaelexamen. Estaláminaeslaquejustificaquelasclases6y7 noquedaron
obsoletas. Larespuestacorrectaa“¿essiempremejorDeepLearning?” es no: dependedelvolumende
datosdisponible.
�� � �Frasefuertedelprofesor: “nada de lo que tenemos de inteligencia artificial hoy día, o muy poco, funciona sin
Deep Learning. Casi todo es Deep Learning.”
8.1.6InterésenDeepLearning(slide9)—Complementario
�� � �Esun GoogleTrends queelprofesorarmó“haceunpardemeses”,mostrandobúsquedasdeltérmino“Deep
Learning”eneltiempo:
• 2012–2013: muybajo→ �� � �“eso quiere decir que vivía en el mundo de la investigación, de la academia” .
• 2017–2018: yahaymuchointerésdetodoelmundo.
�� � �Lecturainteresante: hay~5añosdedesfaseentrelarevolucióntécnica(2012)ylaconcienciapública
(2017). EselmismofenómenoquereaparececonlosLLM.
8.2¿QuéesDeepLearning? (slides10a12)—Esencial
8.2.1 ������Definiciónformal(slide10)—memorizarliteralmente
DeepLearning: conjuntodealgoritmosque modelanlosdatosatravésdemúltiplesnivelesde
abstracciónusandoun conjuntodecapasjerárquicas .
�� � �Antesdedarla,elprofesorbromea: “les estoy tratando de vender algo que todavía no les explico lo que es… si les
ha gustado, espero que me lo hayan comprado” .
8.2.2 ������Elejemplocanónico: reconocercaras(slide11)
Construcciónenclase, dearribahaciaabajo yluegoalrevés:
Niveldeabstracción Contenido
Nivel3(alto) Caras
Nivel2 Ojos,narices,bocas
Nivel1(bajo) Líneas,puntos,curvas
�� � �Razonamientotextual: “Nosotros como seres humanos, antes de reconocer caras, tenemos que reconocer lo que
es un ojo, una nariz o una boca. Si reconozco un ojo, una nariz y una boca, entonces puedo, en una siguiente capa
de abstracción, reconocer lo que es una cara. Pero para reconocer un ojo, una nariz y una boca, tengo que primero
reconocer lo que son líneas, puntos, curvas.”
������LasdosgraciasdeDeepLearning(segúnlaclase)
1. �� � �“Tú le puedes pasar los datos directamente, sin tener que calcular atributos ni nada.”
2. �� � �Lohace automáticamente: “Yo no le tengo que decir ‘búscame líneas’, sino que aprende automáticamente
a encontrar las líneas, aprende automáticamente a encontrar los ojos, aprende automáticamente a armar lo que
es una cara.”
�� � �AclaraciónimportantesobrelarelaciónDL↔redesneuronales: > “Deep Learning está, hoy en día, es casi
puro red neuronal. Acá simplemente estoy diciendo que van a ver distintos niveles de abstracción. Pero hoy en día se
implementan con redes neuronales los algoritmos de Deep Learning.”
�� � �Esdecir: DeepLearningeselconcepto(nivelesdeabstracciónjerárquicos);lasredesneuronalessonla
implementación. Nosonsinónimospordefinición,perohoylosonenlapráctica.
8

## Lamina 9

8.2.3 ������DeepLearningvs.MachineLearningclásico(slide12)—Esencial
MachineLearningclásico DeepLearning
Pipeline Objeto→ calcularcaracterísticasa
mano→modelo(SVM,Random
Forest…)
Objeto→ redneuronal (extracción
decaracterísticas+clasificación
juntas)
Características Diseñadasporelhumano Extraídasautomáticamentedesde
losdatos
Ejemplosdecaracterísticas �� � �“ellargodelaorejadelanimal”,
“eltamañodelanimal”,“elanchodel
árbol”
Lasquelareddescubra
Interpretabilidaddelas
características
Alta(unolaseligió) �� � �“A veces no son las
características que uno mediría ,
pero son características que te
ayudan a resolver el problema.”
������Losejemplosdecaracterísticasson exactamentelosmismos queenlasclases6y7(tamañodel
animalydelasorejasparaperro/gato;anchodelárbolparaelvolumen). Elprofesorlohaceapropósito
paraqueseveaelcontraste.
�� � �8.2.4Preguntadeestudiante: ¿realmenteaprende“líneas”y“ojos”? —Importante
Pregunta(Germán): enlascapasocultassehacenconvoluciones; “¿eso realmente ocurre así, o es más teórico?
Porque yo lo veo y al final para mí esto son puras funciones lineales que se van haciendo cada vez más complejas.”
Respuestadelprofesor—tienetrespartes,todasrelevantes:
1. Lasconvolucionesfuncionancomofiltros. Desdeelpuntodevistadeextraccióndecaracterísticas,pueden
pensarsecomo filtrospasa-altoopasa-bajo .
2. Síocurre,almenosenlasredesde2012–2014: “tú veías estos filtros y efectivamente tenían ese tipo de
componentes… Automáticamente, la red aprendía filtros parecidos a los que uno armaría como humano, y había
muchos filtros que uno no armaría como humano , pero que también la red aprendía.”
3. ������Matizhonestoymuycitable: “Este es un ejemplo de cómo debiese funcionar teóricamente . En la
práctica, a veces funciona así, a veces no, y depende de la arquitectura que uno use.” —ytambiéndela
naturalezadelosdatos ydelproblemaaresolver.
������Estaeslarespuestacorrectasienunapruebapreguntansilascapasdeunared“siempre”aprenden
bordes,ojosycaras: noestágarantizado;esunailustracióndidáctica,nounaley .
�� � �Laobjecióndelestudiante(“sonpurasfuncioneslineales”) quedarespondidaenlasecciónsiguiente —yel
profesorvuelveexplícitamentesobreella.
8.3Elperceptrónyelentrenamiento(slides13a19) �� �—Esencial
8.3.1 ������Laneuronabiológicacomoanalogía
�� � �Construcciónenclase: -Una neuronabiológica esunacélulaque recibeunimpulsoeléctrico ydespués lo
emitehaciaotrascélulasconectadas; puedeactivarseonoactivarse . -Conunpuñadodeneuronassearmaun
sistemanervioso. -DeepLearningeslamismaidea: “modelar la neurona como una herramienta matemática” ,y
luegoconectarmuchasneuronas parageneraruna redneuronalartificial . -Seconectan encapas: entrada→
capa→capa→capa→salida. Esoes,precisamente, “modelar los datos de entrada a través de distintas capas de
abstracción”.
9

## Lamina 10

8.3.2 ������Elperceptrón(slide13)—fórmulaobligatoria
Launidadbasedelasredesneuronaleseslaneuronaartificial,llamadaPERCEPTRÓN.
̂ 𝑦 = 𝑔 (𝑤0 + 𝑥1𝑤1 + 𝑥2𝑤2 + ⋯ + 𝑥𝑛𝑤𝑛)
Anatomíadelalámina(leídadelaimagen):
Elemento Rol
Entrada1(constante) Multiplicadapor w₀→esel sesgo/intercepto
Entradasx₁,x₂,…,xₙ �� � �“Piensen que cada uno de estos valores puede ser el
píxel de una imagen”
Pesosw₀,w₁,…,wₙ Losparámetrosaajustar
Σ(weightedsum) Sumaponderada
g Funcióndeactivación
ŷ Salida
������ �� � �Lacorrecciónmásimportantedelaclase: elperceptrónNOeslineal
RespondiendodirectamentealaobjecióndeGermán:
�� � �“No son funciones lineales. Son funciones no lineales . El perceptrón es no lineal. Las redes neuronales
son no lineales. De hecho, si tú hicieras un perceptrón lineal y conectas todos los perceptrones
lineales que quieras, al final se transforma todo en un modelo lineal nomás. Entonces no te sirve
mucho.”
Dóndeestáexactamentelanolinealidad (desarrollohechopasoapasoenclase):
1. Tomoel1ylomultiplicoporw₀→w₀
2. Tomox₁ylomultiplicoporw₁→x₁w₁
3. …yasíhastaxₙwₙ
4. Sumotodo → �� � �“acá todavía es un modelo lineal ”
5. Pasoesatransformaciónlinealporlafunciónnolinealg → �� � �“y entonces g transforma el perceptrón en
un modelo no lineal ”
6. Resultado:ŷesunafunciónnolinealdelinput
������Preguntadeexamencasisegura: ¿por qué una red neuronal necesita funciones de activación no
lineales? →Porque lacomposicióndefuncioneslinealeseslineal : apilarcapaslinealesnoaumentala
capacidadexpresivadelmodelo;equivaldríaaunúnicomodelolineal.
�� � �Y luego: “esto es una neurona, pero en la práctica yo conecto muchas de estas neuronas: la salida de esta
neurona la conecto como entrada a otra neurona ”.
8.3.3 ������Ejemplo: laregresiónlinealES(casi)unperceptrón(slides14y15)
Elprofesorrehacedeliberadamenteelejemplodelaclasederegresión:
• Conjuntodedatos: 𝒟={(x₁,y₁),(x₂,y₂),(x₃,y₃),(x₄,y₄)} (4puntos)
• Modelolineal: ŷ=w₀+w₁x
• Laslidemuestra tresrectas (verde,naranja,roja)yrepitelapreguntadelaclase6: “¿cuál es el modelo que es
mejor y por qué?”
• Respuestadeunestudiante,validada: lanaranja,porquetienemenoserror.
������Elpuntoclavedelalámina
�� � �“Fíjense que este modelo que acabo de armar, que es w₀ + w₁x, es un perceptrón . Es muy parecido a
un perceptrón: paso un 1, lo multiplico por w₀, le sumo w₁ multiplicado por x, y después todo esto lo sumo
y sale. Lo único que le está faltando es la función no lineal para transformarse en un perceptrón
propiamente tal.”
10

## Lamina 11

�� � �Laslide15dibujaprecisamenteeso: dosentradas( 1yx),dospesos( w₀yw₁),un Σ,ysalida ŷ. Sing.
������Conexiónconceptualclaveconlaclase6: unaregresiónlinealesunperceptrónsinfunciónde
activación. Equivalentemente:unperceptrónesunaregresiónlinealalaqueseleaplicóunano
linealidadalasalida.
8.3.4 ������Funcióndecosto(slides16y17)—fórmulaobligatoria
Setomaelmodeloelegidoysemidesuerrorcontracadadato.
Errordeunpunto (el“loss”individual):
ℒ𝑖 = ( ̂ 𝑦(𝑥𝑖) − 𝑦𝑖)2
Laslide17losenumeraexplícitamenteparalos4puntos: ℒ₁, ℒ₂, ℒ₃, ℒ₄.
Funcióndecostototal(promediodeloserrores):
ℒ = 1
4 [( ̂ 𝑦(𝑥1) − 𝑦1)2 + ( ̂ 𝑦(𝑥2) − 𝑦2)2 + ( ̂ 𝑦(𝑥3) − 𝑦3)2 + ( ̂ 𝑦(𝑥4) − 𝑦4)2]
FormageneralparaNdatos:
ℒ = 1
𝑁 [( ̂ 𝑦(𝑥1) − 𝑦1)2 + ( ̂ 𝑦(𝑥2) − 𝑦2)2 + ⋯ + ( ̂ 𝑦(𝑥𝑁 ) − 𝑦𝑁 )2] = 1
𝑁
𝑁
∑
𝑖=1
( ̂ 𝑦(𝑥𝑖) − 𝑦𝑖)2
�� � �Desarrolloverbal(útilporqueexplicael porquédecadapaso): 1. Elerrores ladiferenciaentrey₁yŷ(x₁) —la
distanciaverticalentreelpuntoylarecta. 2. “Y yo lo que hago es que lo elevo al cuadrado.” 3. “Y después hago lo
mismo con todos los puntos.” 4. “Voy a promediar los errores.” 5. Objetivo: encontrarelmodeloque minimicela
funcióndecosto.
�� � �Notaterminológica: enDeepLearning “se le suele llamar función de costo ”,peroeselmismoobjetoquela
funcióndeerrordelaclasederegresión. (Enlasslidessedenotaconlaletracaligráfica ℒ.)
8.3.5 �� �������Minimizacióndelafuncióndecosto(slide18)—Esencial
Elproblema
�� � �“Si es que este fuese un modelo lineal, es fácil, ya lo vimos en la clase de regresión cómo podemos
hacerlo. Pero el problema es que las redes neuronales son no lineales, tienen muchas componentes
no lineales entre medio. Entonces, ¿cómo lo puedo resolver?”
�� � �������Esteeselmotivodeexistirdeldescensodegradiente. Enregresiónlinealsepuededespejarlasolución;
enunaredneuronal no,porlanolinealidad. Hayque buscariterativamente.
Elplanteamientográfico
• Eje X:el parámetrow(la slide simplifica a una sola dimensión;�� � �el profesor aclara explícitamente que
“para simplificar la explicación lo hice en una dimensión” ,aunqueenrealidadestánw₀yw₁,yenunaredhay
millones).
• EjeY: lafuncióndecosto ℒ.
• Se parte de unvalorinicialcualquiera w¹ (“parto con algún valor cualquiera, que no sé cuál es” ) y se va
bajandoporlacurva.
11

## Lamina 12

������Lasecuacionesdelaslide18
𝑤2 = 𝑤 1 + Δ𝑤1 𝑤3 = 𝑤 2 + Δ𝑤2 𝑤4 = 𝑤 3 + Δ𝑤3
𝑤𝑡+1 = 𝑤 𝑡 + Δ𝑤𝑡
�� � �Lapreguntaquequedaabiertayquemotivalaslidesiguiente: “¿cómo yo lo hago para encontrar el Δwᵗ?”
�� � �Detallevisualdelaslide: lacurvadibujadatiene variosvalles (noesconvexa),ylatrayectoriaw¹→w²→w³→
w⁴sepasadelmínimoyvuelve —elprofesorlodescribecomo “la pelota sigue avanzando y puede ser que se
pase”. Esunarepresentaciónhonestadequeeldescenso oscila.
8.3.6 �� �������Descensodegradiente(slide19)—lafórmulamásimportantedelbloque
𝑤𝑡+1 = 𝑤 𝑡 + Δ𝑤𝑡
Δ𝑤𝑡 ∝ − 𝑑ℒ
𝑑𝑤
𝑤𝑡+1 = 𝑤 𝑡 − 𝜂 𝑑ℒ
𝑑𝑤 ∣
𝑤𝑡
dondeη(eta) esla tasadeaprendizaje (learning rate),rotuladaasíexplícitamenteenlalámina.
������Lecturaconceptual(loquehayquesaberdecirconpalabras)
Elemento Significado
dℒ/dw Laderivadadelafuncióndecostorespectodelos
parámetros: indicalapendiente,oseahaciadónde
subeelcosto
Elsigno− Poresomemuevoen direccióncontraria aladerivada:
quierobajar,nosubir
η Cuántoavanzoenesadirecciónencadapaso
** _wt**
������Latasadeaprendizajeη
�� � �“La tasa de aprendizaje es uno de los hiperparámetros más importantes de todos los modelos de
redes neuronales, porque te dice qué tan rápido va a aprender .”
�� � �Conexiónconlasclases6y7: ηesun hiperparámetro,nounparámetro. Los parámetrossonlos w(se
aprendendelosdatos);η seeligedesdeafuera —y,porlaregladeorodelcurso, seeligeporvalidacióncruzada .
�� � �8.3.7 ������Mínimoslocales: elintercambiomássustantivodelaclase—Importante
Planteamientodelestudiante: sipartimosconunatasadeaprendizajemuybaja, “¿podríamos llegar solamente a
un [mínimo] local?”
Respuestadelprofesor: “Podría ser. Pero es muy poco probable. ”
12

## Lamina 13

������Elargumento(reconstruido;latranscripciónestámuyfragmentadaenestetramo)
Elrazonamientoexpuestoes dimensional:
• En1dimensión,paraestaratrapadobastaqueelpuntoseaunmínimolocalenesaúnicadimensión.
• En2dimensiones,tienequesermínimolocal enlasdos dimensionessimultáneamente.
• En3dimensiones,tienequesermínimolocal enlastres .
• ⇒Enun espaciodealtísimadimensión (millonesdeparámetros),laprobabilidaddeque todaslasdirecciones
subanalavezesmuybaja: casisiemprequeda algunadirecciónporlacualseguirbajando .
������Conclusiónutilizableenunaprueba: enredesneuronalesreales, losmínimoslocalessonmucho
menosproblemáticosdeloquelaintuiciónen1Dsugiere ,precisamenteporla altadimensionalidad
delespaciodeparámetros.
�� �Advertencia sobre la fuente: enestetramolatranscripciónestácortadapalabraporpalabrayenun
puntodice “hay muy pocos mínimos globales” dondeelsentidodelargumentoexige mínimoslocales.
Setratadeunerrorevidentedetranscripción(ounlapsus),yaquísereconstruyelaversióncoherente.
�� � �8.3.8Notasobreelnombre“estocástico”
Elprofesormencionael descensodegradienteestocástico ydaunajustificacióndeladjetivo: “se le llama estocástico
porque tú lo ajustas desde los datos” .
�� �Eltramoestámuydegradadoenlatranscripción. (Nota externa: el término se refiere a que en cada paso se usa
un subconjunto aleatorio de datos en vez de todo el conjunto — pero esto no fue desarrollado en clase , así que no
debe darse por materia.)
8.4Redesneuronales: forwardybackward(slides20a31)—Esencial
8.4.1Deunaneuronaaunared(slides20a25)
Lasecuenciadeláminasconstruyelaredporacumulación:
1. Slide20: seencierraenuncírculo todoelperceptrón(entradas1,x₁,x₂→pesosw₀,w₁,w₂→Σ→g→ŷ). �� � �
“Voy a hacer como que toda esta parte fuese un solo círculo, y lo voy a esconder.”
2. Slides21–25: esecírculopasaaser unnodo,yseconectanmuchosnodosen capassucesivas.
3. Slide24: apareceelejemplocompleto—una imagen(deunperro,enpíxeles) entraporlaizquierda,sus
valoresalimentanlaprimeracapa,ylaseñalsepropagapordoscapasocultashastaun nododesalida .
������Detalleimportantedelaslide24: laentradason lospíxelescrudosdelaimagen ,nocaracterísticas
calculadas. Eslamaterializaciónvisualde§8.2.3.
8.4.2 ������FORWARDPASS(slide26)—Esencial
�� � �“Cuando yo quiero que el modelo prediga, lo que tiene que hacer es partir desde el input y empezar a
propagar hacia adelante los valores: va a multiplicar por los pesos y va a pasar hacia adelante, multiplicar
por los pesos y pasar hacia adelante, y al final termina acá y dice PERRO.”
Forwardpass(pasadahaciaadelante): losdatosvan desdelaentradahacialasalida ,deizquierdaa
derecha,multiplicándoseporlospesoscapaporcapa,hastaproducirlapredicción.
�� � �Sinónimodadoenclase: aesto selellamahacerinferencia —esloqueocurrecuandoelmodeloyaestá
entrenadoysoloqueremosqueprediga.
�� � �Nombredelaarquitectura: “las redes neuronales así como la que estoy mostrando se llaman feedforward
neural networks, redes neuronales hacia adelante, porque se van alimentando hacia adelante.”
13

## Lamina 14

8.4.3 ������BACKWARDPASS(slides27a31)—Esencial
Lasecuenciadeláminas27–31muestraelcasodelerror: laredpredice GATOcuandolaimageneraun perro.
�� � �“Imagínense que el modelo haya predicho gato y esto era un perro. Entonces yo puedo calcular una
función de costo . Calculo la función de costo, y ahora lo que tengo que hacer es ir modificando la red
hacia atrás: desde la función de costo empiezo a modificar cada una de las neuronas hacia atrás para
tratar de que se vayan ajustando y de esa forma vayan optimizando el modelo. Eso es lo que se llama un
backward pass.”
Laslide31 lodibujaexplícitamente: unaflechagrande BACKWARDdederechaaizquierda,con ℒentrandoporla
salidaytodaslasneuronascoloreadaspropagandolacorrecciónhaciaatrás.
������Nombredelalgoritmo
ElalgoritmoqueajustaelmodelosellamaalgoritmodeRETROPROPAGACIÓNDELERROR(back-
propagation). �� � �“Porque tomo el error y lo voy propagando hacia atrás para ir mejorando la red.”
8.4.4 ������ �� � �Cómosecombinanforward,backwardydescensodegradiente—muyexam-
inable
Surgedeunapreguntadeunestudiante( “¿normalmente se hacen ambas cosas?” ). Larespuestaarticulalastres
piezasyes elresumenoperativodelentrenamiento :
�� � �“El algoritmo de descenso de gradiente tiene que ir calculando los gradientes, y cada vez que yo calculo
los gradientes avanzo una vez hacia adelante [en la curva de costo]. Cuando yo hice el primer paso, tengo
que tomar los datos y hacer el forward con toda la red, calculo el error , y después, para calcular los
gradientes, hago el backward , voy para atrás, y ahí calculo los gradientes, y ahí decido hacia dónde
avanzar.”
������Ciclodeentrenamiento(memorizarelorden)
Repetir para cada paso t del descenso de gradiente:
1. FORWARD : propagar los datos de entrada a través de toda la red → ŷ
2. COSTO : calcular ℒ comparando ŷ con las etiquetas reales y
3. BACKWARD : retropropagar el error para obtener los gradientes dℒ/dw
4. ACTUALIZAR: w^(t+1) = w^t − η · dℒ/dw ← un paso de descenso de gradiente
������Elerrorconceptualqueestopreviene: creerqueforwardybackwardson alternativas. Noloson:
sonlasdosmitadesdecadaiteración. Elforwardcalculaelerror;elbackwardcalculalosgradientes;el
descensodegradienteusaesosgradientesparadarelpaso.
�� � �Honestidaddelprofesorsobreelalcance: “Hay varios detalles que estoy omitiendo… De hecho, hago un curso
entero de esto, pero estoy omitiendo los detalles más matemáticos finos.”
8.5Transformersyelmecanismodeatención(slides32a35)—Esencial
�� � �8.5.1Labromainicialylaaclaración
Elprofesormuestrasu álbumdeláminasdelosTransformers (losdibujosanimados)decuandoeraniño,editado
porTelevisiónNacionaldeChile .
Unestudianteinterviene: “¿esto no tiene que ver con GPT? Porque me acuerdo de que GPT es Generative Pre-trained
Transformer.”
�� � �Respuesta: “Tiene mucho que ver con eso. GPT es un Transformer. ”
������Valelapenaretenereldesglosedelasigla: GPT=GenerativePre-trainedTransformer .
14

## Lamina 15

8.5.2ElbenchmarkGLUE(slide33)—Importante
Asícomohubounarevoluciónenimágenes, tambiénhubounarevoluciónenelprocesamientodelenguaje
natural(NLP).Eldesafíodereferenciafue GLUE:
GeneralLanguageUnderstandingEvaluation(GLUE) constade: -Unpuntodereferenciade nueve
tareasdecomprensióndellenguaje ,basadasenoracionesoparesdeoraciones,construidassobre
conjuntosdedatosexistentesseleccionadosparacubrirunaampliagamadetamaños,génerostextuales
ygradosdedificultad. -Un conjuntodedatosdediagnóstico paraevaluarelrendimientodelmodelo
frenteaunaampliagamadefenómenoslingüísticos. -Una tabladeclasificaciónpública yunpanel
paravisualizarelrendimientoenelconjuntodediagnóstico.
�� � �Lógicadelbenchmark,explicadaenclase: “Si algún algoritmo resuelve estas nueve tareas, entonces quiere
decir que está entendiendo lo que está ocurriendo.” �� � �Ejemplosdetareasmencionados: traducción,análisisde
sentimientos,generacióndetexto.
8.5.3 ������LatabladeresultadosenGLUE(slide34)—datoduro
Modelo Año GLUE
Pre-OpenAISOTA — 74%
OpenAIGPT 2017 75,1%
BERT 2018 82,1%
RoBERTa 2019 88,5%
XLNet 2019 88,4%
ALBERT 2019 89,4%
ELECTRA 2020 85,1%
�� � �Lecturahechaenclase: -GPTsubeapenas 1punto sobreelestadodelarteprevio. - BERTproduceelsalto
grande: ~7puntos(75→82). -RoBERTaagrega ~6puntos más. -Después “ahí como que se mantuvo estable” . -
�� � �Semencionatambiénotrodesafío, SQuAD,dondesepasódelordendel 70%(erapre-OpenAI)alordendel
90%. -�� � �ElañodelquiebreenNLPes2018–2019 (compárese: envisiónfue 2012).
8.5.4 ������ Attention is all you need (2017)—Esencial
�� � �“El año 2017 se publicó un artículo científico que se llamaba Attention is all you need . Lo que decía
es que había un mecanismo que ya conocíamos —creo que se inventó como en el 2014 o 2015— que se
llamaba el mecanismo de atención , y lo que estos investigadores hicieron fue decir: no necesitamos
nada más que atención , solo mecanismo de atención.”
Transformer:modeloqueusa únicamentemecanismosdeatención .
�� � �Comentariodelprofesor: “es súper obvio y súper simple hoy día, pero no era tan obvio y simple antes del 2017 ”.
8.5.5 ������Elmecanismodeatenciónexplicado(slide35)—Esencial
Elproblemaqueresuelve: representacionescontextuales
Oracióndetrabajo(ladelaslide): “Elperrocafésepusofelizymeladró”
• Cadapalabrasetransformaenun vector(x⁽¹⁾…x⁽ᴺ⁾).
• ������Loquequeremosesqueelvectorresultante(h⁽¹⁾…h⁽ᴺ⁾)representelapalabra dentrodesucontexto ,no
deformaaislada.
�� � �Intuicióndadaenclase: “si yo solo veo ‘y me ladró’, contextualmente yo diría: en alguna parte estamos hablando
de un perro, seguramente. O de alguna persona muy malhumorada, podría ser.”
15

## Lamina 16

������Cómofunciona
Pararepresentarunapalabra,elmodelogeneraun vectordeatenciónα⁽ᵗ⁾ queindica quéporcentaje
delaatenciónhayqueprestarleacadaunadelasotraspalabras delasecuencia.
Vectordeatencióndelaslide35 (pararepresentarlapalabra “ladró”):
El perro café se puso feliz y me ladró
0.0 0.3 0.1 0.0 0.0 0.3 0.0 0.0 0.3
Esdecir: pararepresentar ladróencontextosepresta 30%deatencióna“perro” ,30%a“feliz” ,30%alapropia
palabra“ladró” y10%a“café” .
�� � �“Si yo quiero aprender ‘ladró’, yo tengo que prestar atención a la palabra ‘perro’ y a la palabra ‘feliz’.”
������ �� � �¿Dedóndesalenlosα? (preguntadeestudiante—respuestamuyexaminable)
Pregunta: “¿Cómo sabe qué porcentaje asignarle a cada palabra?”
Respuesta,endosniveles:
1. Nivelgeneral: “Esto es una red neuronal. Tiene una red neuronal por detrás que genera este vector; hay una
red neuronal aparte que genera este α .”
2. Niveldeimplementaciónactual: “Depende de cómo está implementado, esa es la verdad. Pero hoy en día
lo que se hace es: tomo la representación de cada una de las palabras, que es un vector, y calculo las
correlaciones entre esas palabras. Por ejemplo, ‘perro’ debe estar muy correlacionado con ‘ladró’; y entonces,
como la correlación es alta, tengo que prestar harta atención a ‘perro’.”
Procedimientocompleto(reconstruidodeldiálogo): 1. Calcularlacorrelacióndelapalabraobjetivocon todas
laspalabrasdelaoración: (ladró,ladró),(ladró,me),(ladró,y),(ladró,feliz),(ladró,puso),(ladró,se),(ladró,café),…2.
������Lacorrelación consigomisma eslamásalta(≈1)— “sí, usa la misma palabra, y generalmente ahí es donde está
la correlación más alta”. 3. Otraspalabrasdanvaloresmenores(elprofesorejemplificacon0,9). 4. ������Normalizar
elvector “para que te quede un vector que sume uno, para que sean porcentajes” .
�� � �Honestidadsobrelosnúmeros: antelaobservacióndeunaestudiante(Priscila)deque“feliz”parecetener
demasiadaatención,elprofesorrespondeque “son números que yo puse como para ilustrar el tema, pero en realidad
a lo mejor ‘feliz’ no debiese ser tan alta la correlación con ‘ladró’ ” . �� � �Losvaloresdelaslide35sonilustrativos,no
medidos.
������������Laconsecuenciadecisiva: PARALELIZACIÓN
�� � �“La gracia de estos modelos es que se pueden entrenar en paralelo , porque cada una de estas
representaciones se puede entrenar independiente del resto de las representaciones. Yo podría ajustar la
función de costo para ‘ladró’ independiente de la función de costo para ‘perro’. Entonces es altamente
paralelizable, y eso quiere decir que yo puedo ponerle muchos, muchos datos … puedo entrenar con
muchos más datos de lo que se podía antes por limitaciones de hardware .”
������Estaeslarespuestaa“¿porquélostransformerscambiarontodo?”. Noessoloquelaatención
capturemejorelcontexto: esque esparalelizable,ylaparalelizaciónpermitióescalarlosdatosyel
cómputo. EsexactamentelamismalógicaquelasGPUsen2012— elcuellodebotellasiemprefueel
hardware.
16

## Lamina 17

8.6Modelosfundacionales,BERTygeneracióndetexto(slides36a41)—
Esencial
8.6.1 ������Modelosfundacionales(slide36)—definiciónliteral
Losmodelosfundacionales(BERT,GPT-3,CLIP,Codex)sonmodelosentrenadosconmuchosdatos
demodoquepuedanadaptarseaunaampliagamadetareasposteriores.
(La slide cita: Devlin et al., “BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding”, 2019,
NAACL-HLT, y la referencia al Center for Research on Foundation Models de Stanford.)
8.6.2BERT(slides37y38)—Esencial
�� � �Datosdecontextodadosenclase: - DesarrolladoporGoogle. - “Fue como el primero que levantó la barra
del procesamiento de lenguaje natural.” - �� � �El paper fue publicado en 2019, pero ganó los desafíos más
importantesdelenguajenaturalen2018. - �� � �Digresiónmenor: elnombrevienedelpersonaje Beto/Bertde
PlazaSésamo (hubounpequeñoidayvueltaenclasesobresieradePlazaSésamoodelosMuppets;seconcluyó
quesí,esdePlazaSésamo).
������MaskedLanguageModel(MLM)—slide38
Arquitectura: laspalabrasentranaun TransformerEncoder.
Procedimiento: 1. Setomaunasecuencia—enlaslide,eninglés: “The brown dog became happy and barked at
me”. 2. Seenmascaranalgunaspalabras(enlaslide: brownybarked→MASK). “El modelo no las va a ver.” 3. El
modelodebe predecirlapalabraenmascarada medianteuna predicciónsoftmax.
������BERTenmascaraalazarun15%delostokensdecadasecuencia. (cifra literal de la slide 38)
�� � �Observaciónconceptualclave: “se transforma en un problema de clasificación , porque tengo que clasificar,
con este vector, y encontrar la palabra que estoy escondiendo” .
�� � �������Conexióndirectaconlaclase7: predecirunapalabra enmascarada esclasificación — la etiquetaes
categórica(cuálpalabradelvocabulario). Todoloaprendidosobreclasificaciónsigueaplicando.
8.6.3 ������������DeBERTalosLLM:elsaltológico(slides39y40)—elpuntomáselegantede
laclase
�� � �“Si ustedes lo piensan: si yo puedo enmascarar una palabra, entonces puedo enmascarar la
última palabra. Enmascaro la última palabra y trato de predecir esa palabra. Si el modelo funciona para
reconocer palabras enmascaradas, entonces puedo enmascarar la última, y esto quiere decir que yo
puedo generar siempre una siguiente palabra .”
Ejemplodesarrollado(slides39–40): -Entrada: “The brown dog became happy and barked at” +MASK-Elmodelo
generaautomáticamentelasiguientepalabra: “me”- �� � �“Y entonces ahora, si yo tengo esa siguiente palabra, puedo
buscar la siguiente palabra, y después puedo buscar la siguiente, y entonces el modelo empieza a generar texto .”
Auto-RegressiveGenerativeTransformer: transformerquegeneratextoprediciendorepetidamente
lasiguientepalabraapartirdetodoloanterior. �� � �“Y como va a generar texto, se llama un modelo
generativo.”
������Cadenalógicacompleta—memorizarestasecuencia
Mecanismo de atención → representación CONTEXTUAL de cada palabra
↓ (paralelizable ⇒ escalable a muchísimos datos)
Transformer (Attention is all you need, 2017)
↓
BERT: enmascarar el 15% al azar y predecirlo (Masked Language Model)
↓ ¿y si enmascaro SIEMPRE la ÚLTIMA palabra?
17

## Lamina 18

Transformer autorregresivo generativo
↓ a gran escala (miles de millones de parámetros)
LLM → ChatGPT, LLaMA, PaLM 2, Gemini
8.6.4 ������Quées(yquénoes)unLLM(slide41)
�� � �“Los grandes modelos de lenguaje, que por su traducción en inglés es Large Language Models , se
les llama LLM, son simplemente modelos que predicen la siguiente palabra . Y son large porque son
grandes, o sea, tienen miles de millones de parámetros. Son como esta red neuronal que yo les mostré —y
les mostré una con dos parámetros—; estos tienen miles de millones de parámetros. Son gigantes, son
unos monstruos. Y todo basado en mecanismos de atención.”
Modelosmostradosenlaslide41: ChatGPT,MetaAI LLaMA,PaLM2,Gemini. �� � �Comentario: “PaLM 2 era una
anteriormente, antiguo, y ya no existe” .
Ejemplodelaslide: elprofesorpide “Por favor saluda a los alumnos de Ingeniería Informática de la Universidad
de Concepción” yChatGPTrespondeconunsaludo;luegopide “hazlo en tono romántico” yelmodeloreescribe
elsaludoenregistropoético. �� � �Ilustraqueel mismomecanismodeprediccióndelasiguientepalabraproduce
estilosdistintos segúnelprompt.
������8.6.5 �� � �GPT≠ChatGPTylostokensespeciales—Esencial,yNOestáenlasslides
Estasecciónescompletamente �� � �ycontienedosdelasdistincionesmásimportantesdelaclase.
������Distinción1: GPTvs.ChatGPT
�� � �“GPT no es lo mismo que ChatGPT. GPT es el modelo de lenguaje. ChatGPT es la herramienta ,
que hoy en día es un sistema multiagente .”
������Distinción2: quépasarealmentecuandoaprietasEnter
�� � �“Cuando ustedes escriben esto y aprietan Enter, lo que pasa es que activa el modelo por detrás y el
modelo empieza a generar texto, no más . Entonces leyó esto y dijo: ‘ya, tengo que generar la siguiente
palabra: Hola. Ahora genere ’Hola’, tengo que generar la siguiente: ‘estudiantes’…’ Y va generando,
generando, generando.”
������Eltokendedetención
�� � �“Y en algún momento genera una palabra especial que no te la muestra a ti, que dice ‘detente’ .
Y cuando genera esa palabra ‘detente’, el sistema se detiene y te toca a ti, al humano .”
�� � �������Implicanciaconceptualfuerte: elmodelo no“sabe”queterminóderesponder . Elturnodeconversación
essimplemente otrotokenmás queaprendióagenerar. Todo—incluidoelritmodeldiálogo—esprediccióndela
siguientepalabra.
������Tokensespecialesqueactivanherramientas
�� � �“Hoy en día ChatGPT tiene muchas palabras especiales para hacer distintas cosas. Por ejemplo, cuando
tú le dices ‘genera una imagen de no sé qué’, el modelo por detrás empieza a generar texto y de repente
dice ‘tengo que generar una imagen de no sé qué, bla bla bla’, y genera un token especial, una palabra
especial, que activa el modelo de generación de imagen .”
�� � �Estemecanismoes exactamenteelqueseformalizadespuésen§8.9como usodeherramientasporpartede
losagentes. Elprofesorloplantaaquíylocosecha20minutosmástarde.
�� � �8.6.6Porquélostokenssoncaros—discusiónextensa—Importante
Largadiscusióniniciadaporunestudiante(Cristóbal): “¿por qué nos parece cómodo adoptar esta tecnología y no
otros modelos? ¿Qué hace que el modelo sea cada vez más ineficiente en cuanto a arquitectura?”
18

## Lamina 19

������Respuesta: elcostoestáenlaINFERENCIA,nosoloenelentrenamiento
Fase Costo Explicacióndelprofesor
Entrenamiento Altísimo,pero unavez �� � �“Fueron ajustados básicamente
con todo el texto que la
humanidad ha generado . Eso tiene
un costo computacional altísimo.”
Inferencia Altoy permanente ������ �� � �“Cada vez que tú generas
una palabra, se hace un forward .
Y como son miles de millones de
parámetros y hay millones de
personas accediendo a estos modelos
en tiempo real, entonces tienes que
usar computadores gigantes.”
������Puntoexaminable: “la inferencia es lo caro. Hacer el forward es caro. ” Cadatokengenerado=
unforwardpasscompletopormilesdemillonesdeparámetros.
�� � �Elcuellodebotellaespecíficoeselanchodebanda: “El problema es el bandwidth. Se demora muchísimo en
hacer la inferencia, porque son miles de millones de parámetros, tienen que pasar por muchas capas una tras otra.”
�� � �Qué estamos pagando realmente:“Lo que nosotros estamos pagando es por el uso de los computadores,
de la infraestructura computacional.” Y: “es más que un computador; está todo distribuido, es una arquitectura
computacional súper compleja”.
�� � �Relaciónconelconsumodeagua: “eso es lo que, entre comillas, se dice que gasta agua, porque es básicamente
un supercomputador que está corriendo a todo dar.”
�� � �Elmodelodenegocioactual—muycitable
�� � �“Actualmente tú pagas menos del costo de lo que usas. … Si tú usas todos esos tokens, estás
pagando mucho menos que lo que cuestan esos tokens. Entonces, básicamente, las empresas hoy día
nos están subsidiando a nosotros . Están en una carrera y quieren tener la mayor cantidad de usuarios, y
una vez que tengan los usuarios bien amarrados, les pueden subir los costos . Entonces, se espera
que esto siga subiendo, y va a seguir subiendo.”
�� � �Puntodecomparacióndado: unasuscripcióndelordende 20a100dólaresmensuales frenteacomputadores
lanzadospor NVIDIAparacorrerunLLMgrandelocalmente,delordende 200.000dólares.
�� � �Digresiónsobredatosyprivacidad
Unestudianteplanteaquelasconversacionesdelosusuariosalimentanelentrenamiento(citandonoticiassobre
Meta y el cifrado de sus aplicaciones), y pregunta si eso no debería retribuir al usuario. El profesormatiza el
supuestotécnico: loqueelusuariohaceprincipalmentealconversares inferencia,noentrenamiento— “estos
modelos se entrenan previamente, en otra línea” —ylainferenciaesjustamentelapartecara. Ladiscusiónregulatoria
seretomaen§8.11.
�� � �8.6.7Destilacióndemodelos—Complementario
Pregunta(Cristóbal): sielhardwareestancostoso, “¿por qué no hacer minimalistas estos hardware?”
Respuesta:- �� � �“Hay una línea de investigación importante en generar modelos de este estilo que usen menos
recursos, que sean más livianos. No es fácil.” - ������ �� � �Destilación(definicióndadaenclase): “tú tienes un modelo
más pequeño que le enseñas desde un modelo grande … trata de que el modelo pequeño vaya aprendiendo desde
lo que el modelo grande le va enseñando” . Todaslasempresaslohacen. - �� � �Evaluaciónhonesta: “No funciona
tan bien, esa es la verdad. No se ha llegado al nivel del funcionamiento de los modelos que tienen por detrás OpenAI
o Anthropic.” - �� � �Evidenciacotidiana: enClaudeoChatGPTunopuedeelegirunmodelomásgrandeomás
pequeño; “los modelos pequeños generalmente funcionan peor, pero son más rápidos y ocupan menos tokens ,
19

## Lamina 20

entonces son más baratos”. -�� � �Analogíavalidada (aportadaporelestudiante): uncamióntolvaquecargamucho
peroconsumetodoelcombustible,versusvehículospequeñosqueaceleranigualperollevanmenoscapacidad. El
profesorprecisa: “la capacidad es cuánta información guarda el modelo ”.
8.7 IA generativa de imágenes: modelos de difusión (slides 42 a 44) —
Esencial
�� � �Enlaceconloanterior: “denante yo les dije: si tú escribes en ChatGPT ‘genera una imagen de no sé qué’ y aprietas
Enter, lo que ocurre es que va a llamar a un generador de imágenes. Los generadores de imágenes funcionan con
modelos de difusión. ”
8.7.1 ������Losdosprocesos(slide42)—definiciónliteral
DenoisingDiffusionModels—dosprocesos: -Procesodedifusiónhaciaadelante: añaderuido
gradualmentealaentrada. - Procesodeeliminaciónderuidoinverso: aprendeagenerardatos
mediantelaeliminaciónderuido.
Lafiguradelaslide muestralasecuenciadeungato: Data→(forwarddiffusionprocess,fixed)→Noise ,y
debajolaflechainversa: Reversedenoisingprocess(generative) .
8.7.2 ������Elmecanismoexplicadoenclase—Esencial
Paso1—Procesohaciaadelante(norequiereredneuronal): > �� � �“Tomo los datos, que por ejemplo es un gato,
y le empiezo a agregar ruido de a poquito . Hago un proceso de difusión hacia adelante donde voy agregándole
cada vez más ruido, y en algún momento la imagen es puro ruido . Yo no distingo al gato en esta imagen.”
�� � �Detalleexplícito: “hago una red… o ni siquiera hago una red neuronal ”—elprocesodeagregarruidoes fijo,
noaprendido(coherenteconel“(fixed)”delaslide).
Paso2—Procesoinverso(aquísíhayredneuronal): > �� � �“Entreno una red neuronal que es capaz de, desde el
ruido, empezar a obtener de a poco la imagen . Es el proceso inverso, de denoising, de eliminar el ruido.”
Paso3— ������Eltrucogenerativo: > �� � �“Si yo tengo una red neuronal que entreno para, desde el ruido, recuperar
una imagen de un gato, entonces después yo puedo olvidarme de la parte de arriba y solo usar la parte de abajo :
le paso una imagen de ruido cualquiera y me va a generar un gato .”
�� � �Aclaraciónaunapreguntadeestudiante (quepreguntósielcontrolerapíxelapíxel): > “No es píxel a píxel.
Es toda la imagen de ruido… Si logro hacer una red neuronal que tome una imagen con ruido y vaya de a poquito
sacándole el ruido y generando un gato, entonces puedo pasarle cualquier tipo de máscara de ruido y va a generar
distintos gatos dependiendo de cuánto ruido o de qué ruido específico yo le pase.”
������Ideacentral: elruidodeentradaeslafuentedelavariedad. Distintoruido ⇒distintogato. El
modelonomemorizaunaimagen;aprendea revertirelprocesodedestrucción.
�� � �Nombreconcretomencionado: “¿no sé si a ustedes les suena Stable Diffusion? Esto es Stable Diffusion.”
�� � �8.7.3Digresiónvalidada: denoisingdeaudio—Complementario
Preguntadeunaestudiante(Priscila)sobresiestoseparecealtrabajoconaudioparapersonasconpérdidaauditiva.
Respuestadelprofesor (seconservasololapartetécnicarelevante): -Elcasoeselde denoisingdeaudio . -Si
unaudífonosimplementetomaraelaudioyloreprodujeramásfuerte, “te va a subir el volumen de todo el ruido
ambiente y del ruido del audífono mismo” . -������ “Entonces, en general, lo que uno hace con el audio también es que
hace un proceso de denoising , donde… uno podría hacer una red neuronal que tome el audio con ruido y te lo
transforme en audio sin ruido .”
�� � �Muestraque denoisingesunatécnicageneral ,noexclusivadeimágenes.
20

## Lamina 21

8.7.4 �� �LatentSpaceDiffusion(slide43)—Importante
�� � �“En la práctica es un poco más complejo que esto.”
Procedimiento(explicado“engrandespalabras”):
1. Setomalaimagen xysegeneraunarepresentacióndelaimagenenunvector (z)medianteunared
neuronal—el codificador(Encoder, ℰ). �� � �“Esta representación se supone que tiene toda la información
necesaria para entender la imagen.”
2. ������Elprocesodedifusiónsehacesobrelarepresentación,NOsobrelaimagenmisma. Seleagrega
ruidoa zhastallegara z_T(representaciónruidosa).
3. Sehaceel procesoinverso desdelarepresentaciónruidosa.
4. Finalmentesepasaporun Decoder( 𝒟)que “desde esta representación me lo transforma en una imagen real”
(x̃).
(La figura de la slide, tomada de Rombach et al., muestra los bloques Pixel Space / Latent Space / Conditioning, la
Denoising U-Net y los bloques de cross-attention Q/K/V.)
8.7.5 ������Condicionamiento: detextoaimagen—Esencial
Preguntaimplícita: cuandoledigoaChatGPT “genérame una imagen de un perrito bailando” ,¿cómopasadel
textoalaimagen?
�� � �“La respuesta es que lo que se hace se llama condicionar. Tomas el texto y lo pasas por otro
codificador —muy parecido al transformer que vimos antes— y te genera un vector . Y después ese
vector entra en el decodificador , y de esa forma condicionamos sobre el texto que escribimos.”
������Enlaslide43estocorrespondealbloque Conditioning,queadmiteSemanticMap, Text,Representationse
Images.
������Condicionartambiénsobreunaimagendeentrada
�� � �“La diferencia es que acá yo estoy condicionando sobre la imagen de entrada también , no solo sobre
el texto. Entonces… tengo también una imagen que entra por el codificador, y de esa forma te genera la
imagen parecida.”
�� � �Ejemploculturalmencionado: elfenómenode “ghiblificar”fotospersonales— “yo creo que ya no está tan de
moda como estuvo el año pasado” . Eseesexactamenteelcasode condicionarsobretexto+imagen .
8.7.6Herramientasyriesgosocial(slide44)—Complementario
Herramientasmostradas: DALL·E2 (OpenAI)y stability.ai.
Ejemplosdelaslide: imágenessintéticasde DonaldTrumpsiendodetenidoporlapolicía ydel Papaconuna
parkablanca,másunpardefotosfamiliares“ghiblificadas”.
�� � �Elprofesorlaspresentacomoejemplosdeloquehoysepuedepedir: “dame una imagen de Donald Trump
siendo llevado por la policía, o dame una imagen del Papa” . �� � �Aunquenosedesarrollacomoseccióndeética, el
ejemploelegidoesdeliberadamenteeldeimágenesfalsasdefiguraspúblicas ,yconectaconladiscusiónde
riesgosde§8.10.
8.8LLMs: capacidadesylimitaciones(slide45)—Esencial
Estaláminaes labisagradelaclase : enumeralaslimitacionesquejustificanlaexistenciadelosagentes.
21

## Lamina 22

8.8.1 ������Contenidoliteraldelaslide45
LLMs: -Tienen billonesdeparámetros queajustar- GPT-3tiene175Bdeparámetros- Llama-2tiene
versionesde 7B,13By70B -Estoquieredecirquenecesitan muchosdatosypoderdecómputo
paraentrenarse-Son muybuenos como: -Asistentede escritura-Asistentede codeo-Son muy
malospara: -Obtenerrespuestasbasadasenhechos(alucinan) -Usarinformaciónposteriorasu
entrenamiento-Razonaryplanificar -Simplementeimitanasusconjuntosdeentrenamiento
�� �Notadeprecisiónnumérica(importanteparanoequivocarseenunaprueba). Tantolaslide
comoelprofesorusan“billones”comocalcodelinglés billions. Enespañol,175B=175milmillones=
175×10⁹ ,no175billones(10¹²). Lomismopara7B/13B/70BdeLlama-2. Sienunapruebahayque
escribirlacifra,loseguroesusarlanotación 175Bo175×10⁹ .
8.8.2 ������Lascuatrolimitaciones,explicadasenclase
Limitación �� � �Explicacióndadaenclase
Alucinan “Inventan cosas. Tú le preguntas a una LLM ‘cómo va a
estar el clima mañana’ y no tiene forma de saber cómo
va a estar el clima mañana. Entonces te va a inventar
algo: te va a generar una palabra, otra, y te va a inventar
cosas.”
Nousaninformaciónposteriorasuentrenamiento Elconocimientoquedacongeladoenlafechadecorte
delentrenamiento
Norazonanniplanifican “No razonan por sí mismas ni planifican por sí
mismas.”
Imitansuconjuntodeentrenamiento ������ “Están entrenadas simplemente a generar datos,
generar palabras que sigan la distribución de las
palabras que nosotros como humanidad hemos
creado.”
������El“porqué”delaalucinación,enunafrase: unLLMestáoptimizadoparaproducirtexto plausible
(que siga la distribución del lenguaje humano),no texto verdadero. La verdad no es parte de su
funcióndecosto. Poresoalucinarnoesunbugocasionalsinounaconsecuenciadirectadelobjetivode
entrenamiento.
�� � �8.8.3Lapreguntaqueabrelaseccióndeagentes
Pregunta(Germán): “¿Qué ocurre en el caso de que hay cierta gente que usa bases de datos vectoriales para
buscar información contextual, cuando le pones por ejemplo un libro de cientos de miles de palabras y busca algo ahí?”
Respuesta: “Lo que pasa es que estoy hablando de la LLM, no estoy hablando de los agentes . Ahora voy a hablar
de los agentes.”
������Distincióncríticaquehayquetenerclarísima: todaslaslimitacionesdelaslide45sonlimitaciones
delLLMdesnudo . Losagentesexistenprecisamentepara superarlas. Confundirambosnivelesesel
errorconceptualmásprobabledeestaclase.
8.9Agentes(slides46a48)—Esencial
8.9.1 ������Definición: contenidoliteraldelaslide46
Agentes: -Unagentepuederealizar accionesautónomassinintervenciónhumanaconstante . -
Puedecontarconun humanoenelproceso paramantenerelcontrol. -Losagentestienen memoria
para almacenar preferencias individuales y permitir la personalización. También puede almacenar
22

## Lamina 23

conocimiento. -UnLLMpuedeencargarsedel procesamientodeinformaciónylatomadedecisiones .
-Losagentesdebensercapacesde percibiryprocesarlainformacióndisponibleensuentorno . -
Losagentestambiénpueden usarherramientas comoaccederainternet,usarintérpretesdecódigoy
realizarllamadasAPI.-Losagentestambiénpueden colaborarconotrosagentesoconhumanos .
8.9.2 ������Loscomponentesdeunagente(slide47)—memorizareldiagrama
Eldiagramadelaláminaessimpleymuyexaminable:
MEMORY ─┐
TOOLS ─┼──► AGENT ──► ACTIONS ──► ENVIRONMENT
GOALS ─┘ ▲ │
└────── OBSERVATIONS ◄────┘
Componente Rol
Memory(memoria) Preferencias,personalización,conocimientoacumulado
Tools(herramientas) APIs,internet,intérpretesdecódigo,basesdedatos,
otrosagentes
Goals(objetivos) �� � �“tienen los objetivos súper claros”
Actions→Environment Elagente actúasobreelentorno
Observations Elagente percibeelresultadoyrealimentaelciclo
�� � �Yenelcentro,lapiezaquefaltaba: “el agente tiene por detrás, o dentro del agente, acceso a una LLM que
genera texto”.
������Ecuaciónmentaldelagente: AGENTE=LLM+MEMORIA+HERRAMIENTAS+OBJETIVOS+
PERCEPCIÓNDELENTORNO
Ynótesequeelciclo Actions→Environment→Observations→Agent esexactamenteladefinición
deIAdela slide4: unsistemaque razona(elLLM)y actúa(modificaelentorno).
8.9.3 ������ �� � �Cómofuncionaunagentepordentro—Esencial,noestáenlasslides
Todoestemecanismoes �� � �yeslapartemásvaliosadelasección.
Paso1: lasinstrucciones
�� � �“Cuando tú construyes un agente… le das las instrucciones : ‘tú eres un agente que hace tal y tal
cosa, y te gusta tal y tal otra, y eres especialista en esto, y responde de cierta forma’. Entonces tú le das
instrucciones y por detrás la LLM toma eso y lo entiende y dice: ‘ah, ahora yo tengo que comportarme
de esta forma’.”
Paso2: declararlelasherramientas
�� � �“Al agente tú le dices: ‘ tienes acceso a estas herramientas , tienes acceso a esta API para ver el
clima, tienes acceso a esta app que se conecta con otro agente’ —y este otro agente lo que hace es generar
imágenes, por ejemplo—. Entonces el agente dice: ‘ah, yo sé que si necesito generar una imagen tengo
que llamar al otro agente para que genere la imagen’.”
������Paso3: elciclodeejecución—elmecanismoclave
�� � �“Los agentes empiezan a funcionar a través de la LLM: empiezan a generar el siguiente token, la
siguiente palabra . Y en algún momento dicen: ‘oh, tengo que llamar a esta herramienta ’. Tengo
acceso a la herramienta, y generan una palabra especial con la cual se conectan a la herramienta ,
ejecutan la herramienta, después le devuelven, y el agente recibe la respuesta de la herramienta y dice:
‘oh, la herramienta me respondió esto’. Y de nuevo siguen prediciendo la siguiente palabra, y la siguiente
palabra.”
23

## Lamina 24

Ciclo,esquematizado:
1. El LLM genera tokens normalmente
2. En algún punto genera un TOKEN ESPECIAL que invoca una herramienta
3. Se ejecuta la herramienta (API, búsqueda, código, otro agente…)
4. El RESULTADO de la herramienta vuelve al agente como texto
5. El agente continúa generando la siguiente palabra, ahora con esa información
6. → volver a 1 hasta generar el token de "detente"
������Estocierraelcírculocon§8.6.5. El“token especial que activa el generador de imágenes” que
elprofesormencionóalhablardeChatGPT esexactamenteestemecanismo . Todo—incluidousar
herramientas—siguesiendo generarlasiguientepalabra .
������Ejemplodesarrollado: búsquedaenundocumento(respondelapreguntadeGermán)
�� � �“De repente tú podrías decir: ‘ah, el usuario me pasó este documento’. Entonces yo lo que puedo hacer
ahora es ir a buscar al documento, y entonces activa la herramienta de búsqueda del documento y va y
hace búsqueda por similitud dentro del documento , vuelve, te retorna y dice: ‘en el documento dice…’ ”
�� � �������Estoesloquerespondelalimitación“nousaninformaciónposteriorasuentrenamiento” : elagente
nosabe elcontenidodeldocumento,pero tieneunaherramientaparairabuscarlo . (Eselmecanismodetrásde
lasbasesdedatosvectorialesquemencionabaelestudiante.)
8.9.4Ejemplosdeagentes(slide48)—Importante
Contenidoliteraldelalámina,conlosagregadosdeclase:
Tipodeagente Descripción(slide) �� � �Agregadoenclase
Agentesdemonitoreoy
mantenimiento
Supervisansensores,cámarasy
maquinariaparadetectar
anomalías,riesgosyfallas en
tiemporeal
Existenagentesdevisión quevena
travésdeunacámaray leretornan
alagenteprincipalentexto loque
vieron
Agentesoperacionales Coordinanproducción,logística,
inventarioyprocesosindustriales
usandodatosysistemas
empresariales
—
Agentesdeanálisisdocumentaly
reportes
Generanyresumen informes
técnicos,médicos(porejemplo
radiológicos),operacionalesyde
mantenimiento
“Tú tienes un agente especializado
que toma el informe, lo vectoriza, y
después te va retornando el resumen”
Agentesdeasistenciaysoporte
inteligente
Ayudanaoperadoresyequipos
técnicosconsultandomanuales,
diagnosticandoproblemasy
recomendandoacciones
“El agente va monitoreando lo que tú
estás haciendo… y te va dando
recomendaciones”
������Nóteseelpatróndelagentedevisión: multimodalidadimplementadapordelegación . Elagenteprincipal
siguetrabajandosolocontexto;otroagentetraducelaimagenatexto.
������8.9.5 �� � �Multiagentes,alucinaciónyresponsabilidad—Esencialymuycitable
Surgedeunapreguntasobresielhumanoenelloopencarecelaoperaciónysilacomunicaciónagente-agente
seríamáseficiente.
������Laarquitecturadeverificaciónmultiagente
�� � �“Hay que tener siempre presente que la LLM tiende a alucinar . Lo que generalmente se hace cuando
uno genera sistemas multiagentes en funciones críticas es que generas varios agentes y haces que un
24

## Lamina 25

agente realice la tarea y le reporte a otro agente ; este agente se encarga de asegurarse de que hizo
la tarea que tenía que hacer y da el check . Si el agente realiza la tarea, le retorna el check, este agente
va y retorna al agente principal. El agente principal generalmente tiene un auditor , que es otro agente
que dice: ‘oye, ¿realizaron la tarea?’. Entonces son varios agentes que empiezan a interactuar y de esa
forma van disminuyendo la tasa de alucinación .”
Esquema:
AGENTE PRINCIPAL
├── agente EJECUTOR → realiza la tarea
├── agente VERIFICADOR → confirma que la tarea se hizo (✓ check)
└── agente AUDITOR → verifica al agente principal
������Matizobligatorio: “Pero igual se te puede pasar una alucinación en todo este sistema. ” La
redundanciareducelatasadealucinación; nolaelimina .
������Elargumentodelaresponsabilidad—porquésiguehabiendohumanos
�� � �“Si tú tuvieras un sistema autónomo de multiagentes, ¿quién se hace responsable por las fallas?
Y se te mueren diez personas, ¿quién se hace responsable? ¿El agente? Entonces, siempre los agentes,
generalmente, hasta hoy, son supervisados. Funcionan como un asistente para el humano. ”
������Respuestamodelosipreguntanporquémanteneralhumanoenelloop: haydosrazones
distintasyconvienedarlasdos: (1) técnica—losLLMalucinanyningúnesquemadeverificaciónlo
elimina;(2) deresponsabilidad —unagentenopuedeasumirresponsabilidadlegalniéticaporun
daño. Lasegundanoseresuelveconmejortecnología .
8.10Últimosavances: historia, riesgosyopensource(slides49a55)—
Importante
(La slide 49 abre esta sección del deck con el título interno “2. La revolución de Deep Learning” ; la slide 50 repite el
gráfico de interés de Google Trends.)
8.10.1 ������PremioTuring2018(slide51)
Recipientsofthe2018ACMA.M.TuringAwardforconceptualandengineeringbreakthroughs
thathavemadedeepneuralnetworksacriticalcomponentofcomputing.
Los tres galardonados: Yoshua Bengio, Geoffrey Hintony Yann LeCun. �� � �Nacionalidades mencionadas:
canadiense,canadienseyfrancés . �� � �Elprofesormencionaquetuvolaoportunidaddeconocerpersonalmentea
YannLeCun. �� � �“El premio Turing es como el premio Nobel de la ciencia de la computación.”
������������Lacronologíalargadelasredesneuronales—muyexaminable
�� � �“Las redes neuronales existen desde los años 40; existe el perceptrón. La red neuronal en sí se hizo
súper popular en los años 80 , y después bajó su popularidad. Después se hizo un poco popular en los
90; después nadie las pescó de nuevo. Y de repente, en 2012, todo explotó . Pero esto es trabajo de casi
100 años… como 80 años de trabajo para llegar a lo que tenemos hoy día.”
Época Estado
~1940s Invencióndel perceptrón �� � �“fue inventado incluso
antes de la definición de inteligencia artificial de
Alan Turing, que fue en los años 50”
1980s Primeraugedelasredesneuronales
(fines80s) Caídadepopularidad
25

## Lamina 26

Época Estado
1990s Segundoauge,menor
(2000s) Nuevamenteolvidadas—eslaépocade SVMy
RandomForest (clase7)
2012 Explosióndefinitiva(ImageNet+GPUs)
�� � �Lalecciónqueelprofesorextrae: “Estos tres personajes son los que nunca se dieron por vencidos
con las redes neuronales, aun cuando todos decían ‘no, no sirven para nada’. Ellos tres seguían y seguían
dándole, y gracias a eso se ganaron el premio Turing.”
�� � �������Conexióndirectaconlaclase7: elprofesorhabíasituadoallílasecuenciahistórica SVM (≈2000) → Random
Forest (2000–2010) → redes neuronales. Estaláminaexplica porqué lasredesestuvieronausentesdeeseperiodo:
noerannuevas,estaban desacreditadas.
8.10.2Lacartade2023: pausarlosexperimentosgigantes(slide52)
Laslidereproducematerialde futureoflife.org/open-letter/pause-giant-ai-experimentsycitasde YoshuaBengio
sobreporquécambiódeopinión: porunaaceleración inesperadaqueunañoantesnolohabríallevadoafirmar
unacartaasí,ysobrelanecesidaddeacuerdosinternacionales,comparandoconlaregulaciónglobaldelasarmas
nuclearestraslaSegundaGuerraMundial.
�� � �Resumen en clase:“Bengio mandó una carta donde dijo: tenemos que tener cuidado con esto porque está
acelerando demasiado rápido. Paremos los experimentos con inteligencia artificial y detengámonos como
humanidad a ver qué es lo que se está haciendo, cuáles van a ser las implicancias.”
������ �� � �Loqueefectivamenteocurrió
�� � �“Por supuesto, lo que ocurrió es que OpenAI y Google dijeron: ‘no podemos parar, porque esto
es una carrera’ . Realmente es una carrera; es como la carrera a la luna . Es la carrera por generar la
inteligencia artificial general , así, tratar de hacer inteligencia artificial que reemplace al ser humano.”
�� � �Losriesgossocialesqueelprofesordestaca—Importante
Bengio “decía que tenemos que preocuparnos de que la inteligencia artificial sea benéfica para los seres humanos ”.
Elprofesormencionadosproblemasqueyaseobservan:
1. Elempleo.
2. ������Lapérdidadecapacidadcrítica —desarrolladocondetalle: > �� � �“Hoy en día hay estudios que muestran
que creemos más en la inteligencia artificial que en nosotros mismos . Entonces, si la inteligencia artificial se
equivoca, yo no la corrijo, porque confío en que ella está haciendo bien la pega. Y entonces nosotros perdemos
nuestra capacidad crítica como seres humanos.”
�� � �������Estepuntoconectadirectamentecon§8.11.4yconelcierredelaclase: losagentesdecodificación “varias
veces se equivocan y están convencidos de que no se equivocaron ”.
8.10.3 ������“Wehavenomoat”ylairrupcióndelopensource(slide53)—Importante
Origen: unmemorandofiltradode untrabajadordeGoogle (publicadoporSemiAnalysis)en 2023.
�� � �Explicacióndeltérmino: “We have no moat . Moat es como, en los castillos, esta zanja que hay alrededor de los
castillos”—esdecir, notenemosfosodefensivo . YtampocolotieneOpenAI: “no están protegidos” frentealaIA
quepuedegenerarlapropiasociedad.
Citadelmemorando(slide53): sostienequeniGoogleniOpenAIestánposicionadosparaganaresacarrera,y
quemientrasambosdiscutían, unatercerafacción—elopensource—lesestabacomiendoelalmuerzo .
26

## Lamina 27

������Lacronologíadelopensource(slide53)—memorizarla velocidad,nolasfechasexactas
Fecha(2023) Hito
24feb LLaMAeslanzado(Meta)
3mar The Inevitable Happens: LLaMAsefiltra
12mar Modelosdelenguaje enunaRaspberryPi
13mar Alpaca : fine-tuningenunlaptop
18mar LLaMAcorreenlaCPUdeunMacBook
19mar Unmodelode 13Blogra“paridad”con Bard
25mar Choose Your Own Model (repositoriodemodelos
descargables)
28mar Cerebras : GPT-3opensource
28mar Entrenamientomultimodalenunahora
3abr Humanosreales nodistinguen entreunmodeloabierto
de13ByChatGPT
15abr RLHFopensource anivelesdeChatGPT
�� � �Comentariosdeclase: “Algunos sugieren que lo filtraron para competir contra GPT ”;ysobrelavelocidad:
“desde que se filtró pasó como una semana y ya teníamos el modelo corriendo en una Raspberry Pi” .
������ Lo evaluable aquí no son las fechas, sino la tesis:en menos de dos meses, la comunidad
abiertallevóunmodelofiltradodesdeundatacenterhastaunaRaspberryPiyalcanzóparidadpráctica
conproductoscomerciales. Eselargumentoempíricodeque el“foso”tecnológicodelasgrandes
empresasesmásfrágildeloqueparece .
8.10.4Lalegislaciónvamáslenta(slide54)—Complementario
Laslidereproduceelcomunicadode GOV.UK: “UK to host first global summit on Artificial Intelligence” —laprimera
cumbreglobalsobre seguridaddelaIA (2023).
�� � �Diagnósticodelprofesor: “Los gobiernos están tratando de legislar… pero vamos mucho más lento . Estamos
recién hablando de los datos y tenemos inteligencia artificial que ya pasó por encima de todo el mundo.”
�� � �Ejemplo dado de intervención estatal efectiva: menciona queel gobierno de Estados Unidos hizo que
Anthropicbajaraunmodelo ,yreflexiona: “imagínense que hoy en día una empresa de inteligencia artificial dijera
‘¿saben qué? vamos a matar todos nuestros modelos’ — pega un impacto gigante a la sociedad ”. �� �Este ejemplo
se menciona de pasada, sin fecha ni fuente en las slides; conviene tratarlo como anécdota ilustrativa y no como dato
examinable.
8.10.5 ������������ElAIIndex: desempeñodelaIAvs.elserhumano(slide55)—Esencial
QuéeselAIIndex
�� � �“Es un índice que genera la Universidad de Stanford una vez al año … Son como 100 páginas; no
tienen que leerlas, van a lo que les interese. Básicamente es como un termómetro de la inteligencia
artificial. Les recomiendo que le peguen una leída.”
(La lámina indica: Source: AI Index, 2026 | Chart: 2026 AI Index report , Stanford HAI.)
������Cómoleerelgráfico
• EjeX: año(2012→2025)
• EjeY:desempeñorelativoalalíneabasehumana(%)
• ������Lalíneapunteadaen100%esel“humanbaseline” : porencimadeella,laIA superaalserhumano.
27

## Lamina 28

������Elmomentopedagógicoclavedelaclase
�� � �“Fíjense que algunas ya son superiores al ser humano, como por ejemplo esta de acá, que es clasificación
de imágenes, que es la que yo les había dicho antes. ¿Y se acuerdan qué año había superado al ser
humano?” —Unestudianteresponde“¿el18?” — “No, 2015. Y fíjense que acá está: el 2015 supera al
ser humano.”
�� � �������Eselcierredelarconarrativoabiertoenla§8.1.3. Sihayunafechaquememorizardeestaclase,es2015
paraclasificacióndeimágenes(ImageNet).
������Losbenchmarksdelalámina
Leyendaoficialdelaslide55 (estaeslafuenteautoritativa):
Benchmark Quémide
Imageclassification(ImageNetTop-5) Clasificacióndeimágenes
Englishlanguageunderstanding(SuperGLUE) Comprensióndelinglés
Multitasklanguageunderstanding(MMLU) Comprensióndelenguajemultitarea
PhD-levelsciencequestions(GPQADiamond) Preguntasdecienciadeniveldoctoral
Agentmultimodalcomputeruse(OSWorld) Usodecomputadorporagentes,multimodal
Autonomoussoftwareengineering(SWE-bench
Verified)
Ingenieríadesoftwareautónoma
Visualreasoning(VQA) Razonamientovisual
Medium-levelreadingcomprehension(SQuAD2.0) Comprensiónlectora
Competition-levelmathematics(MATH) Matemáticasdecompetencia
Multimodalunderstandingandreasoning(MMMU) Comprensiónyrazonamientomultimodal
Mathematicalreasoning(AIME) Razonamientomatemático
������Loqueelprofesorafirmósobreelgráfico
Afirmaciónenclase Comentario
2015: clasificacióndeimágenessuperaalhumano ��ConsistenteconlacurvadeImageNetTop-5
2018: comprensióndelecturasuperaalhumano �� � �“ya los modelos de lenguaje entienden mejor el texto
que los seres humanos mismos”
2023: comprensiónmultimodalsuperaalhumano “no solamente hablo de lenguaje, sino de otras
modalidades: a través del lenguaje comprender
imágenes, series de tiempo, cualquier tipo de datos”
2023: preguntasde niveldoctorado “son preguntas que solo si tienes un grado de doctor en
alguna ciencia específica eres capaz de responder… la IA
es capaz de responder mejor que un doctor especialista
en el área”
2025: manejoautónomodeuncomputador llegando
alnivelhumano
“puede abrir Word, escribir un documento, abrir una
planilla Excel, llenar valores, instalar software, conectarte
a internet, configurar la pantalla” —yañadeque “hoy en
día hay artículos que muestran que esto ya se superó”
2025: agentescondatos multimodales,aúnsubiendo “es como que miraran tu cámara y tú le estuvieras
diciendo lo que hagan y se pongan a hacerlo”
�� �Discrepanciaqueconvieneconocer. Aldescribirlasdoscurvasde2025,elprofesorasignó “manejar
uncomputadordeformaautónoma” alacurvacelestey “agentesmultimodales” alaverde; según
laleyendadelaslideesalrevés : laverde/turquesaes Agent multimodal computer use (OSWorld) yla
celestees Autonomous software engineering (SWE-bench Verified). Delmismomodo,losañosexactos
decrucedealgunascurvas(comprensiónlectora, preguntasdedoctorado)sondifícilesdeleercon
precisiónsobreelgráficoproyectado. Recomendacióndeestudio: memorizarlosconceptosyelaño
2015deImageNet;paraelresto,usarlaleyendaoficialynolascifrasdichasalaire.
28

## Lamina 29

�� � �Elcierredelasección
�� � �“Así de rápida es la evolución de esta cuestión. Entonces, en un año más, ¿qué vamos a estar haciendo?
No tengo idea, de verdad que no lo sé. Yo creo que si me preguntaran hace 10 años dónde va a estar la
inteligencia artificial en un año más, yo más o menos la apuntaba. Ahora no la apunto ni por si acaso. ”
8.11ElimpactodelaIAenlaindustria(slides56a64)—Importante
(La slide 56 abre esta sección del deck con el título interno “3. El impacto de la IA en la industria” . Todos los gráficos
provienen del AI Index 2026 de Stanford o de las McKinsey Global Surveys .)
8.11.1 ������AdopcióndeIA(slide57)—eldatomáscitabledelasección
Gráfico: Speed of AI adoption by technology (fuente: TheProjectonWorkforceatHarvard,2025). - EjeX: años
desdelaintroduccióndelprimerproductomasivo- EjeY: tasadeadopción
Tecnología Adopciónalcanzada Encuántosaños
Computadores 69% 22años
Internet 91% (fuenteITU)/76%(fuenteCPS) 25años
IAgenerativa(GenAI) 53% 3años
�� � �Datosadicionalesdadosenclase: loscomputadoresalcanzaron~20%delapoblaciónalos 3años;internet
alcanzó~20%alos 2años.
������Conclusiónqueelprofesorenunciaexplícitamente: laIAgenerativaes “la tecnología que ha
sido absorbida más rápido por la humanidad ”.
�� � �Confirmaciónintuitivaofrecidaalasala: “¿desde cuándo existe ChatGPT? Después de un año desde que existió,
todos estábamos usando ChatGPT. ”
8.11.2 ������InversiónenIA(slide58)
Contenidoliteraldelalámina: >-LainversiónenIAha crecidodeformaexplosivaenlaúltimadécada . >-
LaIApasódeseruna tecnologíaemergente auna prioridadestratégica paraempresaseindustrias. >-En
2025,lainversiónenIAalcanzólos 581,7milmillonesUSD ,principalmentepor inversiónprivada,fusionesy
adquisiciones.
Formadelacurva (gráfico Global corporate investment in AI, 2013–25 ): crecimientosostenidode2013(14,57)a
2021(360,73),unabaja en2022–2023(253,25→201),yluego 2024: 253,02y2025: 581,69.
�� � �Lecturaenclase: “entre 2013 y 2021 hubo un crecimiento gigante, pero después hubo una baja, y después el
2025 creció rápidamente… hoy en día es una tecnología estratégica: todas las empresas quieren tener inteligencia
artificial dentro de su empresa ”.
8.11.3 ������UsodeIAenlaindustria(slides59a61)—cifrasmuypreguntables
Slide59—Cuántoyenquéetapa
Textodelalámina: >-ElusodeIAenempresassiguecreciendorápidamente. >-Sinembargo, lamayoríade
lasorganizacionesaúnseencuentraenetapasdeexperimentaciónopilotos . >-Solocercadeuntercioha
comenzadoaescalar sussolucionesdeIA.
Gráfico(McKinsey): elusodeIAenalmenosunafuncióndenegociopasade 20%(2017) a88%(2025);elusode
IAgenerativa pasade 33%(2023) a79%(2025).
29

## Lamina 30

������FasedeusodelaIAentrelasorganizacionesquelausan(2025)
Fase % Definición(slide)
Fullyscaled 7% LaIAestá completamente
desplegadaeintegrada enla
organización
Scaling 31% Creciendoeldespliegue/adopcióna
lolargodelaorganización
Piloting 30% ImplementandoIAparaun primer
casodeuso
Experimenting 32% Cualquierusoopruebatemprana
������Lalecturaclave(yelcontrastequehayquesaberarticular): 88%delasempresasusaIA,pero
solo7%latienerealmenteenproducciónaescala. �� � �Elprofesorloenfatiza: hayun 31%queestá
tratandodeescalar“peronolologran” .
�� � �Aclaración pedida por un estudiante:“¿‘escalar’ se refiere a crear una herramienta comercial o a usarlo
internamente?” →Respuesta: “Me refiero a usar inteligencia artificial en producción. ”
Slide60—Reduccióndecostos
• Aunque todavía son pocos los casos donde la IA impacta directamente los resultados fi-
nancierosdetodalaempresa ,muchasorganizacionesyareportan reduccióndecostosencasos
deusoespecíficos .
• Losmayoresbeneficios seobservanen ingenieríadesoftware,manufacturaytecnologíasde
lainformación.
(Cifras del gráfico: software engineering 56%, manufacturing 56%, IT 54%, strategy and corporate finance 53%.)
Slide61—Aumentodeingresos
• Losmayoresaumentosdeingresos asociadosalusodeIAseobservanen marketing,ventasy
desarrollodeproductosyservicios .
Función %quereportaalgúnaumentodeingresos
Marketingandsales 67% (43%≤5%,14%entre6–10%,10%>10%)
Strategyandcorporatefinance 65%
Productorservicedevelopment 62%
�� � �Elprofesordesglosaenvozaltaprecisamentelafilademarketingyventas(43/14/10).
������ Contraste conceptual entre las dos láminas — muy examinable: Los ahorros de COSTOS
apareceneningenieríadesoftware,manufacturaeIT.LosaumentosdeINGRESOSaparecenen
marketing,ventasydesarrollodeproductos. Nosonlasmismasáreas,yesaasimetríaeselpuntode
lasdosláminas.
�� � �8.11.4CómoadoptarIAenunaorganización—Importante
Preguntadeunestudiante: ¿pordóndepartir—gobiernodedatos,definicióndeprocesos,odiagnóstico?
������Respuesta1: loprimeroeslaculturaorganizacional
�� � �“Lo más complejo es la cultura organizacional. Entonces eso es lo primero. En general, lo que
ocurre es que alguien toma alguna herramienta de IA y la empieza a usar; después viene otra
persona que la toma y la empieza a usar, y de repente todos empiezan a usarla, pero de manera
no coordinada.”
30

## Lamina 31

������Respuesta2: elproblemaestructuraldelavelocidad
�� � �“Hay que ir actualizándose y capacitándose constantemente . Las empresas de inteligencia artificial
simplemente lanzan los modelos, así como ‘este es el mejor y eso es todo’, y te tratan de explicar más o
menos, pero en la práctica es distinto. Cuando quieres adoptar una nueva tecnología no lo puedes
hacer de un día para otro , tienes que tomarte tu tiempo — y la empresa de inteligencia artificial va
mucho más rápido .”
������Respuesta3: prácticasconcretasquelehanfuncionado
Elprofesoradviertequeélmismo “también se ha sobrepasado un poco con todo esto” ,yofrecedosprácticas:
1. ������Compartirlosprompts/archivosdeconfiguracióndentrodelosrepositorios —mencionaexplícita-
mentelosarchivos CLAUDE.mdcompartidosenelrepositorio ,demodoquecualquieraseconecteytrabaje
conelmismocontexto.
2. ������Trabajarenparejas (pair programming): “que te vayas a trabajar con la otra persona al lado e ir codeando
en conjunto”.
�� � �Larazón,dichaenunaimagenmemorable: “para que el producto no se empiece a transformar
en un monstruo de mil cabezas ”.
�� � �Elproblemadefondoqueestoresuelve: “la IA hoy en día se usa mucho por como cada persona la usa
individualmente. Cuando tú quieres usarlo a nivel de organización, necesitas acceder, entre comillas, a la misma
inteligencia artificial de tus colegas… para después hacer el merge, juntar todo en una misma rama.”
8.11.5Elmercadolaboral(slide62)—Complementario
Gráfico: AI job postings (% of all job postings) by select geographic areas, 2014–25 (fuente: Lightcast,2025/AIIndex
2026).
Valores2025destacadosenlalámina: Singapur4,69%, HongKong3,48%, Luxemburgo3,43%, España3,31%,
Canadá3,00%,Polonia2,92%,EmiratosÁrabesUnidos2,87%,Suecia2,77%,EstadosUnidos2,56%, Chile2,41%,
ReinoUnido1,93%.
�� � �Lecturaenclase: “se está contratando mucha gente en inteligencia artificial, y hay una correlación con el gráfico
de la inversión en IA que había mostrado antes” .
������Valelapenanotarque Chileapareceexplícitamenteenelgráfico(2,41%) ,porencimadelReino
UnidoynomuylejosdeEstadosUnidos.
�� � �8.11.6LasituacióndeChile—ImportanteparaelcontextodelMACI
Surgededospreguntasdeunaestudiante(Priscila): ¿existenestosdatosparaLatinoamérica? y¿cómoestamos
comopaís?
Sobrelosdatosregionales
�� � �ExisteunreportedeIAparaLatinoamérica( “Latam AI report o algo así” — �� � �elprofesordudadelnombre
exacto,asíqueestedatodebetomarseconreserva),pero “la última vez que lo vi no llegaba a este nivel; era mucho
más superficial el reporte”.
������EldiagnósticodeChile
31

## Lamina 32

Aspecto Diagnósticodelprofesor
Fortaleza �� � �“Tenemos la gracia de que entramos antes.
Empezamos a definir nuestra política de inteligencia
artificial mucho antes que otros países y fuimos los
primeros en preocuparnos de la IA a nivel de Estado.” Se
armaronmesasdetrabajo ,entornoalaño 2018.
Debilidadestructural ������ �� � �“El problema que tenemos, como con cualquier
otra tecnología en nuestro país, es que estamos
acostumbrados a comprarla y no a desarrollarla . Yo
no veo que le vayamos a competir a OpenAI.”
Asimetríadetamaño �� � �Lasgrandesempresas llevan “casi diez años, ocho
años quizás” enestoyestándesarrollandosupropiaIA;
ala pequeñaymedianaempresa “le cuesta mucho más,
porque es súper caro desarrollar inteligencia artificial”.
Barrerasparastartups ������ �� � �Dos,explícitas: “primero, porque tienes que
tener gente que sepa harto ; y después, tienes que
tener la plata para la infraestructura ”.
������SobrelapolíticadeIA:porquéseve“comountodo”
Preguntadelaestudiante: lapolíticatratólaIA comountodo envezdereconocer subgrupos,loquegenera
problemas.
Respuestadelprofesor: - �� � �Sobrequiénlaelaboró: “la política de inteligencia artificial se armó por un panel de
expertos que realmente eran expertos… Las mesas de trabajo fueron un insumo, pero la política misma fue hecha —o
al menos asesorada— por un panel de expertos.” - ������ �� � �Laexplicaciónhistóricaclave: “Cuando se generó la
política de IA, que fue el 2018, no existía ChatGPT , partamos por ahí. Entonces la primera versión veía la IA como
el área en general, como un todo . Lo que pasa es que, como se popularizó tanto, empezaron a salir especialistas y
se empezó a aplicar a distintas especialidades: hay IA para A, IA para B, IA para C, y cada una era como un mundo
aparte. Y entonces ahí ya se complejiza más el tema. ” - �� � �Ladificultadpráctica: “¿entonces qué hacemos?
¿Una política de IA para la industria forestal, una política de IA para los modelos de lenguaje? Es difícil, no es tan
fácil.”
8.11.7Runwayyelemprendimiento(slide63)—Complementario
Runway(RunwayML): sistemaqueayudaa generaryeditarvideosconinteligenciaartificial ,usado envarias
películas.
������ �� � �Eldatorelevante: fuedesarrolladoporchilenos —doschilenosqueseconocieron haciendounmagíster
enNuevaYork ,juntoconuntercersocio.
������Laadvertenciasobrelosemprendimientos—elpuntorealdelalámina
�� � �“Tengo que decir algo. Al igual que cualquier emprendimiento exitoso, suena así como que ayer se
juntaron y hoy día ya tienen esto . Ellos empezaron con esto hace como 10 años , cuando los modelos de
inteligencia artificial no eran tan buenos, entonces tuvieron que empujar y empujar y empujar , porque
así es como funcionan los emprendimientos.”
�� � �Otrosunicornioschilenoscitadoscomoevidencia: NotCo (~10años)y Cornershop(~10años).
������Conclusión: “Todos estos unicornios chilenos se toman del orden de 10 años en tener éxito. Entonces
tienes que ser muy resiliente para ser un emprendedor .”
8.11.8 ������“…lascosasestáncambiando”(slide64)
Herramientasmostradas: ClaudeCode,GitHubCopilot,OpenAICodex,GeminiCodeAssist —juntoauna
capturadeunasesióndeagentedecodificaciónleyendoyeditandoarchivosdeunproyectoreal.
32

## Lamina 33

�� � �“Hoy en día tenemos estos agentes que te asisten en la codificación , y entonces uno puede codificar
mucho más rápido . Pero varias veces se equivocan y están convencidos de que no se equivocaron :
tú hablas con ellos y ellos están convencidos de que no se equivocaron. Pero sí se equivocan. ”
������Cierraelarcocompletodelaclase: slide45(losLLMalucinan)→§8.9.5(agentesverificadores)→
§8.10.2(perdemoscapacidadcríticasiconfiamosciegamente)→aquí,elcasoconcretoycotidiano. La
confianzacalibradaenestasherramientasesunadelastesiscentralesdelaclase.
8.12Comentariosfinales(slide65)
Contenidoliteraldelaláminadecierre:
ComentariosFinales -LaInteligenciaArtificialestáconnosotros. -Elgranboomsedebegraciasa:
-las redesneuronalesartificiales ,-la grancantidaddedatos quehemosproducidocomohumanidad,
-ya avancesencómputocontarjetasgráficas . -(aplicadoa: Imágenes·Texto·Videos )- Losagentes
puedenrazonaryutilizarherramientaspararesolvertareascadavezmáscomplejas.
�� � �Ampliaciónoralsobrelosagentes: “los agentes usan las redes neuronales por detrás, pero el desarrollo de agentes
es como desarrollo de software con un LLM metida adentro , y básicamente funciona súper bien: tienen ciclos de
razonamiento, ciclos de chequeo de lo que están haciendo, y ayuda a resolver tareas mucho más complejas.”
������������Lostresfactoresdelboomsonunapreguntadeexamencasigarantizada (esliteralmente
la lámina de conclusiones). Memorizar la tríada:(1) redes neuronales artificiales · (2) enormes
volúmenesdedatos·(3)cómputoconGPUs.
Nótesequelostresestabananticipadosenlaprimeramediahora: lasredes(§8.3),losdatos(slide8,
§8.1.5)ylasGPUs(§8.1.4).
�� � � � � � � � �FORMULARIODELACLASE
Concepto Expresión Slide
Perceptrón ŷ=g(w₀+x₁w₁+x₂w₂+ ⋯+xₙwₙ),
congnolineal
13
Modelolineal/regresión
(perceptrónsinactivación)
ŷ=w₀+w₁x 15
Conjuntodedatos 𝒟={(x₁,y₁),(x₂,y₂),(x₃,y₃),(x₄,y₄)} 15
Costodeundato ℒᵢ=(ŷ(xᵢ)−yᵢ)² 17
Funcióndecosto(Ndatos) ℒ=(1/N)·Σᵢ₌₁ᴺ(ŷ(xᵢ)−yᵢ)² 17
Actualizacióndeparámetros �� � w^(t+1)=w^t+Δw^t 18
Direccióndelpaso �� � Δw^t ∝−d ℒ/dw 19
Descensodegradiente �� � **w^(t+1)=w^t−η·(d ℒ/dw) _{w^t}**
Tasadeaprendizaje η (eta)—hiperparámetro 19
Vectordeatención α⁽ᵗ⁾,conΣαⱼ=1(normalizado ⇒
porcentajes)
35
Ejemplodeα (para“ladró”) [0.0,0.3,0.1,0.0,0.0,0.3,0.0,0.0,0.3] 35
EnmascaramientodeBERT 15% delostokensalazarpor
secuencia
38
ParámetrosdeGPT-3 175B(=175×10⁹) 45
ParámetrosdeLlama-2 7B/13B/70B 45
InversiónenIA2025 581,7milmillonesUSD 58
AdopciónGenAI 53%en3años 57
EmpresasusandoIA(2025) 88% ,delascualessolo 7%fully
scaled
59
33

## Lamina 34

����� �LISTADEDEFINICIONESIMPORTANTES
Término Definición(segúnslides+clase)
InteligenciaArtificial Áreaquetrabajaensistemasquepuedan razonar
(procesardatosycrearnuevoconocimientoapartirdel
existente)y actuar(tomardecisionesymodificarel
medioambiente)
DeepLearning Conjuntodealgoritmosque modelanlosdatosa
travésdemúltiplesnivelesdeabstracción usandoun
conjuntode capasjerárquicas
Redneuronalartificial Conjuntodeneuronasartificiales(perceptrones)
conectadas,habitualmenteorganizadasen capas;esla
implementaciónactualdeDeepLearning
Perceptrón Launidadbase delasredesneuronales: neurona
artificialquemultiplicaentradasporpesos,lassumay
aplicauna funcióndeactivaciónnolineal
Funcióndeactivación(g) Funciónnolineal aplicadaalasumaponderada;eslo
queimpidequelaredcolapseenunmodelolineal
Funcióndecosto( ℒ) Promediodeloserrorescuadráticosdelmodelosobreel
conjuntodedatos;loqueelentrenamiento minimiza
Descensodegradiente Algoritmoiterativoqueactualizalosparámetros
moviéndoseendirección contrariaaladerivada dela
funcióndecosto
Tasadeaprendizaje(η) Hiperparámetroquecontrola cuántoseavanza encada
pasodeldescensodegradiente; “qué tan rápido va a
aprender”
Forwardpass Propagacióndelosdatos delaentradaalasalida para
producirunapredicción;equivaleahacer inferencia
Backwardpass Propagacióndelerror desdelafuncióndecostohacia
atrásparaajustarlasneuronas
Retropropagacióndelerror Elalgoritmoqueajustaelmodelotomandoelerrory
propagándolohaciaatrásporlared
Feedforwardneuralnetwork Redneuronalenlaquelainformaciónsealimenta hacia
adelante,capatrascapa
GPU Unidaddeprocesamientográfico;originalmentepara
videojuegos,claveparaentrenarmodelosrápidamente
desde2012
Mecanismodeatención Mecanismoque,pararepresentarunapalabraensu
contexto,asigna porcentajesdeatención alasdemás
palabrasdelasecuencia
Representacióncontextual Vectorquerepresentaunapalabra dentrodelcontexto
desuoración,nodeformaaislada
Transformer Modelobasado únicamenteenmecanismosde
atención( Attention is all you need,2017);altamente
paralelizable
GLUE General Language Understanding Evaluation: benchmark
denuevetareas decomprensióndellenguaje,con
datasetdediagnósticoytabladeclasificaciónpública
Modelosfundacionales Modelos(BERT,GPT-3,CLIP,Codex) entrenadoscon
muchosdatos demodoquepuedan adaptarseauna
ampliagamadetareasposteriores
34

## Lamina 35

Término Definición(segúnslides+clase)
BERT ModelofundacionaldeGooglebasadoenTransformer
Encoder,entrenadocon MaskedLanguageModel
MaskedLanguageModel(MLM) Estrategiadeentrenamientoque enmascaratokensal
azar(15%enBERT) yhacequeelmodelolosprediga;
esun problemadeclasificación
Transformerautorregresivogenerativo Transformerque enmascarasiemprelaúltimapalabra ,
yportanto generatexto palabraapalabra
LLM(LargeLanguageModel) Modeloque predicelasiguientepalabra ,conmilesde
millonesdeparámetros,basadoenmecanismosde
atención
Alucinación QueunLLM inventeinformación presentándolacomo
hecho;consecuenciadeestaroptimizadoparaimitarla
distribucióndellenguaje,nolaverdad
GPT Generative Pre-trained Transformer;elmodelode
lenguaje
ChatGPT �� � �Laherramienta,quehoyesun sistema
multiagente—noeslomismoqueGPT
Tokenespecial �� � �Palabrageneradaporelmodeloquenosemuestra
alusuarioyque disparaunaacción (detenerse,invocar
unaherramienta,generarunaimagen)
Destilación �� � �Entrenarunmodelopequeñoenseñándoledesde
unmodelogrande ,parareducircosto; “no funciona tan
bien”
Agente Sistemaquerealiza accionesautónomas usandoun
LLMparaprocesarinformaciónydecidir,con memoria,
herramientas,objetivosycapacidadde percibirsu
entorno
Sistemamultiagente Conjuntodeagentesquecolaboran;enfunciones
críticasseusanagentes verificadoresyauditores para
reducirlatasadealucinación
Modelodedifusión Modelogenerativocondosprocesos: difusiónhacia
adelante(añadirruidogradualmente)y eliminaciónde
ruidoinverso (aprenderagenerardatos)
Denoising Procesodeeliminarruido;tambiénseaplicaaaudio,no
soloaimágenes
LatentSpaceDiffusion Varianteenlaqueladifusiónsehacesobreuna
representaciónvectorial delaimagen(espaciolatente)
ynosobrelospíxeles;requiere encoderydecoder
Condicionamiento �� � �Pasareltexto(ounaimagen)poruncodificadory
entregaresevectoraldecodificador ,paraquela
generacióndependadelprompt
IAgenerativa �� � �“Inteligencia artificial que genera datos”
Moat �� � �“Foso”deuncastillo: metáforadelaventaja
competitivadefendible;elmemorandodeGoogle
sostienequenolatienenfrentealopensource
AIIndex Reporteanualdela UniversidaddeStanford ; “un
termómetro de la inteligencia artificial”
���������POSIBLESPREGUNTASDEEXAMEN(conrespuestasbreves)
Verdadero/Falsoconjustificación
35

## Lamina 36

# Afirmación V/F Justificación
1 DeepLearningsiempre
funcionamejorquelos
algoritmosclásicos
F Soloconmuchosdatos .
Conpocosdatos,los
algoritmosclásicos(SVM,
RandomForest)funcionan
mejor(slide8)
2 Unperceptrónesun
modelolineal
F Lafuncióndeactivación g
esnolineal ,loquehace
nolinealalperceptrón
3 Apilarmuchascapas
linealesaumentala
capacidaddelmodelo
F “Se transforma todo en un
modelo lineal nomás”;sin
nolinealidad,apilarno
aporta
4 Laregresiónlinealpuede
versecomounperceptrón
V(conmatiz) Esunperceptrón alquele
faltalafunciónde
activaciónnolineal
5 EnDeepLearninghayque
calcularlascaracterísticas
amanoantesdeentrenar
F DLextraelas
características
automáticamentedesde
losdatoscrudos
6 Eldescensodegradiente
semueveenladirección
deladerivada
F Semueveenladirección
contraria(deahíelsigno
−): laderivadaapunta
haciadondeelcosto sube
7 Latasadeaprendizajees
unparámetroqueel
modeloaprende
F Esun hiperparámetro;se
eligedesdeafuera(ypor
validacióncruzada)
8 Forwardybackwardson
dosmétodosalternativos
deentrenarunared
F Sonlasdosmitadesde
cadaiteración: forward
calculaelerror,backward
calculalosgradientes
9 Elforwardpasstambiénse
llamainferencia
V Esloquesehacecuando
elmodeloyaestá
entrenadoysolodebe
predecir
10 Lostransformersganaron
soloporquelaatención
captamejorelcontexto
F(incompleto) Larazóndecisivaesque
sonaltamente
paralelizables,loque
permitióentrenarcon
muchísimosmásdatos
11 Elvectordeatenciónde
unapalabrapuedeincluir
alapropiapalabra
V “Usa la misma palabra, y
generalmente ahí es donde
está la correlación más
alta”
12 Losvaloresdeatenciónde
laslide35sonmedidas
realesdeunmodelo
F Elprofesoraclaraque “son
números que yo puse para
ilustrar el tema”
13 BERTenmascarael15%de
lostokensdecada
secuenciaalazar
V Datoliteraldelaslide38
14 Predecirunapalabra
enmascaradaesun
problemaderegresión
F Esclasificación: la
etiqueta(quépalabra)es
categórica
36

## Lamina 37

# Afirmación V/F Justificación
15 UnLLMrazonayplanifica F Slide45: “son muy malos
para razonar y planificar”;
imitansuconjuntode
entrenamiento
16 GPTyChatGPTsonlo
mismo
F GPTes elmodelode
lenguaje;ChatGPTes la
herramienta,hoyun
sistemamultiagente
17 Unagentepuedeacceder
ainformaciónposteriora
suentrenamiento
V Medianteherramientas
(APIs,búsqueda,
documentos). ElLLMsolo,
no
18 Lossistemasmultiagente
conagentesverificadores
eliminanlaalucinación
F Lareducen: “igual se te
puede pasar una
alucinación en todo este
sistema”
19 ElcostodeunLLMestá
principalmenteenel
entrenamiento
F(incompleto) Elentrenamientoescaroy
único;la inferenciaes
caray permanente—
“hacer el forward es caro”
20 Enunmodelodedifusión,
elprocesodeañadirruido
requiereunaredneuronal
F Elprocesohaciaadelante
esfijo;laredseentrena
parael procesoinverso
(denoising)
21 Unmodelodedifusión
generasiemprelamisma
imagen
F Distintoruidodeentrada
⇒distintaimagen
generada
22 2012eselañoenquelaIA
superólavisiónhumana
F 2012esla revoluciónde
ImageNet/GPUs;elnivel
devisiónhumana se
alcanzóen 2015
23 Lasredesneuronalesson
unainvenciónreciente
F Elperceptrónesdelos
años40,anteriorinclusoa
ladefinicióndeIAde
Turing;huboaugesenlos
80y90
24 LaIAgenerativaesla
tecnologíadeadopción
másrápidadelahistoria
V 53%en3años,versus22
años(computadores)y25
años(internet)
25 Lamayoríadelas
empresasqueusaIAla
tienedesplegadaaescala
F 88%usaIA,pero solo7%
está fully scaled
Preguntasdedesarrollo
1. ¿QuéesDeepLearningyenquésediferenciadelMachineLearningclásico? DeepLearningesunconjunto
dealgoritmosquemodelanlosdatosatravésde múltiplesnivelesdeabstracción usandocapasjerárquicas. La
diferenciacentralconelMLclásicoesqueesteúltimorequierequeelhumano calculecaracterísticasamano
(largodelasorejas,anchodeltronco)paraentregárselasaunclasificador(SVM,RandomForest),mientrasqueDeep
Learningseconectadirectamentealafuentededatosyextraelascaracterísticasautomáticamente . Estas
característicasavecesnosonlasqueunhumanomediría,perosirvenpararesolverelproblema.
2. Expliqueelperceptrónyporquénecesitaunafuncióndeactivaciónnolineal. Elperceptróntomaentradas
x₁…xₙmásunaentradaconstante1,lasmultiplicaporpesosw₀…wₙ,lassuma,ypasaesasumaporunafunciónde
activacióng: ŷ=g(w₀+x₁w₁+ ⋯+xₙwₙ). Hastalasuma,elmodeloeslineal; gesloquelohacenolineal . Es
37

## Lamina 38

indispensableporque,silosperceptronesfueranlineales,conectarcuantossequiera produciríadetodosmodos
unúnicomodelolineal —lacomposicióndefuncioneslinealeseslineal—ynoseganaríanadaencapacidad
expresiva.
3. Describaelprocesocompletodeentrenamientodeunaredneuronal. (1)Sedefineuna funcióndecosto ,
típicamenteelerrorcuadráticopromedio ℒ=(1/N)Σ(ŷ(xᵢ)−yᵢ)². (2)Comolaredesnolineal,nosepuededespejarla
soluciónanalíticamente(adiferenciadelaregresiónlineal),asíqueseminimizaiterativamente. (3)Encadaiteración
sehaceun forwardpass: losdatossepropagandelaentradaalasalidayseobtienelapredicción. (4)Secalculael
errorcomparandoconlaetiquetareal. (5)Sehaceun backwardpass: seretropropagaelerrorhaciaatrásporlared
paracalcularlos gradientes(algoritmoderetropropagacióndelerror). (6)Seactualizanlospesoscon descensode
gradiente: w^(t+1)=w^t−η·d ℒ/dw,moviéndoseendireccióncontrariaaladerivada. Serepitehastaconverger.
η,latasadeaprendizaje,esunodeloshiperparámetrosmásimportantes.
4. ¿Porquéenlaprácticalosmínimoslocalesnoarruinanelentrenamientodeunared? Porqueelespaciode
parámetrostiene altísimadimensión. Paraquedaratrapadoenunmínimolocal,elpuntotendríaquesermínimo
simultáneamenteentodaslasdimensiones : en2Denambas,en3Denlastres,yasísucesivamente. Conmillones
deparámetros,laprobabilidaddequetodaslasdireccionessubanalavezesmuybaja,porloquecasisiempre
quedaalgunadirecciónporlacualseguirbajando.
5. Expliqueelmecanismodeatenciónyporquéfuedecisivo. Laatenciónbuscagenerarunarepresentación
contextualdecadapalabra: unvectorquelarepresente dentrodesuoración . Paraellogeneraun vectorde
atenciónα queindicaquéporcentajedeatenciónprestaracadaunadelasotraspalabras(porejemplo, para
“ladró”: 30%a“perro”,30%a“feliz”,30%asímisma,10%a“café”). Losαseobtienencalculando correlaciones
entrelasrepresentacionesvectorialesdelaspalabrasy normalizándolasparaquesumen1 . Fuedecisivopordos
razones: captaelcontexto,ysobretodo esaltamenteparalelizable —larepresentacióndecadapalabrapuede
ajustarseindependientementedelasdemás—,loquepermitióentrenarconvolúmenesdedatosantesimposibles
porlimitacionesdehardware.
6. ¿CómosepasadeBERTaunLLMgenerativo? BERTseentrenacomo MaskedLanguageModel : enmascaraal
azarel15%delostokensdecadasecuenciayentrenaalmodeloparapredecirlos(unproblemade clasificación). La
observaciónclaveesque sielmodelopuedepredecircualquierpalabraenmascarada,entoncespuedepredecir
laúltima. Alenmascararsistemáticamentelaúltimapalabra,elmodelogeneralapalabrasiguiente;luego,conesa
palabraincorporada,generalasiguiente,yasíindefinidamente. Esoloconvierteenun transformerautorregresivo
generativo,esdecir,un modelogenerativodetexto . Escaladoamilesdemillonesdeparámetros,esoesun LLM.
7. ¿QuéesunLLM,quéhacebienyquéhacemal? UnLLMesunmodeloque predicelasiguientepalabra ,
conmilesdemillonesdeparámetros(GPT-3: 175B;Llama-2: 7B/13B/70B),basadoenmecanismosdeatención,
querequieremuchosdatosypoderdecómputo. Esmuybueno comoasistentedeescrituraydecodeo. Esmuy
maloparaobtenerrespuestasbasadasenhechos( alucina),parausarinformaciónposteriorasuentrenamiento,
ypara razonaryplanificar . Fundamentalmente,imitaladistribucióndesuconjuntodeentrenamiento : está
optimizadoparaproducirtextoplausible,noverdadero.
8. ¿QuéesunagenteycómoresuelvelaslimitacionesdeunLLM? Unagenteesunsistemaquerealizaacciones
autónomasusandoun LLMparaprocesarinformaciónytomardecisiones,yqueademáscuentacon memoria,
herramientas,objetivosclarosycapacidadde percibirsuentorno . ResuelvelaslimitacionesdelLLMporque
puedeusarherramientas: consultarunaAPIdelclima(resuelve“nosécosasposterioresamientrenamiento”),
buscarporsimilituddentrodeundocumentoentregadoporelusuario(resuelve“noconozcoestainformación”),
ejecutarcódigo,accederainternet,ollamara otrosagentes. Además,ensistemasmultiagentepuedenincorporarse
agentesverificadoresyauditores querevisansilatareasecumplió,reduciendo—aunquenoeliminando—latasa
dealucinación.
9. ¿Cómofuncionapordentrolainvocacióndeunaherramientaporunagente? Elagenterecibe instrucciones
iniciales(quiénes,quéhace)yuna declaracióndelasherramientasdisponibles . Luegofuncionacomocualquier
LLM:generandolasiguientepalabra . Enalgúnpuntogeneraun tokenespecial quecorrespondeainvocaruna
herramienta;elsistemaejecutaesaherramienta;el resultadovuelvealagenteenformadetexto ;yelagente
continúagenerandotexto,ahoraconesainformaciónincorporada. EselmismomecanismoporelcualChatGPT
disparaungeneradordeimágenesosedetienealfinaldeunturno.
10. Expliquecómofuncionanlosmodelosdedifusiónycómoselesindicaquégenerar. Tienendosprocesos.
Elproceso de difusión hacia adelantetoma un dato (por ejemplo, la imagen de un gato) yle agrega ruido
38

## Lamina 39

gradualmentehastaquelaimagenespuroruido;esteprocesoes fijo,norequiereredneuronal. El procesoinverso
deeliminaciónderuido entrenaunaredneuronal pararevertirlo: recuperarlaimagendesdeelruido. Unavez
entrenada,sedescartaelprocesohaciaadelanteyseleentrega ruidocualquiera alared,quegeneraunaimagen
nueva;distintoruidoproducedistintaimagen . Paraindicarlequégenerarseusa condicionamiento: eltexto
delusuariosepasapor otrocodificador (similarauntransformer)queproduceunvector,yesevector entraal
decodificador,demodoquelageneraciónquedecondicionadaporelprompt. Tambiénsepuedecondicionar
sobreunaimagendeentrada (casodela“ghiblificación”defotos).
11. Segúnlaclase,¿aquésedebeelgranboomdelaIA? Atresfactores(slide65): (1)las redesneuronales
artificiales;(2)la grancantidaddedatos quehemosproducidocomohumanidad;y(3)los avancesencómputo
contarjetasgráficas(GPUs) . Semanifiestaenimágenes,textoyvideos. Históricamente,elpuntodeinflexión
fue2012enImageNet,cuandoelerrorcayóde~25%a~16%enunañograciasalusodeGPUs,yen 2015laIA
alcanzóelniveldevisiónhumana.
12. ¿QuémuestranlosdatosdeindustriadelAIIndexylasencuestasdeMcKinsey? Quela adopciónes
rapidísimaperolamadurezesbaja . LaIAgenerativaalcanzó 53%deadopciónen3años —latecnologíade
adopciónmásrápidadelahistoria,frentea22añosdelcomputador(69%)y25añosdeinternet(91%). Lainversión
llegóa 581,7milmillonesUSDen2025 . El88%delasempresasusaIAenalmenosunafunción,perosoloel
7%está fully scaled: 32%experimentando,30%piloteando,31%intentandoescalarsinlograrlo. Los ahorrosde
costosseconcentraneningenieríadesoftware,manufacturaeIT;los aumentosdeingresos ,enmarketing,ventas
ydesarrollodeproductos.
�� �ERRORESYCONFUSIONESCOMUNES
1. CreerqueDeepLearningreemplazóalosmodelosdelasclases6y7. Conpocosdatos,losalgoritmos
clásicossiguensiendomejores(slide8). Noestánobsoletos.
2. Confundir Deep Learning con red neuronal por definición.DL es elconcepto (múltiples niveles de
abstracciónconcapasjerárquicas);lasredesneuronalessonla implementacióndominantehoy. “Hoy en día
se implementan con redes neuronales.”
3. Pensarqueelperceptróneslineal. Esnolineal,graciasalafuncióndeactivacióng. Estafueunacorrección
explícitadelprofesorenclase.
4. Nosaberjustificarporquéhacefaltalanolinealidad. Porquecomponerfuncioneslinealesdauna
funciónlineal: apilarperceptroneslinealescolapsaenunúnicomodelolineal.
5. Confundirdóndeestálanolinealidad. Lasumaponderada todavíaeslineal ;lanolinealidadentra después,
alaplicarg.
6. Confundirlafuncióndecostoconelmodelo. Elmodeloesŷ=f(x);lafuncióndecosto ℒmidequétan
maloesesemodelosobrelosdatos.
7. Olvidarelsignonegativodeldescensodegradiente. Laderivadaapuntahaciadondeelcosto sube;hay
quemoverseen direccióncontraria.
8. Creerqueηseaprende. Esun hiperparámetro(comoelgradodelpolinomio,elumbraldeclasificaciónola
medidadeimpurezaenlasclases6–7): seeligedesdeafuera,porvalidacióncruzada.
9. Creerqueforwardybackwardsonalternativas. Sonlasdosmitadesdecadaiteración delentrenamiento.
10. Confundir“forwardpass”con“entrenamiento”. Elforwardporsísoloes inferencia. Elentrenamientoes
forward+costo+backward+actualización.
11. Pensarquelascapassiempreaprendenbordes→ojos→caras. Eslailustración teórica;enlapráctica “a
veces funciona así, a veces no, y depende de la arquitectura” ydelanaturalezadelosdatos.
12. Creer que el mecanismo de atención es una idea de 2017.El mecanismo de atenciónes anterior
(≈2014–2015);lonuevoen2017fueafirmarque nosenecesitanadamásqueatención .
13. Explicareléxitodelostransformerssoloporelcontexto. Faltalamitaddecisiva: sonaltamenteparaleliz-
ables,yesopermitióescalarlosdatos.
14. Pensarqueunapalabranoseprestaatenciónasímisma. Sílohace,ysueleser lacorrelaciónmásalta .
15. Olvidarquelosαsenormalizan. Debensumar1paraserporcentajes.
16. Creerquepredeciruntokenenmascaradoesregresión. Esclasificación: seeligeentrelaspalabrasdel
vocabulario.
39

## Lamina 40

17. ConfundirGPTconChatGPT. GPTes elmodelodelenguaje ;ChatGPTes laherramienta,hoyun sistema
multiagente.
18. AtribuirlealLLMloquehaceelagente. Buscarenundocumento,consultarelclimaoejecutarcódigo nolo
haceelLLM :lohacenlas herramientasdelagente. Todaslaslimitacionesdelaslide45sondel LLMdesnudo.
19. Creerquelaalucinaciónesundefectocorregibleconmásdatos. Derivadel objetivodeentrenamiento :
imitarladistribucióndellenguajehumano,nodecirlaverdad.
20. Creerquelosagentesverificadoreseliminanlaalucinación. Lareducen; “igual se te puede pasar una
alucinación”.
21. Darsololarazóntécnicaparamanteneralhumanoenelloop. Hayunasegundarazónquenoseresuelve
contecnología: laresponsabilidad porlasfallas.
22. CreerqueelcostodelosLLMestásoloenelentrenamiento. “La inferencia es lo caro. Hacer el forward es
caro”—cadatokengeneradoesunforwardcompleto.
23. Pensarqueelprocesodedifusiónhaciaadelanteusaunaredneuronal. Esfijo;laredseentrenaparael
procesoinverso.
24. Creerqueladifusióngenera“píxelapíxel”. “No es píxel a píxel. Es toda la imagen de ruido.”
25. Confundirdifusióncondifusiónenespaciolatente. EnLatentSpaceDiffusionelruidoseagregaa una
representaciónvectorial delaimagen,noalospíxeles,yhacefaltaencoder+decoder.
26. Confundir2012con2015. 2012 =revoluciónImageNet/GPUs(error25%→16%). 2015=sealcanzael nivel
devisiónhumana . Elprofesorpreguntaestoexplícitamente.
27. Creerquelasredesneuronalessonrecientes. Elperceptrónesdelosaños40 ,anterioraladefiniciónde
IAdeTuring(años50). Huboaugesenlos80y90ydesinterésenmedio: ~80añosdetrabajo.
28. Leer“billones”como10¹². Slideyprofesorusanelcalcodelinglés: 175B=175milmillones=175×10⁹ .
29. Confundir“88%deempresasusanIA”conmadurez. Soloel 7%está fully scaled;lamayoríaexperimentao
pilotea.
30. Confundirdóndeaparecenlosahorrosydóndelosingresos. Costos : ingenieríadesoftware,manufactura,
IT.Ingresos: marketing,ventas,desarrollodeproductos.
31. Creerquelosagentesdecodificaciónnoseequivocan. “Varias veces se equivocan y están convencidos de
que no se equivocaron .” Eselriesgodeperdercapacidadcrítica.
��CONEXIONESCONELRESTODELCURSO
Conceptodeestaclase Seapoyaen/seconectacon
Aprendizajesupervisado,regresiónyclasificación(slide
2)
Clases6y7 —repasoliteraldelasmismasdefiniciones
Notaciónŷvs.y Convenciónestablecidaenlaclasede regresión(clase
6)
Funcióndecosto ℒ=(1/N)Σ(ŷ−y)² Clase6: eselmismoerrorcuadráticomedio,ahora
llamado“funcióndecosto”
“Sifueselineal,yavimoscómohacerloenlaclasede
regresión”
Clase6 —elcontrasteconelcasonolinealesloque
motivaeldescensodegradiente
Laregresiónlineal esunperceptrónsinactivación Clase6 —reinterpretacióndirectadeŷ=w₀+w₁x
Elejemplodelastresrectasy“lanaranjatienemenos
error”
Clase6 —elprofesorrehacedeliberadamenteelmismo
ejercicio
Tasadeaprendizajeη comohiperparámetro Clases6y7 —parámetrovs.hiperparámetro;seelige
porvalidacióncruzada
Predeciruntokenenmascarado esclasificación Clase7 —etiquetacategórica
Característicasamano(tamañodelanimal,orejas,ancho
delárbol)
Clases6y7 —losmismosejemplos,ahoracomo
contrasteconDL
SVMyRandomForestcomo“losalgoritmosclásicos” Clase7 —ylaslide8explica cuándosiguensiendo
preferibles
Eleclipsehistóricodelasredesneuronales(2000s) Clase7 —lasecuenciaSVM→RandomForest→redes
neuronalesquedaexplicada
40

## Lamina 41

Conceptodeestaclase Seapoyaen/seconectacon
Píxelesdeunaimagencomoatributos Unidaddedatos : atributosquenorequiereningeniería
previa
“Ningúnmodeloesperfecto”/losLLMalucinan Clase7 —elprofesoryahabíausadoalasLLMcomo
ejemplodequeningúnmodeloesperfecto
Vectorizarundocumento/búsquedaporsimilitud Unidaddecalidaddedatosyrepresentación ;también
anticipatécnicasderecuperación
Aprendizajenosupervisado Noesmateriaobligatoriadeestecurso —seveenun
cursoposteriordelmagíster(MACI),oenunaclase
optativadeldiploma
Reduccióndedimensionalidad/representaciones
vectoriales
Seconectaconlaideade representación(vector
latenteendifusión,embeddingsenatención)
������MAPAMENTALDELACLASEENUNAPÁGINA
DE LOS MODELOS CLÁSICOS A LA IA DE HOY
│
├── CONTEXTO
│ IA = razonar + actuar "la nueva electricidad" (Andrew Ng)
│ IMAGENET: 1.2M imágenes · 1000 categorías
│ · error 25% ──2012──► 16% ⇒ REVOLUCIÓN (causa: GPUs)
│ · GPUs en el desafío: 2011:0 · 2012:4 · 2013:60 · 2014:110
│ · 2015 ⇒ NIVEL DE VISIÓN HUMANA ← 🎯 dato más señalizado
│ slide 8: pocos datos ⇒ clásicos ganan | muchos datos ⇒ DL gana
│
├── 01. DEEP LEARNING
│ def: modelar datos en MÚLTIPLES NIVELES DE ABSTRACCIÓN (capas jerárquicas)
│ líneas/puntos → ojos/nariz/boca → CARA
│ vs ML clásico: DL extrae las características AUTOMÁTICAMENTE
│ │
│ ├── PERCEPTRÓN ŷ = g(w₀ + x₁w₁ + … + xₙwₙ)
│ │ g = activación NO LINEAL ← sin ella todo colapsa a lineal
│ │ regresión lineal = perceptrón SIN g
│ │
│ ├── ENTRENAMIENTO
│ │ ℒ = (1/N)Σ(ŷ(xᵢ) − yᵢ)² ← igual que en clase 6
│ │ no lineal ⇒ no se despeja ⇒ ITERAR
│ │ w^(t+1) = w^t − η·dℒ/dw ⚠ slides 18–19
│ │ η = TASA DE APRENDIZAJE (hiperparámetro clave)
│ │ mínimos locales: poco probables en ALTA DIMENSIÓN
│ │
│ └── CICLO: FORWARD (→ predicción, = inferencia)
│ ↓ calcular ℒ
│ BACKWARD (retropropagación del error → gradientes)
│ ↓
│ ACTUALIZAR w [feedforward neural network]
│
├── 02. IA GENERATIVA
│ │
│ ├── TEXTO
│ │ benchmark GLUE (9 tareas): 74% → GPT 75,1 → BERT 82,1 → RoBERTa 88,5
│ │ ATENCIÓN (Attention is all you need, 2017)
│ │ representación CONTEXTUAL: α = [0, .3, .1, 0, 0, .3, 0, 0, .3]
41

## Lamina 42

│ │ α = correlaciones normalizadas (suman 1)
│ │ 🎯 ALTAMENTE PARALELIZABLE ⇒ muchísimos más datos
│ │ MODELOS FUNDACIONALES (BERT, GPT-3, CLIP, Codex)
│ │ BERT = Masked Language Model, enmascara el 15% al azar
│ │ ¿y si enmascaro SIEMPRE LA ÚLTIMA? ⇒ AUTORREGRESIVO
│ │ ⇒ genera texto ⇒ LLM (ChatGPT, LLaMA, PaLM 2, Gemini)
│ │ 🆕 GPT ≠ ChatGPT · token "detente" · tokens que llaman herramientas
│ │
│ └── IMÁGENES: MODELOS DE DIFUSIÓN
│ forward: añadir ruido gradualmente (FIJO, sin red)
│ reverse: DENOISING aprendido (red neuronal)
│ ⇒ ruido cualquiera ⇒ imagen nueva (distinto ruido = distinta imagen)
│ Latent Space Diffusion ⚠ : difusión sobre la REPRESENTACIÓN (encoder/decoder)
│ CONDICIONAMIENTO: texto (y/o imagen) → codificador → vector → decodificador
│
├── 03. AGENTES ← resuelven las limitaciones de la slide 45
│ LLM solo: ✅ escritura, codeo
│ ❌ ALUCINA · no sabe lo posterior a su entrenamiento
│ ❌ no razona ni planifica · IMITA su entrenamiento
│
│ AGENTE = LLM + MEMORIA + HERRAMIENTAS + OBJETIVOS + PERCEPCIÓN
│ MEMORY ┐
│ TOOLS ├─► AGENT ─► ACTIONS ─► ENVIRONMENT
│ GOALS ┘ ▲ │
│ └──── OBSERVATIONS ◄───┘
│ mecanismo: genera tokens → TOKEN ESPECIAL → ejecuta herramienta
│ → resultado vuelve como texto → sigue generando
│ multiagente: ejecutor → verificador → auditor ⇒ ↓ alucinación (no la elimina)
│ humano en el loop: por alucinación Y por RESPONSABILIDAD
│
└── 04. ÚLTIMOS AVANCES
Turing 2018: BENGIO · HINTON · LeCUN (perceptrón: años 40 · ~80 años)
2023: carta "pausar" (Bengio) → "no podemos parar, es una carrera"
"We have no moat" → open source: LLaMA filtrado → Raspberry Pi en 1 semana
riesgo social: empleo + PÉRDIDA DE CAPACIDAD CRÍTICA
AI INDEX (Stanford): 2015 imágenes · …· 2025 agentes y uso de computador
INDUSTRIA: GenAI 53% en 3 años ⇒ ADOPCIÓN MÁS RÁPIDA DE LA HISTORIA
inversión 2025: 581,7 MMM USD
88% usa IA · solo 7% FULLY SCALED
costos ↓: software, manufactura, IT
ingresos ↑: marketing, ventas, productos
CHILE: política temprana (2018) · "compramos, no desarrollamos" · Runway (chilenos, 10 años)
ORGANIZACIONES: lo más difícil es la CULTURA ORGANIZACIONAL
CIERRE: el boom = REDES NEURONALES + DATOS + GPUs
los agentes razonan y usan herramientas
42
