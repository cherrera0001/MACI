# 09 · CLASES — Grabaciones transcritas

Las clases del curso pasadas a texto, para poder buscarlas, citarlas y leerlas
sin conexión.

---

## Por dónde empezar

**No abras las transcripciones directamente.** Pesan entre 60 y 120 KB cada una.

Empieza por [`indice_clases.yaml`](indice_clases.yaml): dice **qué conceptos
trata cada clase y en qué minuto se mencionan por primera vez**. Buscas el
concepto, obtienes clase y marca de tiempo, y recién entonces vas al texto.

Ejemplo de lo que resuelve: *"¿dónde explicó matriz de confusión?"* →
clase del 7 de agosto, minuto **0:49:48**.

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
```

Detecta las transcripciones nuevas, mapea qué conceptos del curriculum aparecen
y en qué minuto, escribe el índice, y las sube a NotebookLM.

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
