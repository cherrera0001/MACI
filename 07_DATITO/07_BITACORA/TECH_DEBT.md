# Technical Debt — MACI Navegación

**Prioridad:** MEDIA (afecta reproducibilidad, no funcionalidad)

---

## Problema Identificado

`construir_navegacion.py` requiere refactor completo:

### Bugs Específicos
1. **Línea 92-94:** `VISUAL` apunta a `07_DATITO/visual/` pero archivos están en `07_DATITO/01_CONCEPTOS/visual/`
   - **Fix:** Usar fallback o variable explícita de rutas migradas

2. **Línea 95:** `CLASES_YAML` no definida
   - **Fix:** Definir como `str(RUTAS["clases"])` después de `resolver_rutas()`

3. **Líneas 103-125:** `VISUAL_DE` tiene nombres viejos que no coinciden con archivos migrados
   - **Fix:** Generar dinámicamente desde `grafo.yaml` campo `archivo` o actualizar manualmente

4. **Línea 910:** `mapa["conceptos"]` espera estructura que no existe en `mapa_ensenanza.yaml`
   - **Fix:** Normalizar en `cargar()` o crear wrapper

### Scope
- Script: ~950 líneas
- Archivos YAML: clases.yaml, curriculum.yaml, dudas.yaml, mapa_ensenanza.yaml
- Interdependencias: 5+ (cargar_curso, bloque_nav, etc.)

---

## Solución Actual (Parche Temporal)

`generar_index.py` (150 líneas):
- ✅ Funciona sin dependencias complejas
- ✅ Genera index.html offline
- ❌ No inyecta nav en HTML individuales
- ❌ No integra con bloque_leccion, bloque_dudas, etc.

**Usado por:** índice central
**Limitaciones:** No es solución canónica

---

## Fix Completo (Próxima Sesión)

### Paso 1: Definir Variables Globales Correctamente
```python
RUTAS = resolver_rutas(cargar_config())
CLASES_YAML = str(RUTAS["clases"])  # Fix línea 212
VISUAL = (RAIZ / "07_DATITO" / "01_CONCEPTOS" / "visual")  # Fallback correcto
```

### Paso 2: Actualizar VISUAL_DE Dinámicamente
```python
# Generar desde grafo.yaml si existe
if Path(RUTAS["grafo"]).exists():
    grafo = cargar(str(RUTAS["grafo"]))
    VISUAL_DE = {cid: c.get("archivo", f"{cid}.html") 
                 for cid, c in grafo.get("conceptos", {}).items()}
```

### Paso 3: Normalizar Estructura YAML
```python
def cargar_yaml_tolerante(ruta):
    data = cargar(ruta)
    # Normalizar claves / estructuras esperadas
    if "conceptos" not in data:
        data["conceptos"] = {}
    return data
```

### Paso 4: Integrar generar_index.py
```python
# Dentro de main(), después de inyectar nav:
if not os.path.exists(index_path):
    generar_index_desde_grafo(RUTAS["grafo"], index_path)
```

**Esfuerzo:** 2-3 horas (refactor + test)
**Beneficio:** Script canónico funcional, reproducible, mantenible

---

## Status Actual

| Componente | Estado | Deuda |
|---|---|---|
| index.html | ✅ Funciona (generar_index.py) | parche temporal |
| HTML KEEP | ✅ Funciona (nav nativa) | no inyectada dinámicamente |
| construir_navegacion.py | ❌ Roto | requiere refactor |
| Documentación | ✅ Completa | — |

---

## Recomendación

**Próxima sesión: Hacer el fix completo** antes de escalar a Fase 2B (gráficos).
Razón: Una navegación reproducible es infraestructura crítica para agregar contenido nuevo.

**No:** Seguir usando generar_index.py como solución a largo plazo.
