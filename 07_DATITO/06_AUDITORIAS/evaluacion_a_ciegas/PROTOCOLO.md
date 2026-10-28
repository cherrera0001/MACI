# Protocolo de evaluación a ciegas (REQ-TUT-004)

**Propósito:** medir aprendizaje, no uso. El auto-registro del tutor dice qué se
le explicó; solo un desempeño **sin asistencia del tutor** dice qué aprendió.
Diseño alineado con la evidencia externa (Bastani et al., PNAS 2025): practicar
con IA sube el desempeño *con* IA; el examen sin IA es la prueba honesta.

## Reglas

1. **Sin tutor:** durante la evaluación el alumno no usa Datito ni ningún LLM.
   Papel y lápiz, como el certamen real (`datito.config.yaml` → evaluación).
2. **Sin aviso de fecha:** se acuerda la ventana (semana de práctica), no el día
   exacto, para medir retención y no preparación dirigida.
3. **Corrección con criterio del profesor:** se corrige con `/datito-corregir`
   *después* de rendida cada prueba; la corrección no cuenta como evidencia de
   dominio (spec §3: acertar tras recibir la respuesta no es evidencia).
4. **Dos mediciones por concepto clave:** al inicio del bloque (pre) y a las
   ~3 semanas (post). El delta es la señal; una sola medición no dice nada.
5. **Consentimiento previo** (Clarify 6): el alumno acepta este protocolo como
   parte del método. Sin consentimiento, esta carpeta queda vacía.

## Flujo

1. Elegir el instrumento en `07_DATITO/04_EJERCICIOS/certamenes/` (hay certámenes
   sin solución; usar las versiones de práctica, no las del curso rendido).
2. **Pre:** el alumno lo rinde a ciegas. Registrar puntaje y detalle en
   `mediciones.csv`.
3. Corregir con `/datito-corregir`; registrar las dudas (quedan en `dudas.yaml`
   con estado `practica` u `abierta`, sin tocar `progreso.yaml`).
4. Entrenar el período normal con el tutor.
5. **Post:** a las ~3 semanas, instrumento equivalente (mismo formato, distinta
   versión). Registrar.
6. Comparar en `mediciones.csv`: delta por concepto. Alimentar el resultado a
   `progreso.yaml` solo si hay evidencia de las 4 cadenas (spec §3).

## Qué NO es

- No es evidencia de `APLICAR`/`TRANSFERIR` por sí solo: es medición externa
  del aprendizaje. Las evidencias siguen exigiendo producción del alumno.
- No es benchmark del tutor: compara al alumno contra sí mismo en el tiempo.
