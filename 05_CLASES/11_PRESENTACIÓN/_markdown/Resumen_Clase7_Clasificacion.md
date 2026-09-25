# Resumen_Clase7_Clasificacion

> Material de clase de Fundamentos de Ciencia de Datos, UdeC T2-2026.
> Texto extraido de `Resumen_Clase7_Clasificacion.pdf` para busqueda e indexacion.
> 30 laminas. Las figuras no se extraen: si una lamina
> depende de un grafico, hay que abrir el PDF.

---

## Lamina 1

FundamentosenCienciadeDatos—CLASE7: Clasificación
Apuntescompletos: diapositivasoficiales+transcripcióndeclase
Profesor: GuillermoCabrera-Vives(IngenieroCivilInformático;MScyPh.D.enCienciasdelaComputación,
UniversidaddeChile)·guillecabrera@inf.udec.cl UniversidaddeConcepción —FacultaddeIngeniería·
IITUdeC·UnidaddeDataScience Modalidad: clasedictadaporZoom,conanotacionesenvivosobrelas
diapositivasyaltaparticipacióndeestudiantes.
Cómoleerestedocumento. Integraelcontenidodelas40diapositivasoficialescontodolo
dichoenclase,organizadosegúnelordenrealdelaexposición. Semarcancon �� � �loscontenidos
quesoloaparecenenlatranscripción (noestánenlasslides),porquesuelenserjustamentelo
queunestudianteolvidarepasar. Semarcacon �� �elcontenidomatemáticoqueenlaspropias
slidesllevaelsímbolodeadvertenciadelprofesor(enestaclaseaparece soloenlasláminas14
y30). Semarcacon ������loquetienemayorprobabilidaddeserevaluado.
Notasobrelasfuentes. Latranscripciónesautomáticaycontieneerroresdereconocimiento
evidentes(p.ej. “SupportVectorMatching” porSupportVectorMachine, “criteriodeemergencia”
porcriteriodeconvergencia, “ReceiverOperatorRatingCharacteristic” porReceiverOperating
Characteristic);cuandoeltérminocorrectoapareceenlasslides,seusaeldelasslidesysedeja
constanciadelerror. Todoloqueestáenestedocumentoprovienedelasdosfuentesentregadas;
lasescasísimasaclaracionesexternasestánmarcadasexplícitamentecomo (notaexterna).
Documentoautónomo. Norequierehaberleídolosapuntesdeclasesanteriores: elmaterialde
repasoqueelprofesorusó(slides2–8)estáreproducidoenla§7.0.
����RESUMENEJECUTIVO
Estaclaseesel espejoexactodelaclasederegresión ,peroparaelcasoenquelaetiquetaapredecires
unacategoría envezdeunnúmero: esoes clasificación,laotragrantareadelaprendizajesupervisado.
Elprofesorrecorrelosmismoscuatrobloquesqueenregresión—modelo, evaluación, generalizacióny
validacióncruzada—reemplazandocadapiezaporsuequivalenteenclasificación. Primerofijaladistinción
críticaentrevariable categórica(sinnocióndeorden)y numérica(conorden),yrecuerdaqueunacategoría
seentregaaunmodelomatemáticomediante one-hotencoding. Luegopresentaelmodelolinealpor
excelencia,la SupportVectorMachine(SVM) ,queeligeentrelasinfinitasrectasque“separanbien”aquella
que maximiza el margenentre los vectores de soporte de cada clase, lo que formalmente equivale a
minimizar‖w‖sujetoayᵢ(w·xᵢ−b)≥1. Elbloquede evaluacióneselcorazóndelaclase: verdaderos/falsos
positivosynegativos, exactitud,error,recall(tasadeverdaderospositivos),precisiónytasadefalsos
positivos,juntoconla matrizdeconfusión ,queelprofesorcalificacomounadelasherramientasmás
útilesparaentenderunmodelo. Apartirdel umbraldeclasificación —unhiperparámetroquemuevela
frontera—seconstruyela curvaROC yelconceptode puntodeoperación ,esdecir,ladecisióndenegocio
sobredóndeubicarseeneltrade-offentrerecallyfalsospositivos. Laclasecierraconlosmodelosnolineales
basadosen árbolesdedecisión : cómoelegirdóndedividirusandomedidasde impureza(Gini,entropía,
errordeclasificación),la gananciadepureza ,elalgoritmo C4.5ysuscriteriosdeconvergencia;yfinalmente
RandomForest,quecombinamuchosárbolesdecorrelacionadosmediantebootstrappingdedatosyde
atributos,promediandosuspredicciones. Ideatransversalrepetidavariasveces: ningúnmodeloesperfecto ,
yantecualquierdudasobrecómoelegiralgo,larespuestaes validacióncruzada.
�CONCEPTOSCLAVEDELACLASE
1

## Lamina 2

# Concepto Prioridad Porquéimporta
1 Clasificación=etiqueta
categórica(vs.regresión
=valorreal)
Esencial Defineelobjetodetoda
laclase
2 Categóricavs.numérica
⇒criteriodel orden
Esencial Elprofesorlopersiguió
10minutoshastala
definiciónexacta
3 One-hotencodingpara
entregarcategoríasaun
modelo
Esencial Puenteconlaunidadde
calidaddedatos
4 Nocióndecercanía:
objetoscercanos ⇒
mismaclase
Esencial Justificatodoeldiseño
deunclasificador
5 SVM:vectoresde
soportey maximizarel
margen
Esencial Modelolinealde
referenciadelaclase
6 margen=2/‖w‖;min
‖w‖s.a. yᵢ(w·xᵢ−b)≥1
�� �
Importante Matemáticamarcada
con �� �(slide14)
7 VP,VN,FP,FN Esencial Basedeabsolutamente
todaslasmétricas
8 Exactitud,error,recall,
precisión,TFP
Esencial Fórmulasde
memorización
obligatoria
9 ������Recall≠Precisión Esencial Laconfusiónmás
probabledetodoel
curso
10 Matrizdeconfusión Esencial Permiterecalculartodas
lasmétricasyextenderse
aNclases
11 Umbraldeclasificación
comohiperparámetro
Esencial Generatodalacurva
ROC
12 CurvaROCypuntode
operación
Esencial Ejercicioexplícitoenlas
slides22–24
13 Sobreajusteen
clasificación(frontera
demasiadocompleja)
Esencial Equivalentealpolinomio
degrado10delaclase
anterior
14 Validacióncruzadasobre
cualquiermétrica
Esencial “Sinosabenla
respuesta,digan
validacióncruzada”
15 ImpurezadeGiniysu
fórmula
Esencial Únicocálculonumérico
completodesarrollado
enclase
16 Gananciadepureza
(ponderadaportamaño
denodo)
Esencial Criteriodedivisióndel
árbol
17 AlgoritmoC4.5y
criteriosdeconvergencia
Importante Procedimiento
enumerable,fácilde
preguntar
18 Entropíayerrorde
clasificacióncomo
alternativasaGini �� �
Importante Slide30,marcadacon
�� �
2

## Lamina 3

# Concepto Prioridad Porquéimporta
19 Lamedidadeimpureza
esun hiperparámetro
Importante Preguntahecha
explícitamenteenclase
20 RandomForest:
bootstrappingdedatos
ydeatributos
Esencial Cierredelaclase;
algoritmomuyusado
21 Importanciadevariables
enRandomForest
Importante Ventajadistintivadel
método
22 Ningúnmodeloes
perfecto(incluidaslas
LLM)
Importante Ideafilosóficarepetida
tresveces
23 KNN(Kvecinosmás
cercanos)
Complementario Digresiónsurgidadeuna
pregunta
24 Historia: SVM(≈2000)→
RandomForest
(2000–2010)→redes
neuronales
Complementario Contexto,útilcomo
marcomental
7.0Encuadredelaclaseyrepaso(slides2a8)
�� � �Lafrasequeabrelaclase
“Lasemanapasadavimosregresión,queescuandoqueremospredecirunaetiquetaquetieneun
valorcontinuoounvalornumérico. Hoydíavamosaverclasificación,queescuandoqueremos
predecirunaetiquetaquetieneunvalorcategórico,oseaqueunacategoría.”
7.0.1Elciclodelcientíficodedatos(slide2)
Elprofesorparte,comoessucostumbre,poreldiagramadelciclo:
requerimiento/pregunta→recoleccióndedatos→limpieza→exploración→modelamiento→visual-
ización/resultados→comunicaciónytomadedecisiones→puestaenmarcha→(vueltaalrequerim-
iento)
• �� � �“Siempremegustapartirporestemonoparanuncaolvidarlo.”
• �� � �Lasflechasvanenambossentidos: avecesunoestámodelandoydescubrequeelmodelono
funcionabien,yhayquevolveraexplorarlosdatos.
• Ubicacióndeestaclase: etapade modelamiento,igualquelaclaseanterior.
7.0.2Aprendizajedemáquinas ⟨P,T,E ⟩(slides3y4)
Aprendizajedemáquinas: estudiodealgoritmosque mejoransurendimientoP enalguna
tareaT conexperienciaE.Unatareadeaprendizajebiendefinidaeslatripleta ⟨P,T,E ⟩.
�� � �Precisionesdelrepaso: -Alamáquina seleenseñadesdelaexperiencia,ylaexperienciavienedesde
losdatos. Losdatosson“experienciaprevia”queseleentregaparaqueaprendaaresolverunatarea. -La
máquinaintentareduciralgúnerror relacionadoconesatarea;despuésunolehaceunapreguntayella
responde.
3

## Lamina 4

7.0.3Repasoderegresiónycomplejidad(slides5,6y7)
• Ejemplodelárbol: predecirelpesodeunárbolenfuncióndelradiodeltroncoaunaalturadefinida,
sinnecesidaddecortarlo. Sedisponedeárbolesyacortadosdelosqueseconocepesoyradio.
• �� � �Laregresiónlineal eslinealenlosparámetrosaajustar ,loquepermiteusarpolinomiosdegrado
1,2,10o p.
• Complejidad: unmodeloconpocosparámetrosessimple;unodegrado10tienemuchosparámetros.
• Problema: elmodelodegrado10pasaperfectamenteportodoslosdatospero sesobreajustayno
generaliza. Mirarsoloelerrorsobreelconjuntoconelqueseentrenónopermitedecidirlacomplejidad
correcta.
7.0.4Generalizaciónyvalidacióncruzada(slide8)
Preguntadelprofesor: “¿cómopodemosmedirsielmodeloestágeneralizandocorrectamente?” Respuesta
de un estudiante, validada:con un conjunto de datos de prueba que no se haya usado durante el
entrenamiento.
¿Cómoevaluarsiestoysobreajustado? ¡VALIDACIÓNCRUZADA! Dividomiconjuntodedatos
entres: - Conjuntodeentrenamiento: seusaparaqueelmodeloaprenda. - Conjuntode
validación: se utiliza para ajustarhiperparámetros(por ejemplo, el orden del polinomio). -
Conjuntodetest: seusaparaevaluar. Elmodelonuncalohavisto.
DistintasestrategiasdeVC: k-fold,shufflesplit,bootstrapping .
�� � �Dos afirmaciones fuertes del profesor en el repaso: 1.“Validación cruzada en general uno lo usa
casisiempre. Yodiríaquesiempre.” 2. Seusa paracualquiertareadeaprendizaje,supervisadaono
supervisada.
�� �Sobreelsímbolodeadvertencia: “cuandoaparezcaestesimbolito,quieredecirquehayun
pocodematemáticamásdensa” ,yquienestenganbackgroundmatemáticopuedenprestarlemás
atención. Enestaclaseapareceúnicamenteenlas slides14(SVM) y30(medidasdeimpureza) .
�� � �7.0.5Declaracióndeintencionesdelaclase
“Laclasedehoyvamosahaceralgomuyparecidoalodelaclasepasada,peroenvezdehablarde
regresiónvamosahablardeclasificación. Yvamosaverlosdistintoscomponentesquehabíamos
vistoenlaclasepasadapararegresión. Clasificaciónesmuyparecidoaregresión.”
�� � �Implicanciadeestudio: convieneestudiarestaclase enparalelo conladeregresión,componentepor
componente(modelo→funcióndeerror/métricas→generalización→validacióncruzada).
Agendaoficial(slide9)
Unidad Tema
01 Clasificación
02 SupportVectorMachine
03 Evaluación
04 Métodosbasadosenárboles
4

## Lamina 5

7.1Clasificación—Esencial
7.1.1Definiciónformal(slide11)
Elaprendizaje supervisado: - Utiliza unconjunto de entrenamientocompuesto por: -atributos xᵢ-
etiquetasyᵢ -Objetivo: determinaruna funciónquetomelosatributosypredigalaetiqueta . -Sila
etiquetaapredeciresunacategoría,entonceslollamamosclasificación.
Formalmente: ŷ=f(x) .
�� � �Convencióndelgorrito(idénticaalaclasederegresión):
Símbolo Significado
ŷ(congorrito) Estimación/ prediccióndelmodelo
y(singorrito) Etiqueta realdeldato
�� � �“Todoestoqueacabodemostraracáesexactamentelomismoquevimoslasemanapasada
con regresión. Pero ahora la diferencia: si la etiqueta es una categoría, entonces lo llamamos
clasificación.”
7.1.2Ejemplocentral: perrosygatos(slide10)
Construcciónpasoapasoenclase:
Elemento Enelejemplo
Atributos(x) x₁= tamañodelanimal ;x₂= tamañodelasorejas
Etiqueta(y) perro ogato(marcadaconelcolordelbordede
cadaimagen: azul=perro,verde=gato)
Modelo Unalínearecta quedivideelplano: arriba/derecha,
perro;abajo/izquierda,gato
Uso(inferencia) Anteunanimalnuevosemidensusdosatributosy
sevedequéladodelarectacae
�� � �Porquéessupervisado: “porqueyoséquéesloqueescadaanimaldentrodemiconjuntodedatosode
miconjuntodeentrenamiento” .
�� � �Advertenciarealistadelprofesor: enlaprácticanosetendrándosatributosniserántamañosdeoreja;
setendránmuchosmásatributosylastareaspuedensertancomplejascomosequiera.
7.1.3 ������Variablecategóricavs.variablenumérica—Esencial
Estefueelpuntoenqueelprofesormásinsistió(≈10minutos,convariasrespuestasdescartadas). Elcriterio
correctonoes“cualitativovs.cuantitativo”,ni“interpolablevs.nointerpolable”:
�� � �LadiferenciaeslanocióndeORDEN.
UnavariablecategóricaNOtienenocióndeorden . UnavariablenuméricaSÍlatiene.
• “Siyodigoperro,gato,conejo,yonopuedodecirelperrovieneantesqueelgatoodespuésdelgato.”
• “El1esmenorqueel2,el2esmenorqueel3…Yonopuedodecirelperroesmayorqueelgato.”
5

## Lamina 6

Respuestaspropuestasenclaseyporquéfuerondescartadas
Propuestadelestudiante Veredicto Razóndadaporelprofesor
“Lacategóricamidecualidades” �Descartada Puedenexistircualidadesquese
midennuméricamente
“Enlanuméricatienesentido
interpolar(entre1y2hay1,5),en
lacategóricano”
�“Estásmuycerca,estásallado” Vaenladireccióncorrecta,peroel
criterioexactoeselorden
“Unaescualitativaylaotra
cuantitativa”
�Descartada Contraejemplo: asignarun
puntajede1a5segúnquétan
bonitoesunpaisajees numérico
ycualitativo alavez
“Adultomayor/adultojoven/
adolescente”
�“Zonagris” Soncategorías asociadasauna
variablenumérica (laedad),que
sísepuedeordenar→esuna
discretizacióndeunavariable
numérica,conservaelorden
“Frío/templado/caliente” �Mismocaso Estánasociadasalatemperatura,
queesordenable
“Hombre/mujer” ��Correcta Notieneorden
“Árbol/planta” ��Correcta Elconceptoensímismonotiene
orden(sepuedeordenarsu altura,
peroesoordenalaaltura,noel
árbol)
“Círculo/cuadrado/triángulo” ��Correcta(propuestaporel
profesor)
Nosepuededecirqueuncírculo
seamayorqueuncuadrado
“10°C,20°C” �Esnumérica Sepuedenordenarlas
temperaturas
�� � �Reglaoperativaparaelexamen: “Unacategoríatienenquepensarencosasquetienenciertas
categorías,yesasclasesnoestánasociadasaunavariablenumérica.”
�� � �7.1.4One-hotencoding(preguntadeestudiante)
Pregunta: “¿Seríamalodarleunvalornuméricoaunavariablecategóricaparahacerlosmodelos?”
Respuesta:unmodelomatemático noentiende loquees“perro”o“gato”,asíquehayquetransformarlo
enunnúmero. Esosehacecon one-hotencoding:
Seconstruyeun vectordeltamañodelnúmerototaldecategorías ,seponeun 1enlaposición
delacategoríaalaqueperteneceelobjetoy 0entodaslasdemás.
�� � �Conectadirectamenteconlaunidaddecalidaddedatos,dondeesteconceptoseintrodujo.
������7.1.5Aclaracióncrítica: locategóricoeslaETIQUETA,nolosatributos
Surgidadeunapreguntadeunestudiantequenoentendíacómoajustarunarectasilasvariableseran
categóricas:
�� � �“Cuandohablodevariablescategóricas,estoydiciendoque lo que quiero predecir esuna
variable categórica. Perono estoy diciendo que x₁ o x₂ sean categóricas ; en este caso son
numéricas.”
Enelgráficotípicodelaclasehay tresvalores porcadaobjeto: x₁(numérico),x₂(numérico)yla etiqueta
(categórica,representadacomo+1/−1).
6

## Lamina 7

7.2Modeloslinealesylanocióndecercanía—Esencial
7.2.1Elplanteamiento(slide12enadelante)
Sepasadelejemploconfotosalarepresentaciónabstracta: triángulos(unaclase)y círculos(otraclase)en
elplano(x₁,x₂).
Modelolineal: unalínearectaquedivideelespacioendos. “¿Aquémerefieroconqueeslineal?
Aquedependelinealmentedex₁ydex₂.”
�� � �Paraleloexplícitoconregresión: igualqueenregresiónlineal,sepuedentenermodelosque nosean
linealesenx₁yx₂perosíloseanenlosparámetros .
7.2.2 ������Elexperimentodidácticodelastresrectas
Elprofesordibuja tresrectasdistintas (verde,naranjayazul)ypreguntacuálesmejor. Todas“cumplen”:
todasseparancorrectamentelosdatosdeentrenamiento.
Argumentosdelosestudiantes: -Laverde “estámáspegada” aunodelosconjuntos;haypocoespacioa
unlado. -“Ladistanciacontralarectaesmuybaja,esposiblequeseequivoque.” -Unmodelodebe “dejar
másespacioaesaclasificación” .
Demostracióndelprofesor: colocaelcursorenunpuntonuevocercanoaloscírculos. Esepunto debería
clasificarsecomocírculo, “porqueestámáscercadelosazules” . Larectaverdeloclasificaríamal.
�� � �������Principiofundamentaldelaclase
“Enlarealidad,losobjetosmáscercanosgeneralmentesondelamismaclase.” Poresoel
modelotienequedividirelespaciodemodoquelascoordenadasmáscercanascorrespondana
lasclasesmáscercanas.
�� � �Analogíaaportadaporunestudianteyvalidadacomo “muy buena”: loscírculossoncasasdeun
barrio,lostriánguloscasasdeotrobarrio,y loqueestáentremedioesunacalle queseparaambosbarrios;
alconstruirunacasanuevahayquerespetareseespacio.
�� � �7.2.3Ningúnmodeloesperfecto
“Losmodelosnuncasonperfectos. Unmodelo100%perfecto,yoaltirodudodeesemodelo,porque
lanaturalezanoes100%perfecta. Hayperrosqueparecengatos,haygatosqueparecenperros.”
Ejemplodado: unchihuahua(perromuypequeño)podríaserclasificadocomogato. Esoesunerror,pero
esesperable.
�� � �Estaideaserepite tresveces enlaclase(aquí,enlacurvaROCyalhablardeLLMquealucinan). Esun
candidatoclaroapreguntaconceptual.
�� � �7.2.4Digresión: KNN—Kvecinosmáscercanos—Complementario
Surgidadeunapreguntadeunestudiantequerecordabaelmodelo.
• Sedefine Kapriori (porejemplo,K=3).
• Para clasificar un punto nuevo se buscan susKvecinosmáscercanos y se le asigna una etiqueta
relacionadaconellos.
7

## Lamina 8

• Ejemplosnuméricosdadosenclase(K=3):
Vecinosencontrados Predicción
3triángulos 100%probabilidaddetriángulo
3círculos 100%probabilidaddecírculo
2triángulos+1círculo 66,6%triángulo/33,3%círculo
�� � �Nota: elmodeloentrega probabilidades,nosolounaetiqueta. Estoreapareceen§7.5conelumbralde
clasificación.
7.3SupportVectorMachine(SVM) �� �—Esencial
(Notadetranscripción: latranscripciónautomáticaescribesistemáticamente“SupportVectorMatching”;el
términocorrecto,queapareceenlasslides12,13y14,es Support Vector Machine =máquinadesoporte
vectorial.)
7.3.1Ideaintuitiva(slide13)
1. Setomaunmodelolinealcandidato(larectasólida).
2. Seidentificanlos vectoresdesoporte : elcírculomáscercano yel triángulomáscercano aesarecta.
�� � �“Cuandodigounvectorestoyhablandocomounpuntoenelespaciodeparámetros.”
3. Setrazandos planosparalelos alarectaquepasanporesosvectoresdesoporte.
4. Elmargenesladistanciaentreesosdosplanos.
5. SebuscaelmodeloqueMAXIMIZAelmargen.
�� � �Comparaciónhechaenvivo: paralarectaazul(pegadaalosdatos),losplanosdesoportequedan
muchomásjuntos→margenmenor. Larectademáximomargeneslapreferible.
7.3.2Etiquetas+1y−1
�� � �“Primeroaunodelosobjetosleponemoslaetiquetamásunoyalotroobjetolepongola
etiqueta menos uno. Esto es solamente unaherramienta matemática para poder ajustar el
modelo.”
Convenciónusadaenlasslides13y14: círculos=+1 ,triángulos=−1 .
7.3.3 �� �Formulaciónmatemática(slide14)
Lostreshiperplanos:
𝑤 ⋅ 𝑥 − 𝑏 = 0 (fronteradedecisión)
𝑤 ⋅ 𝑥 − 𝑏 = 1 (planodesoportedelaclase + 1)
𝑤 ⋅ 𝑥 − 𝑏 = −1 (planodesoportedelaclase − 1)
Elmargen:
8

## Lamina 9

margen = 2
‖𝑤‖
Elproblemadeoptimización:
min
𝑤, 𝑏
‖𝑤‖ sujetoa 𝑦𝑖(𝑤 ⋅ 𝑥𝑖 − 𝑏) ≥ 1
�� � �Desarrolloexplicadoenclase
Elemento Explicacióndada
x(negrita) Vectordeatributos: (x₁,x₂)enelejemplo,pero
puedetenercualquierdimensionalidad
w(negrita) Vectorde parámetrosaajustar : (w₁,w₂). �� � �“Se
acuerdancuandoajustabaunmodeloderegresión,
teníamoselθ₁,elθ₂;acáloswsonesosparámetros
quehayqueajustar”
Productopunto w·x=w₁x₁+w₂x₂→unmodelolineal
b �� � �Valorconstantequepermite moverelplano ;sin
élelplanoquedaríasiemprepasandoporelorigen
¿Porquéestaforma? Esla formagenéricadedefinirunhiperplano ,
válidaparacualquierdimensionalidad
Maximizar2/‖w‖ Esequivalenteaminimizar‖w‖
������Interpretacióndelarestricción(desarrolladaconpreguntasalaclase)
• Para loscírculos(yᵢ = +1): se exige quew·xᵢ−b≥1 → todos los puntos de un lado dan valores
positivosy≥1.
• Paralos triángulos(yᵢ=−1): comoyᵢ=−1,paraqueelproductoyᵢ(w·xᵢ−b)sea≥1,eltérmino (w·xᵢ−
b)tienequesernegativo .
�� � �“Deaquíhaciaallátodotienequesernegativo;deaquíhaciaacátodotienequeserpositivo.”
Usodelmodeloyaajustado(inferencia): secalculaw·x−bparaelpuntonuevoysemiraelsigno/valor
paraasignarlaclasepositivaonegativa. (Observación: enlatranscripciónelprofesordice“siesmayorque1
esdelaclasepositivaysiesmenorque1esdelaclasenegativa”;porlaconstruccióndelostreshiperplanos,la
condiciónsimétricacorrespondientealladonegativoeselplanow·x−b=−1. Sedejaconstanciaporquees
unaimprecisiónverbal,nouncontenidodelaslide.)
�� � �7.3.4Dimensionalidadehiperplanos
• Con2atributoslafronteraesuna línearecta;conmuchasdimensionesesun planoenaltadimen-
sionalidad=hiperplano .
• Ladimensionalidaddelproblema=elnúmerodeatributos. Siaperro/gatoseleagregancolor,
altura,peso,tamañodelaspiernas,etc.,creceladimensionalidad.
• �� � �“Enlaprácticayonotengodosatributos,sinoquetengo,nosé,cienatributos” ;elejemplo2Dessolo
pictórico.
• �� � �Anticipodelcurso: existentécnicasdereduccióndedimensionalidad queseveránmásadelante.
9

## Lamina 10

�� � �7.3.5ContextohistóricodelaSVM—Complementario
• Fueelmodelomatemáticomásutilizadoalrededordelaño2000 .
• Razones: esmatemáticamentemuypuro (esfácildemostrarcosasconél),es fácildeajustar yes
rápido,porquesolohayqueresolverunproblemadeoptimización.
• Enlaprácticaseresuelve numéricamente,sobretodocuandolosdatosdeambasclases secruzan (es
decir,nosonperfectamenteseparables).
• �� � �Sepuededemostrarmatemáticamenteque, bajociertossupuestossobreladistribucióndelos
datos,maximizarelmargenequivaleaquetodoslospuntosdelespaciodeparámetrosquedenmás
cercadesupropiaclase. “Nolovamosahacerenestaclase.”
7.4 Evaluación de modelos de clasificación — Esencial (bloque más
examinable)
7.4.1Elplanteamiento(slides15y16)
Conelmodelolinealajustadoaparecenerrores: enlafiguradelaslide16hay dostriángulosenlazonade
loscírculos yuncírculoenlazonadelostriángulos .
�� � �Spoilerdelprofesor: unopodríadibujarunafronteracurvaquenocometaningúnerror, “perohayun
problemaconesemodelo” →unestudianterespondedeinmediato: nogeneraliza. Seretomaen§7.4.5.
7.4.2Positivosynegativos: laconvención
�� � �“Unodelosobjetoslosvoyallamarpositivosylosotrosobjetoslosvoyallamarnegativos. Y
noesqueamímegustenmásloscírculosquelostriángulos,eslaconvención.”
Laelecciónesarbitraria: siseinvierte(triángulospositivos,círculosnegativos) “tambiénfunciona,todo
funcionaperfecto,unollegaalasmismasconclusiones” .
Enelejemplodelaclase: círculos=positivos ,triángulos=negativos .
7.4.3Definiciones(slide17)—memorizar
Símbolo Nombre Definiciónoficial(slide)
P Positivosreales Totaldeobjetosque realmente
sonpositivos
N Negativosreales Totaldeobjetosque realmente
sonnegativos
VP VerdaderoPositivo Positivo correctamente
clasificado
VN VerdaderoNegativo Negativo correctamente
clasificado
FP FalsoPositivo Negativoincorrectamente
clasificadocomopositivo
FN FalsoNegativo Positivoincorrectamente
clasificadocomonegativo
�� � �Reglamnemotécnicaimplícita: elprimertérmino(verdadero/falso)dicesielmodeloacertó;el segundo
(positivo/negativo)dice quépredijoelmodelo . Unfalsonegativo “deberíaserpositivo,perofalsamentese
disfrazódenegativo” .
10

## Lamina 11

������7.4.4Fórmulas(slide18)
Métrica Fórmula Quéresponde
Exactitud(accuracy) (VP+VN)/(P+N) ¿Quéporcentajedeltotalfue
clasificadocorrectamente?
Error (FP+FN)/(P+N) ¿Quéporcentajefueclasificado
incorrectamente?
Tasadeverdaderospositivos =
recall
VP/(VP+FN)= VP/P Detodoslosque realmenteeran
positivos,¿cuántosrecuperóel
modelo?
Precisión VP/(VP+FP) Detodoloqueelmodelo dijo
queerapositivo ,¿cuánto
realmenteloera?
Tasadefalsospositivos FP/(FP+VN)= FP/N Detodoslosque realmenteeran
negativos,¿acuántosmarcó
falsamentecomopositivos?
�� � �Observaciónclavesobreeldenominadordelrecall: “losverdaderospositivosmáslosfalsosnegativos
sonlospositivostotales” →poresoVP/(VP+FN)=VP/P.Análogamente,FP+VN=N.
�� � �Sobreelnombre: enlaslibreríasdeprogramaciónlatasadeverdaderospositivosaparececomo recall,
yporesoenlaprácticatodoslallamanasí.
������Ejemplonuméricocompleto(slides16y19)—conteohechoenclase
Cantidad Valor Cómoseobtuvoenclase
P(círculosreales) 7 Conteodirectoenlafigura
N(triángulosreales) 9 Conteodirecto(unestudiantedijo
7;elprofesorrecontó: 9)
VP 6 Círculosdelladodelospositivos
VN 7 Triángulosdelladodelos
negativos
FP 2 Triángulosquecayeronenlazona
delospositivos
FN 1 Elúnicocírculoquecayóenla
zonadelosnegativos
Verificación:VP+FN=6+1=7=P ��·VN+FP=7+2=9=N ��·Total=16objetos.
Métricasresultantes (cálculoderivadodelasfórmulasdelaslide18aplicadasaestosconteos;elprofesorno
losevaluónuméricamenteenclase) :
Métrica Cálculo Resultado
Exactitud (6+7)/16 0,8125
Error (2+1)/16 0,1875
Recall(TVP) 6/7 ≈0,857
Precisión 6/(6+2) 0,75
Tasadefalsospositivos 2/9 ≈0,222
11

## Lamina 12

������7.4.5Recallvs.Precisión—laconfusiónmásprobable
�� � �“Nosésientiendenladiferenciaentrelatasadeverdaderospositivosylaprecisión. Creoque
esoessúperimportante,porque miden dos cosas distintas aunque se parecen mucho .”
Precisión Recall(TVP)
Preguntaqueresponde “Mimodelomedijoquetodoesto
erapositivo: ¿quéporcentajede
esorealmenteespositivo?”
“Detodoslosquerealmenteeran
positivos,¿quéporcentajefue
capazderecuperarmimodelo?”
Denominador Loqueelmodelo predijocomo
positivo(VP+FP)
Loque realmenteera positivo
(VP+FN=P)
Sedegradapor… Falsospositivos (falsasalarmas) Falsosnegativos (casosquese
escapan)
�� � �Ejemplodesarrollado: deteccióndeanomalíasenunamáquina
Escenario: unmodelopredicecuándovaafallarunamáquina. Lasfallassonraras: unacadamilmediciones .
Sedefine falla=positivo .
Supongamosrecall=100% yprecisión=70% :
Métrica Interpretación
Recall100% Todas lasfallasrealessondetectadas: siempreque
hayunafalla,elmodelolaencuentra. Nuncase
escapaninguna
Precisión70% Decada 10alertas quedaelmodelo, 7sonfallas
realesy3sonfalsasalarmas
Consecuenciaoperativaconcretadescritaenclase: “Elmodelomedijoquevaafallarlamáquinayyo
frenolamáquina,ydigoparen,paren,paren” …yvariasdeesasvecesnohabíafallareal.
�� �Notadefuente: elprofesorseequivocóalplantearlosnúmerosporprimeravezysecorrigió
explícitamenteenclase( “meequivoqué,lohicealrevés” ). Laversióncorrecta,laquequedó,esla
delatablaanterior: precisión=7/(7+3)=0,7.
�� � �Aportedeunestudiante,validadoporelprofesor—ejemplomédico: enunexamendeunaenfer-
medadgrave(semencionóelVIH)interesaquela tasadeverdaderospositivosseamuyalta : “nomequiero
perderninguno;medalomismoequivocarme,porquesimeequivocoprefierodiagnosticarequivocadamentey
quelapersonasevayaahacerunsegundoexamen” .
7.4.6Matrizdeconfusión(slide19)—Esencial
�� � �“Lamatrizdeconfusión,yocreoquees una de las herramientas más útiles parasabercómo
seestácomportandomimodelo.”
Construcción: enunejela etiquetareal yenelotrola etiquetapredicha (“dalomismocuálpongo” ). Cada
celdacuentacuántosobjetoshayenesacombinación.
Matrizdelejemplodelaclase(concírculos=positivos):
Real: ○(círculo) Real: △(triángulo)
Predicho: ○(círculo) 6 (VP) 2(FP)
Predicho: △(triángulo) 1 (FN) 7(VN)
12

## Lamina 13

������Dospropiedadesqueelprofesordestacó
1. Conlamatrizsepuedecalculartodoloanterior : exactitud,error,recall,precisiónytasadefalsos
positivossalendirectamentedesuscuatroceldas.
2. Segeneralizaamásdedosclases : sepuedenagregarrombos,cuadradosoloquesea. Yentoncesla
matrizmuestra quéseestáconfundiendoconqué ,dandounaintuicióndeporqué: “seguramentelos
gatossevanaconfundirconlosperrosmásqueconunaserpiente,porquesonmásparecidos” .
�� � �7.4.7Aclaración: elR²esderegresión,nodeclasificación
Preguntadeunestudiante: ¿estasmétricasreemplazanalR²vistoantes? Respuesta: elR²seusapara
regresión(mideelporcentajedevarianzaquerepresentaunmodeloderegresión). Enclasificaciónsemiden
estosotrostiposdeerrores .
7.5Complejidad,sobreajusteyvalidacióncruzadaenclasificación—
Esencial
7.5.1Modelosmáscomplejos(slides15y20)
Ademásdelmodelolinealexistenmodelosmuchomáscomplejos: �� � �“comoporejemplounaredneuronal;
lasredesneuronalesqueseusanhoyendíasonmuycomplejas” .
Laslide20muestrauna fronteradedecisiónmuyirregular queencierraperfectamentecadagrupode
puntosy nocometeningúnerrordeentrenamiento . Sobreellaapareceunpuntonuevo(elrombocon
“?”) rodeadodecírculosperoencerradodentrodelaregióndelostriángulos.
������Eldiagnóstico: esemodelo nogeneraliza. “Sidespuésmeaparecealgoacá,vaadecirmi
modeloqueesuntriángulo” ,cuandoporcercaníadeberíasercírculo.
�� � �Esteeselequivalenteexacto,enclasificación,delpolinomiodegrado10delaclasederegresión.
Laslide15loilustraconelmismopardefiguras: unafronteracurvaycomplicadafrenteaunafronteralineal
simple.
7.5.2Lasolución: validacióncruzada(slide21)
Laslide21es idénticaalaslide8 : elprofesorlarepitedeliberadamente. Lostresconjuntos(entrenamiento
/validación/test)ylasestrategias( k-fold,shufflesplit,bootstrapping )son exactamentelosmismos que
enregresión.
������Logenuinamentenuevodeestaclase
�� � �“Hagoexactamentelomismoquehiceconregresión[…]ypuedomedirtodoloqueyoquiera
demaneradesabersielmodeloescapazdegeneralizar: generalizarentérminosdela precisión,
odela tasa de falsos positivos,oenfuncióndela exactitudodel error. Puedomedirtodoeso
usandovalidacióncruzada.”
�� � �La validación cruzada esagnóstica a la métrica: en regresión se usaba con el error cuadrático; en
clasificaciónseusaconcualquieradelascincométricasdela§7.4.4.
�� � �7.5.3Laregladeorodelcurso
������“Acuérdensequesinosabenlarespuesta,diganvalidacióncruzada. Nosiempre,perolamayor
partedelasveceslarespuestaesvalidacióncruzada.”
13

## Lamina 14

7.6Umbral,puntodeoperaciónycurvaROC—Esencial
7.6.1Delaprobabilidadalaetiqueta
�� � �Muchosmodelos noentreganunaetiquetasinounaprobabilidad . Ejemplosdiscutidosenclase:
Salidadelmodelo Decisión
90%perro/10%gato Razonablemente, perro
50%perro/50%gato Indeterminado—hacefaltaunaregla
�� � �Definiciónoperativa: parapasardeprobabilidadaetiquetasedefineun umbral. “Enmi
cabezasiempreelumbralescomodeun50%,pero no tiene por qué ser un 50% : podríaserun
55%oun60%.”
������7.6.2Elumbralesunhiperparámetroquemuevelafrontera
Alsubirobajarelumbral, lafronteradedecisiónsedesplaza haciaunladouotro,cambiandosimultánea-
menteelrecallylatasadefalsospositivos. Laslide22lodiceexplícitamente: “elmodelopuedevariarde
acuerdoaunhiperparámetro,porejemplo,unumbraldeclasificación” .
7.6.3 ������Elejerciciodelasslides22y23
Enunciado(slide22): dadoscuatromodelosquedifierensoloenelumbral,calcularlatasadeverdaderos
positivosylatasadefalsospositivos,usando:
TVP = 𝑉 𝑃
𝑃 TFP = 𝐹 𝑃
𝑁
Soluciónoficial(slide23)ylecturahechaenclase:
#
Posicióndela
frontera TVP TFP
Comentariodel
profesor
1 Muyrestrictiva 0,3 0,0 “¡Québuenatasa
defalsospositivos,
notengoningún
falsopositivo!…
peroseteestá
yendoel70%delos
positivosa
negativos”
2 Unpocomás
permisiva
0,6 0,0 Estrictamente
mejorquela
anterior: subeel
TVPyelTFPse
mantieneen0
3 Máspermisiva 0,8 0,2 Mejorrecall,pero
“latasadefalsos
positivosempezóa
aumentar”
14

## Lamina 15

#
Posicióndela
frontera TVP TFP
Comentariodel
profesor
4 Máximamente
permisiva
1,0 0,6 Recallperfecto,al
costodeun60%
defalsospositivos
7.6.4LacurvaROC(slide24)
CurvaROC (ReceiverOperatingCharacteristic ): gráficodela tasadeverdaderospositivos(eje
Y)enfuncióndela tasadefalsospositivos(ejeX) ,obtenidoalrecorrertodoslosvaloresdel
umbral.
Loscuatropuntosdelejerciciosegraficancomo(TFP,TVP):(0,0·0,3),(0,0·0,6),(0,2·0,8)y(0,6·1,0).
������CómoleerunacurvaROC
Pregunta Respuestadadaenclase
¿Dóndeestáelmodeloperfecto? Esquinasuperiorizquierda: ejeX(TFP)lomás
cercanoa 0yejeY(TVP)lomáscercanoa 1
¿Sealcanzaenlapráctica? No. “Ningúnmodeloesperfecto,entoncesnuncavaa
llegarhastaallá” ;haymodelosqueseacercan
mucho
¿Cómocomparardosmodelos? Seprefierelacurvaque pasamáscercadela
esquinasuperiorizquierda
(Laslide24incluyeademásunarectadiagonaldereferenciadesde(0,0)hasta(1,1);elprofesornolacomenta
explícitamenteenlatranscripción.)
������7.6.5Puntodeoperación
�� � �Definición: elpuntodeoperación eselumbralqueseelegiráalponerelmodeloen
producción.
• Siesmuyimportantequela tasadefalsospositivosseabaja →hayqueubicarseenla parteizquierda
delacurva.
• Siesmuyimportantetenerun recallalto →hayqueubicarseenla partesuperior delacurva.
• Siemprehayuntrade-off. Laelección noesmatemáticasinodenegocio : “enalgúnmomentotú
tienesquehacerlosnúmeros—asícomolohicimosantesconcuántasvecesfallalamáquina—yconese
númerodefineselpuntodeoperacióndelmodelo” .
�� � �Preguntadeestudiante: ¿existeunóptimoglobal? Respuesta: elóptimoteóricoeslaesquinasuperior
izquierda,pero ningúnmodelollegaahí ;enlapráctica dependedeloqueunoestébuscando .
�� � �Cierredelasección: “Inclusolosmodelosdeinteligenciaartificialmássofisticadosdehoyendía,como
losmodelosdelenguaje,seequivocan,yesoesloqueunodiceque alucinan.”
15

## Lamina 16

7.7ÁrbolesdeDecisión—Esencial
7.7.1Ideageneral(slides25y26)
Unárboldedecisión dividerecursivamenteelespaciodeatributos . Enelejemplodelaslide26elconjunto
inicialtiene 9triángulosy8círculos (17objetos):
Paso División Resultado
1 Seeligeunatributo(x₁)ysecorta Izquierda: 1 △+6○ ·Derecha: 8
△+2○
2 Enelsubconjuntoizquierdose
cortaporx₂
Arriba: 1 △+1○ ·Abajo: 5○
(puro)
3 Enelsubconjuntoderechose
cortaporx₂
Arriba: 1○ (puro)·Abajo: 8 △+
1○
�� � �Objetivodecadadivisión: “tratodequetodosloscírculosquedenaunladoytodoslostriángulosalotro” ,
aunqueengeneralnoseconsiguedeunasolavez.
������Cómoprediceunárbol
Unobjetonuevo caeenunadelascajas (hojas)yseleasignalaproporcióndeclasesdeesacaja:
Hojadondecaeelpunto Predicción
Cajaconsolocírculos 100%deprobabilidaddesercírculo
Cajacon1círculoy1triángulo 50%deprobabilidaddesercírculo
�� � �IgualqueenKNN,lasalidanaturaldelárbolesuna probabilidad,nounaetiquetadura. Poresoreaparece
elconceptodeumbral(§7.6).
7.7.2 ������Elproblemacentral: ¿quéatributousarydóndedividir? (slide26)
Idea: escogerdivisionesquehagan “puros”lossubconjuntos.
Laslide26contrasta,sobreelmismoconjuntodedatos: - Conjuntosimpuros: uncorteverticalquedeja
mitadtriángulosymitadcírculosacadalado. - Conjuntospuros: uncortehorizontalquedejasolotriángulos
arribaysolocírculosabajo.
Preguntaqueabrelasección: ¿cómomedirlaimpureza?
7.7.3 ������ImpurezadeGini(slides27,28y29)—Esencial
Definición(slide27): laimpurezadeGini mideelerroresperado …siseescogealeatoriamente
unobjeto …ysepredicelaclasedetodoelconjuntobasadoenél.
Ejemplo1(slide27)—conjuntocon3triángulosy5círculos
Paso Valor
P(elegirtriángulo) 3/8
P(elegircírculo) 5/8
16

## Lamina 17

Paso Valor
Sielijotriánguloyclasificotodocomotriángulo,el
errores…
5/8(meequivocoentodosloscírculos)
Sielijocírculoyclasificotodocomocírculo,elerror
es…
3/8
Erroresperado 3/8×5/8+5/8×3/8=0,46875
Ejemplo2(slide28)—conjuntocon1triánguloy7círculos
Paso Valor
P(triángulo)=1/8·P(círculo)=7/8
Errorsielijotriángulo 7/8
Errorsielijocírculo 1/8
Erroresperado 1/8×7/8+7/8×1/8=0,21875
Ejemplo3(slide29)—conjuntototalmentepuro(solocírculos)
0×1+1×0=0. �� � �Razonamientopedidoenclase: laprobabilidaddeelegiruntriánguloes0;ladeelegir
uncírculoes1, peroelerrordehaberelegidouncírculoes0,porquenohayningúntriánguloquese
puedaequivocar.
������Interpretaciónclave
�� � �“Fíjensequeloqueestámidiendoestoesla impureza: mientrasmásimpuroeldataset,más
altovaaserestaimpurezadeGini.”
Escala: 0=conjuntoperfectamentepuro ;valoresmayores=másmezcla.
Fórmulageneral(slide29)
ConCclases,Npuntostotalesy Nᵢpuntosdelaclase i:
𝐼𝐺 =
𝐶
∑
𝑖=1
𝑁𝑖
𝑁 (1 − 𝑁𝑖
𝑁 )
�� � �“Exactamentelomismoquehicimosantesconlostriángulosycírculos,peroacáestáparamuchasclases.”
7.7.4 �� �Otrasmedidasdeimpureza(slide30)
Medida Fórmula(segúnlaslide)
Descripcióndadaen
clase Máximo(2clases)
Gini 𝐼𝐺 =
∑𝐶
𝑖=1
𝑁𝑖
𝑁 (1 − 𝑁𝑖
𝑁 )
Erroresperadoal
predecirconunobjeto
elegidoalazar
0,5
Entropía 𝐻 =
∑𝐶
𝑖=1
𝑁𝑖
𝑁 log2( 𝑁𝑖
𝑁 )
�� � �“Elpromediodela
informaciónquecontiene
elexperimentodesacar
undato”
1
17

## Lamina 18

Medida Fórmula(segúnlaslide)
Descripcióndadaen
clase Máximo(2clases)
Errordeclasificación 𝐼𝐸 = 1 − max𝑖 ( 𝑁𝑖
𝑁 ) �� � �“Siyoclasificotodo
deunaciertaforma,
¿cuálvaasereseerror?”
0,5
Lecturadelgráficodelaslide30: elejeXes Nᵢ/N(proporcióndeobjetosdeunaclase). En 0todoslos
objetossondeunaclaseyen 1todossondelaotra;enambosextremoslastresmedidasvalen0. Elmáximo
delastresestáen0,5(mezclaperfecta).
(Notaexterna: talcomoestáimpresaenlaslide,lafórmuladelaentropíanollevaelsignonegativo
quelaharíapositivaycoincidenteconlacurvagraficada. Sereproducelafórmulatalcualaparece
enlaláminaysedejaconstanciadelaobservación.)
������7.7.5LamedidadeimpurezaesunHIPERPARÁMETRO
Preguntadeunestudiante: “¿Enquécontextoconvienemásusarunauotra?”
Respuestadelprofesor,construidasocráticamente: > �� � �“Fíjensequeestoesalgoqueunoescoge antes
deajustarelmodelo. ¿Cómosellamaeso? […]Esun hiperparámetro. Entoncestúlotienesqueelegirapriori,
ygeneralmenteloqueunohaceesque lo elige usando validación cruzada.”
�� � �Aporte de un estudiante:desde el punto de vista computacional,la entropía es más costosa de
calcularporquetieneunlogaritmo . Elprofesornodauncriterioadicionaldesdelacienciadedatos: remite
avalidacióncruzada.
7.7.6 ������Gananciadepureza(slide31)
Preguntaqueresuelve: ¿cuántapurezaestoyganandoconcadadivisión? Secomparan: -La impurezadel
nodopadre. -Laimpurezadelosnodoshijos ,ponderadaporsutamaño.
Δ𝐼𝐺 = 𝐼 𝐺(𝐴) − 𝑁 (𝐵)
𝑁 (𝐴)𝐼𝐺(𝐵) − 𝑁 (𝐶)
𝑁 (𝐴)𝐼𝐺(𝐶)
�� � �Porquélaponderación: “EstoestáponderadoporelnúmerodeobjetosqueestáenBsobreel
númerodeobjetosqueestáenA.Osea, si hay muchos objetos en un lado, esa impureza pesa
másqueladelotrolado.”
Ejemplonuméricodelaslide31
Nodo Composición N Gini
A(padre) 9 △+8○ 17 (vercálculo)
B(hijoizq.) 1 △+6○ 7
C(hijoder.) 8 △+2○ 10
Desarrollo(cálculoderivadoaplicandolasfórmulasdelasslides29y31alosconteosdelalámina;elprofesor
noloevaluónuméricamenteenclase) :
• 𝐼𝐺(𝐴) = (9/17)(8/17) + (8/17)(9/17) ≈ 0,4983
• 𝐼𝐺(𝐵) = (1/7)(6/7) + (6/7)(1/7) ≈ 0,2449
• 𝐼𝐺(𝐶) = (8/10)(2/10) + (2/10)(8/10) = 0,3200
• Δ𝐼𝐺 = 0, 4983 − (7/17)(0, 2449) − (10/17)(0, 3200) ≈ 0,2092
18

## Lamina 19

7.7.7AlgoritmoC4.5(slide32)—memorizarelprocedimiento
Mientrasnosecumplaalgúncriteriodeconvergencia: 1. Paracadaatributo, calcular la
gananciadedividireneseatributo. 2. Sea xelatributocon mayorganancia. 3. Crearunnodo
dedecisión quesepareconrespectoax. 4. Aplicarestemismoalgoritmo alossubconjuntos
creadosaldividirporx (recursión).
(Notadetranscripción: latranscripciónautomáticaregistra“criteriodeemergencia”;laslide32dice criterio de
convergencia.)
7.7.8Criteriosdeconvergencia(slide33)—cuándodejardedividir
Elárboldejadecrecercuando:
1. Elnodocontiene solamenteunaclase .
2. Elnodocontiene menosdeunvalordeseadodeobjetos .
3. Sealcanzóuna alturamáxima.
4. Lapurezaessuficiente .
5. Secomienzaasobreajustar →detectadomediante validacióncruzada.
�� � �“Amedidaqueempiezaadividir,unopuedeestarhaciendovalidacióncruzada.”
������7.7.9Laconfesióndelprofesor: losárbolessolossonmalos
�� � �“Losárbolesdedecisión—yometoméeltiempodeexplicarloytodoesto—pero son muy
malos modelos, son como de los peores modelos que uno podría tener en la vida . Entonces
ustedesvanadecir‘¿peroporquémeestánenseñandoesto?’,yyolesvoyadecir: porque los
árboles de decisión son la base de los modelos basados en bosques ,ydentrodeesoestáel
Random Forest yel XGBoost.”
7.8RandomForest—Esencial
7.8.1Lasabiduríadelosgrupos(slide35)
Citadelaslide(JamesSurowiecki): elconocimientocolectivodeun grupodiversoeinde-
pendientedepersonasgeneralmente excedeelconocimientodecualquierindividuo,ypuede
aprovecharsemediantelavotación .
�� � �Matizimportantequeelprofesorcorrigióenvivo: primerodijoquelasdecisionesnodebenestar
correlacionadas,ydeinmediatosecorrigió: “miento; siempreycuando haya correlación, pero que esa
correlación no sea muy alta”.
�� � �Analogíaconestudiantesreales: siselepreguntaadospersonasylasegundaopina exactamentelo
mismoquelaprimera, “nomesirviómuchohaberlepreguntado” . Lovaliosoesquecadauna veacosasque
laotranove .
7.8.2Motivación(slide36)
• Unárbolsolitarionosuelepredecirmuybien.
• Peroesmuyrápido deajustar.
• Idea: utilizarmúltiplesárboles.
• Restricción: hayqueasegurarsedeque noaprendantodosexactamentelomismo .
19

## Lamina 20

7.8.3 ������Elalgoritmo(slide37)
• nárboles
• Paracadaárbol:
– Seleccionaraleatoriamente Npuntosconreemplazo (bootstrapping)
– Entrenarusando matributosseleccionadosdemaneraaleatoria
• Predicción: promediarlapredicciónhechaporlosárboles
������Ladoblealeatorización(elpuntomásexaminabledeestasección)
Nivel Quésealeatoriza Consecuencia
Datos Cadaárbolrecibeunsubconjunto
distintodepuntos(con
reemplazo)
“Cadaárbolnoesentrenadocon
exactamentelosmismosdatos”
Atributos Cadaárbolrecibeunsubconjunto
distintodeatributos
“Algunosárbolesseespecializanen
algunosatributosyotrosenotros”
�� � �“Entonceshaysolapamiento,hayciertacorrelación” —esdecir,laaleatorización decorrelacionaparcial-
mente,queesexactamenteloquepidelasabiduríadelosgrupos.
�� � �Ejemplodeprediccióncon4árboles
Árbol Predicción
1 perro
2 perro
3 gato
4 perro
→75%deprobabilidaddequeseaunperro.
Formalmente: lapredicciónes 1/nporlasumadelasprediccionesdecadaunodelosárboles .
7.8.4Ventajas(slide38)
1. Ungrannúmerodeárbolesnocorreladostienemejordesempeño quecadaunodelosmodelos
porseparado.
2. Loserrorescometidosporunárbolpuedensercorregidosporotros.
3. Esunodelosalgoritmosmáscerterosqueseconocen . �� � �“EngeneralunocomienzaconunRandom
Forest, y hay muchos problemas en los cuales un Random Forest lo hace mucho mejor que una red
neuronal.”
4. Permiten estimar la importancia de las variables, contandocuántas veces cada variable fue
escogidaporcadaárbolcomorelevante almomentodedividir.
������Importanciadevariables—ejemplonuméricodadoenclase
Variable %devecesescogida Lectura
A 50% Muyrelevante paraclasificar
B 20% Relevante
C 10% Pocorelevante
20

## Lamina 21

Variable %devecesescogida Lectura
D 10% Pocorelevante
�� � �Casoextremo: “sihayunavariablequeningúnárbolescogiónuncaparadividir,entoncesesavariablees
cerorelevante” ynosirveparaclasificarelobjeto.
�� � �Porquéimporta: “tedacomounaintuicióndeloquelosmodelosestánhaciendo” —esdecir,aporta
interpretabilidad.
�� � �7.8.5ContextohistóricoyRandomForestvs.DeepLearning—Complementario
Líneadetiempomencionada:
Época Modelodominante
≈2000 SupportVectorMachine
2000–2010 RandomForest (“fueelquereemplazóalSupport
VectorMachine”)
Después Redesneuronales
¿Cuándoconvienecadauno? (preguntadeestudiante)-Dependedel problema,delos atributosysobre
tododela cantidaddedatos . -Losmodelosde DeepLearning sonmuybuenos “porquesonmuycomplejos
yporquesonentrenadosconmuchos,extremadamentehartosdatos” . -Sinosealcanzaeserégimendedatos
suficientes,unmodeloclásicocomoRandomForestpuedeserpreferible. �� � �“Hayvecesdondetúentrenas
unRandomForestyentrenasunaredneuronalmuycompleja,yelRandomForestlasupera. Y pasa mucho
más seguido de lo que uno creería .” -“Suficientesdatos”esambiguo: “nohayunnúmero,dependedel
problema”.
(Notadefuente: enestepasajelatranscripciónregistralafrase“entonces,engeneral,esmejorusar
unmodelodeDeepLearning”enuncontextodondeelrazonamientocompletodelprofesorapunta
alocontrario—quesindatossuficientesconvieneelmodeloclásico—. Sedejaconstanciadela
aparenteinversión,probablementeundeslizverbalounerrordetranscripción.)
7.9Resumenoficialdelaclase(slide39)
• Clasificación: aprendizajesupervisado paracategorías
• Modelolineal: SupportVectorMachine
• Evaluaciónygeneralización
• Modelosnolineales:
– árbolesdedecisión
– randomforest
(Notadetranscripción: lanarracióndeestaláminaestádegradadaenlatranscripciónautomática,querepite
lapalabra“una”durantecasiunminuto. Elcontenidodelaslideeselreproducidoarriba.)
�� � �Informaciónadministrativa
Lapróximasemanahaypresentacióndeproyectos.
21

## Lamina 22

�� � � � � � � � �FORMULARIODELACLASE
# Concepto Fórmula Prioridad
1 Fronteradedecisión
(SVM)
𝑤 ⋅ 𝑥 − 𝑏 = 0 Esencial
2 Planosdesoporte 𝑤 ⋅ 𝑥 − 𝑏 = ±1 Esencial
3 Margen margen = 2
‖𝑤‖ Esencial
4 OptimizacióndelaSVM
�� �
min𝑤,𝑏‖𝑤‖ s.a. 𝑦𝑖(𝑤 ⋅
𝑥𝑖 − 𝑏) ≥ 1
Importante
5 Productopunto
desarrollado(2D)
𝑤 ⋅ 𝑥 = 𝑤 1𝑥1 + 𝑤2𝑥2 Importante
6 Exactitud 𝑉 𝑃 + 𝑉 𝑁
𝑃 + 𝑁 Esencial
7 Error 𝐹 𝑃 + 𝐹 𝑁
𝑃 + 𝑁 Esencial
8 Recall/Tasade
verdaderospositivos
𝑉 𝑃
𝑉 𝑃 + 𝐹 𝑁 = 𝑉 𝑃
𝑃 Esencial
9 Precisión 𝑉 𝑃
𝑉 𝑃 + 𝐹 𝑃 Esencial
10 Tasadefalsospositivos 𝐹 𝑃
𝐹 𝑃 + 𝑉 𝑁 = 𝐹 𝑃
𝑁 Esencial
11 Identidadesútiles 𝑉 𝑃 + 𝐹 𝑁 = 𝑃 ;
𝑉 𝑁 + 𝐹 𝑃 = 𝑁
Esencial
12 ImpurezadeGini 𝐼𝐺 =
∑𝐶
𝑖=1
𝑁𝑖
𝑁 (1 − 𝑁𝑖
𝑁 )
Esencial
13 Entropía �� � 𝐻 =
∑𝐶
𝑖=1
𝑁𝑖
𝑁 log2( 𝑁𝑖
𝑁 )
(talcomoapareceenla
slide30)
Importante
14 Errordeclasificación �� �𝐼𝐸 = 1 − max𝑖 ( 𝑁𝑖
𝑁 ) Importante
15 Gananciadepureza Δ𝐼𝐺 = 𝐼 𝐺(𝐴) −
𝑁 (𝐵)
𝑁 (𝐴)𝐼𝐺(𝐵) −
𝑁 (𝐶)
𝑁 (𝐴)𝐼𝐺(𝐶)
Esencial
16 Máximosdelasmedidas
deimpureza(2clases)
Gini0,5·Entropía 1·
Errordeclasificación 0,5
Importante
17 PrediccióndeRandom
Forest
̂ 𝑦 =1
𝑛 ∑𝑛
𝑗=1 ̂ 𝑦𝑗
(promediodelosn
árboles)
Esencial
18 Umbralpordefecto 50%(peroesun
hiperparámetro
ajustable)
Importante
22

## Lamina 23

����� �LISTADEDEFINICIONESIMPORTANTES
Término Definición(segúnslidesyclase)
Clasificación Tareadeaprendizajesupervisadoenquelaetiqueta
apredecires unacategoría
Regresión Tareasupervisadaenquelaetiquetaapredeciresun
valorcontinuoonumérico
Variablecategórica �� � �Variablesinnocióndeorden
(perro/gato/conejo;hombre/mujer;
círculo/cuadrado/triángulo)
Variablenumérica �� � �Variableconnocióndeorden (sepuededecir
queunvaloresmayoromenorqueotro)
One-hotencoding Vectordeltamañodelnúmerodecategorías,conun
1enlacategoríadelobjetoy 0enelresto
Aprendizajesupervisado Elqueusaunconjuntodeentrenamientocon
atributosxᵢyetiquetasyᵢ,buscandounafunciónque
tomelosatributosypredigalaetiqueta
Modelolineal(clasificación) �� � �Modelocuyafronteradedecisióndepende
linealmentedelosatributos;divideelespacioen
dos
Hiperplano �� � �Planoenaltadimensionalidad;en2Desuna
línearecta
Vectoresdesoporte �� � �Lospuntosdecadaclase máscercanosala
frontera,quedefinenlosplanosdesoporte
Margen �� � �Distanciaentrelosdosplanosdefinidosporlos
vectoresdesoporte
SupportVectorMachine Modelolinealque maximizaelmargen entrelas
clases
P/N Positivosreales/Negativosreales
VerdaderoPositivo(VP) Positivocorrectamenteclasificado
VerdaderoNegativo(VN) Negativocorrectamenteclasificado
FalsoPositivo(FP) Negativoincorrectamenteclasificadocomopositivo
FalsoNegativo(FN) Positivoincorrectamenteclasificadocomonegativo
Exactitud Porcentajedeobjetosclasificadoscorrectamente
Error Porcentajedeobjetosclasificadosincorrectamente
Recall(tasadeverdaderospositivos) Detodoslospositivosreales,quéporcentaje
recuperóelmodelo
Precisión Detodoloqueelmodelopredijocomopositivo,qué
porcentajerealmenteloera
Tasadefalsospositivos Detodoslosnegativosreales,quéporcentajefue
marcadofalsamentecomopositivo
Matrizdeconfusión Tablaquecruza etiquetareal conetiqueta
predicha;permitecalculartodaslasmétricasyver
quéseconfundeconqué
Umbraldeclasificación �� � �Valordeprobabilidadapartirdelcualseasigna
laclasepositiva;esun hiperparámetro
CurvaROC Gráficodelatasadeverdaderospositivosenfunción
delatasadefalsospositivos,alvariarelumbral
Puntodeoperación �� � �Elumbralqueefectivamenteseusaráalponerel
modeloenproducción
Árboldedecisión Modeloquedividerecursivamenteelespaciode
atributosbuscandosubconjuntospuros
Conjuntopuro Subconjuntoquecontieneobjetos deunasolaclase
23

## Lamina 24

Término Definición(segúnslidesyclase)
ImpurezadeGini Erroresperadosiseescogealeatoriamenteunobjeto
ysepredicelaclasedetodoelconjuntobasadoenél
Entropía �� � �Lainformación enpromedio quecontieneel
experimentodesacarundato
Errordeclasificación(impureza) Errorresultantedeclasificartodoelconjuntocomo
laclasemayoritaria
Gananciadepureza Impurezadelnodopadremenoslaimpurezadelos
nodoshijos, ponderadaporsunúmerodeobjetos
C4.5 Algoritmoclásicodeconstruccióndeárbolesde
decisión,quedividerecursivamenteporelatributo
demayorganancia
RandomForest Conjuntodenárbolesentrenadosconsubmuestras
aleatoriasdedatos(conreemplazo)ydeatributos,
cuyaprediccióneselpromedio
Bootstrapping SelecciónaleatoriadeNpuntos conreemplazo
Sabiduríadelosgrupos Elconocimientocolectivodeungrupodiversoe
independienteexcedeeldecualquierindividuoyse
aprovechamediantelavotación
KNN �� � �Modeloqueclasificaunpuntosegúnlasclases
desus Kvecinosmáscercanos ,conKdefinidoa
priori
���������POSIBLESPREGUNTASDEEXAMEN(conrespuestasbreves)
Verdadero/Falsoconjustificación
# Afirmación V/F Justificación
1 Ladiferenciaentreuna
variablecategóricayuna
numéricaesquela
primeraescualitativay
lasegundacuantitativa.
F Elcriteriocorrectoesla
nocióndeorden .
Contraejemplodel
profesor: puntuarun
paisajede1a5es
numéricoycualitativo
2 “Adultomayor/adulto
joven/adolescente”es
unavariablepuramente
categórica.
F Esuna discretizaciónde
unavariablenumérica
(laedad),quesítiene
orden
3 Enunproblemade
clasificación,los
atributosxdebenser
categóricos.
F Locategóricoes la
etiqueta;losatributos
puedenser
perfectamente
numéricos
4 LaSVMeligecualquier
rectaquesepare
correctamentelosdatos
deentrenamiento.
F Entretodaslasque
separan,eligelaque
maximizaelmargen
24

## Lamina 25

# Afirmación V/F Justificación
5 Maximizar2/‖w‖es
equivalenteamaximizar
‖w‖.
F Esequivalentea
minimizar‖w‖
6 Lasetiquetas+1y−1de
laSVMsignificanque
unaclasees“mejor”que
laotra.
F Essolouna herramienta
matemáticaparapoder
formularlarestricción
7 Unfalsopositivoesun
positivorealqueel
modeloclasificómal.
F Esun negativoreal
clasificadocomo
positivo. Elpositivoreal
malclasificadoesun
falsonegativo
8 Recallyprecisiónmiden
lomismoconnombres
distintos.
F Recallusacomo
denominadorlos
positivosreales;
precisiónusa loqueel
modelopredijocomo
positivo
9 Unmodeloconrecalldel
100%nocometeerrores.
F Puedetenermuchísimos
falsospositivos;elrecall
sologarantizaquenose
escapeningúnpositivo
real
10 Lamatrizdeconfusión
solosirvepara
problemasdedosclases.
F Seextiendeacualquier
númerodeclasesy
ademásmuestra con
quéseconfundecada
clase
11 Elumbraldeclasificación
esunparámetroqueel
modeloaprendedurante
elentrenamiento.
F Esun hiperparámetro:
seeligeantes,
típicamentepor
validacióncruzada,y
defineel puntode
operación
12 EnunacurvaROC,el
modeloperfectoestáen
laesquinasuperior
izquierda.
V TFPlomáscercanoa0y
TVPlomáscercanoa1
13 Alsubirelumbralpara
lograrrecall=1,0,latasa
defalsospositivosse
mantieneconstante.
F Enelejerciciodelaslide
23subea 0,6: siempre
haytrade-off
14 UnaimpurezadeGini
altaindicaunconjunto
muypuro.
F Alrevés: mientrasmás
impuroelconjunto,
másaltalaimpurezade
Gini. Unconjuntopuro
da0
15 LaelecciónentreGini,
entropíayerrorde
clasificaciónseaprende
duranteel
entrenamiento.
F Esun hiperparámetro;
seeligeapriori,
generalmentepor
validacióncruzada
25

## Lamina 26

# Afirmación V/F Justificación
16 Enlagananciadepureza,
ambosnodoshijos
pesanlomismo.
F Estánponderadospor
sunúmerodeobjetos :
N(B)/N(A)yN(C)/N(A)
17 Losárbolesdedecisión,
porsísolos,sondelos
mejoresmodelos
disponibles.
F Elprofesordicequeson
“delospeoresmodelos” ;
suvalorestáenser la
basedelosmodelosde
bosques
18 EnRandomForestbasta
condarleacadaárbol
unsubconjuntodistinto
dedatos.
F Tambiénseleentregaun
subconjuntoaleatorio
deatributos
19 EnRandomForestel
muestreodedatosse
hacesinreemplazo.
F Sehace conreemplazo
(bootstrapping),segúnla
slide37
20 UnRandomForest
nuncapuedesuperara
unaredneuronal.
F “Pasamuchomás
seguidodeloqueuno
creería”,sobretodo
cuandonohay
suficientesdatos
21 Lavalidacióncruzada
soloaplicaaregresión.
F Aplicaacualquiertarea,
supervisadaono,y
sobrecualquiermétrica
(exactitud,error,
precisión,TFP…)
22 ElR²eslamétrica
estándarparaevaluarun
clasificador.
F ElR²esde regresión;en
clasificaciónseusanlas
métricasdelamatrizde
confusión
Preguntasdedesarrollo
P1. ¿Cuálesladiferenciaentreregresiónyclasificación? Ambassontareasdeaprendizajesupervisado
quebuscanunafunciónŷ=f(x)apartirdeatributosyetiquetas. Ladiferenciaestá únicamenteeneltipo
deetiqueta: enregresiónlaetiquetaesun valorcontinuoonumérico ;enclasificaciónesuna categoría.
P2. Distingavariablecategóricadevariablenuméricaydéuncontraejemplodelcriterio“cualita-
tivo/cuantitativo”.Lacategórica notienenocióndeorden (perro,gato,conejo);lanuméricasí(1<2<3).
Elcriteriocualitativo/cuantitativofalla: asignarunpuntajede1a5segúnquétanbonitoesunpaisajeesuna
variablenuméricaycualitativa simultáneamente.
P3. ¿Cómoseleentregaunavariablecategóricaaunmodelomatemático? Medianteone-hotencoding:
unvectordeltamañodelnúmerodecategorías,conun1enlaposicióndelacategoríacorrespondientey0
enelresto. Unmodelomatemáticonoentiendedirectamente“perro”o“gato”.
P4. ExpliquequéhaceunaSupportVectorMachineyporquémaximizaelmargen. Definelos vectores
desoporte (puntosdecadaclasemáscercanosalafrontera),trazadosplanosparalelosalafronteraque
pasanporellosybuscalosparámetrosque maximizanladistanciaentreesosplanos (elmargen=2/‖w‖,
equivalenteaminimizar‖w‖sujetoayᵢ(w·xᵢ−b)≥1). Lajustificaciónconceptualesque losobjetoscercanos
enelespaciodeatributossuelenperteneceralamismaclase : almaximizarelmargen,cadaregióndel
espacioquedaasignadaalaclasecuyadistribuciónestámáscerca. Unafronterapegadaaunadelasclases
clasificaríamalpuntosnuevosqueestánclaramentecercadeella.
P5. ConVP=6,VN=7,FP=2yFN=1,calculelascincométricasdelaclase. P=7,N=9,total=16.
26

## Lamina 27

Exactitud=13/16=0,8125·Error=3/16=0,1875·Recall=6/7≈0,857·Precisión=6/8=0,75·Tasade
falsospositivos=2/9≈0,222.
P6. ������Expliqueladiferenciaentrerecallyprecisiónconunejemplo. Laprecisiónresponde: detodolo
queelmodelomarcócomopositivo,¿quéporcentajerealmenteloera? El recallresponde: detodoslos
positivosreales,¿quéporcentajelogródetectarelmodelo? Ejemplodelaclase: undetectordefallasde
máquina(unafallacadamilmediciones)con recall100%yprecisión70% detectaabsolutamentetodaslas
fallasreales,perodecada10alertas3sonfalsasyllevanadetenerlamáquinainnecesariamente.
P7. ¿Paraquésirvelamatrizdeconfusiónyquéventajatienesobreunamétricaaislada? Cruzala
etiquetarealconlapredicha. Consusceldassepueden recalculartodaslasmétricas (exactitud, error,
recall,precisión,TFP).Suventajaadicionalesque segeneralizaamúltiplesclases ymuestra quéclasese
confundeconcuál ,dandounaintuicióndelporqué(losgatosseconfundenconperros,noconserpientes).
P8. ¿QuéeselumbraldeclasificaciónyquérelacióntieneconlacurvaROC? Cuandounmodeloentrega
probabilidades,elumbraleselvalorapartirdelcualseasignalaclasepositiva(pordefectosueleser50%,
peroesajustable). Esun hiperparámetroquedesplazalafronteradedecisión . Recorriendotodoslos
umbralesygraficandolatasadeverdaderospositivosfrentealatasadefalsospositivosseobtienela curva
ROC.
P9. ¿Quéeselpuntodeoperaciónycómoseelige? Eselumbralconcretoqueseusaráenproducción.
Nohayunóptimouniversal: seeligesegún quéerroresmáscostosoenelproblema . Siimportaevitar
falsasalarmas,seoperaenlazonadeTFPbaja;siimportanoperderningúncasopositivo(porejemplo,un
examenmédicodeunaenfermedadgrave,dondeexisteunsegundoexamendeconfirmación),seoperaen
lazonaderecallalto.
P10. ExpliquelaimpurezadeGiniconelejemplode3triángulosy5círculos. Mideelerroresperadode
elegirunobjetoalazaryclasificartodoelconjuntosegúnsuclase. P(triángulo)=3/8yelerrordeclasificar
todocomotriánguloes5/8;P(círculo)=5/8yelerrorcorrespondientees3/8. Elerroresperadoes3/8×5/8
+5/8×3/8= 0,46875. Unconjuntopuroda 0.
P11. ¿Cómo decide un árbol de decisión dónde dividir?Para cada atributo calcula laganancia de
purezaqueseobtendríaaldividirporél, comparandolaimpurezadelnodopadreconladelosnodos
hijosponderadaporsutamaño ,yeligeelatributode mayorganancia. Luegorepiteelprocedimiento
recursivamentesobrelossubconjuntosgenerados(algoritmo C4.5).
P12. Enumereloscriteriosdeconvergenciadeunárboldedecisión. Elnodocontienesolounaclase;el
nodocontienemenosobjetosqueunvalordeseado;sealcanzóunaalturamáxima;lapurezaessuficiente;
secomienzaasobreajustar(detectadoporvalidacióncruzada).
P13. Describa el algoritmo Random Forest y explique por qué funciona.Se entrenan n árboles; a
cadaunoseledaunsubconjuntodeNpuntoselegidos conreemplazo (bootstrapping)yunsubconjunto
aleatoriodematributos ;lapredicciónfinalesel promediodelaspredicciones. Funcionaporla sabiduría
delosgrupos : unconjuntograndedeárbolespococorrelacionadossuperaacadaárbolporseparado,
porqueloserroresdeunárbolsoncorregidosporlosotros . Ladoblealeatorizaciónesloquegarantiza
quenotodosaprendanlomismo.
P14. ¿CómoestimaRandomForestlaimportanciadelasvariables? Contandocuántasvecescada
variablefueescogidaporlosárbolescomocriteriodedivisión . Unavariablequeningúnárbolescoge
nuncaesirrelevante;unaescogidaportodosesmuyimportante. Estoaportainterpretabilidadsobreloque
elmodeloestáhaciendo.
P15. Uncompañeroentrenaunclasificadorconunafronteramuycomplejaquenocometeningún
errorenentrenamiento. ¿Quélediría? Quemuyprobablementeestá sobreajustado: eselanálogoen
clasificacióndelpolinomiodegrado10enregresión. Lafronteraencierralosdatosdeentrenamientopero
clasificarámalpuntosnuevosquecaiganclaramentecercadelaotraclase. Además, ningúnmodeloes
perfecto,asíqueunerrornuloesensímismomotivodesospecha. Hayqueevaluarla generalizacióncon
validacióncruzada sobrelasmétricasrelevantes.
27

## Lamina 28

�� �ERRORESYCONFUSIONESCOMUNES
1. Definir“categórica”como“cualitativa”. Elcriteriocorrectoes laausenciadeorden . Elprofesor
descartóexplícitamenteelcriteriocualitativo/cuantitativoconelcontraejemplodelpaisajepuntuado
de1a5.
2. Creerquerangoscomo“adultojoven/adultomayor”o“frío/templado/caliente”soncategóri-
cospuros. Sondiscretizacionesdevariablesnuméricas yconservanelorden.
3. Pensarqueenclasificaciónlosatributosdebensercategóricos. Locategóricoes laetiqueta;x₁yx₂
suelensernuméricos.
4. ������Confundirrecallconprecisión. Elerrormásprobabledelaclase. Recalldividepor P(positivos
reales);precisióndividepor VP+FP (lopredichocomopositivo).
5. Interpretarmal“falsopositivo”. Esun negativoreal clasificadocomopositivo,nounpositivomal
clasificado.
6. Creerquerecall=100%significamodeloperfecto. Solosignificaquenoseescapaningúnpositivo;
puedehabermuchísimasfalsasalarmas(precisiónbaja).
7. OlvidarqueVP+FN=PyVN+FP=N. Estasidentidadessonlasquepermitenescribirrecall=VP/P
yTFP=FP/N.
8. Creer que la elección de positivo/negativo cambia el resultado.Es una convención arbitraria;
invertirlallevaalasmismasconclusiones.
9. Pensarqueelumbraldeclasificaciónessiempre50%. Esun hiperparámetroajustable,yajustarlo
esloquegeneratodalacurvaROC.
10. CreerqueexisteunpuntoóptimouniversalenlacurvaROC. Elóptimoteórico(esquinasuperior
izquierda)esinalcanzable;elpuntodeoperaciónseeligesegúnloscostosdelproblema.
11. Confundirmaximizar2/‖w‖conmaximizar‖w‖. Maximizarelmargenequivalea minimizar‖w‖.
12. Creerquelosvectoresdesoportesontodoslospuntos. Sonsololos máscercanosalafrontera
encadaclase.
13. OlvidarelroldebenlaSVM. Sinb,elhiperplanoestaríaobligadoapasarporelorigen.
14. InvertirlalecturadelaimpurezadeGini. Ginialto=conjuntoimpuro ;Gini=0=conjuntopuro.
15. Olvidarlaponderaciónportamañoenlagananciadepureza. Losnodoshijospesanproporcional-
menteasunúmerodeobjetos.
16. Creerque la medida de impureza(Gini / entropía / error de clasificación) se aprende.Es un
hiperparámetro;seeligeporvalidacióncruzada.
17. PensarqueenRandomForestsolosealeatorizanlosdatos. Tambiénsealeatorizan losatributos;
esadoblealeatorizacióneslaclavedelmétodo.
18. CreerqueenRandomForestlosárbolesdebenestartotalmentedescorrelacionados. Elprofesor
secorrigióenclase: puedehabercorrelación,peronomuyalta .
19. ConfundirelbootstrappingdeRandomForest(conreemplazo)conunsubmuestreosimple. La
slide37diceexplícitamente conreemplazo.
20. Descartarlosárbolesdedecisiónpor“malos”. Sonmalosporsísolos,peroson labasedeRandom
ForestyXGBoost .
21. UsarR²paraevaluarunclasificador. ElR²esunamétricaderegresión.
22. Pensarquelavalidacióncruzadaessoloparaelegirelgradodelpolinomio. Sirveparacualquier
hiperparámetro(incluidoselumbralylamedidadeimpureza)ysobrecualquiermétrica.
23. Aspiraraunmodeloperfecto. “Ningúnmodeloes100%perfecto,porquelanaturalezanoes100%
perfecta.” InclusolasLLMalucinan.
��CONEXIONESCONELRESTODELCURSO
28

## Lamina 29

Conceptodeestaclase Seapoyaen/seconectacon
Etapademodelamiento Elciclodelcientíficodedatosysucarácter
bidireccional
⟨P,T,E ⟩yaprendizajesupervisado Clasede Regresión(clase6),dondesedefinieron
Notaciónŷvs.y Convenciónestablecidaenlaclasederegresión,
válidaparatodoelcurso
Linealenlosparámetros ,noenx Puntocentraldelaclasederegresión,reutilizado
aquí
One-hotencoding Unidadde calidaddedatos (variablescategóricas
endatostabulados)
Atributos=columnas;etiqueta=unacolumnamás Unidaddedatostabulados
Sobreajusteygeneralización Clasederegresión(polinomiodegrado10)—
mismofenómeno,fronteraenvezdecurva
Validacióncruzada(k-fold,shufflesplit,
bootstrapping)
Clasederegresión—sereutiliza sincambios,
aplicadaamétricasdeclasificación
Parámetrovs.hiperparámetro Clasederegresión—aquíseaplicaalumbralyala
medidadeimpureza
BootstrappingenRandomForest Estrategiadevalidacióncruzadadelaclasede
regresión,reutilizadacomomecanismodemuestreo
Reduccióndedimensionalidad Anticipo: severámásadelanteenelcurso
Redesneuronales,LLMyagentes Mencionadascomocontinuaciónnatural;se
profundizanmásadelante
������MAPAMENTALDELACLASEENUNAPÁGINA
CLASIFICACIÓN = aprendizaje supervisado con etiqueta CATEGÓRICA
│ (categórica ⇔ SIN noción de orden; entra al modelo vía ONE-HOT)
│
├── PRINCIPIO RECTOR
│ "Los objetos más cercanos generalmente son de la misma clase"
│ ⇒ ningún modelo es perfecto
│
├── MODELO LINEAL: SUPPORT VECTOR MACHINE
│ ├── vectores de soporte = puntos más cercanos a la frontera
│ ├── w·x − b = 0 (frontera); = ±1 (planos de soporte)
│ ├── margen = 2/‖w‖
│ └── min ‖w‖ s.a. yᵢ(w·xᵢ − b) ≥ 1 ⚠ slide 14
│
├── EVALUACIÓN P = VP + FN N = VN + FP
│ ├── Exactitud = (VP+VN)/(P+N) Error = (FP+FN)/(P+N)
│ ├── Recall = VP/P ← ¿cuántos positivos reales recuperé?
│ ├── Precisión = VP/(VP+FP) ← ¿cuánto de lo que dije era cierto?
│ ├── TFP = FP/N
│ └── MATRIZ DE CONFUSIÓN (real × predicho) → todo lo anterior + N clases
│
├── UMBRAL (hiperparámetro) → mueve la frontera
│ └── CURVA ROC: TVP vs TFP ideal ↖ (TFP=0, TVP=1)
│ └── PUNTO DE OPERACIÓN = decisión de negocio (trade-off)
│
├── GENERALIZACIÓN
29

## Lamina 30

│ frontera demasiado compleja ⇒ SOBREAJUSTE
│ ⇒ VALIDACIÓN CRUZADA (k-fold · shuffle split · bootstrapping)
│ sobre CUALQUIER métrica "si no sabes, di validación cruzada"
│
└── MODELOS NO LINEALES
├── ÁRBOLES DE DECISIÓN
│ ├── dividir buscando subconjuntos PUROS
│ ├── impureza: GINI · entropía · error de clasificación⚠ slide 30
│ │ I_G = Σ (Nᵢ/N)(1 − Nᵢ/N) (0 = puro)
│ ├── ganancia: ΔI_G = I_G(A) − (N_B/N_A)I_G(B) − (N_C/N_A)I_G(C)
│ ├── algoritmo C4.5 (recursivo, mayor ganancia)
│ └── convergencia: 1 clase · pocos objetos · altura máx ·
│ pureza suficiente · sobreajuste
│
└── RANDOM FOREST (sabiduría de los grupos)
├── n árboles; datos con reemplazo (bootstrapping)
├── + m atributos aleatorios
├── predicción = promedio de los árboles
└── bonus: importancia de variables por frecuencia de uso
30
