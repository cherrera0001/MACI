# Qué es MACI y Datito

## MACI

MACI es el repositorio. Tiene tres productos y la plataforma que los sostiene.

```mermaid
flowchart LR
    subgraph Fuentes["Fuentes del profesor"]
        T["15 clases transcritas"]
        P["Presentaciones y prácticos"]
        C["Certámenes 1, 2 y 3"]
    end
    subgraph MACI["Repositorio MACI"]
        Y["Fuente única<br/>07_DATITO/*.yaml"]
        V["Curso<br/>23 clases en HTML"]
        D["Datito<br/>tutor socrático"]
        F["Proyecto semestral<br/>Melbourne y Galaxy Zoo"]
        L["Learning Loop<br/>lecciones de construcción"]
    end
    W["maci.c4a.cl<br/>solo el curso"]
    A(["Alumno"])

    Fuentes --> Y
    Y --> V
    Y --> D
    V --> W
    W --> A
    V --> A
    D <--> A
    L -.-> V
    F -.->|caso del curso| V
```

| Pieza | Qué es | Dónde vive |
|---|---|---|
| **Curso** | 23 clases en 6 unidades. Cada una abre con objetivo, ficha Bloom y una pregunta de activación, y cierra con qué aprendiste, qué no confundir, un procedimiento y una pregunta final. Funciona sin conexión. | `07_DATITO/01_CONCEPTOS/visual/`, `02_REFERENCIA/`, `04_EJERCICIOS/` |
| **Datito** | Tutor personal. Corre en Claude Code, no en el sitio. | `.claude/skills/datito*/`, contrato en `00_INICIO/spec.md` |
| **Proyecto semestral** | Predicción de precios en Melbourne (entrenar con 2016, predecir 2017) y desafío Galaxy Zoo. | `08_PROYECTO_FCD/`, `09_RESULTADOS/` |
| **Plataforma** | Generador de navegación, verificación y publicación. | `03_SCRIPTS/`, `04_CODIGO/`, `.github/workflows/` |
| **Learning Loop** | Memoria de fallos de los agentes que construyen las páginas. | `07_DATITO/07_BITACORA/learning_loop/` |

## Datito

Datito no explica y se va. Pregunta, **espera la respuesta**, diagnostica el error y registra evidencia. Un concepto llega a `DOMINADO` solo cuando el alumno lo explicó, lo aplicó, lo interpretó y lo transfirió a un caso nuevo.

```mermaid
stateDiagram-v2
    [*] --> NO_ESTUDIADO
    NO_ESTUDIADO --> EN_ESTUDIO: primera sesión
    EN_ESTUDIO --> COMPRENSION_PARCIAL: explica con huecos
    COMPRENSION_PARCIAL --> COMPRENDIDO: explica y aplica
    COMPRENDIDO --> DOMINADO: además interpreta y transfiere
    DOMINADO --> [*]
```

| Comando | Para qué |
|---|---|
| `/datito` | Sesión socrática sobre un concepto |
| `/datito-corregir` | Corrige un lote de respuestas escritas y actualiza el progreso |
| `/datito-progreso` | Informe de qué se domina y qué sigue. Solo lectura |
| `/datito-pedagogia` | Audita si el material apunta al nivel que la evaluación exige |
| `/datito-visual` | Construye una página del curso desde la plantilla canónica |
| `/datito-loop` | Una corrida del Learning Loop tras un fallo de construcción |

Archivos que Datito lee y escribe:

- `07_DATITO/curriculum.yaml`: 21 conceptos con prerrequisitos y fuentes.
- `07_DATITO/progreso.yaml`: estado y evidencia de cada concepto.
- `07_DATITO/errores_conceptuales.yaml`: errores observados, con la frase del alumno.
- `07_DATITO/estado.md`: resumen generado por `datito_estado.py`. No se edita a mano.

## Qué no es

- No es un curso oficial de la universidad. El contenido académico es del profesor titular; aquí se estudia y se cita.
- El sitio no tiene tutor. Datito corre en local.
- El score del Learning Loop no mide aprendizaje. Mide que la página respeta la plantilla y no depende de la red.
