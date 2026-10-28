# Pruebas manuales — interfaz web y paquete distribuible

Ejecutar antes de cada release del paquete. Tiempo total: ~30 minutos.
Precondición: el ZIP construido (`python 15_TERMINITO/scripts/build_paquete.py`).
Las verificaciones API equivalentes a cada flujo corren en `tests/` (50 tests
pytest); este documento es lo que un humano hace con el navegador.

## Flujo 1 — De maci.c4a.cl al primer chat (5 minutos)

1. Abrir `public/01_CONCEPTOS/visual/00_index.html` (o maci.c4a.cl en producción).
2. Verificar: existe la sección **"Tu propio Datito"** con el botón
   "Descargar para tu curso" (si el ZIP no se construyó, el botón aparece como
   texto plano: es el comportamiento anti-404 esperado).
3. Descargar el ZIP, descomprimir en una carpeta nueva.
4. Doble clic en `start` (`start.py` / `start.sh` / `start.bat`).
5. Esperar: primera vez crea el entorno (~30–60 s); el navegador se abre en
   `http://localhost:8377`.
6. Verificar en la Home: pill **"modo exploración"** (sin Ollama) o **"modo tutor"**,
   y el curso "Fundamentos de Ciencia de Datos" listado.
7. Entrar a **Chatear**, escribir "¿qué diferencia hay entre overfitting y
   underfitting?" → respuesta con chips de evidencia → clic en un chip → se abre
   el fragmento fuente.
8. Cerrar la ventana del terminal: el servidor se detiene.

**Con Ollama** (modo tutor): instalar Ollama, `ollama pull qwen2.5:3b`, repetir
paso 5 → la Home muestra "modo tutor · qwen2.5:3b" y las respuestas son
explicaciones generadas con citas validadas.

## Flujo 2 — Crear un Datito nuevo desde la web (10 minutos, sin terminal)

1. Con el servidor corriendo, Home → **＋ Crear Datito**.
2. Paso 0: nombre del curso ("Álgebra I") + subir 1–2 archivos `.md`/`.pdf`.
3. Pasos 1–8: responder o aceptar la sugerencia en cada pantalla (una decisión
   por pantalla; botón "usarla" copia la sugerencia).
4. Final: se muestra el system prompt completo → **Confirmar y empezar**.
5. Verificar: el chat responde citando SOLO los archivos subidos; una pregunta
   fuera de los materiales produce "No tengo fuente en los materiales…".
6. `datito lista` (opcional, en terminal) muestra el curso nuevo.

## Flujo 3 — Evaluación por distinciones y panel de dominio (5 minutos)

1. En el curso fcd: **Evaluarme**.
2. Responder las 3 distinciones (buena, parcial, mala) verificando:
   - feedback con resultado en color y checklist de criterios ✓/✗;
   - micro-progreso "Distinciones de esta sesión: N/M" actualizándose;
   - botón "Siguiente distinción" cicla los ítems.
3. Ir a **Dominio**: la cadena "del error a la validación" muestra ● en los
   conceptos evaluados; el toggle "Mostrar todo el mapa" revela el resto.
4. Refrescar la página: el dominio persiste (viene de `grafo/dominio.yaml`).
5. Botón "✏️ registrar como duda" en una respuesta con fuente → confirmar que
   `dudas.yaml` del curso ganó una entrada con sus citas.

## Flujo 4 — Lucha productiva: ejercicio sin trampa (5 minutos)

1. En el chat de fcd, pegar un ejercicio real (ej. el del certamen: "Tres
   modelos con R² train/test: A 0,98/0,54 · B 0,72/0,70 · C 0,41/0,39…").
2. Verificar: la respuesta pide TU INTENTO primero y muestra el chip de estado
   azul "pista". No entrega material.
3. Escribir "pista" → llega UN paso con su cita (chip "paso N/M").
4. Escribir "dame la respuesta" → el tutor se niega (estado
   "esperando_intento"); no aparece ninguna evidencia.
5. Escribir el intento (aunque esté mal) → estado "revision", revisión con
   citas del material.
6. Solo entonces, si el estudiante lo pide, la solución se revela y queda
   registrada en `sesion.yaml` (campo `revelaciones`).
7. Verificar en disco: `cursos/fcd/sesion.yaml` contiene la sesión con sus
   revelaciones paso a paso.

## Flujo 5 — Ciclo de vida: nota, cierre y portabilidad (5 minutos)

1. CLI: `datito nota fcd "Certamen 2" 3.5 --observaciones "me faltó tiempo"` →
   imprime los ajustes derivados; `curso.yaml` ganó una línea de
   retroalimentación que el prompt verá desde la siguiente interacción.
2. `datito exportar fcd` → crea `exportados/fcd-<fecha>.term.zip`.
3. En otro directorio (otra "máquina"): copiar el ZIP, `datito importar <ruta>`
   (o `POST /api/importar`) → el curso reaparece completo, materiales
   incluidos (los symlinks se materializan como archivos reales).
4. `datito cerrar fcd` → "cerrado · registro integro: True". El chat responde
   409 `datito_cerrado`; `datito status fcd` y `GET /registro` siguen
   mostrando dudas, notas y dominio.
5. Home: el curso cerrado aparece con estado "cerrado" en la lista.

## Flujo 6 — Idioma (2 minutos)

1. En cualquier página, clic en el botón **EN** de la barra superior → la
   interfaz completa cambia a inglés y persiste tras refrescar.
2. Clic en **ES** → vuelve al español.
3. Con Ollama activo, escribir en inglés en el chat → el Datito responde en
   inglés (regla del system prompt, FR-022).
