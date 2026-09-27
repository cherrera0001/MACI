# LECCIÓN PROFUNDA: ADR-004 vs CONVENCIONES (Estructura Rota)

**Fecha:** 2026-09-27  
**Severidad:** CRÍTICA — Arquitectura contradictoria  
**Categoría:** Design Debt / Documentation Mismatch

---

## El Problema Real

**CLAUDE.md dice:**
```
Estructura numerada por función (00_INICIO, 01_DOCUMENTACION, 02_DATOS, ..., 10_ARCHIVO).
Ningún documento suelto en la raíz excepto `.env*` y `.claude/`.
```

**La realidad en disco:**
```
00_INICIO/            ✅ Numerado
01_DOCUMENTACION/     ✅ Numerado
02_DATOS/            ✅ Numerado
...
10_ARCHIVO/          ✅ Numerado
docs/                ❌ SIN NUMERAR (viola convención)
herramientas/        ❌ SIN NUMERAR (viola convención)
tests/               ❌ SIN NUMERAR (viola convención)
.github/             ❌ NO NUMERADO (especial, pero no en CLAUDE.md)
03_SCRIPTS/generar_materiales_curso.py   (correcto)
```

**¿Por qué existen?** ADR-004 (Migration Plan)  
**¿Por qué están aquí?** Sesión 1-2 las implementó  
**¿Por qué esto es error?** CLAUDE.md NO se actualizó para reflejar ADR-004

---

## Raíz del Problema

```
ADR-004 DECIDE:      docs/ para gestion, adr, curso
↓
IMPLEMENTADO EN:     F3 merges, F5 generación
↓
DOCUMENTADO EN:      ❌ NO — CLAUDE.md sigue diciendo 00-10 sin excepciones
↓
YO FALLÉ:            Creé archivos sin ver que ADR-004 ya había cambiado convención
```

### El Ciclo Vicious

1. **ADR-004 decide nueva estructura** (docs/, herramientas/, tests/)
2. **Se implementa en commits** (silenciosamente violando convención)
3. **CLAUDE.md NO se actualiza** (sigue con 00-10 como verdad)
4. **Yo veo CLAUDE.md como fuente única** (pero está desincronizado)
5. **Creo archivos en lugar "correcto" según CLAUDE.md**
6. **Pero ese lugar es INCORRECTO según ADR-004 implementado**
7. **Resultado: estructura contradictoria**

---

## La Decisión que Falta

**ADR-004 está a mitad:** Implementado físicamente, pero NO formalizado en CLAUDE.md.

**Opciones:**

### Opción A: Ratificar ADR-004 en CLAUDE.md
```markdown
## Convenciones (actualizado 2026-09-27)

Estructura base: 00_INICIO, 01_DOCUMENTACION, ..., 10_ARCHIVO

EXCEPCIONES (ADR-004):
- docs/ — gestión, ADRs, curso de gestión (creado Sesión 1-2)
- herramientas/ — scripts consolidados (H-05 Sesión 1-2)
- tests/ — pytest suite (H-11 Sesión 1-2)
- .github/ — workflows y templates (H-11 Sesión 1-2)

Estos NO se numeran (son estructuras modernas, no funcionales).
```

**Pro:** Reconoce realidad, permite futuro.  
**Con:** Viola filosofía original 00-10.

### Opción B: Rechazar ADR-004, volver a 00-10
```bash
rm -rf docs/ herramientas/ tests/ .github/
mkdir 11_GESTION 12_HERRAMIENTAS 13_TESTS 14_GITHUB
# Mover todo respetando 00-10
```

**Pro:** Mantiene convención pura.  
**Con:** Deshace 2 sesiones de trabajo, rechaza ADR-004 sin razón.

### Opción C (ACTUAL): Contradictorio
Implementar ADR-004 pero no documentar en CLAUDE.md.

**Pro:** Ninguno.  
**Con:** CLAUDÉ.md es mentira, yo fallo intentando respetar mentira.

---

## La Lección para Sesión 3

**No es "verificar antes de actuar".**  
**Es "verificar que fuentes de verdad coincidan".**

### Checklist Correcto:

1. **Leer CLAUDE.md Convenciones** ← Fuente A
2. **Leer 00_INICIO/ADR-*.md** ← Fuente B
3. **Observar estructura en disco** ← Realidad
4. **¿Fuente A vs Fuente B vs Realidad coinciden?**
   - ✅ Sí → Crear seguindo estructura
   - ❌ No → STOP. Pedir decisión. No es mi lugar resolver.

```bash
# Sesión 3 antes de crear archivo:
echo "FUENTE A (CLAUDE.md):"
grep -A5 "Convenciones" 00_INICIO/CLAUDE.md

echo "FUENTE B (ADR-004):"
grep -A10 "opcion A:" 00_INICIO/ADR-004-estructura-destino.md

echo "REALIDAD (disco):"
ls -d */

echo "¿Coinciden?"
# Si NO → FALLA. No crear. Pedir decisión a Cristóbal.
```

---

## Acción Requerida

**No yo, no en Sesión 2.**  
**Decisión de arquitectura que falta:** Ratificar ADR-004 en CLAUDE.md.

**Próximo paso (Sesión 3+):**
1. ¿Ratificar ADR-004 (Opción A)?
2. ¿Rechazar y volver a 00-10 (Opción B)?
3. Formalizar decisión en CLAUDE.md

**Hasta entonces:** Estructura contradictoria. Yo esperaré decisión.

---

## Por Qué Esto Importa

Spec.md G14: "El material es un curso, no una carpeta"
- Convención numérica = navegabilidad
- Pero ADR-004 dice que los módulos modernos (gestión, herramientas, tests) NO se numeran
- CLAUDE.md debería reflejar esto

Si no está formalizado, ocurre lo que pasó: Yo creo en lo que está escrito (CLAUDE.md), violo lo que está implementado (ADR-004), y la estructura se vuelve contradictoria.

---

**Conclusión:** No es mi falla verificar convención. Es defecto arquitectónico: ADR-004 se implementó sin actualizar CLAUDE.md.

**Sesión 3 debe decidir:** ¿Ratificar o rechazar ADR-004?

Yo respetaré decisión. Pero necesita formalizarse en CLAUDE.md para que sea auditable.
