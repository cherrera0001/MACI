# MACI — Máquina Asistida de Ciencia de Datos Interactiva

**MACI** es el curso estático de **Fundamentos de Ciencia de Datos** (FCD) de la Universidad de Concepción, semestre T2-2026. 

## Qué es este sitio

Un curso interactivo sin conexión que funciona desde el navegador:
- **22 clases** sobre conceptos de ML: desde datos hasta deep learning
- **3 certámenes** con preguntas que el profesor realmente pide
- Transcripciones completas de todas las clases  
- Todo funciona localmente (sin API, sin servidor, sin Internet)

## Cómo estudiar

1. Abre el índice (archivo `07_DATITO/01_CONCEPTOS/visual/00_index.html` localmente, o desde la URL tras el deploy)
2. En cada clase: **predice antes de mover** un control
3. Resuelve los ejercicios **antes de** abrir las respuestas (`<details>`)
4. Lee la lección final y pasa a la siguiente

**21 clases están listas. La clase 19 (Repaso integrado: el proyecto Melbourne) está pendiente.**

## El tutor Datito

Datito es el asistente que **no está en este sitio**. Sigue siendo local en tu máquina (en `F:/MACI`). Aquí solo tienes el curso estático.

En Datito puedes:
- Estudiar cada concepto paso a paso
- Hacer preguntas en lenguaje natural
- Grabar audio de tus respuestas

Ese es un software aparte. **Este deploy es solo el material del curso.**

## Navegación y estructura

```
Entrada
  ↓
07_DATITO/01_CONCEPTOS/visual/00_index.html
  ├─ 22 clases (01_fundamentos.html → 19_deep_learning.html)
  ├─ 3 certámenes (04_EJERCICIOS/certamen_1.html, certamen_2.html, ...)
  ├─ Transcripciones (05_CLASES/transcripciones/)
  └─ Guías y referencias (04_EJERCICIOS/guias/, 02_REFERENCIA/)
```

Cada visual es independiente. Los enlaces funcionan sin servidor.

## Garantías

✅ **Todo funciona sin conexión**
✅ **Todas las clases tienen el mismo diseño (template canónico v1)**
✅ **Los certámenes son autocorregibles**
✅ **Las transcripciones están integradas y citadas**
✅ **Los tests verifican que no hay enlaces rotos**

## Información técnica

- Lenguaje: HTML5 + CSS3 (sin CDN, sin frameworks pesados)
- Gráficos: Canvas y SVG inline
- Interactividad: JavaScript plano (sin librerías remotas)
- Deploy: Static site en Vercel (sin build, sin servidor)
- Almacenamiento: LocalStorage (marca de clases leídas, solo en tu navegador)

## Para estudiantes

Abre `07_DATITO/01_CONCEPTOS/visual/00_index.html` en tu navegador. No necesitas nada más.

Si estás viendo esto desde Internet: la URL que ves es el sitio publicado. Los enlaces funcionan igual.

## Para profesores / mantenimiento

El curso se genera automáticamente desde:
- `grafo.yaml` (estructura curricular y prerrequisitos)
- `clases.yaml` (metadatos de cada clase)
- `progreso.yaml` (marcas de Datito)
- HTML individuales en `07_DATITO/01_CONCEPTOS/visual/`

Para regenerar la navegación: `python 03_CODIGO/test_indice_curso.py` (corre tests, luego edita a mano si algo falla).

**No uses `datito_migracion_inicio.py` ni `repair_piel.py` en producción.**

## Estado actual (2026-09-26)

| Sección | Estado |
|---------|--------|
| Conceptos 1-18 | ✅ Estructura OK, validación en progreso |
| Concepto 19 | 🟡 Pendiente (clase futura) |
| Certamen 1 | ✅ Funcional |
| Certamen 2 | ✅ Funcional |
| Certamen 3 | ✅ Funcional |
| Transcripciones | ✅ 15/15 integradas |
| Dudas resueltas | ✅ Integradas en visuales |

## Licencia y atribución

Contenido del curso: Dr. [Profesor], UdeC  
Desarrollo de Datito: [Equipo de desarrollo]  
Estructura de este sitio: 2026

---

Para dudas, consulta al profesor o revisa las transcripciones integradas en cada clase.
