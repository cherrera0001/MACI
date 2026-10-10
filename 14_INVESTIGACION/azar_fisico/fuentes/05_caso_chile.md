# 05 · Caso Chile: sistemas de sorteo de Polla Chilena de Beneficencia y Lotería de Concepción

Investigación documental cerrada el 2026-10-09. Todo lo afirmado fue abierto en esta sesión; cada dato lleva tipo de fuente y URL. Lo que no pude abrir o confirmar está en la sección 8.

Convención de tipos de fuente: **[N]** norma legal (texto en LeyChile/BCN), **[O]** documento oficial del operador, **[E]** documento oficial de otro órgano del Estado o tribunal, **[P]** prensa, **[T]** tercero (Wikipedia, sitios de resultados, repositorios), **[I]** inferencia o cálculo mío.

Nota de método: las páginas de LeyChile se leyeron por la interfaz XML de la BCN (`leychile.cl/Consulta/obtxml?opt=7&idNorma=…`), con un modelo resumidor; las citas entre comillas son breves y conviene cotejarlas con el texto antes de citarlas en un escrito formal. Las páginas de `polla.cl` y `loteria.cl` son aplicaciones que se dibujan con JavaScript y no pude verlas renderizadas (sin navegador en esta sesión); lo que sé de ellas viene del sitio corporativo `pollachilena.cl`, de copias en Wayback Machine y de terceros.

---

## 1. Síntesis

1. En Chile hay dos operadores legales de lotería: **Polla Chilena de Beneficencia S.A.** (sociedad anónima estatal: 99 % Corfo, 1 % Fisco) y **Lotería de Concepción** (repartición de la Universidad de Concepción, corporación de derecho privado, sin personalidad jurídica propia).
2. La pista «DL 1.298 de 1975 rige a Polla» era imprecisa: ese decreto ley **crea el Sistema de Pronósticos Deportivos** (Polla Gol, Xperto). La empresa se rige por el DFL 120 de 1960 (texto refundido en DS 152 de 1980) y la Ley 18.851 de 1989; los juegos de números (Loto, Loto 3, Loto 4, Racha, Kino) nacen del **artículo 90 de la Ley 18.768**, cada uno con su decreto supremo de Hacienda.
3. Los decretos **no fijan la matriz**: dan un rango y dejan que el operador la elija y la cambie con aviso previo (Loto: 6 de entre 36 y 42 bolillas; Kino: hasta 20 de entre 20 y 50). La matriz vigente (Loto 6 de 41 más comodín; Kino 14 de 25) sale de los documentos del operador, no del decreto.
4. Los decretos tampoco fijan el mecanismo: permiten **tómbola con bolillas o «selección aleatoria por sistema informático»**, a elección del operador, con aviso al público de 7 días (Loto).
5. **Hallazgo principal: el Loto no ha sido siempre un sorteo físico.** Polla comunicó que desde el sorteo **5112 (14-may-2024)** los números se obtendrían por su «sistema de elección aleatoria», y que desde el sorteo **5302 (31-jul-2025)** vuelven las tómbolas. Son 190 sorteos por generador electrónico incrustados en la serie. No encontré publicada la razón de ninguno de los dos cambios.
6. **Loto 3, Loto 4 y Racha son electrónicos** (generador de números aleatorios certificado por GLI, alojado en el centro de datos de Intralot). Loto 3 y Loto 4 dejaron las tómbolas en 2011 (Memoria 2011 de Polla). Polla Boleto también se sortea hoy por sistema informático.
7. **Kino** se describe en su reglamento vigente como extracción de 14 bolillas sin reposición de una tómbola de 25, con transmisión en vivo; la categoría «Premios Especiales» admite «tómbola computacional» y los sorteos al RUT (Club Kino) son por software. El **Boleto de Lotería** pasó a sistema informático desde su sorteo 2522 (8-sep-2024) y dejó de transmitirse en vivo.
8. Cambio de matriz conocido en Kino: de 15 a 14 números desde el sorteo 799 (8-ene-2006). Fuente débil (Wikipedia sin referencia y un reclamo de usuario), pero la suma de frecuencias que publica la propia Lotería es coherente con unos 800 sorteos de 15 números [I].
9. Cambio de matriz en Loto: 6 de 36 en 1989 (DS 846); desde 2002 el rango 36–42 queda a discreción de Polla. **No encontré la fecha en que pasó a 41.**
10. Fiscalización: Contraloría General de la República (ambos, con alcance distinto), Ministerio de Hacienda (autoriza cada juego y recibe la auditoría anual del generador), CMF y SEP (Polla), CMF sobre la Universidad de Concepción solo como emisora de bonos. **La Superintendencia de Casinos de Juego no fiscaliza loterías**; su único vínculo es indirecto: los generadores deben ser validados por laboratorios acreditados ante ella.
11. **No hay regulador especializado del sorteo físico.** No encontré norma alguna que fije tolerancias de masa o diámetro de bolillas, rotación de juegos de bolillas, pruebas previas, ni publicación del orden de extracción. El control normativo del sorteo con tómbola es el notario público como ministro de fe.
12. No encontré marca, modelo ni fabricante de ninguna tómbola, ni licitaciones de tómbolas o bolillas, ni protocolos de pesaje y custodia.
13. No encontré ningún sorteo anulado o repetido documentado por fuente seria. Los incidentes documentados son de publicidad de pozos, premios caducados y cartones dañados, no de integridad del sorteo.
14. Datos: ningún dataset en datos.gob.cl; no hallé ninguno en Kaggle; en GitHub hay varios repositorios recientes hechos por raspado de sitios de terceros, con números **ordenados de menor a mayor**. No encontré ninguna fuente pública con el **orden real de extracción**.
15. Tamaño de la serie al 9-oct-2026: Loto sorteo n.º 5488 (8-oct-2026); Kino sorteo n.º 3290 (9-oct-2026).
16. Con esos tamaños, y partiendo la serie por matriz y por mecanismo, una prueba de frecuencias solo detecta sesgos groseros por bolilla: del orden de 7 % relativo en Kino (≈2.500 sorteos de 14/25) y de 13 % a 28 % en Loto según cuántos sorteos de 6/41 con tómbola sean recuperables; en el tramo de tómbolas posterior a julio de 2025 (187 sorteos) no se detecta nada menor a ≈70 % [I].
17. Vía de acceso a información: Polla no está sujeta a solicitudes de acceso (transparencia pasiva) ante el Consejo para la Transparencia (Corte de Apelaciones de Santiago, Rol 608-2010); Lotería es privada. Lo exigible por Ley 20.285 es lo que tengan **Hacienda, Contraloría, Corfo, SEP y la Superintendencia de Casinos**.

---

## 2. Tabla por juego

Certeza: **Alta** = norma más documento oficial del operador coinciden; **Media** = una sola fuente oficial, o fuente oficial sin fecha; **Baja** = prensa o tercero.

| Juego | Operador | Matriz vigente | Frecuencia | Mecanismo de sorteo | Fuente del mecanismo | Certeza |
|---|---|---|---|---|---|---|
| **Loto** (y Recargado, Revancha, Desquite, Jubilazo, Multiplicar) | Polla | 6 de 41, más 7.ª bolilla «comodín». Decreto: 6 de entre 36 y 42 | Martes, jueves y domingo, 21:00; los adicionales se sortean uno tras otro | **Tómbolas** hoy. **Generador electrónico entre los sorteos 5112 y 5301** (14-may-2024 a fines de jul-2025). Tómbolas desde 5302 (31-jul-2025). Antes de 2011 el decreto solo permitía tómbola | [N] DS 542/2011 arts. 2, 8, 9; [O] comunicados de Polla 07-may-2024 y 17-jul-2025; [O] ficha del juego y Memoria 2025 p. 87 | Alta (mecanismo y fechas de cambio). Sin dato sobre máquina |
| **Loto 3** (ex Toto 3) | Polla | 3 dígitos, 000–999 | 3 sorteos diarios (≈14:00, 18:00, 21:00) | **Electrónico** (generador certificado por GLI). Tómbolas hasta 2011 | [N] DS 47/1997 art. 2; [O] Memoria 2011 p. 46; [O] ficha del juego; [O] preguntas frecuentes; [O] Memoria 2025 p. 87 | Alta |
| **Loto 4** (ex Polla 4) | Polla | 4 de 23 | 2 sorteos diarios (≈14:00 y 21:00) | **Electrónico**. Tómbolas hasta 2011 | [N] DS 767/2002 art. 2; [O] Memoria 2011; [O] ficha; [O] Memoria 2025 | Alta |
| **Racha** | Polla | 10 de 20 (gana con 10, 9, 8, 7 y con 0, 1, 2, 3 aciertos) | 2 sorteos diarios (15:00 y 22:00) | **Electrónico** | [N] DS 767/2002; [O] preguntas frecuentes; [O] Memoria 2025 | Alta |
| **Polla Boleto** | Polla | Número de 5 cifras (00001–99999), enteros y vigésimos | Quincenal, lunes ≈14:00 | **Electrónico** hoy; el reglamento permite tómbola, sistema informático o ambos | [N] DS 1.411/2008 arts. 2 y 3; [O] ficha del juego; [O] preguntas frecuentes | Media: la misma página oficial se contradice (ver 8.3) |
| **Raspes** | Polla | Instantáneos impresos y electrónicos | Continuo | Sin sorteo (premio predeterminado en la emisión) | [N] DS 1.470/1995; [O] Memoria 2025 p. 86 | Alta |
| **Polla Gol / Xperto** | Polla | Pronósticos deportivos | Según eventos | Sin sorteo | [N] DL 1.298/1975; [O] Memoria 2025 | Alta |
| **Kino** | Lotería | 14 de 25 (15 de 25 hasta el sorteo 798, ene-2006) | Miércoles, viernes y domingo, ≈22:30 | **Tómbola**, 14 bolillas sin reposición de 25 | [N] DS 659/1990 en texto de DS 1.114/2005 art. 2; [O] «Productos y Reglamentación Kino» (copia Wayback 16-oct-2025) | Media-alta: reglamento oficial dice tómbola; no vi un sorteo ni un acta |
| **ReKino, RequeteKino, Chao Jefe** y otros adicionales | Lotería | 14 de 25 cada uno, extracción independiente | Con cada Kino | **Tómbola** según reglamento | [O] mismo reglamento; [O] descargos de Lotería ante CONAR (2019) citan el reglamento | Media |
| **Kino · Premios Especiales** | Lotería | 14 de 25 | Ocasional | Tómbola **o «tómbola computacional»** | [O] reglamento Kino, categoría Premios Especiales | Media |
| **Kino · Club Kino y premios al número de cartón** | Lotería | RUT o n.º de cartón | Domingos (Club Kino) | **Software** («software informático de Lotería») | [O] reglamento Kino | Media |
| **Boleto de Lotería** | Lotería | Número de boleto | Domingos (22:15 desde sep-2024) | **Electrónico** desde el sorteo 2522 (8-sep-2024); ya no se transmite en vivo | [N] DS 80/1987 en texto de DS 158 (publ. 21-abr-2016) arts. 10 y 11; [P] Focus Gaming News 30-ago-2024 | Media (una sola nota de prensa; no hallé el comunicado original) |
| **Kino 5** | Lotería | No verificada | No verificada | Decreto: tómbola (hasta 20 bolillas) o sistema informático | [N] DS 1.136 (publ. 27-abr-2005) en texto de DS 158 | Baja: no confirmé matriz ni si sigue vigente |

URL de respaldo de la tabla, en las secciones 3 y 5.

Probabilidades del premio mayor [I], por combinatoria: Loto 6/41 = 1 en 4.496.388; Kino 14/25 = 1 en 4.457.400; Kino 15/25 (hasta 2006) = 1 en 3.268.760; Loto 6/36 (1989) = 1 en 1.947.792; Loto 4 (4/23) = 1 en 8.855; Racha 10/20 = 1 en 184.756 por extremo. No encontré una tabla **oficial** de probabilidades publicada por ninguno de los dos operadores.

---

## 3. Marco legal y fiscalización

### 3.1 Polla Chilena de Beneficencia S.A.

| Norma | Contenido | Fuente |
|---|---|---|
| Ley 5.443 (publ. 13-jul-1934) | Autoriza a la Junta Central de Beneficencia a establecer la «Polla Chilena de Beneficencia». El propio sitio de Polla cita el número de forma inconsistente (5.433, 5.443 y 5.548 en páginas distintas); LeyChile registra 5.443 | [N] LeyChile idNorma 288260 (listado de búsqueda); [O] https://www.pollachilena.cl/polla-chilena/historia/ |
| DFL 271 de 1953 | Fija dependencia; personalidad jurídica y patrimonio propio | [N] idNorma 270849; [O] Memoria 2025 |
| **DFL 120 de 1960** (texto refundido: DS 152 de Hacienda, 1980) | Ley orgánica: empresa del Estado; Contraloría fiscaliza sus actos; regula la lotería tradicional (Boleto) | [N] https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=178613 |
| **DL 1.298 (publ. 26-dic-1975)** | **Crea el Sistema de Pronósticos Deportivos**, administrado por Polla. No es la ley orgánica de la empresa | [N] idNorma 6559; https://iura.cl/dl-1298-minhda/ |
| **Ley 18.768, art. 90** (1988) | Autoriza a Polla y a Lotería de Concepción a administrar «sorteos de números, juegos de azar de resolución inmediata y combinaciones de ambos», previo decreto supremo de Hacienda. Reparto de ingresos brutos: 47 % premios, 20 % comisión de agentes y administración; Polla: 18 % a rentas generales y 15 % a deportes; Lotería: 33 % a la Universidad | [N] https://iura.cl/18768/90 |
| **Ley 18.851** (1989) | Transforma a Polla en sociedad anónima estatal; objeto social | [O] Memoria 2025; [O] preguntas frecuentes |
| DS 1.411 (prom. 3-nov-2008, publ. 28-mar-2009) | Reglamento de sorteos tradicionales (Boleto): 26 sorteos al año; art. 2: bolillas de tómbolas, selección aleatoria por sistema informático o combinación; art. 3: notario supervisa bolillas y extracción, o certifica los números si es informático; acta notarial | [N] https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=288430 |
| DS 846 (publ. 20-oct-1989) | Primer decreto del «Polla-Loto»: 6 de 36, tómbola, sin reposición, sin importar el orden; notario ministro de fe (art. 13). Derogado | [N] https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=15925 |
| DS 696 de 2001 (publ. 30-ene-2002) | Reemplaza el texto del anterior: universo «no inferior a 36 ni superior a 42» bolillas, fijado por Polla con 30 días de aviso; 7.ª bolilla «comodín»; Revancha y «Siempre Sale». Derogado el 30-dic-2011 | [N] https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=194203 |
| **DS 542 de 2011 (publ. 30-dic-2011)** | Texto vigente del Loto. Art. 2: 6 de entre 36 y 42 bolillas; **tómbola o selección aleatoria por sistema informático**, validado y auditado anualmente por laboratorios acreditados ante la Superintendencia de Casinos de Juego; Polla elige modalidad y avisa con 7 días. Arts. 8 y 11: notario como ministro de fe con tómbola. Art. 14: Polla fija la frecuencia. Modificado por DS 577 de 2021 (solo premios caducados) | [N] https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=1035539 ; DS 577: idNorma 1162546 |
| DS 47 de 1997 (versión 10-abr-2010) | Loto 3: tres dígitos 000–999; tómbola, formación dígito a dígito o sistema informático validado y auditado anualmente; copia del informe al Ministerio de Hacienda | [N] https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=70900 |
| DS 767 de 2002 (versión 10-abr-2010) | Loto 4 y Racha: entre 20 y 90 bolillas, hasta 20 extraídas; tómbola o sistema informático validado por laboratorio acreditado; auditoría anual con copia a Hacienda | [N] https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=207150 |
| DS 504 (publ. 10-jul-2024) | Autoriza un sorteo de números nuevo: universo de 10 a 35, hasta 10 extraídos; tómbola o sistema informático. Nombre comercial no identificado | [N] https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=1204828 |

Asignación juego → decreto confirmada por la Memoria Anual 2025 de Polla, pp. 86–87 [O]: https://www.pollachilena.cl/app/uploads/2026/04/Memoria-Anual-Polla-Chilena-2025.pdf

### 3.2 Lotería de Concepción

| Norma | Contenido | Fuente |
|---|---|---|
| Ley 4.885 (1930) | Establece una lotería de beneficencia administrada por la Universidad de Concepción | [N] idNorma 24957 (listado) |
| **Ley 18.568 (publ. 30-oct-1986)** | Autoriza a la Universidad a mantener el sistema de sorteos por la repartición «Lotería de Concepción», que «carecerá de personalidad jurídica»; contabilidad independiente y balance anual; sorteos «semana por medio, en forma alternada» con Polla (26 o 27 al año); 60 % a premios; **art. 11: la Contraloría fiscaliza el cumplimiento de los porcentajes** de premios y beneficiarios. Última modificación registrada: 2006 | [N] https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=29960 |
| DS 80 de 1987, texto sustituido por DS 158 (publ. 21-abr-2016) | Reglamento de la ley. Art. 9: sorteos de libre acceso público, presenciales o en línea. Art. 10: tómbola, sistema informático o ambos; el sistema debe ser validado antes de operar por laboratorio acreditado ante la Superintendencia de Casinos de Juego, y auditado, con copia del informe a Hacienda. Art. 11: notario supervisa bolillas y extracción, o certifica las apuestas ganadoras que informe el sistema | [N] https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=1089623 |
| **DS 659 de 1990, texto sustituido por DS 1.114 (publ. 29-dic-2005)** | Decreto del Kino. Art. 2: «extracción, sin reposición, de a lo más 20 bolillas de una tómbola» con entre 20 y 50 bolillas; art. 8: notario ministro de fe; art. 14: Lotería fija frecuencia | [N] https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=245596 |
| DS 691 (publ. 20-jul-1996; versión 17-dic-2013) | Otro sorteo de números: 7 de 30, tómbola, sin reposición, no importa el orden; notario. Nombre comercial no fijado en el decreto | [N] https://www.leychile.cl/Consulta/obtxml?opt=7&idNorma=15130 |
| DS 1.136 (publ. 27-abr-2005), texto sustituido por DS 158 | Sorteo de números con nombre de fantasía (Kino 5, según el resumen de la norma y la lista de juegos derivados que da la propia Lotería) | [N] idNorma 237399 y 1089623; [O] descargos CONAR 2019 |

Naturaleza jurídica en palabras de la propia Lotería [O]: «entidad sin personalidad jurídica propia, dependiente de la Universidad de Concepción, persona jurídica de derecho privado, sin fines de lucro» (descargos ante CONAR, 20-may-2019): https://www.conar.cl/wp-content/uploads/2019/05/Descargos-Conar-Loter%C3%ADa.pdf

### 3.3 Quién fiscaliza

| Órgano | Sobre Polla | Sobre Lotería | Fuente |
|---|---|---|---|
| **Contraloría General de la República** | Sí: fiscaliza a la empresa (DFL 120 art. 1; art. 16 de la Ley 10.336) y auditó sus operaciones de 2017 | Sí, acotado: cumplimiento de porcentajes de premios y beneficiarios (Ley 18.568 art. 11) | [N]; [O] Memoria 2025; [P] https://www.eldinamo.cl/pais/2019/07/05/contraloria-auditoria-polla-chilena/ |
| **Ministerio de Hacienda** | Autoriza cada juego por decreto supremo; recibe copia de la auditoría anual del sistema de selección aleatoria | Lo mismo | [N] Ley 18.768 art. 90; DS 47, 767, 542, 158 |
| **Comisión para el Mercado Financiero** | Sí: sociedad inscrita en su registro; estados financieros y hechos esenciales | Solo sobre la Universidad de Concepción como emisora de bonos (desde 2013) | [O] Memoria 2025; [O] descargos CONAR 2019 |
| **Sistema de Empresas Públicas (SEP) y Corfo** | Sí: políticas y directrices del dueño | No | [O] Memoria 2025; preguntas frecuentes |
| **Notario público** | Ministro de fe en sorteos con tómbola; certifica los números si es informático. Según la Memoria 2011, con el generador certificado «ya no se requiere la presencia de un Notario Público en cada sorteo» de Toto 3 y Polla 4 | Igual | [N] decretos citados; [O] Memoria 2011 p. 46 |
| **Superintendencia de Casinos de Juego** | **No fiscaliza loterías.** Su ley (19.995) es de casinos. Vínculo indirecto: acredita a los laboratorios que validan y auditan los generadores | Igual | [N] decretos citados; [E] Contraloría, toma de razón con alcance del DS 158 (los laboratorios son los del art. 33 del DS 547/2005); [T] Carey, capítulo Chile de Legal 500 (resultado de búsqueda): supervisión de la Superintendencia «limited to licensed brick-and-mortar casinos»; [P] dictamen de Contraloría de 29-oct-2025: la Superintendencia tampoco puede fiscalizar el juego en línea, https://www.diarioconstitucional.cl/2025/11/11/contraloria-aclara-que-la-superintendencia-de-casinos-no-tiene-facultades-para-fiscalizar-apuestas-en-linea/ |
| **Consejo para la Transparencia** | **Sin competencia sobre solicitudes de acceso a Polla**: solo transparencia activa (art. décimo de la Ley 20.285). Corte de Apelaciones de Santiago, Rol 608-2010, 29-jul-2010, rechaza reclamo contra la decisión de amparo C450-09 | No aplica (entidad privada); no hallé decisión específica | [E] https://ciperchile.cl/wp-content/uploads/fallo-corte-caso-polla.pdf |
| **Sernac y CONAR** | Publicidad de pozos | Igual | Ver sección 4 |

No encontré que la Contraloría, Hacienda u otro órgano haya auditado alguna vez la **aleatoriedad física** de un sorteo (bolillas, tómbolas). La norma exige auditoría anual del generador electrónico, pero **no exige auditoría técnica equivalente para las tómbolas**: ahí el control escrito es la supervisión notarial de «la revisión de las bolillas y su colocación en la tómbola».

### 3.4 Certificaciones

- Polla [O] (https://www.pollachilena.cl/documentos-cumplimiento/): ISO 9001:2015 que cubre 15 procesos, **el primero «Sorteo»**; ISO/IEC 27001:2022; certificación de Juego Responsable de la World Lottery Association nivel 3; NCh 3262; modelo de prevención de delitos.
- Polla, generador [O]: certificado por Gaming Laboratories International (GLI), «alojado en el Centro de Datos Principal de nuestro proveedor tecnológico Intralot Chile S.A.» (https://www.pollachilena.cl/preguntas-frecuentes/). En 2011 el proveedor era GTECH (Memoria 2011). El contrato con Intralot vence el 27-ene-2027 y hay licitación privada en curso con dos oferentes, Intralot y Brightstar (ex IGT) (Memoria 2025).
- Lotería [P]: Juego Responsable WLA nivel 4, obtenido en diciembre de 2023 (Focus Gaming News; no abrí el certificado).
- **WLA-SCS (norma de control de seguridad de la WLA): no encontré que ninguno de los dos operadores la tenga.** Un resultado de búsqueda atribuye WLA-SCS e ISO 27001 a las operaciones de Intralot en Chile (comunicado de Intralot; no abierto).

### 3.5 Proyecto de ley de apuestas en línea (Boletín 14.838-03), solo lo que toca a loterías

- Ingresó en marzo de 2022. Segundo trámite en el Senado. Comisión de Hacienda lo aprobó en general (nota del Senado, 6-ago-2025); la Sala lo aprobó en general por 27-3-5 (nota del Senado, 14-ago-2025); indicaciones hasta el 29-sep-2025; discusión en particular en comisiones unidas de Economía y Hacienda. [E] https://www.senado.cl/comunicaciones/noticias/apuestas-en-linea-comisiones-unidas-de-economia-y-hacienda-analizaran-el
- El Ejecutivo le puso suma urgencia en mayo de 2026. Al 29-sep-2026 seguía en comisiones unidas, con una mesa técnica y **sin fecha de votación**. [P] https://los40.cl/2026/09/29/ley-de-apuestas-online-en-chile-que-cambiaria-para-los-usuarios-si-se-aprueba/
- **No está aprobado al 9-oct-2026** según lo que pude abrir. La Superintendencia pasaría a llamarse Superintendencia de Casinos, Apuestas y Juegos de Azar.
- Loterías: el **artículo quinto transitorio** contiene «la regulación que en dicha disposición se considera para Polla Chilena de Beneficencia S.A.» (nota del Senado de 6-ago-2025: https://www.senado.cl/comunicaciones/noticias/conozca-los-aspectos-claves-del-proyecto-que-regulara-el-desarrollo-de). **No abrí el texto del artículo.** Nada de lo que leí indica que el proyecto regule el mecanismo físico de sorteo de las loterías.

---

## 4. Incidentes documentados

Busqué sorteos anulados, repetidos, errores de bolilla, sumarios y fallos. **No encontré ningún caso documentado por fuente seria de un sorteo de Loto o Kino anulado o repetido, ni de una investigación sobre bolillas o tómbolas.** Eso es ausencia de hallazgo en búsquedas web, no prueba de que no haya ocurrido (la prensa chilena anterior a 2000 está mal indexada).

Hechos documentados, ninguno sobre integridad física del sorteo:

| Año | Hecho | Naturaleza | Fuente |
|---|---|---|---|
| 1999–2000 | «Kino 2000» y «Loto Millenium»: pozos anunciados muy superiores a lo repartido (Kino ≈26 % menos; Loto repartió $689 millones frente a $2.611 millones proyectados). Comisión de Economía de la Cámara, constituida en investigadora; informe de 9-may-2000. Sernac concluyó publicidad engañosa sin dolo y denunció ante el 3.er Juzgado de Policía Local de Santiago (Rol 8150) | Publicidad de pozos | [E] https://www.bcn.cl/laborparlamentaria/participacion?idParticipacion=1979875 |
| 2009–2010 | Periodista de CIPER pide información a Polla; el Consejo para la Transparencia se declara incompetente (C450-09); la Corte de Apelaciones de Santiago rechaza el reclamo (Rol 608-2010) | Acceso a información | [E] https://ciperchile.cl/wp-content/uploads/fallo-corte-caso-polla.pdf |
| 2011 | Polla sustituye las tómbolas de Toto 3 y Polla 4 por generador electrónico certificado por GLI | Cambio de mecanismo | [O] https://www.pollachilena.cl/app/uploads/2023/08/Memoria_2011.pdf (p. 46) |
| 2018–2024 | Cartón dañado del Kino, sorteo 2049 (4-mar-2018, ≈$2.400 millones): Lotería no paga; denuncia por posible fraude; el 3.er Juzgado Civil de Concepción rechaza la demanda en 2024 por falta de prueba; apelación pendiente según prensa | Validez del boleto | [P] https://www.meganoticias.cl/nacional/452139-javier-zapata-carton-ganador-kino-se-limpio-con-el-justicia-fallo-en-su-contra-pdp-08-07-2024.html |
| 2019 | Contraloría audita las operaciones de 2017 de Polla: premios de Loto caducados en dic-2016 por $3.111 millones no destinados según el DS 542; sin política interna. Número de informe no encontrado | Destino de premios caducados | [P] https://www.eldinamo.cl/pais/2019/07/05/contraloria-auditoria-polla-chilena/ |
| 2019 | CONAR, Rol 1114/19: Polla reclama contra la publicidad del pozo de «Chao Jefe de por Vida»; el Consejo acoge el reclamo y rechaza la reconsideración el 11-jul-2019; Lotería apela. Resultado final no verificado | Publicidad | [O] https://www.conar.cl/wp-content/uploads/2019/07/Apelacion-Conar-Rol-N%C2%BA-1114-2019.pdf |
| 2024 | Polla pasa el Loto a generador electrónico desde el sorteo 5112; comunicado de una frase, sin motivo | Cambio de mecanismo | [O] https://www.pollachilena.cl/informacion-sorteo-loto-5112/ |
| 2024 | Lotería pasa el Boleto a sistema informático desde el sorteo 2522; deja de transmitirse en vivo | Cambio de mecanismo | [P] https://focusgn.com/latinoamerica/la-loteria-de-concepcion-presenta-su-sistema-informatico-certificado-de-seleccion-aleatoria |
| 2025 | Polla vuelve a las tómbolas en el Loto desde el sorteo 5302; comunicado de una frase, sin motivo | Cambio de mecanismo | [O] https://www.pollachilena.cl/informacion-sorteo-loto-5302/ |

Rumor, no hecho: en reclamos.cl hay quejas de usuarios (acceso a cuentas, apuestas, una sobre la «columna 15» de las estadísticas del Kino desde el sorteo 799). Son declaraciones individuales no verificadas; la última solo sirve como indicio independiente de la fecha del cambio de matriz.

---

## 5. Datos históricos disponibles

### 5.1 Fuentes oficiales

| Fuente | Qué constaté | Qué no pude constatar |
|---|---|---|
| Polla, resultados: https://www.polla.cl/es/view/resultados | Existe la página «Resultados de todos los últimos sorteos», con filtros «Todas las fechas» y «Todos los sorteos» y columnas Juego / Fecha-Hora / Números ganadores. Las fichas de juego tienen pestañas «Últimos números sorteados / frecuencias / Última aparición» | Profundidad del histórico, formato de descarga, **orden de extracción**, términos de uso. La página se dibuja con JavaScript y no la vi cargada. `robots.txt` devolvió vacío |
| Lotería, estadísticas: https://www.loteria.cl/loteriaweb/estadisticas/kino/ (hoy también https://www.loteria.cl/resultados/estadisticas/) | En copia de Wayback del 28-jun-2024: tabla de **frecuencia por número (1 a 25) para cada juego** (Kino, ReKino, variantes de Chao Jefe, Súper Combo Marraqueta), número más y menos frecuente, **«Cantidad Sorteos realizados: 2.932»** para Kino, y un botón **«Descargar Archivo»** | Contenido del archivo descargable; si hay consulta sorteo a sorteo; orden de extracción; términos de uso |
| Lotería, consulta de resultados: https://www.loteria.cl/resultados/consulta-resultado/ y https://www.loteria.cl/resultados/resultado-completo/ | Existen en el mapa del sitio. `robots.txt` permite `/` y excluye rutas privadas y de promociones | Contenido (aplicación JavaScript) |
| Memorias anuales de Polla 2006–2025: https://www.pollachilena.cl/polla-chilena/transparencia/memorias/ | Descargables en PDF. Sirven para fechar cambios de mecanismo y proveedor. No contienen resultados de sorteos | — |
| Actas notariales de cada sorteo | Los decretos ordenan levantarlas, con los números sorteados | No encontré ninguna publicada. Es la única fuente primaria donde podría constar el orden de extracción |

Cifras de frecuencia que la Lotería publicaba el 28-jun-2024 [O, vía Wayback: https://web.archive.org/web/20240628233047/https://www.loteria.cl/loteriaweb/estadisticas/kino/]: 1:1.678, 2:1.649, 3:1.646, 4:1.703, 5:1.729, 6:1.651, 7:1.670, 8:1.683, 9:1.693, 10:1.742, 11:1.692, 12:1.720, 13:1.677, 14:1.635, 15:1.684, 16:1.640, 17:1.648, 18:1.691, 19:1.656, 20:1.646, 21:1.657, 22:1.636, 23:1.648, 24:1.681, 25:1.706. Suma 41.861.

Comprobación mía [I]: 14 × 2.932 = 41.048; sobran 813 apariciones, lo que cuadra con unos 800 sorteos iniciales de 15 números (el cambio de matriz en el sorteo 799). Con esa mezcla, el estadístico chi-cuadrado corregido por muestreo sin reposición da ≈29,0 con 24 grados de libertad, p ≈ 0,22: **las frecuencias agregadas que publica el operador son compatibles con uniformidad**. Es un cálculo sobre totales publicados, no una auditoría: mezcla dos matrices, no separa juegos de bolillas ni máquinas y no dice nada sobre orden de salida.

### 5.2 Terceros

| Fuente | Cobertura declarada | Orden | Condiciones |
|---|---|---|---|
| openloto.cl | Estadísticas del Loto «desde el año 2010»; página por sorteo | **Ascendente** (etiquetado «Casilla 1…6»); no declara orden de extracción | Canal independiente; términos no abiertos |
| resultadoloto.com | No indica profundidad | No determinable | Se declara no oficial |
| chileresultados.com, resultadoskinochile.com | Usados como fuente por los repositorios de abajo | Ascendente en los datos derivados | No abiertos |
| Prensa (24horas, T13, RedGol, Pauta) | Una nota por sorteo | Ascendente | Derechos reservados |
| Wikipedia, «Lotería de Concepción» y «Polla Chilena de Beneficencia» | Fechas de lanzamiento y cambios | — | Los datos sobre Kino y Loto **no llevan referencia** |

### 5.3 Portales de datos y repositorios

- **datos.gob.cl**: consulté la API del catálogo con «loto», «kino», «polla chilena», «sorteo»: **0 conjuntos de datos**. («lotería de concepción» devuelve 16 resultados, todos ajenos: vivienda, salud, trenes.)
- **Kaggle**: no encontré ningún dataset de Loto o Kino chilenos por búsqueda web. No consulté la API de Kaggle; no es concluyente.
- **GitHub** (API pública de búsqueda, 9-oct-2026). Todos con 0 o 1 estrella y creados en 2022–2026:
  - `Nicovh-Analytics/analisis-loteria-chile` (MIT, creado 12-ago-2026): CSV de Loto principal, Recargado, Revancha, Desquite y Kino con adicionales; ≈1.222 sorteos de Loto (desde el n.º 4239) y ≈889 de Kino (desde el n.º 2362), raspados de chileresultados.com. Verifiqué las cabeceras: `sorteo;n1…n6;comodin` y `sorteo,n1…n14`, **números en orden ascendente**; el CSV de Loto tiene filas finales sucias. Aplica unas 40 pruebas y concluye compatibilidad con azar; declara que solo detectaría sesgos groseros. Afirma que el Loto usa «4 bombos físicamente independientes», **sin fuente**, y no menciona el tramo electrónico 5112–5301, que cae dentro de sus datos. https://github.com/Nicovh-Analytics/analisis-loteria-chile
  - `77ruben/kino-scraper`: Kino desde ≈sorteo 1506 (dic-2012) hasta ≈3226 (may-2026), de resultadoskinochile.com; sin licencia.
  - `Blank2D/datos-de-azar` (MIT): andamiaje de raspado y análisis; el histórico aún no está cargado.
  - Otros: `peteraraya/juegakino`, `gaaguile/Kino2026`, `monxero/kinobot`, `Fernando8955/kino`, `GioFranco79/kinoso`, `javiercollao/lottery-simulator`. Sin licencia declarada.

**Conclusión de datos:** existen resultados sorteo a sorteo en varios sitios, pero **no hallé en ninguna fuente pública el orden real de salida de las bolillas**, ni qué tómbola o juego de bolillas se usó. Los datos derivados heredan los términos de uso de sitios de terceros, que no revisé.

---

## 6. Literatura chilena

Resultado principal: **no encontré ningún artículo arbitrado ni tesis chilena que analice estadísticamente la aleatoriedad del Loto o del Kino, ni un estudio econométrico publicado de la demanda de loterías en Chile.** Lo que sigue es lo que sí existe.

Trabajos confirmados (ficha abierta):

1. Rojas Inostroza, Nicolás Santiago (2012). *Grito y plata. Crónicas sobre casinos, hípica y juegos de azar en Chile*. Memoria para optar al título de Periodista, Instituto de la Comunicación e Imagen, Universidad de Chile. Profesora guía: Ximena Póo Figueroa. https://repositorio.uchile.cl/handle/2250/194720 — Historia y crónica; no estadística.
2. Morales Maureira, Sharon y Moreno Silva, Cristóbal (2018). *El verdadero juego de azar*. Memoria para optar al título de Periodista, Universidad de Chile. Profesor guía: Manfred Schawer Valenzuela. https://repositorio.uchile.cl/handle/2250/151710 — No abrí el PDF; contenido sobre loterías no verificado.
3. Figueroa V., Fernando (apellido completo ilegible en el PDF). «Nota sobre los orígenes de la Lotería de Concepción». *Revista de Historia*, Universidad de Concepción. Año y volumen no verificados. https://revistas.udec.cl/index.php/historia/article/download/7164/6630/15635
4. Díaz Soto, Maximiliano y Muñoz Labraña, Carlos. *Lotería de Concepción. Cien años de historia (1921–2021)*, 265 pp. Solo confirmado por nota de prensa (Focus Gaming News); no vi el libro.
5. Biblioteca del Congreso Nacional, Departamento de Estudios, Extensión y Publicaciones (junio de 1997). *Normativa vigente en materia de apuestas y juegos de azar*. Serie Estudios, año VII, n.º 158. https://obtienearchivo.bcn.cl/obtienearchivo?id=documentos/10221.1/75011/2/juegosazar_serie158.pdf — Compendio legal; útil para el estado de los decretos en 1997.
6. Cámara de Diputados (2000). Informe de la Comisión de Economía, Fomento y Desarrollo, constituida en investigadora, sobre los sorteos Kino 2000 y Loto Millenium. Sesión 1.ª, legislatura 342, 6-jun-2000. https://www.bcn.cl/laborparlamentaria/participacion?idParticipacion=1979875

Material gris del operador: la Memoria 2023 de Polla menciona un «modelo de demanda de las apuestas del sorteo Loto» que analiza elasticidad precio y efecto de los pozos (según resultado de búsqueda; no abrí esa memoria). El modelo no está publicado.

Descartados tras abrirlos (aparecían en búsquedas pero no tratan de loterías): tesis de Mellado (2015, impuesto a los alcoholes) y de Schlesinger y Balázs (2010, pasajes aéreos), ambas de la Universidad de Chile.

No consulté los buscadores internos de repositorio.udec.cl, repositorio.uc.cl ni repositorio.usm.cl; solo búsqueda web sobre ellos, sin resultados pertinentes.

---

## 7. Qué se puede y qué no se puede concluir

### 7.1 Tamaño real de las series (hecho más inferencia)

**Loto.** Numeración: sorteo 5488 el 8-oct-2026 [P]. La serie no es homogénea:

| Tramo | Matriz | Mecanismo | Sorteos | Certeza |
|---|---|---|---|---|
| Desde 1989 hasta fecha no hallada | 6 de 36, luego valores entre 36 y 42 a elección de Polla | Tómbola | No determinable | El primer decreto es de oct-1989; Wikipedia (sin referencia) da 17-nov-1989 |
| Hasta el sorteo 5111 | 6 de 41 más comodín | Tómbola | No determinable sin la fecha del cambio a 41 | — |
| 5112 a 5301 | 6 de 41 | **Generador electrónico** | 190 | Alta [O] |
| 5302 a 5488 | 6 de 41 | Tómbola | 187 | Alta [O] |

Cada noche de Loto hay además Recargado, Revancha, Desquite, Jubilazos y Multiplicar, sorteados uno tras otro. Son extracciones adicionales de 6 de 41, pero **no sé si usan la misma tómbola y el mismo juego de bolillas**; sin eso no se pueden agrupar para estudiar una máquina.

**Kino.** Numeración: sorteo 3290 el 9-oct-2026 [P]. Sorteos 1 a 798 con 15 de 25; desde el 799, 14 de 25: unos 2.490 sorteos con la matriz actual [I]. Frecuencia: semanal hasta 2006, dos por semana desde 2006, tres desde marzo de 2020 (Wikipedia, sin referencia). Los adicionales (ReKino y otros) son extracciones independientes de 14 de 25; mismo problema: no sé qué tómbola ni qué bolillas.

### 7.2 Lo que sí puede concluirse solo con resultados públicos

- **Uniformidad de frecuencias por número**, por tramo homogéneo. Sensibilidad aproximada [I] (una bolilla sesgada, potencia 80 %, nivel 5 % con corrección de Bonferroni por el número de bolillas):

| Serie | Sorteos | Error estándar relativo de la frecuencia de una bolilla | Sesgo relativo mínimo detectable |
|---|---|---|---|
| Kino 14/25, matriz actual | ≈2.490 | 1,8 % | ≈7 % |
| Kino, lo que cubren los datos de terceros | ≈900 | 3,0 % | ≈12 % |
| Loto 6/41, si se recuperara toda la numeración (cota optimista: ignora cambios de matriz) | 5.488 | 3,3 % | ≈13 % |
| Loto 6/41, lo que cubren los datos de terceros | ≈1.250 | 6,8 % | ≈28 % |
| Loto, tómbolas desde jul-2025 | 187 | 17,7 % | ≈72 % |

  Es decir: los datos públicos permiten descartar un sesgo grosero (una bolilla que sale 10–30 % más de lo debido) y nada más fino. Los sesgos físicos plausibles por diferencias de masa o desgaste son, según la literatura que cubren los otros informes del concilio, de un orden menor; aquí quedarían bajo el umbral.
- **Independencia serial entre sorteos** (repeticiones, rachas, autocorrelación por número), con la misma limitación de potencia.
- **Frecuencia de pares, sumas, paridad y huecos**: pruebas de consistencia, no de mecanismo.
- **Comparación entre tramos de mecanismo distinto**: el Loto ofrece un experimento natural (190 sorteos electrónicos entre tramos de tómbola), pero con 190 y 187 sorteos la potencia es casi nula.
- **Comprobación de la contabilidad publicada** (como la suma de frecuencias del Kino en 5.1).

Advertencia sobre el electrónico: para Loto 3, Loto 4, Racha, Boleto y el tramo 5112–5301 del Loto **no hay sistema físico que estudiar**. La pregunta pasa a ser la calidad del generador y de su semilla, que tampoco es observable desde fuera; solo consta que GLI lo certifica y que el informe anual va a Hacienda.

### 7.3 Lo que no puede concluirse sin datos no públicos

- **Pruebas de posición** (qué bolilla sale primera, sesgo por orden de carga): imposibles; ninguna fuente pública da el orden de extracción, y los propios reglamentos declaran que el orden no importa para premiar.
- **Atribución a una máquina o a un juego de bolillas**: no se publica qué tómbola ni qué juego de bolillas se usa en cada sorteo, cuántos juegos existen ni cada cuánto se reemplazan. Un sesgo de un juego se diluye al mezclarlo con otros.
- **Causa física**: masa y diámetro de cada bolilla, material, desgaste, modo de mezcla (aire o gravedad), presión, tiempo de mezcla, temperatura, orden de carga. Nada de esto está publicado.
- **Marca, modelo y mantenimiento de las tómbolas.**
- **Predicción**: con lo público no hay base para predecir ningún sorteo. Aun si existiera un sesgo bajo el umbral de la tabla, no sería explotable ni demostrable con estos tamaños de muestra.

---

## 8. No verificado, no encontrado y solicitudes que convendría presentar

### 8.1 No encontrado (busqué y no apareció)

1. Marca, modelo o fabricante de las tómbolas de Polla o de Lotería (probé Smartplay, WinTV, Editec, Ryo Catteau, Venus).
2. Si la mezcla es por aire o por gravedad.
3. Licitaciones u órdenes de compra de tómbolas o bolillas. Polla publica un manual de compras y una lista de principales proveedores (Intralot, canales de televisión, Eagle Press para raspes): **no figura ningún proveedor de equipos de sorteo**. No consulté Mercado Público directamente.
4. Protocolo de pesaje, medición, custodia o rotación de bolillas; cantidad de juegos de bolillas.
5. Actas notariales de sorteos; nombre del notario de los sorteos de Polla.
6. Informes de auditoría externa del proceso de sorteo; informes de GLI.
7. Razón del paso del Loto a generador electrónico (may-2024) y del regreso a tómbolas (jul-2025).
8. Fecha y número de sorteo en que el Loto pasó a 41 números, y las matrices intermedias.
9. Tabla oficial de probabilidades por categoría de cualquiera de los dos operadores.
10. Certificación WLA-SCS de alguno de los dos operadores.
11. Sorteos anulados o repetidos, sumarios, dictámenes de Contraloría sobre un sorteo.
12. Dataset en datos.gob.cl; dataset en Kaggle.
13. Literatura académica chilena sobre aleatoriedad o demanda de Loto y Kino.
14. Cualquier fuente con el orden de extracción.

### 8.2 No verificado (hay indicio, falta confirmación)

1. Primer sorteo del Loto (17-nov-1989) y del Kino (30-sep-1990); frecuencias históricas de Kino; cambio 15→14 en el sorteo 799 (8-ene-2006). Fuente: Wikipedia sin referencia. El último tiene dos apoyos indirectos (reclamo de usuario y suma de frecuencias).
2. Que la numeración del Loto (5488) cuente desde 1989 sin saltos.
3. Que el Kino principal no haya tenido tramos electrónicos. El reglamento dice tómbola; no hallé comunicados en contrario, pero tampoco pude leer la sección de novedades de loteria.cl.
4. Transmisión: Loto en vivo por polla.cl y sala abierta al público en Compañía 1085, 2.º piso (oficial); señales de televisión, no verificadas. Kino por el canal de YouTube de Lotería (prensa, feb-2026).
5. Contenido de la página de resultados de polla.cl y de consulta de loteria.cl: profundidad, descarga, términos de uso.
6. Contenido del botón «Descargar Archivo» de las estadísticas del Kino.
7. Texto del artículo quinto transitorio del proyecto de apuestas en línea; estado exacto al 9-oct-2026 (última fuente abierta: 29-sep-2026).
8. Acuerdo tecnológico de Lotería con Intralot (resultado de búsqueda, no abierto).
9. Número del informe de Contraloría de 2019; resultado final del caso CONAR 1114/19; estado de la apelación del caso del cartón dañado.
10. Matriz y vigencia de Kino 5; nombre comercial del juego del DS 691 (7 de 30) y del DS 504 de 2024; un DS 87 de 1992 de Polla (14 de 24), no identificado.
11. Las citas literales de decretos provienen de un resumidor automático sobre el XML de la BCN: cotejar antes de citar.

### 8.3 Contradicciones en las propias fuentes oficiales

- Las preguntas frecuentes de Polla dicen en una respuesta que Polla Boleto se sortea en la Sala de Sorteos y en la siguiente que se sortea con el generador; la ficha del juego dice sistema informático y sala de sorteos a la vez.
- La misma página nombra como fiscalizador a la Superintendencia de Valores y Seguros (hoy CMF) y da dotación «a septiembre de 2022»: está desactualizada.
- Polla cita tres números distintos para su ley de origen.
- La Memoria 2025 describe el Loto como «6 números seleccionados aleatoriamente por el Sistema Informático […] o extraídos de una tómbola […] según lo determine Polla»: el operador se reserva expresamente el cambio de mecanismo.

### 8.4 Solicitudes que convendría presentar

Por lo dicho en 3.3, la Ley 20.285 no permite exigir respuesta a Polla ni a Lotería. El orden eficaz es: primero los órganos del Estado obligados, luego peticiones voluntarias a los operadores.

**A. Ministerio de Hacienda (solicitud de acceso, Ley 20.285)**
1. Copia de los informes anuales de auditoría o inspección de los sistemas de selección aleatoria de Polla y de Lotería que los decretos ordenan remitirle (DS 47/1997, DS 767/2002, DS 542/2011, DS 158), 2011 a la fecha.
2. Comunicaciones de Polla sobre el cambio de modalidad del Loto en mayo de 2024 y julio de 2025, y de Lotería sobre el Boleto en septiembre de 2024.
3. Antecedentes fundantes del DS 504 de 2024.

**B. Contraloría General de la República (solicitud de acceso)**
1. Informe final de la auditoría a Polla sobre el ejercicio 2017 (remitido a Hacienda el 28-jun-2019) y su seguimiento.
2. Cualquier informe de auditoría o fiscalización que haya examinado el proceso de sorteo, las tómbolas, las bolillas o la sala de sorteos de Polla, o el cumplimiento de porcentajes de Lotería (Ley 18.568, art. 11).

**C. Corfo y Sistema de Empresas Públicas (solicitud de acceso)**
1. Actas o informes del directorio de Polla donde se acordó el cambio de mecanismo de 2024 y de 2025, y sus fundamentos.
2. Bases de la licitación privada de servicios tecnológicos en curso, en lo relativo al generador de números y a equipos de sorteo.

**D. Superintendencia de Casinos de Juego (solicitud de acceso)**
1. Nómina de laboratorios acreditados y cualquier informe de validación de sistemas de selección aleatoria de Polla o Lotería que obre en su poder.

**E. Polla Chilena (petición voluntaria; canal de transparencia: https://www.pollachilena.cl/polla-chilena/transparencia/)**
1. Histórico completo del Loto y adicionales, sorteo a sorteo, **con orden de extracción**, modalidad (tómbola o electrónico), identificador de tómbola y de juego de bolillas.
2. Marca, modelo, año y principio de mezcla de cada tómbola; número de juegos de bolillas; especificación y tolerancias de masa y diámetro; protocolo y registros de pesaje; criterio de rotación y reemplazo.
3. Procedimiento certificado del proceso «Sorteo» bajo ISO 9001.
4. Fecha y número de sorteo de cada cambio de matriz desde 1989.
5. Copia de un acta notarial de sorteo, como muestra del contenido.

**F. Lotería de Concepción (petición voluntaria; sclientes@loteria.cl)**
1. Los mismos cinco puntos para Kino y adicionales, más confirmación de si el Kino principal ha usado alguna vez sistema informático.
2. Contenido y formato del archivo de estadísticas descargable y condiciones de uso para investigación.

**G. Notarías**
1. Las actas de sorteo son instrumentos notariales; si están protocolizadas, puede pedirse copia en la notaría respectiva (el reglamento del Kino se protocoliza en la notaría de Ramón García Carrasco, de Concepción).

**H. Fuente alternativa para el orden de extracción**
1. Las grabaciones de los sorteos transmitidos (canal de YouTube de Lotería; transmisiones de Polla). Si siguen publicadas, el orden de salida puede transcribirse sorteo a sorteo; es la única vía pública que identifiqué para pruebas de posición. No verifiqué cuántas grabaciones hay ni desde cuándo.
