# Procesos

Todo issue del tablero pertenece a uno de estos seis procesos (campo **Proceso**). Cada proceso tiene subprocesos con un comando y un criterio de salida.

```mermaid
flowchart LR
    P5["P5 Gestionar el backlog"] --> P1["P1 Construir una clase"]
    P1 --> P3["P3 Verificar y publicar"]
    P3 --> P2["P2 Estudiar con Datito"]
    P1 -. un fallo .-> P4["P4 Aprender de fallos"]
    P3 -. un fallo .-> P4
    P4 -. lección .-> P1
    P2 -. duda o error del alumno .-> P5
    P6["P6 Proyecto semestral"] -. caso Melbourne .-> P1
```

## P1 Construir una clase

```mermaid
flowchart TD
    A["1.1 Declarar la clase<br/>clases.yaml"] --> B["1.2 Leer lecciones<br/>agent_lessons.yaml"]
    B --> C["1.3 Construir desde la plantilla<br/>/datito-visual"]
    C --> D{"1.4 Gate del loop<br/>datito_loop_once.py"}
    D -- discard --> E["Volver a la última versión buena<br/>y anotar la lección"]
    E --> C
    D -- keep --> F["1.5 Regenerar navegación<br/>construir_navegacion.py"]
    F --> G["Pasa a P3"]
```

| Subproceso | Entrada | Salida | Criterio |
|---|---|---|---|
| 1.1 Declarar | Material del profesor | Entrada en `07_DATITO/clases.yaml` con objetivo, Bloom, activación y cierre | La clase cita su concepto de `curriculum.yaml` |
| 1.2 Leer lecciones | `agent_lessons.yaml` | Lista de fallos que aplican | `failure_patterns` leído completo |
| 1.3 Construir | `_TEMPLATE_CANONICO.html` | Un HTML | Sin CDN, con el marcador de plantilla, cifras fieles a la fuente |
| 1.4 Gate | El HTML | Fila en `results.tsv` | `keep_eligible=true` y lectura comprobada en navegador |
| 1.5 Navegación | `clases.yaml` | Portada, barras, cierres y dudas | El generador no deja cambios pendientes |

## P2 Estudiar con Datito

```mermaid
sequenceDiagram
    actor A as Alumno
    participant D as Datito
    participant R as Repo
    A->>D: /datito
    D->>R: lee estado.md y errores abiertos
    D->>A: pregunta al estilo del profesor
    Note over D: se detiene y espera
    A->>D: respuesta escrita
    D->>D: diagnostica contra el criterio de dominio
    D->>R: progreso.yaml, errores_conceptuales.yaml
    D->>R: datito_estado.py regenera estado.md
    D->>R: entrada en 07_BITACORA/
    D->>A: siguiente concepto recomendado
```

| Subproceso | Comando | Salida |
|---|---|---|
| 2.1 Sesión socrática | `/datito` | Evidencia en `progreso.yaml` y entrada de bitácora |
| 2.2 Corrección por lote | `/datito-corregir` | Informe y entrenamiento dirigido a los fallos |
| 2.3 Informe de avance | `/datito-progreso` | Qué se domina, qué se confunde y qué sigue |
| 2.4 Auditoría pedagógica | `/datito-pedagogia` | Brechas entre el material y el nivel que exige la evaluación |

## P3 Verificar y publicar

```mermaid
flowchart TD
    A["3.1 Verificar en local<br/>verificar_todo.py --navegador"] --> B{"¿LISTO?"}
    B -- no --> A0["Corregir. No se publica"]
    B -- sí --> C["3.2 Rama y pull request<br/>Closes #issue"]
    C --> D["3.3 CI en GitHub Actions<br/>tests de 04_CODIGO"]
    D --> E["3.4 Fusionar a main"]
    E --> F["3.5 Vercel corre publicar_sitio.mjs<br/>arma public/ solo con el curso"]
    F --> G["maci.c4a.cl"]
    G --> H["3.6 Verificar en línea<br/>verificar_todo.py --en-linea"]
    H --> I{"¿rotos o privados expuestos?"}
    I -- sí --> A0
    I -- no --> J["Cerrar el issue con la evidencia"]
```

`verificar_todo.py` reúne seis comprobaciones: generador sin pendientes, contrato de Datito, citas y enlaces, tests, navegador real a 390 y 1280 px, y el sitio en vivo. Cada una existe porque ese error ya ocurrió.

## P4 Aprender de fallos (Agents Learning Loop)

No se entrena ningún modelo. Lo que mejora es el repositorio: un agente cambia un archivo, lo mide con un gate fijo y deja escrito si el cambio se conserva.

```mermaid
flowchart TD
    A["4.1 Leer program_loop.md,<br/>failure_patterns y la última fila"] --> B["4.2 Una hipótesis, un archivo"]
    B --> C["4.3 Editar solo lo necesario"]
    C --> D["4.4 Medir con el gate"]
    D --> E{"¿mejora la línea base?"}
    E -- sí --> F["keep<br/>fila en results.tsv"]
    E -- no --> G["discard<br/>revertir el cambio"]
    F --> H["4.5 Lección en keep_patterns"]
    G --> I["4.5 Lección en failure_patterns"]
    H --> A
    I --> A
```

Reglas:

- Una lección `-FAIL-` va en `failure_patterns` y una `-KEEP-` en `keep_patterns`. Lo comprueba `04_CODIGO/test_learning_loop.py`.
- Toda lección lleva su fila en `results.tsv`.
- El score no cierra una tarea por sí solo: certifica la piel de la página, no que el control funcione.

## P5 Gestionar el backlog

```mermaid
flowchart TD
    A["5.1 Aparece trabajo<br/>hallazgo, duda, fallo"] --> B["5.2 Issue con plantilla<br/>tipo, área, prioridad"]
    B --> C["5.3 Colgarlo de su padre<br/>épica → historia → tarea"]
    C --> D{"¿es una decisión?"}
    D -- sí --> E["La responde el dueño<br/>en un comentario"]
    D -- no --> F["Todo"]
    E --> F
    F --> G["In Progress<br/>rama y PR"]
    G --> H["P3 Verificar y publicar"]
    H --> I["Done<br/>el PR cierra el issue"]
    I --> J["5.4 El milestone avanza"]
```

Detalle en [Cómo opera el tablero](Como-opera-el-tablero).

## P6 Proyecto semestral

```mermaid
flowchart LR
    A["6.1 Datos crudos<br/>02_DATOS"] --> B["6.2 Partición temporal<br/>2016 entrena, 2017 prueba"]
    B --> C["6.3 Modelar<br/>scripts y DashAI"]
    C --> D["6.4 Evaluar fuera de muestra"]
    D --> E["6.5 Resultados<br/>09_RESULTADOS"]
    E --> F["6.6 Informe y pitch<br/>06_ENTREGABLES"]
```

Regla del método: ninguna información de 2017 entra al entrenamiento, y cada cifra de un informe se regenera con un script del repo.
