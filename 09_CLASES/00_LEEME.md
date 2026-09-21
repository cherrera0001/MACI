# 09 · CLASES — Grabaciones transcritas

Las clases del curso pasadas a texto, para poder buscarlas, citarlas y leerlas
sin conexión.

---

## Por dónde empezar

**No abras las transcripciones directamente.** Pesan entre 10 y 235 KB cada una.

Empieza por [`mapa_ensenanza.yaml`](mapa_ensenanza.yaml): dice **dónde se
enseñó cada concepto**, con rango de tiempo y quién hablaba (profesor, segundo
docente, ayudantía, alumnos). Curado a mano; es lo que usan los visuales.

[`indice_clases.yaml`](indice_clases.yaml) es automático: dice en qué minuto se
**menciona por primera vez** cada término. Sirve para buscar, pero una mención no
es una explicación, y no sabe quién habla.

Ejemplo: *"¿dónde explicó matriz de confusión?"* → clase del 7 de agosto,
0:44:25–0:47:52 y 1:00:54–1:02:54, y el ejercicio de 100 pacientes del 4 de
septiembre, 1:28:40–1:48:16.

**Qué entra al certamen.** El profesor: «Entran solo mis clases. No entran las
clases de Alejandra» (clase del 15 de julio, 1:18:16). Las ayudantías se
estudian, pero no son materia de certamen.

---

## El flujo

Cada grabación nueva entra por el mismo camino:

```
vídeo  →  transcribir_clases.py  →  integrar_clase.py  →  disponible para estudiar
              faster-whisper          mapea conceptos,
              CPU, sin GPU            indexa, sube a NotebookLM
```

### 1 · Transcribir

```bash
uv run --with faster-whisper python 03_CODIGO/transcribir_clases.py --listar
uv run --with faster-whisper python 03_CODIGO/transcribir_clases.py --todas
```

Usa `faster-whisper` con cuantización int8 sobre CPU. No requiere GPU ni
`ffmpeg`. Una clase de 90 minutos tarda entre 30 y 60 minutos con el modelo
`small`, así que conviene dejarlo corriendo.

Genera dos archivos por clase: `.md` con marcas de tiempo por segmento, y
`_plano.txt` para buscar con `grep`.

### 2 · Integrar

```bash
python 03_CODIGO/integrar_clase.py              # todas las pendientes
python 03_CODIGO/integrar_clase.py --sin-subir  # sin tocar NotebookLM
python 03_CODIGO/integrar_clase.py --estado     # ver qué hay integrado
python 03_CODIGO/integrar_clase.py --sin-subir --remapear   # recalcula todas
```

Detecta las transcripciones nuevas, mapea qué conceptos del curriculum aparecen
y en qué minuto, escribe el índice, y las sube a NotebookLM.

### 3 · Llevarla a los visuales

Agrega la clase y sus tramos a `mapa_ensenanza.yaml` y corre
`python 03_CODIGO/construir_navegacion.py`: los visuales muestran el nuevo tramo
en «Dónde se enseñó» y el índice `07_DATITO/visual/index.html` se regenera. Luego
`python 03_CODIGO/verificar_visuales.py` comprueba que cada marca exista.

Es **idempotente** —lo ya integrado se omite— y **degrada**: si NotebookLM no
responde, el índice local se completa igual y queda anotado para reintentar.

---

## Qué hay indexado

Consulta el estado actual con:

```bash
python 03_CODIGO/integrar_clase.py --estado
```

---

## Advertencias

**La transcripción es automática.** Puede errar en términos técnicos y nombres
propios. Contrástala con el material del curso antes de citarla como fuente.

**Las marcas de tiempo pueden desviarse** unos segundos respecto del vídeo
original.

**No se recorta nada a mano.** Algunas grabaciones incluyen los minutos previos
al inicio —pruebas de audio, gente conectándose— y quedan en el texto. Recortar
introduciría criterio propio en una fuente que debe poder contrastarse con el
vídeo.

**Los vídeos no se versionan.** Pesan cientos de MB y están en `.gitignore`. Se
versiona la transcripción, que es lo que aporta.
