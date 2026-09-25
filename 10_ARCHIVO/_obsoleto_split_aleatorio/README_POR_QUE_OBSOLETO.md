# OBSOLETO — no usar para el Hito 2

Estos archivos se generaron ANTES de leer la guía del curso y contienen:

1. Un split aleatorio 80/20 (viola la instrucción del Proyecto 3: entrenar con 2016, evaluar en 2017).
2. Cifras que NO fueron calculadas (p. ej. "brecha Train-Test 0.8263/0.8226", "R² 0.7842", los "%" de importancia
   del HTML y del informe de justificación). Fueron escritas a mano antes de ejecutar código.
3. Una conclusión ("Gradient Boosting es el mejor") basada en (1) y (2).

El análisis válido y reproducible está en F:\MACI\:
  - modelamiento_temporal.py  -> resultados_temporal.json      (train 2016 / test 2017, baseline->lineal->árbol->ensambles, 5 semillas)
  - bootstrap_comparacion.py  -> comparacion_estadistica.json  (bootstrap pareado, error por segmento, importancia por permutación)
  - dashai_driver.py          -> dashai_resultados.json        (misma partición replicada en DashAI)
  - INFORME_MODELO_FCD_P3.md  -> informe final con la justificación del modelo
