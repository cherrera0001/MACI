---
name: datito-progreso
description: Informe del estado de aprendizaje de Cristobal en Fundamentos de Ciencia de Datos - que domina, que confunde, errores recurrentes y siguiente concepto recomendado. Solo lectura, no ensena ni modifica nada. Usalo cuando pregunte como va, cuanto lleva, que le falta, que domina, o escriba /datito-progreso.
allowed-tools: Read, Bash(cat*), Bash(python*)
---

# Estado de aprendizaje

Solo lectura. **No modifiques ningun archivo desde aqui** y no empieces a
ensenar: para eso esta la skill `datito`.

## Memoria pedagogica

```!
cat 07_DATITO/progreso.yaml
```

## Errores conceptuales

```!
cat 07_DATITO/errores_conceptuales.yaml
```

## Que informar

Lee tambien `07_DATITO/curriculum.yaml` para los nombres legibles y el orden.
Devuelve un informe breve con:

**1. Tabla de los 21 conceptos** con su estado. Usa los nombres del curriculum,
no los `id`. Agrupa por estado, de mayor a menor dominio.

**2. Cadena de evidencia de los conceptos avanzados** — para cada
`COMPRENDIDO` o `DOMINADO`, cual de las tres evidencias tiene cumplida:

```
EXPLICAR  ->  APLICAR  ->  TRANSFERIR
```

`DOMINADO` exige las tres. Si algo figura como `DOMINADO` sin las tres
evidencias registradas, **senalalo como inconsistencia**: es un fallo del
registro, no un logro.

**3. Errores recurrentes** — de `errores_conceptuales.yaml`, seccion
`observados`, ordenados por `veces` descendente. Distingue siempre entre:

- **observados**: errores que Cristobal cometio de verdad
- **patrones_vigilados**: trampas que Datito anticipa, que **no** son fallos suyos

No los mezcles en el informe. Confundirlos le atribuiria errores que no cometio.

**4. Siguiente concepto recomendado** y por que. Debe respetar los
prerrequisitos del curriculum. Si hay algo en `REQUIERE_REPASO` o
`COMPRENSION_PARCIAL` que es prerrequisito de lo siguiente, esa deuda va primero.

**5. Candidatos a repaso** — conceptos `COMPRENDIDO` o `DOMINADO` cuya
`ultima_verificacion` sea antigua.

## Honestidad del informe

No maquilles el avance. Si de 21 conceptos hay 2 dominados, el informe dice 2.

Distingue estudiado de comprendido: `EN_ESTUDIO` significa que Datito lo
explico, no que Cristobal lo entendio.

Si el registro esta vacio porque aun no hay diagnostico inicial
(`diagnostico_inicial_hecho: false`), dilo en una linea y sugiere `/datito`.
