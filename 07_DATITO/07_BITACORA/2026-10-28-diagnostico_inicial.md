# Sesión 4 — Diagnóstico inicial (demo)

**Fecha:** 2026-10-28
**Conceptos:** los 21 de `curriculum.yaml`
**Modo:** instrucción explícita «responde tú mismo emulando un estudiante que no conoce nada» (G11: se obedece). Demo: alumno simulado.
**Estado al cerrar:** `train_validation_test` → `REQUIERE_REPASO` · `overfitting_underfitting` → `REQUIERE_REPASO` · resto sin cambio

**Preguntas con espera real:** 21/21 — banco fijo, una pregunta por concepto, sin pistas
**Respuestas antes de 2 intentos:** 0
**Dudas registradas:** ninguna

---

## Qué pidió

Correr el diagnóstico inicial con las 21 `pregunta_diagnostico` del banco fijo, con un alumno que no conoce nada.

## Qué se le dio

Las 21 preguntas, sin reformular y sin pistas. No se corrigió en la sesión: el diagnóstico solo registra.

## Evidencia

8 «no sé», 9 errores conceptuales, 2 intuiciones vagas, 1 intuición parcial y 1 evasiva. Respuesta por concepto en `progreso.yaml` → `diagnostico`. Ninguna respuesta cumple un paso de la cadena de evidencia. Hubo dos re-verificaciones fallidas: eligió el 81 % del split aleatorio y no supo qué es sobreajustar.

## Siguiente paso

Repasar `train_validation_test` (split temporal frente a aleatorio) y después `overfitting_underfitting`.
