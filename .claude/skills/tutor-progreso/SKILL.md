---
name: tutor-progreso
description: Muestra el estado de aprendizaje de Ciencia de Datos de Cristobal - que domina, que confunde, errores frecuentes y cual es el siguiente concepto recomendado. Solo lectura, no ensena ni modifica nada. Usalo cuando pregunte como va, que le falta, que domina, o escriba /tutor-progreso.
allowed-tools: Read, Bash(cat*), Bash(python*)
---

# Estado de aprendizaje

Solo lectura. **No modifiques `progreso.yaml` desde aqui** y no empieces a
ensenar: para eso esta la skill `tutor`.

## Registro actual

```!
cat 07_TUTOR/progreso.yaml
```

## Que mostrar

Lee tambien `07_TUTOR/curriculum.yaml` para los nombres legibles y el orden, y
devuelve un informe breve con:

**1. Una tabla de los 21 conceptos** con estado y nivel. Usa los nombres del
curriculum, no los `id`.

**2. Dominados** — con la fecha en que se verifico cada uno. Recuerda que
`dominado` exige las dos evidencias: explicacion propia y ejercicio nuevo
resuelto sin ayuda.

**3. En duda** — y para cada uno, la confusion concreta registrada, no una
descripcion vaga.

**4. Errores transversales** — patrones que aparecen en mas de un concepto. Es
la seccion mas util del informe: un error que se repite en tres conceptos
distintos no es un despiste, es un modelo mental equivocado.

**5. Siguiente concepto recomendado** — y la razon. Debe respetar los
prerrequisitos del curriculum; si hay algo `en_duda` que es prerrequisito de lo
siguiente, esa deuda va primero.

**6. Conceptos `dominado` sin verificar hace tiempo** — candidatos a repaso.

## Honestidad del informe

No maquilles el avance. Si de 21 conceptos hay 2 dominados, el informe dice 2.
Distingue siempre entre estudiado y comprendido: `en_curso` significa que se
explico, no que se entendio.

Si el registro esta vacio porque aun no hay diagnostico inicial
(`diagnostico_inicial_hecho: false`), dilo en una linea y sugiere ejecutar
`/tutor` para hacerlo.
