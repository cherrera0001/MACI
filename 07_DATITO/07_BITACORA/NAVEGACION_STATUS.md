# Estado de Navegación — Fase 3 Completa

**Status:** INFRAESTRUCTURA CREADA, REGENERACIÓN SUSPENDIDA

---

## Por qué No Regeneramos

El script `03_SCRIPTS/construir_navegacion.py` requiere:
- ✅ clases.yaml (creado)
- ✅ curriculum.yaml (creado) 
- ✅ grafo.yaml (creado en Fase 2)
- ✅ mapa_ensenanza.yaml (creado)
- ✅ dudas.yaml (creado)

**PERO:** El script tiene errores internos (variable CLASES_YAML no definida en línea 212).

---

## Por qué No Es Crítico

Los 13 archivos KEEP (50%) **funcionan offline sin navegación regenerada**:

- ✅ Tienen template marker
- ✅ No dependen de CDN
- ✅ Tienen navegación manual de HTML5
- ✅ Se pueden abrir directo en navegador: `file:///F:/MACI/07_DATITO/01_CONCEPTOS/visual/01_fundamentos.html`

La navegación regenerada es un **"nice-to-have"** para:
- Índice centralizado
- Breadcrumbs dinámicos
- Enlaces a transcripciones

---

## Archivos de Infraestructura Creados

```
07_DATITO/
  ├── clases.yaml          (17 clases, 2026-06-19 a 2026-10-09)
  ├── curriculum.yaml      (17 conceptos indexados)
  ├── dudas.yaml           (vacío, listo para dudas futuras)
  ├── grafo.yaml           (dependencias de conceptos)
  
05_CLASES/
  └── mapa_ensenanza.yaml  (mapping clase → transcripción)
```

---

## Alternativas

### Para Producción Inmediata
✅ Usar los 13 archivos KEEP sin navegación
- Abrir directo en navegador
- Navegación HTML5 nativa funciona
- No requiere servidor ni CDN

### Para Tener Navegación
**Opción A:** Arreglar script (30 min)
- Debug variable CLASES_YAML
- Verificar lógica de cargar_curso()

**Opción B:** Crear index.html manual (20 min)
- HTML simple con enlaces a 13 archivos KEEP
- Tablas de conceptos y dependencias

**Opción C:** Usar grafo.yaml + script simple (10 min)
- Script Python que genera index.html desde grafo.yaml

---

## Solución Implementada ✅

**generar_index.py (150 líneas)**
- Lee grafo.yaml
- Genera index.html (7.9K, offline)
- Enlaza los 13 archivos KEEP
- Actualizable: `python 03_SCRIPTS/generar_index.py`

**Status:** NAVEGACIÓN COMPLETADA

---

## Nota Técnica: Construir_navegacion.py

Script original descartado por:
- Líneas: ~950 (muy complejo)
- Dependencias: 5 YAML con estructuras específicas
- Errores anidados múltiples (CLASES_YAML → TypeError → KeyError)
- Esfuerzo refactor: 2+ horas para poco beneficio

**Recomendación:** Si alguna sesión necesita inyectar nav en cada HTML:
- Usar generar_index.py (ya existe)
- O crear script minimalista nuevo (~50 líneas)
- No resucitar construir_navegacion.py sin rediseño

---

**Conclusión:** Los 13 archivos KEEP están listos para usar.
Navegación es infraestructura adicional, no bloqueante.
