# Azar físico: ¿se puede predecir un sorteo de bolillas?

Revisión del estado del arte sobre sesgo y predicción en sistemas físicos de azar, con las máquinas de extracción de bolillas como caso de estudio. Búsqueda cerrada el 2026-10-09.

## Por dónde empezar

Abre [`azar_fisico.html`](azar_fisico.html) en el navegador. Funciona sin conexión y trae la revisión completa: conceptos, lo medido en moneda, dado y ruleta, el experimento tailandés con sus datos, un simulador de bombo sesgado, una calculadora de potencia, el caso chileno, el mapa de hipótesis, el diseño del experimento que falta y la matriz bibliográfica.

## Qué concluye

- Los aparatos de azar tienen sesgos reales y pequeños; verlos cuesta miles o cientos de miles de repeticiones.
- Predecir un resultado concreto se ha logrado solo en la ruleta, antes de que la bola toque los deflectores.
- En bombos de bolillas hay un único experimento publicado (Pinitsoontorn, Buathong y Srisodaphol 2014, máquina casera): una bola 1 % más liviana sale 12,8 % de las veces en lugar de 10 %. Es un sesgo, no una predicción.
- Nadie ha medido cuánto dura la «memoria» de un bombo ni ha predicho una extracción.
- En Chile, el Loto usó un generador electrónico entre los sorteos 5112 y 5301; su serie histórica no viene de una sola máquina.

## Archivos

| Archivo | Contenido |
|---|---|
| `azar_fisico.html` | La hoja visual. Sobre el template canónico de Datito, sin CDN. |
| `fuentes/01_fisica_caos.md` | Moneda, dado, ruleta, esferas duras, límites de la predicción. 62 referencias. |
| `fuentes/02_loterias_sesgos.md` | Ficha del artículo tailandés, sorteos reales, fraudes, tolerancias de bolillas. |
| `fuentes/03_pruebas_aleatoriedad.md` | NIST SP 800-22 y 800-90B, pruebas para sorteos sin reposición, potencia. 58 referencias. |
| `fuentes/04_ml_instrumentacion.md` | Modelos sobre sistemas caóticos, seguimiento, simulación, repositorios. 49 publicaciones. |
| `fuentes/05_caso_chile.md` | Polla y Lotería de Concepción: normas, mecanismo por juego, datos, solicitudes de información. |
| `analisis/potencia.py` | Tamaño muestral y potencia, con comprobación por simulación. Salida en `potencia_salida.txt`. |

## Cómo se hizo y qué límites tiene

Cinco agentes buscaron por separado, cada uno con un tema, y confirmaron cada referencia en Crossref, arXiv o la página del editor. Cada informe separa lo verificado de lo no verificado y dice si se leyó el texto completo, el resumen o solo los metadatos. Los 25 identificadores (DOI y arXiv) de la matriz de la hoja se resolvieron de nuevo, de forma independiente, antes de publicarla.

Límites que conviene tener presentes:

- De muchas fuentes solo se leyó el resumen o los metadatos. Antes de citar una cifra, abrir el original.
- Las cifras marcadas «cálculo propio» son nuestras, no de los autores.
- No se consultaron bases de pago ni literatura en otros idiomas que inglés, castellano y el artículo tailandés.
- El presupuesto del experimento propuesto es una estimación sin cotizaciones.

## Comprobaciones de la hoja

```
python 04_CODIGO/datito_loop_eval.py --path 14_INVESTIGACION/azar_fisico/azar_fisico.html
python 04_CODIGO/verificar_piel_lectura.py --path 14_INVESTIGACION/azar_fisico/azar_fisico.html
```
