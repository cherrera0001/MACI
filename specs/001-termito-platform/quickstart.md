# Quickstart: validación de MACI 1.0 (Datito)

**Fecha**: 2026-10-17 · **Prerequisitos**: Python 3.12, uv/pip, Ollama con un modelo
(≥3B, Q4) —sin él el sistema opera en "modo exploración" y los escenarios 2–3 quedan
bloqueados, lo cual también es una validación válida del edge case—.

Guía de escenarios ejecutables que demuestran la feature de extremo a extremo. No
incluye implementación; referencia contratos (`contracts/`) y data model
(`data-model.md`).

## 0. Preparación

```bash
# instalar dependencias de la plataforma (manifiesto que fije tasks.md)
# arrancar Ollama (fuera de MACI) con un modelo pequeño, ej.:
ollama pull qwen2.5:3b        # o equivalente evaluado en research R2
datito --help                # CLI operativo
```

## 1. Crear un Datito desde materiales reales (US1 — SC-001)

```bash
datito nuevo fcd --nombre "Fundamentos de Ciencia de Datos" --periodo 2026-T2
datito ingestar fcd ruta/a/programa.pdf ruta/a/laminas.pptx ruta/a/certamenes/
```

**Esperado**: resumen de ingesta con fuentes procesadas, fragmentos por fuente y
advertencias de lo no extraíble. Con materiales ya reunidos, el trabajo activo del
estudiante hasta aquí <10 min. El asistente de construcción es **narrativo, una
decisión por pantalla** (patrón de onboarding de Duolingo, validación REA 2026-10-17):
se siente como conversación con el Datito, no como formulario.

```bash
datito construir fcd         # asistente de los 8 componentes
datito prompt ver fcd
```

**Esperado**: prompt íntegro reflejando las decisiones; `datito verificar fcd` en
verde. Tiempo total acumulado de trabajo activo <30 min (SC-001).

## 2. Conversar con evidencia y lucha productiva (US2 — SC-002, SC-003)

```bash
datito servir                # http://127.0.0.1:8377
```

En la UI: pedir una explicación de un concepto del curso.

**Esperado (SC-002)**: cada afirmación muestra evidencia con clic a página/timestamp,
o el tutor declara "sin fuente". Luego, pedir un ejercicio e intentar "dame la
respuesta" sin haber intentado:

**Esperado (SC-003)**: el tutor ofrece una pista y solicita un intento; la solución
solo aparece tras intento o con revelación consentida (botón explícito) que queda
registrada. Tras un intento **fallido**, el feedback ofrece acciones graduadas —
"mostrar un paso" (un paso del procedimiento, patrón "Show a step" de Khan Academy,
validación REA) e "intentar de nuevo" — antes que la solución completa. Resolver mal
un ejercicio deja una duda en `dudas.yaml` con procedimiento y evidencia (FR-010).

## 3. Evaluación por distinciones (US3 — FR-012)

```bash
datito evaluar fcd --tema <concepto-con-vecinos>
```

**Esperado**: ítems que exigen distinguir conceptos vecinos (no recitar), criterios
explícitos y actualización del estado de dominio en el panel del grafo (US5).

## 4. Ciclo de vida: notas y cierre (US4 — SC-005)

```bash
datito nota fcd --evaluacion "Certamen 1" --nota 4.2 --observaciones "confundí X con Y"
datito cerrar fcd
datito prompt ver fcd        # → error de estado: Datito inactivo
cat cursos/fcd/dudas.yaml     # registro íntegro
```

**Esperado**: la nota genera ajustes visibles; tras el cierre el Datito no conversa
y el 100% del registro permanece consultable (SC-005).

## 5. Offline y portabilidad (US7 — SC-004, SC-006)

```bash
# desconectar la red del equipo, repetir escenarios 2–4: idénticos resultados (SC-004)
datito exportar fcd --destino /mnt/usb/fcd-exportado/
datito importar /mnt/usb/fcd-exportado/ --slug fcd-copia
```

**Esperado**: el paquete se valida (sin rutas absolutas ni secretos), la copia abre en
otro equipo sin red con historial íntegro.

## 6. Migración v0.0.1 sin regresiones (SC-007)

```bash
# antes de migrar: la verificación actual del repo está en verde
python3 03_SCRIPTS/verificar_todo.py     # baseline (hoy: con FALLOs conocidos de
                                         # rutas F:\ en EVALUACION.md C1 — registrar baseline)
datito ingestar fcd --legacy 07_DATITO/ # adaptador research.md R6
python3 03_SCRIPTS/verificar_todo.py     # posterior: idéntico resultado
```

**Esperado**: el sitio estático y sus verificaciones no se ven afectados; el primer
Datito real funciona sobre los mismos YAML. (Nota: el baseline hoy tiene fallos
documentados en `EVALUACION.md`; SC-007 exige *no empeorar*, no sanar deuda previa.)

## 7. Idiomas (SC-006)

En la UI con `?lang=en`: interfaz en inglés; preguntar en inglés al Datito → responde
en inglés con evidencia intacta.
