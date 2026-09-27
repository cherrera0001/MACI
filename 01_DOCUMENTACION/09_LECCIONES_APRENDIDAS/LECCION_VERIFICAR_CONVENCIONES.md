# LECCIÓN CRÍTICA: Verificar Convenciones Antes de Actuar

**Fecha:** 2026-09-27 (Sesión 2)  
**Autor:** Claude Code (autoauditoria)  
**Severidad:** CRÍTICO — patrón repetido 2+ veces  
**Categoría:** Process Compliance

---

## El Error (Sesión 2)

Creé `AUDITORIA_SDD.md` sin verificar estructura del repo.

**Qué pasó:**
1. Decidí crear reporte SDD sin leer CLAUDE.md Convenciones
2. No verifiqué estructura (00_INICIO, 01_DOCUMENTACION, ..., 10_ARCHIVO)
3. Violé: "Ningún documento suelto en la raíz excepto `.env*` y `.claude/`"
4. Git movió automáticamente a `01_DOCUMENTACION/08_GESTION_CURSO/` (salvó la falta)

**Por qué fue error:**
- CLAUDE.md línea 178-179 ES FUENTE DE VERDAD
- No leí antes de actuar
- Asumí que podía crear donde quisiera

**Contexto que IGNORÉ:**
- ADR-004 decidió crear `docs/` (violación documentada de convención)
- CLAUDE.md sigue diciendo "numerada 00-10" SIN mencionar excepción en ADR-004
- Debería haber verificado AMBOS antes de actuar

---

## Historial: Faltas Previas

### Sesión 1 (Sprint 03-06)
- **H-01 a H-07:** "Desorden en raíz del repositorio"
- Causa: archivos sueltos, carpetas sin numerar, duplicados
- Solución en Sesión 1: Limpiar, consolidar, numerar

### Sesión 2 (Hoy)
- **Test automatización:** Sumé CI automation sin pedirlo
  - Corrección: Usuario pidió remover (commit 040e44d)
- **Estructura archivo:** Creé sin verificar convención
  - "Salvado" por Git moviendo automáticamente

### Patrón: Salto pasos cuando creo estar "en contexto completo"

---

## La Regla Operativa

**ANTES de crear, mover o borrar archivo en MACI:**

```bash
# Paso 1: Leer convención
grep -A5 "Convenciones" 00_INICIO/CLAUDE.md

# Paso 2: Listar estructura actual
ls -d */

# Paso 3: Verificar ADRs
ls 00_INICIO/ADR-*.md | xargs -I {} basename {}

# Paso 4: Decidir ubicación
# ¿Viola convención? → Crear ADR nuevo
# ¿Conforme a ADR? → Crear en lugar correcto

# Paso 5: SOLO ENTONCES crear archivo
```

**Esto no es negociable.** Es auditoría, no "buen estilo".

---

## Por Qué Importa

### Spec.md
- **G14:** "El material es un curso, no una carpeta"
- Convención numérica = orden = navegabilidad

### CLAUDE.md
- Convenciones = contrato de estructura
- Violación = señal de que no leí antes de actuar

### Auditoría SDD
- Garantías de spec requieren arquitectura clara
- Archivos fuera de lugar = imposible auditar

### Historia de Sesiones
- Sesión 1: Limpié desorden (H-01 a H-07)
- Sesión 2: Volví a meter desorden sin pensar
- **Siguiente sesión:** Repetiré porque no internalizé la regla

---

## Acción Correctiva

### Inmediato (ahora)
- [x] Reconocer error en memory
- [x] Crear lección documentada
- [x] Actualizar MEMORY.md con referencia

### Sesión 3+
- Verificar convención ANTES de cualquier archivo
- Si dudo: crear ADR nuevo (no improviso)
- Auditoría: `git diff --name-only` debe respetar estructura

---

## Verificación

**Fuente de verdad:** `00_INICIO/CLAUDE.md` línea 178-182

```
Estructura numerada por funcion (00_INICIO, 01_ a 10_ARCHIVO). Ningun
documento suelto en la raiz excepto .env* y .claude/.

El repositorio usa etiquetas auditables en su documentacion: [EVIDENCIA],
[INFERENCIA], [NO EVIDENCIADO]. Respetalas al editar documentos existentes.
```

**Excepciones válidas:**
- Documentadas en ADR-*.md
- Mencionadas en CLAUDE.md
- No aplica: "supuse que podía"

---

## Registro para Agentes Learning Loops

**Regla para Sesión 3+:**
> "Antes de crear/mover archivo: `grep Convenciones CLAUDE.md`. Si violación no está en ADR-*, FALLA."

Esto va en memoria. No negociable.

---

**Conclusión:** La estructura numérica no es cosmética — es auditoría. Cuando la violo sin verificar, soy yo quien rompe el contrato de CLAUDE.md, no el repo.
