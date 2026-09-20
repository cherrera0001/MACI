# Resumen_Clase2_Creatividad_y_Definicion_de_Solucion

> Material de clase de Fundamentos de Ciencia de Datos, UdeC T2-2026.
> Texto extraido de `Resumen_Clase2_Creatividad_y_Definicion_de_Solucion.pdf` para busqueda e indexacion.
> 38 laminas. Las figuras no se extraen: si una lamina
> depende de un grafico, hay que abrir el PDF.

---

## Lamina 1

Prototipos y Creatividad — CLASE 2 (S02): Creatividad y Definición de
Solución
Apuntescompletos: diapositivasoficiales+transcripcióndeclase
Profesor: MartínMelladoGuerrero Curso: 2026G602—Prototiposycreatividad·Sesión02 Temas:Introduccióna
creatividad·Pruebasfuncionalesynofuncionales·Historiasdelusuario
Cómoleerestedocumento. Integraelcontenidodelas60diapositivasoficialesconlodichoenclase,
organizadosegúnelordenrealdelaexposición. Semarcancon �� � �loscontenidosque soloaparecen
enlatranscripción (noestánenlasslides),porquesuelenserjustamenteloqueunestudianteolvida
repasar. Lostemasadministrativosestánconcentradosenlasección §0,alinicio.
Notasobrelasfuentes. Latranscripciónesautomática(Whisper+pyannote-audio)ycontieneerrores
dereconocimientoevidentes,sobretodoennombresdemarcas,empresasyherramientas. Cuandoel
términocorrectosededucedelasslidesodelcontexto,seusaelcorrectoyseindicalareconstrucción.
Todosloscasosestánlistadosenel Anexofinal,consuniveldeconfianza. Loscasosdonde nosepudo
reconstruireltérminosemarcanexplícitamentecomo [término no reconstruible]. Todoloqueestáen
estedocumentoprovienedelasdosfuentesentregadas;noseagregóconocimientoexterno.
Alcance. Seexcluyerondeesteresumenlasanécdotasbiográficasdelprofesorsincontenidodocente
(deportes,aprendizajedeinstrumentos,rutinaspersonales),lasdigresionessobresupropioflujode
trabajopersonalylosintercambioslogísticosirrelevantes. Cuandounaexperienciapersonaldesemboca
encontenidorealdelamateria,seconservó sololaparteconceptual .
�� �Notadefuentessobreeltítulodelasesión. Laslide1rotulaestasesióncomo “S02 – Creatividad
y definición de solución”,mientrasquelaplanificacióndelaS1(slide2delaClase1)larotulabacomo
“Creatividad · Pruebas funcionales · Pruebas no funcionales” . Elcontenidoefectivamentecubiertoabarca
ambasformulaciones,más historiasdelcliente ,queeseltemadecierre.
����RESUMENEJECUTIVO
EstasegundasesiónrespondealapreguntaquequedóabiertaenlaClase1: unavezqueséquedeboprototipar,
¿cómodefinoconprecisiónquéesloquevoyaconstruir? Larespuestasearmaendosmitades. Laprimera
mitades creatividad: se definecomo la habilidadde sobreponerse alos límites (Ackoff& Vergara)y comoel
actodeprovocarresultadosoriginalesydevalor(Amabile),sostenidoportresfactoresquedebenintersectarse—
motivación,especialidadyhabilidaddepensamientocreativo . Seadviertesobrelos silenciadoresdeideas y
sepresentaelperfildel superforecastercomoeltemperamentodeseableeninnovación. Lasegundamitad,que
eselnúcleoevaluabledelramo,esel modelodetrescapasdeladeseabilidad : todasoluciónseexplicaporsu
funcionalidad(lastareasrudimentariasquecumple),su usabilidad(losatributoscualitativosconquelascumple)y
sumaterialidad(laformaconcretaytangibleenquesellevanacabo). Sobreesascapassemontanlosdosgrandes
regímenesdepruebadelramo: las pruebasfuncionales (unitarias,deintegración,deaceptación,deregresión),
queverificanquealgohaceloquedicehacer,ylas pruebasnofuncionales (compatibilidad,estrés,seguridad,
usabilidad,rendimiento,escalabilidad,mantenibilidad,instalabilidad,internacionalización),queverifican con qué
nivel de calidad lohace. Seentreganherramientasdecreatividadaplicada—el cuestionamientofuncional,el
SCAMPERyel reencuadre—ycatálogosdeatributos( ElementsofValue B2CyB2B, approachdecalidad). Laclase
cierraconla historiadelcliente (“Como un {usuario} quiero {objetivo} para {razón}” )comounidadoperativaque
bajatodoloanterioraunbacklogdedesarrollo,juntoconlasdosestrategiasparaenriquecerla: dividirhistorias
grandesybombardearconelementosnofuncionales . Elmensajetransversal: elsoftwarenoeselvalor—el
valoreselproducto—yunbuenproductoexige planificaciónexplícitaenlastrescapas ,nounacorrientede
conciencia.
�CONCEPTOSCLAVEDELACLASE
1

## Lamina 2

# Concepto Prioridad Porquéimporta
1 Lastrescapas:
Funcionalidad·Usabilidad
·Materialidad
Esencial ������ESelconceptodela
clase;slides10–14;
estructuralaEntrega1
2 Deseabilidadcomo
condicióndeefectodel
producto
Esencial Slide10;esloquelastres
capasexplican
3 Pruebasfuncionales(4
tipos)
Esencial Slide16;laEntrega1se
evalúaexactamentecon
esto
4 Pruebasnofuncionales(9
tipos)
Esencial Slide29;basedela
Entrega2
5 Elementosfuncionales
vs.nofuncionales
Esencial Slides15y28;visible
vs.novisible
6 Historiadelcliente:
estructurayuso
Esencial Slides42–43;sepide
explícitamenteenla
Entrega1
7 Lasdosestrategiasde
historiaavanzada
Esencial Slide44;dividir+
bombardearconno
funcionales
8 Definicióndecreatividad
(Ackoff&Vergara;
Amabile)
Esencial Slides3y4;definiciones
formalesexigibles
9 Lostresfactoresdela
creatividad(Amabile)
Esencial Slide4;motivación+
especialidad+habilidad
10 ElárbollógicoFunción→
Tarea→Atributo→
Materialidad
Esencial �� � �Formulaciónoraldel
procedimiento
11 Cuestionamientofuncional
comopalancacreativa
Esencial �� � �“Elprimercomodín
bajolamanga”
12 Tiposdesoluciones:
físicas,digitales,
intangibles
Importante Slides37–40;lamayoría
delassolucionesson
intangibles
13 SCAMPER Importante Slide25;metodología“de
facto”segúnelprofesor
14 Silenciadoresdeideas Importante Slide6;higienedetrabajo
enequipo
15 ElementsofValue(B2Cy
B2B)
Importante Slides30–31;catálogode
atributosnofuncionales
16 Approachdecalidad—
análisisexhaustivo
Importante Slides33–34;13
dimensionesdeanálisis
17 Consideracionesdel
usuario(7dimensiones)
Importante Slide58;quémirarantesy
despuésdeunprototipo
18 Variablesdesegmentación
(consumidores
vs.organizaciones)
Importante Slide59
19 A/Btestingcomoprueba
univariable;sesgodel
canalbeta
Importante �� � �Soloentranscripción
20 Superforecasting Complementario Slide7;perfilde
temperamento,nomateria
dura
21 ReframingCanvas
(ThomasWedell)
Complementario Slide26;elprofesordice
quenoseveenesteramo
22 Definicióndetecnología Complementario Slide36
2

## Lamina 3

# Concepto Prioridad Porquéimporta
23 Ejemplos: músicocallejero,
Dominó,islademall,
WOM,Starbucks
Complementario Ilustranlastrescapas;muy
útilescomorespaldo
��� �§0. INFORMACIÓNADMINISTRATIVADELRAMO
Todalainformaciónoperativadadaenestasesiónestáconcentradaaquí. Elrestodeldocumentoes
contenidoconceptual.
0.1 �� � �Ajustedelcalendariodeentregas
Elprofesor modificólaplanificación respectodeloanunciadoenlaClase1: lasentregasse condensanenlas
últimastressemanas ,demododedejar dossemanasdetrabajoparaelprimerprototipo .
Entrega Cuándo(segúnlodichoenclase) Foco
Entrega1 Endossemanasmás Definicióndesolución+historias+
coberturafuncional
Entrega2 Entressemanasmás Testeoconusuariosymétricas
Entrega3 Últimasemana delramo Mejorademostradadelprototipo
• Razóndeclaradadelcambio: “es mejor para tener un poco más de tiempo para digerir lo que estén construyendo” .
• Sontresversionesdelmismoprototipoquevaairmejorando ,notresproyectosdistintos.
• �� � �Eldesafíoespecíficodela Entrega3aúnnoestabadefinido almomentodelaclase, “entendiendo que
hoy día terminar la solución, que funcione, es muy fácil… toma minutos” .
0.2 �� � �PautadelaEntrega1(Demo1)—leerconatención
Lasinstruccionesyaestán subidasaCanvas . Formato:presentaciónenvideodemáximo20minutos ,enviada
alprofesor(lasrevisatodas). Además,encadasesiónpresentarán ~3equipos envivo,solohaciendo demodel
prototipo(treslaprimerasemana,treslasegunda,ytodosenlaúltima).
Loscuatropuntosexigidos:
1. Definirlasolución quevanadesarrollar.
2. Determinarentre5y10historiasdelcliente/usuario. Cadahistoriadebetener:
• unenunciadodesdeelpuntodevistadelcliente,enprimerapersona ,y
• undetallenofuncionalymaterial decómoseresuelvelahistoria.
• Esdecir: “deben haber condiciones de logro y satisfacción claras asociadas a componentes específicos” . El
profesorlodescribecomo “unaplanificacióndeproductobienestricta” .
3. Seleccionaruna(oalgunas)deesashistorias paratrabajarenelprototipo, explicarporquéseeligióesa
porsobrelasotras ,yexplicar quévanaconstruirfuncionalmente .
4. Demostrarunprototipoconcoberturacompleta dela(s)historia(s)elegida(s): 100%delasfunciones
definidas,cubiertas. “Tienen que demostrar que el prototipo hace todo lo que dijeron que iban a hacer las dos
historias. Todo.”
LoqueNOseevalúaenlaEntrega1: - �Nosepiderendimientodeatributosnofuncionales. “Solo comprobar
que cumpla con sus funciones principales.” - �Noseevalúasilasoluciónesútilosifuncionabien: “Si eso es útil,
no es útil, no es problema de esta primera entrega.” - �Nohayreglasdetesteoconusuariosenestaentrega(eso
empiezaenlaEntrega2). - ��Loquesíseaplica: pruebasfuncionalesydeaceptaciónmuybásicas .
�� � �Sobre el origen de las historias (pregunta de un alumno):no hay pauta ni filtro. Pueden ser historias
hipotéticasconstruidasporelequipo. Laposturadeclaradadelprofesoresde escuelaágil: “es mejor construir, es
3

## Lamina 4

decir, establecer hipotéticamente algo y construir con eso, y después con eso levantar información” ,envezdepartir
preguntándolealusuario—porquelevantardatatomamuchotiempoyhoyconstruiresbarato. Sinoconocenel
dominio,puedenusar informaciónprimaria (personas)o secundaria(Internet: G2,Trustpilot,Reddit),quehoyse
recomiendamuchoporque “hay información súper visceral” dondelagenteexplicitaquélepasó.
0.3 �� � �Equipos
• 20personas enlanómina. Unaalumnapidiótrabajar solaporunproyectopropio(autorizado).
• Configuraciónestimadaporelprofesor: cuatrogruposdecinco ,aunque gruposdeseisnosonproblema
(yahabíaunoformadodeseis).
• Losequiposyaarmadosdeben enviarseporcorreoelectrónico alprofesor.
• Aquienesnotenganequipo,elprofesorlosasigna, evitandorepetirintegrantesdeequiposderamos
anterioresparaasegurarvariedad.
0.4 �� � �Talleres
• Miércolesde19:00a21:00 ,comenzando elmiércolessiguienteaestaclase .
• Quedangrabadosysesuben elmismodía víaYouTube/Canvas.
• Nosepudocambiaralsábado(preguntadeunalumno): elhorariodelprogramanolopermiteylostalleres
sonuna actividadcomplementaria,nooficial .
• Contenidodelprimertaller: setup. Conectarseaagentesparapoderprogramar;semostrarácómotrabajar
conCodexyClaudeCode,ycómoconectarsea GeminivíaGoogleAIStudio (capagratuita).
• Contenidoposterioranunciado: definirhistoriascon skillsenlabasedecódigo,mandarlasa GitHubcomo
issues,milestonesyroadmapgestionablesporelagentevía GitHubCLI;gitworktrees paratrabajaren
paralelo;subagentes;ylascapasdeunaaplicaciónconIA(texto, text-to-speech, speech-to-text, embeddingsy
basesvectoriales).
0.5 �� � �HerramientasdeIA—decisióndelcurso
• Geminieslaopcióngratuita: capagenerosa,delordende 1.600solicitudesdiariaspormodelo ,con~4
modelosdisponibles. Losmodelosde textosongratuitos;losde imagennormalmenterequierenactivar
billing.
• Sehizouna encuestaporWhatsApp entrelosalumnos. Resultadoleídoenvozalta: lamayoríaseinclinapor
Codex;tambiénaparecen ClaudeCode,Antigravity(elIDEdeGoogle, “como Visual Studio pero en el entorno
de Gemini”)y MicrosoftCopilot.
• Decisión: “vamos a trabajar con Codex y ahí voy a mostrarles también con Claude Code” . Elprofesordeclaraque
losusacasiindistintamente;prefiereClaudeCodeporque “me permite observar mejor lo que están haciendo
los subagentes”.
• Requisitopráctico: usaralgunadelastresaplicacionesdeconsola —Codex,ClaudeCodeoGeminiCLI.
0.6 �� � �Recursosrecomendadospara benchmarkingdematerialidad
ElprofesormostróenvivocuatrofuentesyofreciódejarenlacesenCanvas:
Recurso Paraquésirve
TrendHunter Verproyectosyproductosnuevosqueestáhaciendola
gente
Behance Propuestasconceptuales,nuevostiposdesoluciones,
porcampocreativo
YCombinator—StartupDirectory Estadodelarteenstartups,buscablepor batch;muy
cargadoaSaaSyalgode hard tech
a16zSpeedrun (AndreessenHorowitz) Programadeaceleración;alternativaaldirectoriodeYC,
consedesenSanFranciscoyNuevaYork
4

## Lamina 5

Recomendaciónexplícita: “es una buena época para pensar en grande, porque hoy con relativamente poco esfuerzo
uno puede competir con equipos que tienen millones de dólares en ingeniería” .
0.7Bibliografíadelasesión(slide60)
Libro Autores Paraquélorecomienda
Gamestorming DaveGray,SunniBrown,James
Macanufo
“Técnicas rápidas de creatividad”. �� � �
“Si ya de entrada les tincó el
SCAMPER, cómprense
Gamestorming”;librodeconsulta
rápida,clásicodedinámicasde
innovación
MappingExperiences JimKalbach “Pensar en multiproductos / Construir
interacciones”. Diseñodeservicios
DesigningforBehaviorChange StephenWendel “Resolver problemas comunes de uso
/ Evaluar interacción”. �� � �Elprofesor
lodestacacomo ellibropara
desarrollarcriteriode
materialidad
�� � �Complementariosofrecidosenclase: -LacharlaTED “Laperspectivaloestodo” deRorySutherland (slide
32),~15minutos,sobrelaimportanciadelosfactoresemocionalesfrentealosmeramentefuncionales. Yahabía
sidorecomendadaenelramoanterior. -Un instructivodereencuadre queelprofesorelaborópara CMPC;ofreció
compartirlocomomaterialcomplementarioporsermetodologíapúblicasincláusuladeconfidencialidad.
2.0Encuadre: porquéunramodeprototiposseapellida“creatividad”—
Importante
�� � �Todaestasecciónprovienedelaexposiciónoralinicial.
• “El apellido es creatividad porque el proceso de construir es muy importante para el proceso de innovación, y yo
diría que es de las cosas que tienen un impacto mayor en el desarrollo de habilidades creativas.”
• Mecanismodeclarado: larepeticióngenerahabilidad. Elactoderepetiralgounayotravezhaceque
unosevuelvamáshábilcreandoenesecontexto. “La práctica hace al maestro.” Secitacomoreferenciaque
elemprendedorpromedioreciénlevabienalrededordelsextouoctavonegocio,porquealiniciohayque
aprenderdetodo.
• Construirsueltalamente. Meterlemanoaalgotécnicoayudaadestrabarelpensamiento;hayunpuntode
inflexiónenquelascosas“hacenclic”.
• Laincomodidadespartedelproceso ,especialmenteensoftware: “hay gente que no podía con el proceso de
que tenías que fallar mucho, demasiado, en programación” .
• Cambiodefocorespectodeversionesanterioresdelramo: antesseenseñabalapartedecodificación
necesariaparaarmarprototipos. “Ahora como eso ya no se necesita” ,elfocosetrasladaaquelosalumnos
seanbuenosobservandounsoftware ydetectandocómosepodríanarreglarcosas,ya cómosetestea
software(queesloquesetrabajaráenlostalleres).
• Culturadeinnovación: “equivocarse es parte de la regla del juego” . Elcontrastedifícilaparececuandoun
negocioyatomóvueloyhayqueestabilizarlo,queeselmundoenquevivelamayoría.
5

## Lamina 6

2.1Creatividad: definicionesyfactores—Esencial
2.1.1Definición1—Ackoff&Vergara(slide3)
“Lacreatividadeslahabilidaddesobreponersealoslímites.”
�� � �Lectura del profesor:“siempre hay límites, siempre hay límites, y uno siempre los va empujando, y esa es la
parte más interesante de esto”. Aplicadoalramo: alconstruirlaprimeraaplicaciónapareceránlímitestécnicos,y
sobreponerseaellos eselejerciciocreativo.
2.1.2Definición2—Amabile(slide4)
“Lacreatividadesprovocarresultadosoriginalesydevalor.”
Ysesostienesobrela interseccióndetresfactores :
ESPECIALIDAD
▲
│
PENSAMIENTO CREATIVO
╱ ╲
MOTIVACIÓN HABILIDAD
Factor Quésignifica(slide4+ �� � �desarrollooral)
Motivación Hayque quereraprender/haceralgo. �� � �“A menos que
lo hagan por la fuerza”,lamotivaciónescondiciónpara
desarrollarcualquieridea
Especialidad Tenerconocimientostécnicos deloqueseestá
haciendo. �� � �“Cuando uno le aplica técnicas a las cosas,
también va a avanzar más rápido”
Habilidad(pensamientocreativo) �� � �Seaprendeeneltiempo;incluyecierto nivelde
aperturaaequivocarse
�� � �Corolarioprácticosobreeltalento: eltalentoexisteyesrelevante,perola técnicaaceleraenormemente .
Recomendaciónoperativaderivada: pedirayudaalinicio yacercarseaalguienqueademásdeexperiencia tenga
pedagogía. “Si quieren armar aplicaciones, acérquense a alguien que ya construye aplicaciones y que también le
guste enseñar.”
2.1.3ModelocomponencialdeAmabile(slide5)—Importante
Fuentecitada: The Social Psychology of Creativity: A Componential Conceptualization ,TeresaM.Amabile.
Componente Incluye Dependede
Dominio/especialidad Conocimientodeldominio·
Habilidadestécnicas·Talento
relevanteparaeldominio
Habilidadescognitivasinnatas·
Habilidadesperceptualesymotoras
·Educaciónformaleinformal
Habilidadescreativasrelevantes Estilocognitivoapropiado·
Conocimientoexplícitoeimplícito
delaheurísticaparagenerarideas
nuevas·Estilodetrabajoconductivo
Entrenamiento·Experienciaen
generacióndeideas·Características
depersonalidad
Motivaciónfrentealatarea Actitudesfrentealatarea·
Percepcionesdemotivaciónpropia
paraenfrentarlatarea
Nivelinicialdemotivaciónintrínseca
·Presenciaoausenciade
restriccionesextrínsecasenel
ambientesocial·Habilidadde
minimizarcognitivamentelas
limitantesextrínsecas
6

## Lamina 7

�� � �Notasdeclasesobrecadauno: -Sobrela heurísticaparagenerarideas : existenmuchasmetodologíasde
brainstorming;elprofesormencionaSCAMPERyellibro Gamestorming. -Sobrelas actitudesfrentealatarea :
laclaveesquelatarea noseaengorrosa paraquienlahace. “Para alguna gente sentarse a construir algo es el
infierno”,yparaotraeslonatural. -Sobrela motivaciónpropia: “hay que creerse el cuento” . Almirarhistorias
deemprendedoresnosevenhiperhabilidades,sinogentequesetomóenseriolacuestión,empezó,aguantóy
empujó.
2.1.4 �� � �Lafronteracreatividad↔innovación(repasodelaClase1,reformulado)
Formulacióndadaenestaclase,másprecisaqueladelaClase1:
Algo NUEVO pero NO ÚTIL productivamente → no genera retorno → NO hay innovación
Pero: NO HAY INNOVACIÓN SIN CREATIVIDAD.
������ “Acuérdense que uno puede generar creatividad, pero si lo que hacen es simplemente algo nuevo pero
no útil a nivel productivo para una empresa o una persona, no genera retorno: no hay innovación. Pero
siempre parte de la creatividad. No hay innovación sin creatividad, ojo con eso. ”
Esdecir: lacreatividades condiciónnecesariaperonosuficiente delainnovación. Loquefaltaeselretorno.
2.2Silenciadoresdeideas(slide6)—Importante
Definiciónoperativa: frasesoactitudesque cortanelflujocreativo enunequipo. Fuente: Barriers to Creativity,
GaryA.Davis.
Catálogocompletodelaslide:
Nuncahemoshechoesoantes ¿Estásloc@? Noestáenelpresupuesto
Nopuedeserhecho Esunapérdidadetiempo Tienepocasposibilidades
Demasiadoacadémico Esteeselúltimointento Teestoydiciendo,novaafuncionar
Hacesdemasiadaspreguntas Novaafuncionarennuestro[barrio] Lohicimosbiensineso
Discutámosloenotromomento Metienesqueestarleseando ¿Ves? Nofuncionó
Noentiendeselproblema Esperemosyveamos Nopodemoshacerloconestas
regulaciones
Vaasignificarmástrabajo Alguienyalohabríasugeridosi
fueratanbueno
�� � �Comentariosdeclasesobreporquécadatipoesdañino:
Tipodesilenciador Porquédaña
“Nunca hemos hecho eso antes” Cierralapuertaalodesconocido. Muycomúnhoycon
IAgenerativa: “nunca hemos ocupado agentes para
hacer tal cosa”. Lainstrucciónes nopensarsiquieraesa
ideayaplicarlasnuevastécnicasparatestear
“Tiene pocas posibilidades” Anticipaelfracasoantesdeintentar. Cuandounose
ponedesafíostécnicos, leestáponiendo
intencionalmenteincertidumbretécnicaaloutput :
esoespartedeldesafíoasumido,noundefecto
“Lo hicimos bien sin eso” Agarrarsedeexperienciaspreviasparanegarcosas
nuevas;muycomún
“No está en el presupuesto” / “Este es el último intento” Ponencondicionesdeborde artificialesqueasfixianla
conversación
�� � �Regladehigienecreativa: “traten de mantener una conversación fluida, sin muchos juicios” . La
ausenciadejuicioprematuroesloquehaceposiblelaexploración.
7

## Lamina 8

2.3Superforecasting(slide7)—Complementario
Fuente: Superforecasting: How to upgrade your company’s judgment ,PaulJ.H.SchoemakeryPhilipE.Tetlock,2016.
�� � �Porquéapareceaquí: eninnovaciónnobastaconquererhaceralgonuevoyvalioso; “para eso tienes que
ser bueno pensando en qué es lo que viene” . Elperfildelbuenpronosticadorcoincideengranmedidaconelperfil
creativo.
Dimensión Rasgos(slide7)
Puntodevistayaproximaciónfilosófica Cautos (pocascosassonciertas)· Humildes(aprecian
suslímites)· No-deterministas(noasumenqueloque
ocurreteníaqueocurrir)
Habilidadesyestilosdepensamiento Aperturamental (vencreenciasehipótesiscomoalgoa
testear)· Indagadores·Reflexivos(autocríticose
introspectivos)· Matemáticos(cómodosconnúmeros)
Métodosdeprevisión Pragmáticos (nocasadosconlaagendadenadie)·
Analíticos(consideranotrasvistas)· Sintetizadores·
Enfocadosenprobabilidades (no“cierto/nocierto”,
sinomásomenosprobable)· Actualizadores
conscientes(cambiandeparecercuandoloshechoslo
ameritan)· Conscientesdesussesgos cognitivosy
emocionales
Éticadetrabajo Mejoramientomental (buscansermejores)· Tenacidad
(seapeganaunasuntomientrasseanecesario)
�� � �Conexiónconlaculturadedatosenstartups(dichoenclase): -Losbuenosequiposdeinnovaciónestán
muyorientadosalosdatos ;cuandounastartuptomadecisionesrápido, “en general es porque la cultura es una
cultura orientada a datos”. -Elpatróndetrabajo: “uno plantea las cosas como hipótesis — ‘mi hipótesis respecto a
esto es esto’ — pero al final del día uno casi siempre trata de mirar los números duros” . -“Se simplifica mucho la toma
de decisiones cuando uno tiene un buen modelo de medición.” →anticipala clasedemétricas (S3/S4).
2.4 ������DESEABILIDADYLASTRESCAPAS—ELNÚCLEODELACLASE
2.4.1Deseabilidad(slides10y11)
Deseabilidad: condición de efecto del producto, en la que se manifiesta la forma en que sus usuarios lo
adoptan. (slide10)
�� � �Precisionescríticasdadasenclase: -Esuna condicióndeefecto ,nounacondicióndeintención: “independiente
de que a uno le guste o no le guste, es lo que logró ”. -Incluyeelcasoenqueelproductoseusadeformadistintaa
ladiseñada: “quizás diseñé un objeto para un fin y la gente lo empezó a ocupar de otra forma — que también pasa
harto”. -Esunconceptoabstractoque seexplicacontrescapas .
�� �ConexiónconlaClase1: enlaS1aparecióla estructura de deseabilidad comoherramientadeideación(slide13
delaClase1). Aquíseretomaelmismoconceptoy seledasuestructurainternaoperativa .
2.4.2Lastrescapas(slide11)—definicionesoficiales
Capa Definición(slide11)
FUNCIONALIDAD Tareasofuncionesquecumpleunproductooservicio
8

## Lamina 9

Capa Definición(slide11)
USABILIDAD Característicasdeunproductoquelodestacandelresto
delassoluciones
MATERIALIDAD Formamaterialyconcretaenquesellevaacabouna
solución
�� � �Precisiónoralimportantesobrelajerarquía: - “Las primeras dos son casi calcadas de cómo uno las utiliza
después en otro concepto” →funcionalidadyusabilidadsecorrespondencon elementosfuncionales yelementos
nofuncionales (secciones2.5y2.7). - ������ “La usabilidad es literalmente la representación de la experiencia del
usuario… en el software se llama la capa no funcional .”
2.4.3 ������ �� � �Elárbollógico(procedimientocentraldelaclase)
EstaeslaformulaciónoperativaqueelprofesordaexplícitamenteyqueestructuralaEntrega1:
PRODUCTO
└── FUNCIÓN ¿qué hace? (tareas rudimentarias, sin juicio)
└── TAREAS
└── ATRIBUTOS ¿cómo lo hace? (capa cualitativa: rápido, barato, fluido…)
└── MATERIALIDAD ¿con qué, exactamente? (números, colores, medidas, stack)
�� � �“El árbol lógico siempre es el mismo. Uno dice: tengo un producto, tengo una función, y esa función
tiene distintas tareas. Esas tareas tienen distintos atributos, y esos atributos yo los materializo de alguna
forma.”
Eltestdelamaterialidad: cadavezqueapareceunadjetivo,hayqueexigirleunnúmeroouncomponente.
Sedice… Lapreguntadematerialidades…
“queseaintuitivo” ¿Quéesintuitivo? →tienequehaberuníndiceaquí,
estegráficocontalescolores…
“queatiendarápido” ¿Quéesrápido? ¿Cincominutos? ¿Cuántasdecisiones
puedetomarelusuario?
“quesearesistente” “¿Resistente cuánto? Esa es la pregunta del millón” →
140kilos,¿conquématerial,revestimiento,pintura?
������Regladeordendetrabajo( �� � �,muycitable): > “Lo primero que hay que hacer es armar un buen producto.
Y el buen producto no es software. El software normalmente es como una liability. La verdad, el software en sí, el
código, no aporta valor — es algo que hay que hacer para construir el producto. Y lo importante es el producto.”
Reciéndespuésdedefinidalamaterialidadsepasaalaarquitecturadesoftware. Elprofesordescribesupropio
flujo: “prácticamente cualquier feature que parto pensando, normalmente parto con una historia del cliente, después
lo bajo a esto, y después me pongo a trabajar en arquitectura de software” .
2.4.4 �� �� � � �Ejemplointegrador1: elmúsicocallejero— �� � �(todooral)
Ejercicioabiertoalaclase: ¿qué es importante para alguien que toca música en la calle? (slides8y9sonlasimágenes
deapoyo).
Aportesdelosalumnosysíntesisdelprofesor:
Capa Quéapareció
Funcionalidad(tareas) Tocarmúsica· Seleccionarellugar (puntodealta
afluencia)· Presentarse/establecervínculoconel
público·Impresionar·Conectar
9

## Lamina 10

Capa Quéapareció
Usabilidad(atributos) Queelinstrumentosea pococomún (unsaxofónllama
máslaatenciónqueunaguitarra)·Calidaddelartista·
Niveldevínculologrado
Materialidad Formato“escenario”·Presentaciónbreveantesde
empezar·Performanceimprovisadavs.interacción
directa·Ubicaciónespecífica
Quéenseñaesteejemplo: 1. Todoproductooserviciocumpletareasrudimentarias ,inclusolosmás“artísticos”.
“Las tareas son bien fundamentales y no tienen un juicio de cómo se están haciendo, sino que simplemente se hacen.”
2. Elresultado(quelagenteledédinero) esladeseabilidad ; lastrescapaslaexplican. 3. Lametodologíaes
transversalacualquiertipodeproducto : “desde un software hasta tocar música en la calle” . Estoconectacon
diseñodeservicios yconloqueeninformáticasellama diseñodedominio : sermuybuenolevantandoladatade
enquéconsistelainteracciónensunúcleo. �� � �“Para ser un buen product manager o un buen product owner tienen
que ser buenos haciendo eso.”
2.4.5 �� �� � � �Ejemplointegrador2: Dominó— �� � �(todooral)—muycitable
Cadena chilena de comida rápida (completos, sándwiches) concaso de estudio en Harvard sobre eficiencia
operacional.
Bajadaalárbollógico:
Capa EnDominó
Funcionalidad Elclientetieneque tomardecisionesparaelegirun
plato
Usabilidad Quesea rápido
Materialidad ������Lacartaesmatricial : filasporcolumnas(recetas×
tipodepan×tamaño). Elclienteeligehaciendoun“X
porY”envezderecorrerunalista. Además: personal
paradoenlaentradaqueatiendeapenastesientas
(tiempodellegadaalamesa estudiado);maquinitade
Redcompraenelcinturón decadaatendedor; PDA
quemandaelpedidodirectoalacocina
Quéenseña: queunatributoblando(“rápido”) seganacondecisionesmaterialesconcretas ,noconvoluntarismo.
“Es tan simple como eso: hay una matriz y la persona toma una decisión muy rápido.”
�� � �Versiónactualdelmismopatrón: hoylossoftwaredegestiónderestaurantesgeneranlascomandasautomáti-
camente. “Antiguamente había empresas que se daban la vuelta para poder lograr esa interacción; hoy día ya es más
estándar.”
2.4.6Lostresejemploscanónicosdelasslides12–14
Elprofesorrecorretresproductosenlastrescapas. Estatablaeslamásprobabledeserevaluadacomoejercicio.
Silla/mobiliario Ropa Redessociales
FUNCIONALIDAD(slide
12)
Transporte·Adorno·Usar
espacio·Soportar
Adornar·Lavar·Cubrir·
Identificar
Publicar·Buscar·
Asombrar·Entretener
USABILIDAD(slide13) Ergonomía·Estética·
Voluminosidad·
Capacidad(peso,espacio)
·Calidaddemateriales
Estética·Resistencia·
Calidaddefibra·Variedad
Velocidad·Atingencia·
Facilidaddeuso·
Dinamismo
10

## Lamina 11

Silla/mobiliario Ropa Redessociales
MATERIALIDAD(slide14) Estiloestéticoparticular·
Dimensiones· Specsde
resistencia·Materiales
específicos
Estiloestéticoparticular·
Variantes(colores,tallas,
diseño)·Fibraespecífica
Tiempoderespuesta·
Requerimientosde
hardware·Tasadeuso·
Cantidaddepasos·
Tiempodecontenido
�� � �Comentariosdeclasesobrecadauno:
Silla: - “Las sillas no solo se usan para soportar algo o para que alguien se siente, sino que también hay que poder
transportarla; también son adornos; también usan espacio.” Haysillasapilablesjustamenteporeso. -Lassillas
declarancuántoaguantan(130,150,200+kg)→esoesusabilidad; conquémateriallologran esmaterialidad.
-Proliferaciónyseguimientodeestándares: cuandounproductofísicoescalaanivelpaísocontinente, “casi
todas las mesas tienen la misma medida; el estilo cambia, pero los casos de uso están súper estudiados” ,inclusocon
tamañosestándardeestacionesdetrabajoytiposdeenchufes/interruptores.
Ropa: -Laropa identifica: lagenteusaunestiloparaidentificarseconalgo. - Trade-offdeexpectativaspor
segmento: enmarketplacesderopabaratala variedadesgiganteyelpreciobajo;elusuario noesperalafibrade
másaltacalidad ,porque “son otras las características que mueven ese negocio” . -��Estoeslacurvadevalor del
ramoanterior: determinarquécaracterísticassonimportantesycompararquiénlashacemejor paraunsegmento
enparticular.
Redes sociales:- Laatingencia se resuelvea nivel algorítmico→ eso es materialidad. - Ejemplo TikTok: la
percepciónesqueelalgoritmo “es muy equilibrado para hacerte aparecer también cuando no eres muy grande” ,
loqueledioimpulsoinicial. Elprofesoradviertequenoestansimple: “también hay que hacer calzar a la gente
apropiada”. -Ejemplomaestrodematerialidad—YouTube: almedirentiemporeallacalidaddeinternetdel
usuario,bajalacalidaddelvideoa240penvezdecortarlo. ������ “Ese tipo de decisiones hacen que uno tenga un
software mucho más resiliente.” -Lalecciónsemántica: hayqueseparar lotangible (unalgoritmoquemapea
automáticamentelas specsdeldispositivoylaconexión)de elfin (queelsoftwaresearesilienteantecondiciones
adversas). Lomismoaplicasielteléfonoestásobrecargadodememoria. - Inventariocomoatributodelnegocio:
enplataformasmultilateralesdedistribucióndecontenido(tipoYouTube)haydoslados—quienpublicayquien
consume—yademásdemanteneraudiencia “tienes que mantener un inventario de contenidos ”. Enmuchos
mercadosel inventariodedatos escríticoyseolvida.
2.5ElementosfuncionalesyPRUEBASFUNCIONALES—Esencial
2.5.1Elementosfuncionales(slide15)
Definición: “Los elementos funcionales son componentes de la solución que son visibles a los usuarios ;
usan espacio en una pantalla o tienen alguna representación física en un aparato o dispositivo.”
Complementosdelamismaslide: - Enunservicio ,unelementofuncionales “una interacción que funciona vía
múltiples productos”. -Son laspiezasfundamentales deunasolución,quedespuésdebenser organizadaso
inclusoexploradas paraserabordadasdeformasnovedosas. - ������“Losmodelosmentalessonlabasedesu
logro.”
Enobjetosfísicos Ensoftware/servicios
Botón·Escalera·Perilla·Pantalla Pedircomida·Agendar·Enviarunmensaje·Calcular
resultado
�� � �“En los objetos son los componentes visibles con los cuales uno puede interactuar; en el software es distinto, porque
ahí ya son las cosas que puede hacer el software.”
11

## Lamina 12

2.5.2Pruebasfuncionales(slide16)— ������basedelaEntrega1
Descripción: Pruebas basadas en la ejecución, revisión y retroalimentación de funcionalidades previamente
diseñadas en el producto.
Objetivo: Identificar y resolver inconsistencias en componentes dentro de un producto o sistema.
�� � �Formulaciónoral: “Es toda una rama de pruebas que se utilizan justamente para verificar que algo funciona en su
capa más básica: la cuestión funciona o no funciona. Querés saber si hace lo que tiene que hacer. Después empezás a
analizar cómo lo hace, si lo hace con el nivel de calidad que te imaginaste.”
Loscuatrotipos(slide16)+desarrollodeclase
Tipo Definiciónslide �� � �Desarrolloenclase
Pruebasunitariasyde
componentes
— Pruebade unaunidaddesoftware
muypequeña. Ejemplodado: sihay
3rolesdeusuarioycadaunopuede
editardistintoscamposdelperfil,se
escribecódigodepruebaquedice
“esta persona ejecuta esta acción de
actualizar perfil → el resultado
debería ser el perfil actualizado”. En
softwaremaduroexisten suitesde
11.000a30.000pruebasunitarias ,
organizadasporcanales (ej. canal
deautorizacióndeusuario),de
mododenoreprobartodoel
softwareencadadespliegue. ������
Sonrestrictivas: sinosepasan,la
actualizaciónnollegaalentorno
productivo. Tambiénaplicaacapas
deagentesgenerativos: sehacen
pruebassobrelos prompts
Pruebasdeintegración (gruposde
unidades)
— Cuandoseintegranunidadesentre
sí. ������ “Yo diría que son las pruebas
más difíciles, porque es donde se
empiezan a generar las
inconsistencias”
Pruebasdeaceptación Verificación de funciones requeridas
para lanzar versión
Normalmenteunapruebaconuna
persona: lasUAT(User Acceptance
Testing). Consisteenverificarcon
alguiensilafuncióntienelas
característicasquenecesita. “Que
alguien te diga: esta solución
funciona o no funciona”
Pruebasderegresión Divergencias funcionales por cambio
actual
“Pruebas para volver al pasado…
tener que dar unos pasos para atrás
para ver si algo funciona también
con otras capas antiguas”
�� � �Porquéimportanparaelramo(dichodosveces): > “De esto, la primera entrega tiene mucho que ver. Van a
tener que establecer una solución, establecer casos de uso, y en la primera entrega poder demostrar que hacen lo que
dicen que deberían hacer. De eso se trata. Es tan simple como eso.”
�� � �AplicaciónaltrabajoconIA(anunciodetaller): laspruebasunitariassirvenparatener higienealpedirle
cambiosaunagente, “para que no estén dando esa vuelta en círculo” yparatener unaformapredecibledesaber
queloquehicieronantessiguefuncionando .
12

## Lamina 13

2.6Ejerciciodecreatividadaplicada: observar,exploraryreencuadrar—
Importante
Lasslides17–24sonun ejercicioguiado sobredosobjetos: una butacadelujo (sillaloungeconotomana)yuna
isladeretailenunmall (marcaBurt’sBees). Eslaaplicaciónprácticadetodoloanterior.
2.6.1Lasecuenciadepreguntasdelejercicio
Slide Pregunta Respuestasregistradas
17–18 ¿Quéfuncioneshaceel
[producto]? (butaca)
Soporta·Contiene·Adorna·Se
acarrea·Usaespacio
19 ¿Quéhaceel[producto]? (islade
mall)
�� � �Verabajo
20–21 ¿Quéescomúnydiferenteentre
estos[productos]? (butacavs.isla)
N.ºdeusuarios·Cantidadde
objetosqueledanvalor(2vs.n)·
Estética·Materiales·Recursos
visuales·Tamaño
22 ¿Sonlosfinessimilaresenestos
[productos]? (butacadelujovs.silla
ejecutivademalla)
�� � �Verabajo
23 Observar/Explorar ¿Quéestáfueradelugar? ¿Quées
raro? ¿Quésepodríamejorar? ¿Por
quéelproductosoloesasí? ¿Qué
pasaríasi…?
24 ¿Quépasaríasi…? (butaca
vs.estacióngamermultipantalla)
¿Ysielobjetoestuvierapensado
paraconteneraunapersona yuna
mascotamediana? ¿Ysi
pudiésemosunirlacomodidadcon
eltrabajooelentretenimiento ?
2.6.2 �� �� � � ��� � �Elcasodelaislademall—lalecciónmássutildelaclase
Aportesdelosalumnos: -Laislasirvepara comprasimpulsivas,noplanificadas: “oh, qué lindo esto, y te lo llevas de
una”. -Sueletener productospococomunes ;verropaenunaislaharíapensarqueesunatiendachicayperdida.
-Unalumnorecuerdaquehaceaños elconceptodeislanoexistía : esosespaciosdelmallquedabanbotados
hastaquelasadministracionessedieroncuentadequepodíanarrendarlos. Hoyestánllenos,einclusohayferias
artesanales,máquinasexpendedorasyespaciosmásgrandesconjuegos.
Síntesisdelprofesorporperspectiva:
Perspectiva Funcionalidad(tareabásica) Roldelaisla
Elempresarioquearriendalaisla Ocuparunespaciolimitado y
llamarlaatención rápidamente,
porquelapersonavapasando
Laislaesel producto
Eldueño/administradordelmall Optimizarlarentabilidaddel
espacio
������Laisla sevuelvematerialidad :
es “un mecanismo más de cómo
cobrar más”,juntoconferias
artesanales,máquinas
expendedoras,etc.
13

## Lamina 14

������Lalección: lamismacosacambiadecapasegúnquiénseaelsujetodelanálisis. Loqueparaun
actoreslasolucióncompleta,paraotroessololaformamaterialderesolverunatareadistinta. Antesde
aplicarelárbollógicohayque fijardequiéneslafuncionalidadqueseestáanalizando .
�� � �CasoWOM(aportedealumno, validadoporelprofesor): alentraralmercadochileno, WOMusó islas
comoformatodeentrada enubicacionesclavededistintosmallsantesdetenertiendaspropias;lasfilaseran
enormesyfuncionaroncomoindicadortemprano. Conesosdatosdeterminarondespuésdóndeubicartiendas. >
��ConexiónconlaClase1: “Esa es la parte potente de la presencia pop-up: tenés los stands, las islas, o también los
food trucks. Como medio guerrilla, pero si lo hacés bien, es muy poderosa la herramienta.”
2.6.3 �� �� � � ��� � �Butacadelujovs.sillaejecutiva(slide22)
Dosproductos técnicamentecasiequivalentes : ambospermitenunaposicióndedescansosimilar,apoyolumbary
depiernas. “Pero uno sabe por intuición que son productos muy distintos a nivel de experiencia del usuario.”
Quéenseña: lafuncionalidadnodiscrimina . “Es común que uno analice estos productos y las tareas sean las
mismas.” Ladiferenciareal( “no se va a sentir elegante” )vive enlascapasdeusabilidadymaterialidad . ������Por
esoexistenlasotrascapas.
2.6.4 ������ �� � �Elcuestionamientofuncional—“elprimercomodínbajolamanga”
Estaeslatécnicacreativacentralqueelprofesorentrega:
1. Tomo un objeto o software cuya función doy por hecha.
2. Pregunto: ¿por qué no lo amplío y permito que haga OTRAS funciones?
3. Agrego una tarea que normalmente el producto NO hace.
→ Resultado: productos "a lo menos raros", que ya tienen el check de creatividad.
“Lo primero que uno puede hacer es decir: ya, tengo un objeto o un software que hace una función que yo
doy por hecho que es su fin. Pero, ¿por qué no lo amplío y permito que haga otras funciones? ”
Ejemplodesarrollado(slide24): unasillaenlaque tambiénsepuedejugar . “Es parte de la tarea de la silla
entretenerte con multimedia.” Conesalógicasepodríaademásimaginarunsistemadeaudiointegrado.
�� ��� � �Advertenciametodológicaimportante—cómoNOhacerlo: >Antelaobjeción “pero podrías agarrar el
parlante y ponerlo donde quisieras” : “asínofuncionaeltemadelacreatividad. Lacreatividaddice: méteteal
conceptoqueestátratandodehacer.” Esdecir,hayque entrarenlalógicainternadelapropuesta envezde
refutarlaconlasolucióngenéricaexistente. Paraalguienqueproducemúsicatienesentido: losparlantesdeben
estaralaalturaexactadeloído,yunasillaesunentornocontroladoquepermiteresolvereso(sonidoespacial).
�� �� � � �Ejemplodealumno(slide27,imagen;explicación �� � �solooral): unprototipodehace~10añosquehace
uncuestionamientofuncionalalosinterruptoresdeluz . “Los interruptores solo tienen que ser para prender y
apagar la luz — ¿por qué no podría ser algo también ornamental?” Elresultadoesunapiezatemática(estéticade
videojuegos,tipoZelda). Elprofesorobservaquehoyesmuchomásfácilllegaraproducto: “en esa época había que
ir a un laboratorio”,mientrasquehoyconimpresión3Dunemprendedorpuedearmarunmoldeyunaempresade
objetosrápidamente.
�� � �NotasobreIAgenerativaycuestionamientofuncional: “Con la IA generativa muchos software que uno tenía
como limitados, ahora con agentes… te permite hacer muchas más cosas.” Larazóntécnicadada: anteslosdatos
estructuradosestabanacotadosacálculosdeterminísticos;ahorasepuedenescribirenesosobjetos“conclusiones”
oclasificacionesdifícilesdearmarconunalgoritmo .
2.6.5MétodoS.C.A.M.P.E.R.(slide25)—Importante
Versiónmásordenadadelcuestionamientofuncional. �� � �“Yo diría que es la de facto, es de las que más se usa. Ha
resistido todo el embate del tiempo.”
Elacrónimo:
14

## Lamina 15

Letra Acción
S S ustituir
C C ombinar
A A daptar
M M agnificar
P P onerenotrosusos
E E liminar
R R educir/ Reordenar
Secruzaconunsetdedimensiones: Personas·Lugares·Tiempos·Partes·Funciones·Resultados.
Procedimiento( �� � �): setomaunproductoosituacióndereferenciaysejuegaconlascombinaciones. Ejemplo
dadoconunapelota: “¿Cómo podría sustituir los lugares en los cuales se utiliza este producto?” →parquecon
perros,conniños,piscinas,etc.
Paraquésirve: “Es un ejercicio que les permite, de forma relativamente lúdica, encontrar otras opciones… para soltar
rápido la cabeza.”
2.6.6ReframingCanvas—ThomasWedell(slide26)—Complementario
�� ��� � �Elprofesordiceexplícitamente: “Esto no es un tema que vemos en este ramo.” Seincluyeporcompletitud
yporqueofreciómaterialcomplementario.
Fase1—ENCUADRE: ¿Cuáleselproblema? ¿Quiénestáinvolucrado? Elegir 2problemasdeáreasdistintas,
quenoseanmuybásicos ,deestostipos: 1. Problema maldefinido opuntodedolor( “Me siento estancado…”)2.
Objetivoquenosesabecómolograr (“Cómo logramos USD$3MM…”)3. Alguienseenamoródeunasolución
(“Deberíamos desarrollar…”)
Fase2—RE-ENCUADRE(5lentes):
Lente Preguntas
Mirarfueradelacaja ¿Quénoestamosconsiderando? ¿Quéestamos
ignorando?
Repensarlameta ¿Hayalgúnobjetivomejorparabuscar?
Examinarpuntosbrillantes ¿Dóndenoestáelproblema? Excepcionesno
excepcionales·Buscartambiénenexcepcionespositivas
·Problemagatilladoperoirrelevante
Mirarseenelespejo ¿Quéelementopuedeserdemasiadovisibleparamí?
¿Quénoestásiendoconsideradodesdemiperspectiva?
¿Quémiradaexternamepuedeayudar?
Tomarlaperspectivadelresto Listarinvolucrados·Desfragmentarmotivosde
stakeholders·Buscarexplicacionesrazonables:
explicacióninocente,razonesválidas,mejoresintereses,
problemasdeincentivoyproblemasdesistema
Fase3—CONTINUAR(mantenerelmomentum): ¿Cómopodemostestearelproblema? ·Describirelproblema
a stakeholders·Conseguirexternos·Arreglarunasoluciónforzada/ prototiparsolución
2.7ElementosnofuncionalesyPRUEBASNOFUNCIONALES—Esencial
2.7.1Elementosnofuncionales(slide28)
Definición(slide28): “componentes de la solución que no son visibles a los usuarios , sino que son
asociaciones de valor positivas y negativas que resultan del producto o servicio.”
15

## Lamina 16

“Loselementosnofuncionalesmanifiestanelrendimientodeunasolución.”
�� �Errataenlaslide: eltextodelaslide28empiezaliteralmentecon “Los elementos funcionales son componentes
de la solución que no son visibles…”. Poreltítulodelaslideyporelcontexto,evidentementeserefierealoselementos
nofuncionales. Tenerlopresentesiaparecelaslideenunaevaluación.
Ejemplosdelaslide: Estética·Eficiencia·Compatibilidad·Facilidaddeuso·Placer·Cobertura·Completitud
�� � �Precisionesdeclase: - ������ “Los productos en su esencia hacen cosas súper rudimentarias… pero uno elige una
solución versus otra porque la hace de alguna manera distintiva, con alguna característica que es más marcada.” -
Hayasociaciones buenasymalas : “algunas que son buenas, algunas que son malas, pero son parte de lo que marca
el producto”. -������Sonfactoresrelativos: “la eficiencia no es lo mismo para todas las personas” . Poresorequieren
otrotipodepruebas . -Reglanemotécnicadadaenclase: “siempre que hablamos de algo no funcional, hablamos
de atributos”.
2.7.2Pruebasnofuncionales(slide29)— ������basedelaEntrega2
Descripción: Procedimientos para verificar algún requisito específico para juzgar la operación de un
sistema.
Objetivos:-Ajustarunproducto,servicioosistemaa requisitosespecíficosauncontextodereferencia
deconsumo. -Integrarvariablesdecalidadsubjetivasauncontextoobjetivo.
�� � �Formulaciónoral: “son procedimientos para uno saber si la característica que uno está buscando se cumple y en
qué nivel”.
Losnuevetipos(slide29)+desarrollodeclase
# Tipo �� � �Desarrolloenclase
1 Compatibilidad —
2 Estrés Muycomúnensoftware. Sedeclara
“esto va a ser usado por 10.000
personas”yhayqueprobarquela
máquinasirvaa10.000. ������
Distincióncrítica: 160.000usuarios
alolargodeundía vs.160.000
simultáneosson “dos software
completamente distintos”.
Distribuidoseneldía,nuncahay
másde~150almismotiempo
3 Seguridad Ver2.7.4
4 Usabilidad Ver2.7.5
5 Rendimiento —
6 Escalabilidad —
7 Mantenibilidad —
8 Instalabilidad Ver2.7.6
9 Internacionalización Ver2.7.7
2.7.3 ������ �� � �Elproblemadel over-engineering(preguntadealumno)—muyexaminable
Pregunta: enunemprendimientounoquieremoverserápido;pruebasdeestrés,rendimientoeinternacionalización
parecen over-engineering. ¿Cómosebuscaelequilibrio?
Respuestadelprofesor,encuatroreglas:
1. ������Elproductomanda. “Las cosas importan siempre que al cliente le importen… si es determinante para el
producto, el producto siempre determina cuál es la prioridad .” Ejemplo: siunmercadocorporativo exige
SOC2,hayquesacarSOC2,nohayescape. Sinoesrestrictivo,dalomismo.
16

## Lamina 17

2. Utilitarismotemporal. “No me voy a poner a hacer pruebas de estrés si no me voy a poner a pensar en 10.000
usuarios cuando tengo 10.” Critica “toda la cuestión rimbombante de la arquitectura para una aplicación que
están ocupando cinco usuarios”.
3. ������Elrefactoringesunbuenproblema. “Cuando tengas que hacerle refactoring a la solución para adaptarla
a un contexto más grande, es un problema bueno normalmente, y cuando tengas ese problema normalmente
tienes los recursos para resolverlo .”
4. Mododetrabajo: “levantarme en modo urgencia y hacer lo que es urgente… es mejor vivir en modo zen, pero
apurado”. Confocoenelproducto.
�� �Matizaparentementecontradictorio,dichomásadelante: “Al menos desde un punto de vista de arquitectura
de software, creo que siempre hay que armar el software para el peor escenario posible… pero solo si es parte del
producto.” La condición final reconcilia ambas afirmaciones: el peor escenario se diseñacuandoelrequisito
perteneceefectivamentealproducto .
2.7.4 �� � �Pruebasdeseguridad—notasdeclase
• Tienenmuchasubjetividad: “depende de la empresa con la cual uno trabaje… para algunos la seguridad son
un par de revisiones y para otros la verdad son…” organizacionesmuymadurascon cincoáreasdedicadas :
hardening,seguridaddeaplicaciones, compliance,bugbounty,entreotras.
• ������Filosofíadediseñocentral: “uno diseña el producto no [solo] para que no tenga problemas de seguridad —
idealmente uno trata de aspirar a eso — sino que una parte importante es qué pasa cuando ocurre el incidente
de seguridad… cuál es el protocolo.”
• Ladificultadestructural: como el incidente rara vez ocurre,“nunca de facto implementaste el protocolo,
nunca lo viviste”. Lomismopasaenorganizacionesquemanejanemergencias: noesfácildereplicarenel
ambiente.
• Elprofesorapuntaquelaseguridad “va a estar hot por mucho tiempo” comoramaprofesional.
2.7.5 ������ �� � �PruebasdeusabilidadyA/Btesting—contenidoimportante,solooral
Opinióndeclaradadelprofesor: “Las pruebas de usabilidad son las más engorrosas, las pruebas que más detesto
hacer, porque son muy lentas.”
Elargumento(marcadoporélmismocomo“opinióncontroversial”):
Backend Frontend/UX
“Casi todo lo que uno hace lo puede reducir a números, o
a algo determinístico”
“No hay una respuesta que tiene una forma clara”
Testearlosiempreesobjetivo →procesofluido,poco
estrés
Sepuedevalidarquehaceloquetienequehacer, pero
paraquefuncionedependedequealusuariole
guste
Complejidadprincipalmentedediseñoe
implementación
“Y eso ya es iterar, iterar, iterar, iterar” ·Enaplicaciones
muyinteractivas haymuchacomplejidadtécnica
A/Btesting(preguntadealumno)
Concepto Definicióndadaenclase
PruebaA/B ������Pruebaunivariable: “son A-B porque uno cambia
una variable”. Ejemplo: elmismocorreocon dos
asuntosdistintos adospersonas,paravercuál
enganchamásrápido
Pruebamultivariable Paranegociosmuygrandes(semencionaMercado
Libre): segmentarusuariosporgrupos ytestear
distintosabordajesensimultáneo
Inferenciaquepermite “¿Cuál es la forma más ad hoc para enganchar con este
segmento?”
17

## Lamina 18

������Elsesgodelcanalbeta—trampaconceptualclásica
Preguntadealumno: “¿es como cuando una página te dice ‘prueba nuestra beta de la nueva versión’?”
Respuesta:síesunmecanismo, peronoesunapruebaobjetiva :
Quien se mete a un canal beta = el usuario MÁS AVEZADO
≠ el usuario promedio
Además: los canales beta advierten que hay features experimentales
que pueden hacer que la solución funcione de forma inconsistente.
→ Quien toma ese riesgo no es el usuario promedio.
������Regladeobjetividaddelaprueba: “Para que una prueba sea objetiva, la prueba siempre tiene
que ser en condiciones que es como a ciegas . Porque si tú sabes que es parte de algo experimental,
probablemente lo vayas a ocupar más porque querías meterle más — versus algo que simplemente está
ahí, y lo usaste o no lo usaste.”
Cómolohacenlasaplicacionesgrandes: mantienenlasmismasinterfacesporcoberturaydisponibilidadde
servicios,y ajustanalgorítmicamente loqueaparecedentro,paraobservarlareaccióndelosdistintossegmentos.
�� � �Notasobreusuarioscorporativos(aportedealumno,validado): elusuariocorporativoprefiere “que sea
aburrido, pero que funcione”,loquechocaconloscanalesexperimentales. Seilustraconelantiguo mododeveloper
deChatGPT paraconectarservidoresMCP,queponíaunanillonaranjodeadvertenciaalrededordelcuadrode
texto: “la persona no va a hacer esa cuestión” . Hoyesmuchomásfácilporlaexistenciadeunprotocoloestándarde
integración.
2.7.6 �� � �Instalabilidadyportabilidadcomoventajacompetitiva
• “Hay muchos softwares que son muy fáciles de instalar o muy fáciles de portar. Para los usuarios hoy día eso es
muy importante.”
• Doscriteriosqueelprofesorconsidera estándarbásico:
1. Queelusuariopueda probarrápidamente elsoftwareparavercómolefunciona.
2. Quepuedasacarsusdatos eirseaotrosoftware. “Que no tengas un login, empieces a ocupar un software
y después no tengas cómo sacar tus datos.”
• ������ “Para armar un buen software hoy día, no es solo tu función principal: realmente tenés que hacerlo portable,
tenés que hacerlo fácil para que el usuario se pueda mover para otro lado.”
• Recomendaciónfuerte(ydiscutible,presentadacomoopinión): “Si diseñan un software, no le armen el login
[de entrada], porque hoy día la gente no quiere logins. Búsquense otra estrategia para que le vean el valor.”
2.7.7 �� � �Internacionalización—dosejemplosconcretos
Ámbito Ejemplodado
Productofísico Lossellosdeadvertencianutricionalenalimentosen
Chile: “si querés venir a Chile, tenés que ponerle sellos a
tu producto”,ademásdelasetiquetasdelpaísdeorigen
Software Enunastartupde reclutamientoconIA ,lanormativa
europeadeproteccióndedatosesmásrestrictivaquela
chilena. ������Consecuenciadediseño: “hay ciertos
procesos que siempre tienen que ser verificados por
personas… el robot te puede hacer el análisis y decirte
cuáles son los factores, pero una persona siempre tiene
que tomar la última decisión ”. Esoobligaaque el
softwaretengaunpasomásyunainterfazdistinta
Lección: unarestricciónregulatorianoessolountrámite: setraduceenpasoseinterfacesadicionales ,
esdecir,enmaterialidad.
18

## Lamina 19

2.8Catálogosdeatributos: TheElementsofValue—Importante
Amboscatálogossirvencomo inventariodeatributosnofuncionales alquerecurrircuandohayqueenriquecer
unahistoriadelcliente.
2.8.1ElementsofValue—B2C(slide30)
Fuente: EricAlmquist,JohnSenioryNicolasBloch,2016.
Principiorectordelaslide: “El peso del valor percibido es lo más importante en una interacción.”
Pirámidedecuatroniveles(delabasealacúspide):
Nivel Elementos
FUNCIONAL Ahorroentiempo·Simplificar·Hacerdinero·Reducir
riesgo·Organizar·Integrar·Conectar·Reduciresfuerzo
·Evitarmolestias·Reducircosto·Calidad·Variedad·
Apelativosensorial·Informar
EMOCIONAL Reduciransiedad·Recompensar·Nostalgia·
Diseño/Estética·Valor·Emblema·Salud·Valor
terapéutico·Diversión·Atractivo·Accesibilidad
CAMBIAVIDA Motivación·Reliquia·Pertenencia·Esperanzar·
Auto-actualización
IMPACTOSOCIAL Trascendencia
������ �� � �Advertenciacentraldelprofesor(aparececomopreguntadeexamenprobable): > “Esto no significa
que unos sean más importantes que otros . El impacto social no es más importante que cambiar la vida, sino que
por producto a veces hay manifestaciones que son más comunes .”
Ejemplosdadosparailustrarlo:
Tipodeproducto Elementosdominantesesperados
Softwareparagestionarcuentaspersonales Funcionales(utilitaristas,orientadosatareas)
Unclubderunningparaunperfilparticular Emocionales—hayque “buscar alguna temática que lo
enganche”
2.8.2TheB2BElementsofValue(slide31)
Fuente: EricAlmquist,JamieCleghornyLoriSherer,2018. “Los elementos principales del valor para ‘clientes negocio’.”
Cinconiveles(delabasealacúspide):
Nivel Sub-categorías Elementos
REQUERIMIENTOSDEENTRADA — Cumplirespecificaciones·Precio
aceptable·Cumplimiento
regulatorio·Estándareséticos
VALORFUNCIONAL Economía · Rendimiento Líneatopemejorada·(−)costos·
Calidaddeproducto·Escalabilidad·
Innovación
19

## Lamina 20

Nivel Sub-categorías Elementos
FACILIDADDEHACERVALOR Productividad · Operacional · Acceso ·
Relacionamiento · Estratégico
Organización·Simplificación·
Conexión·Integración·
Configurabilidad·(−)riesgo·
Alcance·Flexibilidad·Calidadde
partes·Menoslíos·Información·
Transparencia·Variedad·
Compromiso·Estabilidad·Calce
cultural·(−)tiempo·(−)esfuerzo·
Disponibilidad·Responsividad·
Expertise
VALORINDIVIDUAL Carrera · Personal Expansióndered·Comerciabilidad·
Reputaciónasegurada·Diseñoy
estética·Crecimiento·(−)ansiedad·
Diversión
VALORINSPIRACIONAL Propósito Visión·Esperanza·Responsabilidad
social
2.8.3RorySutherland—“Laperspectivaloestodo”(slide32)—Complementario
Tesisdelaslide: “Las circunstancias de nuestra vida pueden ser menos importantes que el cómo las
percibimos. Puede ser hasta poco conducente preocuparnos de cambiar la realidad, si es que lo más
importante es la percepción.”
�� � �Por qué la recomienda aquí:porque en los productos“uno normalmente se da demasiado a los factores
funcionales — simplificar, ahorrar tiempo, hacer dinero — pero a veces es muy importante que haya factores
emocionales”. Mencionaquelacharlatocatemasde gestión/percepcióndecontrol ,quetambiénsevenen
diseñodeinteracciones.
2.9 Approachdecalidad—análisisexhaustivo(slides33y34)—Importante
�� � �Quées: unaformanormadadeanálisis(semencionala normaISO comoreferencia)queconsisteen “separar una
solución en distintos factores que uno considera relevantes y después ir revisándolos para ver cómo están cumpliendo
o no esas características”.
Es,enlapráctica, elcatálogomásdetalladodeatributosnofuncionalesdelramo .
Dimensión Sub-criterios(slides33–34)
Capacidad Funciones/Tareas: quépuedehacerelproducto
Rendimiento Monetario/recursos: quéimpactoderecurso· Valor
intangible: quéimpactosimbólicogenera
Usabilidad Aprendibilidad: quétancomplejoeshacerusodeél·
Operabilidad: quécaracterísticasyhabilitantesrequiere
suoperador;quétansimpleesmanipularlo·
Accesibilidad: quédisponibilidadtiene,quiénpuede
usarlo
Confiabilidad Seguridadymanejodeerrores: cómoreaccionaante
ocurrenciasnodeseadas· Integridad: cómose
mantieneíntegroenocurrenciasnodeseadaso
escenariosextremos
Seguridad Autorización: quécredencial/entidadesnecesariapara
suuso· Privacidad·Vacíos:cómosehacecargodelos
errores
20

## Lamina 21

Dimensión Sub-criterios(slides33–34)
Escalabilidad Capacidaddemejoras: quéespaciodaparaser
mejorado· Modularidad: quécapacidadpermitepara
separarlasmejorasenbloques/pasos
Compatibilidad Consistemasparticulares (delusuario/cliente)· Con
sistemasglobales (estándaresglobales)· Conel
pasado(explotarecursosdesarrolladoseneltiempopor
elcliente)· Conelusoderecursos (seacoplaacómola
organizaciónproduceresultados)
Instalabilidad Requerimientos·Configuración·Desinstalación: qué
serequiereparadejardeusarlo,quécostogenera
dejarlo· Modificación: ¿esposibleajustarlo?
Soportabilidad Funciones: quépuederesolverseconsoporte·
Modalidad: quéserequiereparasersoportable
Testeabilidad Etapas: quésepuedeprobarantesdesercomprado·
Representatividad:niveldeveracidaddelaspruebas
Mantenibilidad Costoseneltiempo: fijosyvariables· Modalidades:
quémezcladeesfuerzos(monetarios/objetos/
humanos/otros)
Localizabilidad Regulaciones·Lenguaje·Diferenciassocio-culturales
·Disponibilidadderecursos alcambiardecontexto
Portabilidad Impactoenelespacio
�� � �Comentariodelprofesorsobreparaquésirverealmente: > “Cuando uno hace una startup o un producto
nuevo, la motivación principal es que uno tiene un punto de vista respecto a cómo hay que hacer las cosas … uno
quiere armar el producto para que quede como uno quería que quedara. Entonces uno se mete en: ¿qué es usabilidad?
¿qué significa que algo sea usable? Que sea más fácil de aprender, más fácil de operar, más accesible.”
Ycierra: “hay muchos factores para hacer un producto subjetivamente bueno… pero ahí cada uno va desarrollando
su punto de vista respecto a su producto” .
�� � �Sobreel análisisdecapacidad ensoftware: sepuedellevar “una especie de inventario de cómo funciona el
software”. Elprofesorobservaqueelpropiocódigo “te dice qué es lo que el software hace, de forma súper tácita” .
2.10Materialidad: tecnologíaytiposdesoluciones—Importante
2.10.1Tecnología(slide36)
Definición: “Conjunto de conocimientos técnicos, científicamente ordenados (que tienen un método),
que permiten diseñar y crear bienes y servicios que facilitan la adaptación en el medio ambiente y satisfacer
tanto las necesidades esenciales como los deseos de la humanidad.”
������ �� � �Precisiónclave(trampaconceptual): > “Tecnología, para los más puristas, no son las cosas digitales . Nor-
malmente son todas las cosas que uno pueda utilizar para adaptarse mejor a un entorno, ya sea desde metodologías
hasta abstracciones, objetos o lo que sea .”
2.10.2Tiposdesoluciones(slide37)
21

## Lamina 22

FÍSICOS DIGITALES INTANGIBLES
Definición Solucionesqueson
tangiblesenelmundo
físico
Interaccionesqueocurren
enunainterfazque
funcionaenunsistema
operativocomputacional
Solucionesquesebasan
eninteracciones,
acuerdosyestímulos
cognitivosqueresultan
enlasignificación
Ejemplos Objetosymateriales·
Estímuloscognitivos
básicos(luz,tacto,sonido,
olores,gusto)
Solucionesdeinternet·
Aplicacionesmóviles·
Softwaredeescritorio·
Recursosmultimedia·
Licencias
Serviciosdepersonas·
Metodologías·Conceptos
·Algoritmos·Experiencias
·Recuerdos·Activos
financieros·Eldinero·
Estándares
������ �� � �Tesiscentraldeestasección: >“Lamayoríadelassolucionessonintangibles.” “Cuando uno se mete en
tangibilidad, en general uno se mete en hartas cosas de significación o acuerdos incluso… La verdad son abstracciones,
no es algo tangible que uno pueda tocar.”
Yelcorolario,queelprofesorplanteacomo elgrandesafíodeldiseñodeproductos : >“Hacer productos es difícil
porque uno quiere aspirar a un concepto, pero entre querer hacerlo y lograrlo hay una brecha bien grande .”
2.10.3 �� �� � � �Lostresejemplosdesarrollados(slides38–40,56,57)
A)Starbucks(slides38y56)
Capa Elementos
FÍSICO Vaso·Café·Luz·Cadapartedelainfraestructuradela
tienda·Vestimentadelpersonal·Colores·Sabores
DIGITAL Redessociales·Páginaweb·Fotosyarchivos
multimedia
INTANGIBLE Conceptode“lugarparatenerreuniones”·Decoración
contemporánea·Caféarábicaahumadointenso·
Conceptode“lugarparaestar”·“Espaciosvariados”·
Productos“siúticos”·Exclusividad·Unatienda“bonita”·
Losqueatiendensonordenados·Saboresricos·Café
de“malacalidad”·Conceptodelugarparahipsterscon
laptops·Aparienciarústico-industrial·“Equipoatento”
�� � �Observacióndeclase: Starbuckses “un lugar casi por defecto para la gente ir a trabajar, y no solo por la mesa ni
la luz”. Nótesequelalistaintangible incluyeasociacionesnegativas (café de “mala calidad”),coherenteconla
definicióndeelementosnofuncionalescomo “asociaciones de valor positivas y negativas” .
B)Unaaplicaciónwebcolaborativa(slide39)
Capa Elementos
FÍSICO Colores
DIGITAL Lapáginawebcomosistemainteractivoquefunciona
mediante python + mysql + javascript + css + html
22

## Lamina 23

Capa Elementos
INTANGIBLE Aplicaciónmoderna·Simplezaestéticadeinterfaz·
Aplicaciónconveniente·Diseño“flat”,estilo“Material
design”·Permitetrabajarmejor·El stackmismo·
Conceptodetrabajocolaborativo· Seguridadde
“productoGoogle”: siesGoogle,esbueno ·Servicio
pagadoopremium·Appsenlanube·Funcionesdela
plataforma(exportación,guardararchivos,procesar
multimedia)
C)Launiversidad/elpropioramo(slide40)
Capa Elementos
FÍSICO Infraestructura·Materialfísicodeclase·Mobiliario
ergonómico/mobiliarioanticuado·Ladisposiciónde
losmuebles
DIGITAL Páginawebdelauniversidad·Plataformadigital·
Materialdigital·Plataformasinteractivas
INTANGIBLE Estatusintelectual ·Marcadelauniversidad·
Efectividaddeaprendizaje·Metodologíaformativaen
suconjunto·Cadaclase(experienciainstruccional)·
Conceptosespecíficosdelaclase· El“aprendizaje” ·
Conceptodetipodeprofesor
D)Lasíntesis(slide57)
FÍSICO+DIGITAL+INTANGIBLE=“Elgrandesafíoparadesarrollarsolucionesqueseancorre-
spondidasporlosdeseosdelaspersonas.”
Laslidetomaelementosdelostresejemplosanterioresylosmezclaenunsoloplano—elpuntoesque una
soluciónrealsiemprecombinalastresnaturalezas .
2.11 ������ HISTORIAS DEL CLIENTE — Esencial (tema de cierre y eje de la
Entrega1)
2.11.1Elpuente: delateoríaalusocotidiano(slide41)
“Un featurees,ensimple,algoquequierehacerelcliente. Podríamosrelatarlocomounahistoria
enunasituación.”
�� � �“Uno toma una situación de referencia y la convierte en situaciones que son representativas, contextos que son
muy comunes. Y eso es lo que se llaman las historias de los clientes.”
2.11.2Definiciónyreglas(slide42)
Historiadelcliente: “Descripción simple dicha desde la perspectiva de una persona que desea lograr
algo nuevo (una función nueva o una función ya existente con nuevas características ).”
La historia es la unidad más popular para generar requerimientos en unbacklog de desarrollo(lista de
requerimientos/tareasqueelproductodebecumpliroquesedebendesarrollar).
Reglasdelaslide: -Seescriben aliniciodeunproyecto ytambién cuandosehacenmejoras . -Cualquier
integrantedelequipopuedeescribirunahistoria. -Unconjuntodehistoriasrelacionadasoindependientesse
23

## Lamina 24

denominaEpic. UnproyectoesunconjuntodeEpics, peroelEpicseconstruyedespuésdelashistorias . -Un
Epicesseleccionarhistorias. - ������Jerarquía: proyecto > epic > historia
�� � �Bajadaaherramientas(dichoenclase):
Historia → Issue (tarea con descripción y criterios) → Backlog (Scrum) → Sprint
• EnScrumlalistadetareassellama Backlog;en GitHublashistoriasseconviertenen issues.
• Tambiénexistenlos Sprints: “nos sentamos a hacer una planificación y decimos: las próximas dos semanas
vamos a estar trabajando esta historia” ,muyfocalizados.
• �� �Realismosobrelaplanificación: “uno no adivina el futuro. Cuando uno empieza a trabajar en algo, mientras
va trabajando van saliendo nuevos temas… no es que al inicio uno defina todos los issues perfectamente .
Idealmente uno se acerca a eso, pero después va ajustando sobre la marcha.”
• Elprofesoraclaraque lametodología(Scrum,Sprints)noesmateriadeesteramo ,perosíelconceptode
historia.
2.11.3 ������Historiabásica—lafórmula(slide43)
Como un(a) {usuario} quiero {objetivo} para {razón/motivo}
Lostresejemplosoficialesdelaslide:
Historia
Como cliente quiero ver algo llamativo para recordar el local
Como estudiante quiero que me ayuden con recordatorios para cometer menos errores y aprobar el ramo
Como gerente quiero tener un resumen rápido para dedicarme a tomar decisiones
�� �Lostrescomponentessonobligatorios. LaEntrega1exigeexplícitamenteelenunciadoenprimerapersona
desdeelpuntodevistadelcliente.
2.11.4 ������Historiaavanzada—lasdosestrategias(slide44)
Estrategia1—Dividirhistoriasgrandesenhistoriaspequeñas
Historiamadre(deliberadamentemala): Como gerente quiero tener un resumen rápido para dedicarme a tomar
decisiones.
�� � �Porquéesmala: “Es una historia buena para subdividirla porque no dice nada . Te está diciendo ‘un resumen
rápido’, ¿pero qué es un resumen rápido?”
Sub-historias(slide44): 1. Quiero ver en qué está cada colaborador para saber si tengo que ayudar o llamar
la atención de alguien 2. Quiero saber las últimas actualizaciones por proyecto para entender qué ha pasado
últimamente3. Quiero ver algún indicador de actividad global para [saber] si estamos haciendo más o menos que
[mes/día…]
Estrategia2—Agregarcondicionesdeéxito/logroosatisfacción
������“Bombardearconelementosnofuncionales.” (frasetextualdelaslide)
Tomandolasub-historia2( “Quiero saber las últimas actualizaciones por proyecto” ),lascondicionesquelaslide
agrega:
24

## Lamina 25

# Condición Quétipodecondiciónes
1 Verquéactualizacionessonnuevas;
omitirlasyarevisadas (loggerde
vistas)
Funcional+materialidad
2 Que noseantantasporeltamaño
delapantalla(máx. 10) ;porlo
mismo,latarjetanopuedesermuy
grande
Materialidadconnúmero
3 Quetenga prioridadenlatarjeta
losmetadatos delproyecto
involucrado
Materialidad
4 Quehayauna guíavisual que
determineenquépartedelproceso
totalestáavanzado
Materialidad
5 Seconsideraexitoso queveael
resumenynotengaqueirmuchoa
lavistaindividualdelproyecto→
medirtasadeconversiónvista
resumenvs.singular
������Condicióndelogromedible
6 Recibirun correoderesumen
semanalconlosavancesdecada
proyecto
Funcionaladicional
������Nóteseelpunto5: eselmodeloexactodeloquelaEntrega1pidecomo “condiciones de logro y satisfacción
claras asociadas a componentes específicos” —yestambiénelpuentehacialaclasedemétricas.
�� � �Elejemploalternativodesarrolladoenclase(recomendablememorizarlo)
Degenéricaatrabajable:
Versión Historia
�Genérica Como gerente quiero tener un resumen rápido para
dedicarme a tomar decisiones
��Específica Como gerente necesito ver todos los lunes un informe
de incidencias de seguridad para poder establecer
una lista de tareas con mi equipo
Porquélasegundaesmejor: “Porque después vos decís ‘ya, está la lista de incidencias’, y eso sí lo podés trabajar :
ahí podés empezar a meterte en temas de funcionalidad, usabilidad y materialidad.”
Cómosesigueelhilo(cuestionamientodeatributos): -Sitengounalistadeincidenciasyladecisióntieneque
serrápida→ “¿tengo que enriquecer esa lista? ¿Tiene que haber un ranking? ¿Tiene que haber un top 5? ¿Cómo
hago que el gerente convierta esa lista en una recomendación de planificación de tareas de la semana ?” - �� � �
BajadaaIAgenerativa: “Podrías agarrar toda esa lista de incidencias, pasársela a un agente y que te la convierta en el
formato de planning que necesites.” Peroprimerohayquepensarelcasodeuso.
�� �� � � �Casorealmencionado: enunastartupdereclutamiento,elCEOrevisaunreportedequéhacecadareclutador,
loquelepermiteconocerel throughputdecadacolaboradoryajustarelequipo condatadura . Eslasub-historia
1delaslide44enproducción.
2.11.5LastablasHistoria→Funcionalidad/Usabilidad/Materialidad(slides45–55)
Estasslidesmuestranelejerciciocompletoaplicadoa onceproductosconocidos ,conelformato:
25

## Lamina 26

HistoriadelCliente Funcionalidad Usabilidad Materialidad
Productoscubiertos: herramientasdeIAconversacional(45),repositoriosdecódigoycontroldeversiones(47),
repositoriodemodelosdelenguaje(48),plataformadee-commerce(49),agregadordecontenidos(50y53),video
corto(51),espaciodetrabajo/notas(52),visualizacióndedatos(54), notebooksdecienciadedatos(55).
Todasllevanlanota “GeneradoporChatGPT3.5–V.August52023” .
Ejemplodesarrolladoenclase(slide45):
Historia Funcionalidad Usabilidad Materialidad
Como usuario, quiero
generar texto
automáticamente…
Generacióndetextoa
partirdeinstrucciones·
Respuestascoherentesy
relevantes
Interacciónnatural
mediantelenguaje
humano
Plataformabasadaen
GPT-3queprocesay
generatexto·Modelode
lenguajeentrenadoen
datosdiversos
Como redactor, quiero
mejorar la calidad de mi
escritura…
Ediciónyrevisiónde
contenido·Variedaden
estilosdeescritura
Ayudaenlaedicióny
correccióndetextos·
Capacidadparaadaptar
estilos
Herramientasdeedicióny
sugerenciasgramaticales
Slide46—elzoomsobrelamaterialidad: tomalafrase “Modelo de lenguaje entrenado en datos diversos” yla
aterrizaenalgoconcretoyverificable: StanfordAlpaca,un fine-tuningdeLLaMA7B con52Kmuestras,conenlace
alrepositorio. > ������Quéenseña: queunafrasedematerialidadtodavíavaga( “datos diversos”)puedeydebe
bajarseaunartefactoespecífico(quémodelobase,quétamaño,cuántasmuestras).
2.11.6 ������ �� � �Cómosedesarrollael“buengustomaterial”—consejooperativo
Estepasajees larespuestadelprofesoralapreguntaimplícita“¿cómollenolacolumnadematerialidad?” :
“La funcionalidad y la usabilidad en general dependen de que ustedes conozcan el dominio y el contexto.
Pero tener buen gusto material toma mucho tiempo de ser desarrollado .”
Larecomendaciónconcreta: hacer benchmarking. > ������ “Yo creo que una buena forma de tener una buena
materialidad es haciendo un benchmarking. Cuando ustedes se pongan a armar una solución, deberían investigar
qué está haciendo el resto .”
�� � �Ejemplodeconvergenciaestéticamencionadoenclase: elprofesormuestraelsistemadecomponentesde
interfazquehoyusalamayoríadelasaplicaciones(transcritocomo “Chat 100”;muyprobablementeshadcn/ui ),
señalandoqueestátanextendidoque “la gente ya empezó a disgustarlo” . Reconocequeélmismolousa, “un poco
más colorido”,porqueescomoestáconstruidalamayoríadelasaplicacioneshoy.
�� ��� � �AdvertenciasobreIAycalidaddeproducto(muycitable): > “Uno puede hacer un buen desarrollo técnico
con IA, pero hacer un buen producto es difícil , porque la mayoría de las veces la IA generaliza mucho: se va a lo más
evidente, a lo más aceptado, pero no es muy creativa . Así que la mayor parte de hacer un buen producto depende de
ustedes.”
Ysobreescala: “la parte técnica es muy fácil hoy día… pero el software a gran escala sigue siendo difícil. En bases
chicas podés sacar un prototipo en 20 o 30 minutos; en un software grande hacés una modificación chica y son dos
horas iterando”.
2.12Consideracionesdelusuarioysegmentación—Importante
2.12.1Consideracionesdelusuario(slide58)
Quéson: “Aclaraciones a considerar antes y posterior al análisis de un prototipo.”
26

## Lamina 27

Dimensión Definición Ejemplodelaslide
Actitudenlastareas Quéfuncionessonlasmáscomunes
eimportantes,ysurecurrencia
Enunsoftware,lasherramientas
tienendistintoniveldejerarquíay
visualizaciónenpantallasegún
cuántasveceslasusemos
Modelosmentales Cómolaspersonas organizansus
tareasysuinformación
Unmelómanotienesusarchivos
organizadosportipodemúsica,
artistasyálbumes;unapersona
promediotiene unacarpeta con
todasumúsica
Motivacionesyobjetivos Razónporlacualuna
persona/empresadeciderealizar
unatareayquemarcaunadiferencia
sustancialensucomportamiento
Laautoimagenoestatus que
podríagenerarcomprarunamarca,
vs.lacalidadpercibida
Dominiodetecnologíay/o
habilidades
Cómolashabilidadesyla
experienciagatillanel
comportamiento
Unaenfermerapuedenosentirse
cómodausandouncomputador,
perosímuycómodahaciendosu
trabajodeenfermera
Frecuenciadetareas Quéfuncionessonlasmáscomunes
eimportantes,ysurecurrencia
(mismoejemplodejerarquíaen
pantalla)
Ambiente Quéimplicanciastieneelespacio
físicoydigital
Condicionesdeluz,distancia,
frecuenciadeinterrupción,ruido,
espaciofísicoodigitalde
almacenamiento
Característicasfísicasycognitivas Quécondicionesfijanlas
característicasdelcuerpo
Tamañodelcuerpo,vista,destreza,
fuerza,patologías(artritis,diabetes,
etc.)
������ �� � �Ladimensiónqueelprofesordestacaporsobrelasdemás: dominiodetecnología. > “Es un tema que
yo siempre miré menos, y es muy importante… Mientras más he tenido tiempo haciendo aplicaciones con miles de
usuarios, uno se da cuenta de que las aplicaciones no pueden hacer muchas cosas . Por atrás tienen que hacer
muchas cosas, pero para el usuario no pueden hacer muchas cosas, porque cuantas más cosas hagan, más
empeoras la experiencia .”
Consecuenciadediseño: laexperienciadelusuario nopuedesertanparamétricanitangranular ,porque “los
usuarios no son capaces de meterse en muchos submenús” .
�� � �Matizactual: conIA “se abre la posibilidad de que toda esa complejidad se la encargue [uno] a un agente” ,lo
cualpermitequelaspersonaspuedanhacermáscosas sinexponerleslacomplejidad. Elprofesorloseñalacomo
untemaabiertoeinteresantedediseñohoy.
2.12.2Variablesdesegmentación(slide59)
“Organización de desafíos de segmentación.”
Categoría CONSUMIDORES ORGANIZACIONES
Característicasgeo-demográficas Edad,género,raza·Ingreso·
Tamañodefamilia·Estadodelciclo
devida·Ubicacióngeográfica·
Estilodevida
Tipodeindustria·Tamaño·
Ubicacióngeográfica·Cultura
corporativa·Etapadedesarrollo·
Productor/intermediario
Situacionesdeuso Ocasiónyespaciosdetiempo·
Importanciadecompra·Experiencia
previaconelproducto·Estatusdel
usuario
Aplicación·Procedimientode
compra·Nuevatarea/necesidad,
recompramodificada,recompra
directa
27

## Lamina 28

Categoría CONSUMIDORES ORGANIZACIONES
Necesidades/preferencias Lealtadalamarca·Preferenciade
marca·Beneficiosencontrados·
Calidad
Inclinaciónahacerunacuerdo·
Requerimientosde performance·
Preferenciasdemarca·
Característicasdeseadas·
Requerimientosdeservicio
Comportamientodecompra Tamañodecompra·Frecuenciade
compra
Volumen·Frecuenciadecompra
������ �� � �Cómoseusarealmente(dichoenclase): > “En el acto de ir probando soluciones, uno va detectando perfiles
de usuarios distintos. Y eso es parte de la tarea de ir desarrollando una solución e ir convergiendo en quién es el
usuario genérico — que no es el usuario que vas a tener los primeros días .”
Esdecir: lasegmentación nosedefinedeantemanoysecongela ,sinoque convergeatravésdelasiteraciones
deprototipo. Esteeseltrabajoqueseirádigiriendoenlastresentregas.
2.12.3 �� � �Designing for Behavior Change —porquécierralaclase
Elprofesordedicaelcierreaexplicarporquéestelibroeslamejorherramientaparalamaterialidad:
Elproblemaqueresuelve: > “Uno dice: ‘podríamos agregarle un botón a la aplicación’, o ‘una notificación que me
recuerde tal tema’. Y uno puede estar atrapado en esa dinámica de querer hacer mejoras incrementales sin mucha
noción.”
Loqueaportaellibro: lasestrategiassobrelasqueestánconstruidasesasdecisiones,esdecir, patronesde
diseñodeinteracción parainterveniraplicaciones.
Concepto Explicacióndada
Opcionespredeterminadas (defaults) ������ “Muchas veces las aplicaciones, si te metes a la
configuración, la configuración tiene cosas ya prehechas.
Eso es muy importante trabajarlo al inicio de una
aplicación: cuáles son las opciones que tiene el usuario y
cuáles deberían estar predeterminadas para distintos
casos de uso”
Pruebassociales Mencionadacomootratácticacomún
Lanocióndepatrón ������ “No es como el botón, sino que es un patrón que a
veces es un botón y a veces una notificación. Hay un
patrón central, y hay realmente decenas de patrones
interesantes respecto a la psicología de qué hay detrás de
las soluciones que funcionan bien”
�� � �Porquéimportaeldefault: “Esas cosas hacen mucha la diferencia si uno es capaz de darse cuenta dónde está el
volumen más grande de usuarios.”
�� � �Elprofesormencionaademásqueestastácticasseaplicanendominiossensibles(p.ej.,programasderehabil-
itacióndeconsumo)paralograr mayoradherencia aunameta.
��� ���� �����LISTADEDEFINICIONESIMPORTANTES
Término Definición(fuente)
Creatividad(Ackoff&Vergara) Lahabilidadde sobreponersealoslímites . (slide 3)
28

## Lamina 29

Término Definición(fuente)
Creatividad(Amabile) Provocarresultadosoriginalesydevalor ,enla
interseccióndemotivación,especialidadyhabilidadde
pensamientocreativo. (slide 4)
Relacióncreatividad–innovación Lacreatividades condiciónnecesariaperono
suficiente: nohayinnovaciónsincreatividad,perosilo
nuevonogeneraretorno,essolocreatividad. (�� � �
transcripción)
Silenciadoresdeideas Frasesoactitudesque cortanelflujocreativo deun
equipo. (slide 6, Gary A. Davis)
Superforecasting Perfildequienanticipabienelfuturo: cauto,humilde,
no-determinista,abierto,indagador,reflexivo,
matemático,pragmático,analítico,sintetizador,
enfocadoenprobabilidades,actualizadorconsciente,
conscientedesussesgos,tenaz. (slide 7)
Deseabilidad Condicióndeefecto delproducto,enlaquese
manifiestalaformaenquesususuariosloadoptan.
(slide 10)
Funcionalidad Tareasofunciones quecumpleunproductooservicio.
(slide 11)
Usabilidad Característicasdeunproductoquelodestacandel
restodelassoluciones. �� � �Enclase: “literalmente la
representación de la experiencia del usuario” ;en
software,la capanofuncional . (slide 11)
Materialidad Formamaterialyconcreta enquesellevaacabouna
solución. (slide 11)
Elementosfuncionales Componentesdelasoluciónque sonvisiblesal
usuario: usanespacioenpantallaotienen
representaciónfísica. Enunservicio,unainteracciónque
funcionavíamúltiplesproductos. (slide 15)
Elementosnofuncionales Componentesque nosonvisiblesalusuario :
asociacionesdevalorpositivasynegativas que
resultandelproducto. Manifiestanelrendimiento de
lasolución. (slide 28)
Pruebasfuncionales Pruebasbasadasenla ejecución,revisióny
retroalimentacióndefuncionalidadespreviamente
diseñadasenelproducto. Objetivo: identificary
resolverinconsistenciasencomponentes. (slide 16)
Pruebaunitaria Pruebadeuna unidaddesoftwaremuypequeña ,para
verificarquehaceloquedebe. �� � �Esrestrictiva: sino
pasa,nosedespliegaaproducción. (slide 16 + �� � �)
Pruebadeintegración Pruebade gruposdeunidades combinadas. �� � �“Las
pruebas más difíciles”,porqueahíaparecenlas
inconsistencias. (slide 16 + �� � �)
Pruebadeaceptación(UAT) Verificacióndelasfuncionesrequeridasparalanzar
unaversión. �� � �Normalmentesehace conuna
persona. (slide 16 + �� � �)
Pruebaderegresión Detecciónde divergenciasfuncionalesproducidaspor
elcambioactual . �� � �“Volver al pasado” paraversialgo
siguefuncionandoconcapasantiguas. (slide 16 + �� � �)
Pruebasnofuncionales Procedimientosparaverificaralgúnrequisito
específicoparajuzgarlaoperacióndeunsistema.
Objetivos: ajustarlasoluciónarequisitosdeuncontexto
deconsumoe integrarvariablesdecalidadsubjetivas
auncontextoobjetivo . (slide 29)
29

## Lamina 30

Término Definición(fuente)
Pruebadeestrés Verificarquelainfraestructurasoportelacargaesperada.
�� � �Distinguirusuariostotalesenunperíodo
vs.usuariossimultáneos. (slide 29 + �� � �)
PruebaA/B �� � �Pruebaunivariable: secambiaunasolavariable y
secomparalarespuesta. Laversiónconvariosgruposy
variablessimultáneases multivariable. (�� � �
transcripción)
ElementsofValue(B2C) Catálogodeatributosdevalorencuatroniveles:
funcional,emocional,cambia-vidaeimpactosocial.
(slide 30; Almquist, Senior y Bloch, 2016)
B2BElementsofValue Catálogoencinconiveles: requerimientosdeentrada,
valorfuncional,facilidaddehacervalor,valorindividual
yvalorinspiracional. (slide 31; Almquist, Cleghorn y
Sherer, 2018)
Approachdecalidad Separarunasoluciónenfactoresrelevantesyrevisarlos
unoauno. 13dimensiones: capacidad,rendimiento,
usabilidad,confiabilidad,seguridad,escalabilidad,
compatibilidad,instalabilidad,soportabilidad,
testeabilidad,mantenibilidad,localizabilidady
portabilidad. (slides 33–34)
Tecnología Conjuntodeconocimientostécnicos científicamente
ordenados(conmétodo) quepermitendiseñarycrear
bienesyserviciosquefacilitanlaadaptaciónalmedioy
satisfacennecesidadesydeseos. �� � �Noserestringea
lodigital: incluyemetodologíasyabstracciones. (slide
36)
Soluciónfísica Solucióntangibleenelmundofísico : objetos,
materialesyestímuloscognitivosbásicos(luz,tacto,
sonido,olores,gusto). (slide 37)
Solucióndigital Interaccionesqueocurrenen unainterfazque
funcionaenunsistemaoperativocomputacional .
(slide 37)
Soluciónintangible Soluciónbasadaen interacciones,acuerdosy
estímuloscognitivosqueresultanenlasignificación :
serviciosdepersonas,metodologías,conceptos,
algoritmos,experiencias,recuerdos,activosfinancieros,
eldinero,estándares. (slide 37)
Feature “En simple, algo que quiere hacer el cliente” ;sepuede
relatarcomounahistoriaenunasituación. (slide 41)
Historiadelcliente Descripciónsimple desdelaperspectivadelapersona
quedesealograralgonuevo(funciónnueva,ofunción
existenteconnuevascaracterísticas). Unidadmás
popularparagenerarrequerimientosenun backlog.
(slide 42)
Backlog Listaderequerimientos/tareasqueelproductodebe
cumpliroquesedebendesarrollar. (slide 42)
Epic Conjuntodehistorias relacionadasoindependientes.
Seconstruye despuésdelashistorias: “un Epic es
seleccionar historias”. (slide 42)
Modelosmentales Cómolaspersonas organizansustareasysu
información. (slide 58). Además:“los modelos mentales
son la base del logro” deloselementosfuncionales (slide
15)
30

## Lamina 31

Término Definición(fuente)
Variablesdesegmentación Ejesparaorganizardesafíosdesegmentación,distintos
paraconsumidoresyorganizaciones: geo-demográficas,
situacionesdeuso,necesidades/preferenciasy
comportamientodecompra. (slide 59)
������CRITERIOSY“FÓRMULAS”OPERATIVASDELACLASE
Nohayfórmulasmatemáticasenestaclase. Síhay procedimientosyreglasdedecisión quefuncionancomotales:
F1—Lafórmuladelahistoriadelcliente � (la única “fórmula” literal del ramo)
Como un(a) {USUARIO} quiero {OBJETIVO} para {RAZÓN / MOTIVO}
R1—Elárbollógicodedefinicióndesolución
PRODUCTO → FUNCIÓN → TAREAS → ATRIBUTOS → MATERIALIDAD
(qué) (cómo) (con qué, exactamente)
Regla: todo adjetivo debe terminar en un número o un componente concreto.
R2—Regladelastrescapas
FUNCIONALIDAD = tareas rudimentarias, SIN juicio de calidad → elementos funcionales → pruebas FUNCIONALES
USABILIDAD = atributos cualitativos, lo distintivo → elementos NO funcionales → pruebas NO FUNCIONALES
MATERIALIDAD = lo tangible: números, colores, medidas, stack
R3—Criteriodesuficienciadeunahistoria
Una historia sirve si es TRABAJABLE:
(a) permite identificar tareas concretas,
(b) permite colgarle atributos, y
(c) permite bajarla a materialidad.
Si "no dice nada" (ej. "un resumen rápido") → hay que SUBDIVIDIRLA.
R4—Regladeenriquecimientodehistorias(slide44)
Estrategia 1: DIVIDIR historia grande → historias pequeñas
Estrategia 2: BOMBARDEAR con elementos no funcionales
(condiciones de éxito / logro / satisfacción, medibles)
R5—Regladeprioridadanteel over-engineering
¿Vale la pena esta prueba/atributo ahora?
→ ¿Le importa al cliente? SÍ → hacerlo
→ ¿Es restrictivo para el mercado? SÍ → hacerlo (ej. SOC 2 en B2B)
→ Si no: el producto manda. Modo urgencia.
Corolario: el refactoring es un buen problema; cuando lo tengas, tendrás recursos.
R6—Regladeobjetividaddeunaprueba
Prueba objetiva ⟺ el usuario NO sabe que está siendo probado ("a ciegas")
Canal beta → sesgo de perfil (usuario avezado, tolerante al riesgo)
Autoselección → sesgo de motivación (lo usa más porque quería probarlo)
31

## Lamina 32

R7—Regladelcuestionamientofuncional(creatividad)
1. Identificar la función que doy por hecha.
2. Preguntar: ¿por qué solo hace eso?
3. Agregar una tarea que normalmente NO hace.
4. Meterse DENTRO del concepto, no refutarlo con la solución genérica.
→ SCAMPER es la versión ordenada:
{Sustituir, Combinar, Adaptar, Magnificar, Poner en otros usos, Eliminar, Reducir/Reordenar}
× {Personas, Lugares, Tiempos, Partes, Funciones, Resultados}
R8—Jerarquíadeplanificación
proyecto > epic > historia → issue → (backlog) → sprint
↑ el epic se construye DESPUÉS de las historias
���POSIBLESPREGUNTASDEEXAMENCONRESPUESTASBREVES
P1. Definalastrescapasdeladeseabilidadydéunejemplodecadaunaparaunmismoproducto. Funcional-
idad=tareasofuncionesquecumple; Usabilidad=característicasquelodestacandelresto; Materialidad=forma
materialyconcretaenquesellevaacabo. Ejemploconunasilla: soportar / usar espacio (funcionalidad); ergonomía,
voluminosidad, capacidad de peso (usabilidad); dimensiones específicas, specs de resistencia, materiales (materialidad).
P2. ¿Cuálesladiferenciaentreelementosfuncionalesynofuncionales? Losfuncionalessonvisibles alusuario
(ocupanespacioenpantallaotienenrepresentaciónfísica;ensoftware,lascosasqueelsoftwarepuedehacer). Los
nofuncionalesnosonvisibles : sonasociacionesdevalorpositivasynegativas queresultandelproductoy
manifiestansurendimiento (estética,eficiencia,compatibilidad,placer,cobertura,completitud).
P3. Nombre los cuatro tipos de pruebas funcionales y explique para qué sirve cada uno. Unitarias y
de componentes(probar una unidad mínima);de integración(grupos de unidades combinadas — las más
difíciles,porqueahíaparecenlasinconsistencias); deaceptación (verificarconunapersonaquelafuncióntienelas
característicasrequeridasparalanzarlaversión—UAT); deregresión (detectardivergenciasfuncionalescausadas
porelcambioactual,“volveralpasado”).
P4. Nombre al menos seis tipos de pruebas no funcionales.Compatibilidad, estrés, seguridad, usabilidad,
rendimiento,escalabilidad,mantenibilidad,instalabilidadeinternacionalización(lasnuevedelaslide29).
P5. ¿Cuálesladiferenciaesencialentreunapruebafuncionalyunanofuncional? Lafuncionalresponde “¿hace
loquedicequehace?” (binario: funcionaonofunciona);lanofuncionalresponde “¿conquéniveldecalidad
lohace?”,esdecir, silacaracterísticabuscadasecumpleyenquénivel . Lasfuncionalesverificanelementos
objetivos;lasnofuncionalesdeben integrarvariablesdecalidadsubjetivasauncontextoobjetivo .
P6. Escribaunahistoriadelclientebienformadayexpliquesustrescomponentes. “Como gerente necesito
ver todos los lunes un informe de incidencias de seguridad para poder establecer una lista de tareas con mi equipo.”
Componentes: usuario(gerente),objetivo(verelinformesemanaldeincidencias)y razón/motivo(establecerla
listadetareas). Sinlostres,lahistorianoestrabajable.
P7. ¿Porqué“Comogerentequierotenerunresumenrápidoparadedicarmeatomardecisiones”esuna
malahistoria? Porque“nodicenada” : “resumenrápido”esunatributosinmaterialidad,porloquenosepuede
identificartareasnicolgarlecondicionesconcretas. Es,encambio,unabuenacandidataa subdividirse(estrategia1
delaslide44).
P8. Nombrelasdosestrategiasdehistoriaavanzada. (1)Dividirhistoriasgrandesenhistoriaspequeñas . (2)
Agregarcondicionesdeéxito/logroosatisfacción ,esdecir, “bombardearconelementosnofuncionales” —
incluyendocondicionesmedibles(ej. medirlatasadeconversiónentrevistaresumenyvistasingular).
P9. ¿CuálessonlostresfactoresdelacreatividadsegúnAmabileyquéaportacadauno? Motivación (hay
quequererhacerlo), especialidad(conocimientotécnicodeldominio)y habilidaddepensamientocreativo (que
incluyeaperturaaequivocarse). Elpensamientocreativosurgedesuintersección.
32

## Lamina 33

P10. ¿Eslacreatividadlomismoquelainnovación? No.Nohayinnovaciónsincreatividad ,perolacreatividad
solanobasta: silonuevo nogeneraretorno niesútilproductivamente,escreatividad,noinnovación. Lacreatividad
escondición necesariaperonosuficiente .
P11. ¿Qué son los silenciadores de ideas y por qué “lo hicimos bien sin eso” es especialmente dañino?
Sonfrasesoactitudesquecortanelflujocreativodeunequipo. Esafraseenparticularconsisteen agarrarsede
experienciaspreviasparanegarcosasnuevas ,locualbloquealaexploraciónjustamenteenelterrenodondela
novedadeselobjetivo.
P12. ExpliqueelcasoDominóentérminosdelastrescapas. Funcionalidad: elclientedebetomardecisiones
paraelegirunplato. Usabilidad: quesearápido. Materialidad: lacartamatricial (seeligecombinandofilas×
columnas,“XporY”,envezderecorrerunalista),lamáquinadeRedcompraenelcinturóndecadaatendedorylas
PDAqueenvíanelpedidodirectoacocina. Enseñaqueunatributoblandoseconsiguecon decisionesmateriales
concretas.
P13. Analiceunaislademallanivelfuncional. ¿Porquélarespuestadependedequiénpregunta? Parael
empresarioquelaarrienda ,lastareasbásicasson ocuparunespaciolimitado yllamarlaatención rápidamente
dequienpasa. Para eladministradordelmall ,latareabásicaes optimizarlarentabilidaddelespacio ,yentonces
laisladejadeserelproductoypasaasermaterialidad (unmecanismomásdecobrar,juntoaferiasartesanales
omáquinasexpendedoras). Lección: hayquefijardequiéneslafuncionalidadantesdeanalizar .
P14. Dossillaspermitenlamismaposicióndedescansoperounaesdelujoyotraejecutiva. ¿Enquécapa
estáladiferenciayquédemuestraeso? Ladiferencia noestáenlafuncionalidad (lastareassonprácticamente
idénticas),sinoen usabilidadymaterialidad . Demuestraporquélafuncionalidadporsísolanobastaparadefinir
unproducto: escomúnqueproductosdistintoscompartanexactamentelasmismastareas .
P15. ¿Quéeselcuestionamientofuncionalycuáleselerrortípicoalaplicarlo? Estomarunproductocuya
funciónsedaporhechay agregarleunatareaquenormalmentenohace ;elprofesorlollama “el primer comodín
bajo la manga” delacreatividad. Elerrortípicoes refutarlapropuestaconlasolucióngenéricaexistente (“pero
podrías comprar un parlante aparte”). Lainstruccióncorrectaes metersedentrodelconcepto quelapropuesta
intentaconstruir.
P16. ExpliqueSCAMPER.Acrónimode Sustituir,Combinar,Adaptar,Magnificar,Ponerenotrosusos, Eliminar,
Reducir/Reordenar. Secruzaconunsetdedimensiones(personas,lugares,tiempos,partes,funciones,resultados)
sobreunproductodereferencia. Eslaversiónordenadadelcuestionamientofuncionaly,segúnelprofesor, la
metodologíadecreatividad“defacto” .
P17. ¿Por qué participar en un canal beta no constituye una prueba objetiva?Porsesgo de perfil y de
motivación: quienseinscribeauncanalbetaesel usuariomásavezado ytolerantealriesgo(loscanalesbeta
adviertenquehay featuresexperimentalesquepuedenfallar),porloque norepresentaalusuariopromedio ;
además,alsaberqueestáprobandoalgoexperimental,tiendeausarlomás. Unapruebaobjetivadebeser“a
ciegas”.
P18. ¿QuéesunapruebaA/Byenquésediferenciadeunamultivariable? LaA/Bes univariable: secambia
unasolavariable (p.ej. elmismocorreocondosasuntosdistintos)paravercuálfuncionamejor. La multivariable,
propiadenegociosmuygrandes,segmentausuariosenvariosgruposytestea variosabordajesensimultáneo .
P19. Uncompañeroquierehacerpruebasdeestréseinternacionalizaciónparaunaappcon10usuarios.
¿Quélediría? Queelproductodeterminalaprioridad : lascosasimportan siemprequealclienteleimporten o
cuandoson restrictivasparaentraraunmercado (ej. unacertificaciónSOC2enelmundocorporativo). Fuera
deeso,es over-engineering: “no me voy a poner a pensar en 10.000 usuarios si tengo 10” . Además,elrefactoring
futuroesunbuenproblema ,ycuandolleguenormalmentehabrárecursospararesolverlo.
P20. ¿Quétienenencomún160.000usuariosaldíay160.000usuariossimultáneos? Casinada: “son dos
software completamente distintos”. Distribuidos a lo largo del día nunca hay más de unos ~150 concurrentes;
simultáneosexigiríanunainfraestructuradeotroorden. Lalecciónesque lapruebadeestrésdebedefinirsesobre
concurrencia,nosobrevolumentotal .
P21. ¿Cuáleslafilosofíadediseñoenseguridadquemencionaelprofesor? Queademásdeintentarqueno
hayaincidentes, unaparteimportanteesdefinirquépasacuandoelincidenteocurre : cuáleselprotocolo. La
dificultadesque,comoraravezocurre, elprotocolonuncaseimplementadefacto yporesoesdifícildevalidar.
33

## Lamina 34

P22. Déunejemplodecómounarestriccióndeinternacionalizaciónseconvierteenmaterialidad. Enuna
startupdereclutamientoconIAoperandoenEuropa,lanormativaexigeque ciertasdecisionessiemprelastome
unapersona: laIApuedeanalizaryentregarfactores,peroeldescartefinaldebeserhumano. Esoobligaa agregar
unpasoadicionalenelflujoyunainterfazdistinta . (Análogofísico: lossellosnutricionalesobligatoriosen
alimentosenChile.)
P23. ¿Porquéelprofesordicequeelsoftwareesuna liability? Porqueelcódigoensínoaportavalor : esalgo
quehayquehacerparaconstruirelproducto. “Lo importante es el producto.” Poresoelordencorrectoeshistoria→
funcionalidad/usabilidad/materialidad→reciénentoncesarquitecturadesoftware.
P24. ¿Quésonloselementos“intangibles”yporquéelprofesordicequelamayoríadelassolucioneslo
son? Sonsolucionesbasadasen interacciones,acuerdosyestímuloscognitivosqueresultanenlasignificación :
metodologías,conceptos,algoritmos,experiencias,estándares,eldinero. Sonlamayoríaporque,apenasseanaliza
cualquierproductoreal,loqueexplicasuadopciónson conceptosysignificados (el“lugarparaestar”deStarbucks,
el“estatusintelectual”deunauniversidad),nosuscomponentesfísicos.
P25. SegúnElementsofValue,¿eselimpactosocialmásimportantequeloselementosfuncionales? No. “No
significa que unos sean más importantes que otros” : dependedelproducto quémanifestacionessonmáscomunes.
Unsoftwaredegestióndecuentaspersonalessejuegaenelementos funcionales;unclubderunningparaunperfil
específicosejuegaenelementos emocionales.
P26. ¿Cómosedesarrollacriteriodematerialidad, segúnelprofesor? Principalmentecon benchmarking:
investigar qué está haciendo el resto (Trend Hunter, Behance, el directorio de startups de Y Combinator, a16z
Speedrun). Adiferenciadelafuncionalidadylausabilidad—quedependendeconocereldominio— el“buen
gustomaterial”tomamuchotiempodedesarrollarse . Ellibrorecomendadoparaacelerarloes Designing for
Behavior Change.
P27. Nombre las siete consideraciones del usuario (slide 58).Actitud en las tareas · Modelos mentales ·
Motivacionesyobjetivos·Dominiodetecnologíay/ohabilidades·Frecuenciadetareas·Ambiente·Características
físicasycognitivas.
P28. ¿Porquélasaplicacionesagranescala“nopuedenhacermuchascosas”? Porquepordetrássíhacen
muchascosas,perodecaraalusuarionopueden : cuantasmáscosashaganvisibles,peorlaexperiencia. Los
usuariosnosemetenenmuchossubmenús,asíquelaexperiencianopuedesertan paramétricanigranular . Esto
pertenecealaconsideraciónde dominiodetecnología .
P29. ¿Cuándosedefineelsegmentodeusuariosdeunasolución? Nodeantemano: convergeatravésdelas
iteraciones. “En el acto de ir probando soluciones uno va detectando perfiles de usuarios distintos… ir convergiendo
en quién es el usuario genérico, que no es el usuario que vas a tener los primeros días.”
P30. ¿QuéseevalúaexactamenteenlaEntrega1? Cobertura : queelprototipocubrael 100%delasfunciones
definidasen las historias seleccionadas, más la definición de la solución, entre 5 y 10 historias con detalle no
funcionalymaterial,ylajustificacióndeporquéseeligióesahistoria. Noseevalúarendimientodeatributosno
funcionales,nisilasoluciónesútilofuncionabien. Solopruebas funcionalesydeaceptaciónmuybásicas .
�� �ERRORESYCONFUSIONESCOMUNES
1. Confundirusabilidadcon“facilidaddeuso”. Enestemodelo, usabilidadeslacapacompletade caracterís-
ticasquedistinguen lasolucióndelresto(equivalealacapanofuncionaldelsoftware). La facilidad de uso es
solounodesuselementos.
2. Creerque“funcionalidad”significa“quefuncionebien”. No: lafuncionalidades latarearudimentaria,
sinjuiciodecalidad . “Simplemente se hacen.” Eljuiciodecalidadviveenusabilidad.
3. Saltarselamaterialidad. Eselerrormásfrecuenteenlasentregas: quedarseenadjetivos(“intuitivo”,“rápido”,
“resistente”)sinbajaranúmeros,componenteso specs. Lapreguntacorrectaessiempre “¿resistente cuánto?”.
4. Invertirelorden: partirporelsoftware. Elcódigo noaportavalorporsímismo ; primerosearmael
producto(historia→F/U/M),yreciéndespuéslaarquitectura.
5. Confundirpruebafuncionalconpruebanofuncional. Lafuncionalpregunta “¿lo hace?”;lanofuncional,
“¿con qué nivel de calidad lo hace?” . Sonregímenesdistintos yexigeninstrumentosdistintos.
34

## Lamina 35

6. Creerquelapruebadeaceptaciónesautomática. Normalmentees conunapersona (UAT),adiferenciade
lasunitariasydeintegración.
7. Confundir prueba de regresión con prueba de integración.La deintegración verifica que unidades
combinadasfuncionen;lade regresiónverificaque uncambioactualnohayarotoloqueantesfuncionaba .
8. Dimensionarunapruebadeestrésporusuariostotales. 160.000aldía≠160.000simultáneos. Loque
importaesla concurrencia.
9. Tomarelcanalbetacomoevidenciarepresentativa. Tienesesgodeperfil (usuarioavezado)y demotivación
(sabequeestáprobando). Unapruebaobjetivadebeser aciegas.
10. CreerquelapruebaA/Besmultivariable. Esunivariablepordefinición: secambia unavariable.
11. Creerque“tecnología”=“digital”. Ladefinicióndelaslide36incluye metodologías,conceptosyabstrac-
ciones;elprofesorlosubrayaexplícitamente.
12. Clasificartodocomofísicoodigitalyolvidarlointangible. “La mayoría de las soluciones son intangibles” :
conceptos,acuerdos,significación,estándares,experiencias.
13. Escribirhistoriassinel“para”. Lafórmulatiene trespartes: usuario,objetivoyrazón. Sinelmotivo,nose
puedenderivarcondicionesdelogro.
14. Escribir historias demasiado genéricas y darlas por terminadas.Si la historia “no dice nada”, el paso
siguientees subdividirla,noconstruirla.
15. CreerqueelEpicsedefineantesquelashistorias. Laslide42esexplícita: “el epic se construye después de
las historias”;unEpices seleccionarhistorias. Jerarquía:proyecto > epic > historia.
16. ConfundircoberturaconcalidadenlaEntrega1. Seevalúaqueelprototipohaga todoloquelashistorias
dijeron,noquelohagabienniqueseaútil.
17. PensarquesenecesitainvestigacióndeusuariosparalaEntrega1. Nohaypauta: laposturaesdeescuela
ágil— construirsobrehipótesisyluegolevantarinformación . EltesteoconusuariosempiezaenlaEntrega
2.
18. CreerquehayunajerarquíauniversalenlosElementsofValue. Nolahay: dependedelproducto qué
niveldomina.
19. Aplicarelanálisisfuncionalsinfijarelsujeto. Elcasodelaislademallmuestraque lamismacosacambia
decapa segúndequiénsealafuncionalidadanalizada.
20. Refutarunaideacreativaconlasolucióngenéricaexistente. Elcuestionamientofuncionalexige meterse
dentrodelconcepto ,noresponder “pero eso ya se puede hacer de otra forma” .
21. Confundirelreencuadreconmateriadelramo. Elprofesordiceexplícitamentequeel Reframing Canvasno
seveenesteramo ;esmaterialcomplementario.
22. Creerquehayqueoptimizartodoslosatributossiempre. Elcriterioes: importasileimportaalclienteo
siesrestrictivoparaelmercado . Lodemáses over-engineering.
23. AsumirquelaIAresuelveeldiseñodeproducto. “La IA generaliza mucho… no es muy creativa.” Puede
resolvereldesarrollotécnico; elproductodependedelequipo .
24. Creerqueelsegmentosedefinealinicioysecongela. Convergealolargodelasiteracionesdeprototipo.
��CONEXIONESCONLACLASE1YCONLASPRÓXIMASSESIONES
Conceptodeestaclase Seapoyaen/anticipa
Deseabilidadysustrescapas Retomala estructuradedeseabilidad delaS1(slide13
delaClase1)yledaestructurainternaoperativa
Creatividadvs.innovación(retornos) Clase1,definicióndeinnovación;aquíseagrega “no
hay innovación sin creatividad”
Curvadevalor(compararatributosporsegmento) Ramoanterior;reaparecealhablardeusabilidady
expectativasporsegmento
Presenciapop-up(islas,stands,foodtrucks) Clase1 (tiendapop-upcomoherramientadePMV);
aquíreaparececonelcasoWOM
Incertidumbretécnicaasumidadeliberadamente Clase1;aquíaparecealexplicarporqué “tiene pocas
posibilidades”esunsilenciador
RorySutherland—percepciónycontrol Recomendadoyaenelramoanterior;sere-recomienda
Pruebasfuncionalesydeaceptaciónbásicas ������Entrega1,endossemanas
35

## Lamina 36

Conceptodeestaclase Seapoyaen/anticipa
Historiasdelclientecondetallenofuncionalymaterial ������Entrega1,punto2delapauta
Pruebasnofuncionales,atributosysumedición Entrega2 yla clasedemétricas (S3/S4)
Métricaslean,métricaspirata,validacióndeclientes Sesión3/4;anunciadacomo “la clase donde vamos a ver
muchas métricas”
Service blueprint,mapeoconceptual,diseñodeservicio Sesión4;elejemplodelmúsicocallejeroyaloanticipa
(“calza perfecto con el diseño de un servicio” )
Roadmapping,milestones Sesión5;seadelantaoperativamenteenlostalleres
(GitHub)
Arquitecturadesoftware �� �Declaradofueradelalcancedelramo (“es un tema
gigante”)
Scrum,Sprints,metodologíaságiles �� �Declaradofueradelalcancedelramo ;seusasolo
elconceptodehistoria/backlog
ReframingCanvas �� �Declaradofueradelalcancedelramo ;material
complementarioofrecido
������MAPAMENTALDELACLASEENUNAPÁGINA
CREATIVIDAD
├── Ackoff & Vergara: sobreponerse a los LÍMITES
├── Amabile: provocar resultados ORIGINALES y de VALOR
│ ▲ intersección de: MOTIVACIÓN · ESPECIALIDAD · HABILIDAD (pensamiento creativo)
├──⚠ SILENCIADORES DE IDEAS → cortan el flujo (evitar juicios prematuros)
├── SUPERFORECASTING → temperamento: cauto · humilde · no-determinista · probabilístico
└──🎯 NO HAY INNOVACIÓN SIN CREATIVIDAD (pero sin retorno, es SOLO creatividad)
↓ ¿cómo defino entonces QUÉ construir?
DESEABILIDAD = condición de EFECTO del producto (lo que logró, guste o no)
│
├── FUNCIONALIDAD ── tareas rudimentarias, SIN juicio "¿qué hace?"
│ └── ELEMENTOS FUNCIONALES (visibles: botón, pantalla / pedir comida, agendar)
│ └── 🧪 PRUEBAS FUNCIONALES → ¿lo hace o no lo hace?
│ Unitarias · Integración( ⚠ las más difíciles) · Aceptación(UAT) · Regresión
│ ⤷🎯 ENTREGA 1 se evalúa AQUÍ (cobertura 100%)
│
├── USABILIDAD ───── atributos cualitativos, lo distintivo "¿cómo lo hace?"
│ └── ELEMENTOS NO FUNCIONALES (no visibles: asociaciones + y −; rendimiento)
│ └── 🧪 PRUEBAS NO FUNCIONALES → ¿en qué NIVEL lo hace?
│ Compatibilidad · Estrés · Seguridad · Usabilidad · Rendimiento
│ Escalabilidad · Mantenibilidad · Instalabilidad · Internacionalización
│ ⤷ ENTREGA 2
│ └── catálogos: ELEMENTS OF VALUE (B2C / B2B) · APPROACH DE CALIDAD (13 dim.)
│
└── MATERIALIDAD ─── lo concreto: números, colores, medidas, stack "¿con qué?"
└── TECNOLOGÍA (≠ solo digital: incluye metodologías y abstracciones)
└── TIPOS DE SOLUCIÓN: FÍSICO · DIGITAL · INTANGIBLE
└─🎯 la MAYORÍA son intangibles ─┘
└── se desarrolla con BENCHMARKING (Trend Hunter · Behance · YC · a16z Speedrun)
🎯 ÁRBOL LÓGICO: PRODUCTO → FUNCIÓN → TAREAS → ATRIBUTOS → MATERIALIDAD
Regla: todo adjetivo termina en un número o un componente.
("rápido" → 5 minutos → carta MATRICIAL + PDA + Redcompra en el cinturón) [caso Dominó]
36

## Lamina 37

HERRAMIENTAS CREATIVAS PARA MOVERSE EN EL ÁRBOL
├── CUESTIONAMIENTO FUNCIONAL ("el primer comodín bajo la manga")
│ agregar una tarea que el producto normalmente NO hace
│ ⚠ meterse DENTRO del concepto, no refutarlo con lo genérico
├── SCAMPER = {Sustituir,Combinar,Adaptar,Magnificar,Poner en otros usos,Eliminar,Reducir}
│ × {Personas,Lugares,Tiempos,Partes,Funciones,Resultados}
└── REENCUADRE (Wedell) ──⚠ NO es materia de este ramo
↓ ¿cómo lo escribo para poder construirlo?
HISTORIA DEL CLIENTE ⭐ Como un(a) {USUARIO} quiero {OBJETIVO} para {RAZÓN}
│
├── Estrategia 1: DIVIDIR historias grandes en pequeñas
│ ("resumen rápido" no dice nada → "informe de incidencias los lunes")
├── Estrategia 2: BOMBARDEAR con elementos no funcionales
│ → condiciones de logro/satisfacción MEDIBLES ( ⤷ puente a métricas, S3/S4)
│
└── proyecto > epic > historia → issue → backlog → sprint
↑ el epic se arma DESPUÉS de las historias
⚠ CONSIDERACIONES DEL USUARIO antes y después del prototipo
Actitud en tareas · Modelos mentales · Motivaciones · DOMINIO DE TECNOLOGÍA
Frecuencia · Ambiente · Características físicas y cognitivas
🎯 A gran escala: la app hace mucho POR DETRÁS, poco DE CARA al usuario.
⚠ SEGMENTACIÓN: no se define al inicio — CONVERGE con las iteraciones.
🎯 REGLA MAESTRA DE LA CLASE:
El software es una liability; el CÓDIGO NO APORTA VALOR.
Lo importante es el PRODUCTO — y el producto se define en las tres capas,
no en una corriente de conciencia.
���������ANEXO—Erroresdetranscripciónidentificados
Reconstruccioneshechasapartirdelcontextoylasslides. Semarcanexplícitamenteporqueellectordebesaber
quesoninferencias.
TranscritoporWhisper Términoprobable Confianza
“aCofiVergara” Ackoff&Vergara (apareceenslide
3)
Alta
“Amaville” Amabile(TeresaM.Amabile,slide5) Alta
“deshabilidad”/“disabilidad”
(repetido)
deseabilidad Alta
“elindiomismo”(usabilidadde
redessociales)
eldinamismo (apareceenslide13) Alta
“latingencia” laatingencia (apareceenslide13) Alta
“Cloud”/“CloudCode”/“Tropic”
(repetido)
Claude/ClaudeCode /Anthropic Alta
“Codecs”(repetido) Codex(OpenAI) Alta
“Gravity”/“Anti-Gravity” Antigravity(IDEdeGoogle) Alta
“Googledeestudio”/“A-Studio” GoogleAIStudio Alta
“RedLimit” rate limit Alta
37

## Lamina 38

TranscritoporWhisper Términoprobable Confianza
“UADquesellamanUser
AcceptanceTesting”
UAT Alta
“backbounty”(áreadeseguridad) bug bounty Alta
“SOP2”/“SOC2” SOC2 Alta
“foottracks”/“fuchas” food trucks Alta
“WordTrace”/“wordtrees” gitworktrees Alta
“WhiteCombinator”/“UI
Combinator”
YCombinator Alta
“saldera”(en“lasalderamás
importantedelmundo”)
aceleradora Alta
“16ZdeAndreessenHollowitz”/
“AndrésEnjolovitz”
a16z(AndreessenHorowitz) Alta
“Speedbrand”/“Speedrun” Speedrun(programadea16z) Alta
“RoySutherland” RorySutherland (apareceenslide
32)
Alta
“MapofExperiences” Mapping Experiences,deJim
Kalbach(slide60)
Alta
“G8”(juntoaTrustpilotyReddit) G2 Alta
“RAID”/“Reddit” Reddit Alta
“Masi”/“Masai” MASI(sigladelprogramade
magíster)
Alta
“Canva”(dondeestáelmaterial) Canvas(LMS) Alta
“pruebadesubida” pruebadeestrés/decarga Media-alta
“Chat100”(sistemadecomponentes
deinterfazomnipresente)
shadcn/ui Media-alta
“Jane”(marcaderopade
marketplace,muybaratayvariada)
Shein Media
“Flash3.5”(modeloreciénlanzado
porGoogle)
Gemini3.5Flash (odenominación
equivalente)
Media
“IncubusC”(dondeparticipóen
hackatones)
IncubaUdeC Media
“elbio-biodediseñode
arquitecturas”
escueladediseñoenlaregióndel
Biobío
Media
“Barro”(marcadepizza
estadounidenseenfoodtrucks)
[término no reconstruible] —
“modeloSol”enversión ultra fast
(700tokens/s)
[término no reconstruible] —mismo
casoqueenlaClase1
—
“Mitric”(proyectopropiodel
profesor)
[término no reconstruible] —
“Aníbal”(en“nohabríacaídocomo
Aníbal”)
[término no reconstruible] —
“gentequejuegaaMajid”(perfil
paraunclubderunning)
[término no reconstruible] —
“productosraroscomoelcaldo
cultivo”
[término no reconstruible] —
“softwaredegestiónderestaurantes
tipofood”
[término no reconstruible] —
Notaadicionalsobrelatranscripción: envariostramosWhisperatribuyea SPEAKER_06frasesqueclaramenteson
delprofesor(porejemplo,almostrarTrendHunterenpantalla). Ladiarizacióntampocoesfiableenlosintercambios
rápidosdelbloquedepreguntas. Sereconstruyólaatribuciónporcontexto.
Notasobrelapalabra“gente”: enmúltiplespasajeslatranscripciónescribe “la gente” dondeporelcontexto
elprofesorclaramentedice “losagentes” (“lo armé con la gente” , “la gente te ayuda con skills” , “un ejército de
agentes”). Seinterpretócomo agentesdeIA entodosesoscasos.
38
