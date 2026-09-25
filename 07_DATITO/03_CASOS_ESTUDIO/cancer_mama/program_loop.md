# Loop Iterativo: Simulador de Predicción de Falla

**Objetivo:** Madurar `simulador_prediccion_falla.html` en 7 iteraciones.

## Protocolo

Cada iteración:

1. **Leer**: 
   - Última fila de `results.tsv`
   - `agent_lessons.yaml` (lecciones acumuladas)

2. **Formular hipótesis** (1 frase):
   - Qué cambio mejorará el simulador

3. **Editar SOLO archivo permitido**:
   - Iter 1: `simulador_prediccion_falla.html` ✓
   - Iter 2: idem (matriz dinámica)
   - Iter 3: idem (histogramas)
   - Iter 4: idem (ROC)
   - Iter 5: idem (preguntas)
   - Iter 6: idem (UX/diseño)
   - Iter 7: idem (documentación)

4. **Correr checks fijos**:
   - `python 03_SCRIPTS/verificar_navegacion.py` (archivo existe, HTML válido)
   - `python 03_SCRIPTS/verificar_artefactos.py` (estructura CSS Datito)
   - `grep -n "G1\|G9" 07_DATITO/00_INICIO/spec.md` (garantías pedagógicas)

5. **Evaluar**:
   - Si **MEJORA**: KEEP + append lección en `agent_lessons.yaml`
   - Si **IGUAL/PEOR/CRASH**: DISCARD + append patrón de falla

6. **Commit**:
   - `git commit -m "Iter N: [descripción de cambio]"`

7. **Repetir** cada 30 minutos

## Iteraciones Planeadas

| Iter | Cambio | Status | Fecha |
|------|--------|--------|-------|
| 1 | Scatter plot + umbral | ✅ DONE | 2026-09-25 |
| 2 | Matriz confusión dinámica | ⏳ | 2026-09-25 |
| 3 | Histogramas (vibración/temp) | ⏳ | 2026-09-25 |
| 4 | Curva ROC interactiva | ⏳ | 2026-09-25 |
| 5 | Preguntas pedagógicas | ⏳ | 2026-09-25 |
| 6 | UX/diseño coherente Datito | ⏳ | 2026-09-25 |
| 7 | Documentación + README | ⏳ | 2026-09-25 |

## Criterios de Éxito

- ✅ HTML funciona sin errores en navegador
- ✅ CSS mantiene coherencia Datito (`--tinta`, `--acierto`, etc)
- ✅ Código comentado (mín: qué, por qué no)
- ✅ Rutas relativas correctas (desde 07_DATITO/)
- ✅ Accesible (sin JS pesado, funciona offline)
- ✅ G1 (reproducible), G9 (todo en artefacto, nada en terminal)

## Detenerse Si

- Mer queda roto (G1 violado)
- Diseño diverge de Datito (`--tinta` no usado)
- Se pierden horas sin avance (loop falla)
