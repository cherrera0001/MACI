# Prueba de transferencia — Logística de última milla

> **Datos sintéticos.** No son reales. El proceso generador está en
> `generar_dataset.py` y queda disponible para auditar el ejercicio **después**
> de que respondas, no antes.

---

## El encargo

Una empresa de distribución del Gran Concepción quiere **predecir cuántas horas
tardará una entrega** en el momento en que se despacha el pedido, para poder
comprometer una ventana horaria con el cliente.

Tienes dos archivos:

| Archivo | Filas | Período |
|---|---|---|
| `entregas_2024.csv` | 1.200 | año 2024 |
| `entregas_2025.csv` | 1.400 | año 2025 |

La empresa opera hoy, en 2026, y quiere saber si el modelo le va a servir.

---

## Diccionario de datos

| Columna | Tipo | Qué es | Cuándo se registra |
|---|---|---|---|
| `id_entrega` | texto | Identificador único | Al crear el pedido |
| `fecha` | fecha | Fecha del despacho | Al despachar |
| `comuna_destino` | categórica | Comuna de entrega | Al crear el pedido |
| `tipo_vehiculo` | categórica | `moto`, `furgon`, `camion_ligero` | Al asignar la ruta |
| `distancia_km` | numérica | Distancia estimada al destino | Al asignar la ruta |
| `peso_kg` | numérica | Peso total de la carga | Al cargar el vehículo |
| `n_paquetes` | numérica | Cantidad de paquetes | Al cargar el vehículo |
| `hora_salida` | numérica | Hora de salida (6 a 19) | Al despachar |
| `score_gps_ruta` | numérica | Índice de calidad de ruta del sistema GPS de a bordo, de 0 a 1 | Al iniciar el trayecto |
| `costo_combustible_clp` | numérica | Combustible consumido en la entrega | **Al cierre de la entrega** |
| `horas_entrega` | numérica | **TARGET.** Horas transcurridas hasta la entrega | Al cierre de la entrega |

---

## Lo que ya sabes de los datos

Números verificables, sácalos tú mismo si quieres:

```
2024:  1.200 filas | 12 comunas | score_gps_ruta faltante  0,0 %
2025:  1.400 filas | 20 comunas | score_gps_ruta faltante 36,3 %
```

Ocho de las veinte comunas de 2025 no aparecen en 2024. La empresa amplió su
zona de cobertura hacia el sur de la región ese año.

La media de `horas_entrega` pasó de 0,94 en 2024 a 1,53 en 2025.

---

## Tu tarea

**No entrenes nada todavía. Diseña el experimento.**

Responde estas cuatro cosas:

1. **¿Cómo partes los datos?** Qué usas para entrenar, qué para decidir y qué
   dejas intacto. Con los números concretos.

2. **¿Qué columnas usarías como features y cuáles descartarías?** Para cada
   descarte, di por qué. Mira la columna *"cuándo se registra"* del diccionario
   antes de decidir.

3. **`score_gps_ruta` está completa en 2024 y falta en el 36,3 % de 2025.**
   ¿La incluyes? Si la incluyes, ¿cómo tratas los faltantes? Y sobre todo:
   ¿dónde mides si vale la pena incluirla?

4. **Las 8 comunas nuevas.** ¿Qué le pasa a tu modelo con ellas y qué puedes
   hacer al respecto?

No busques el resultado numérico. Lo que se evalúa es el **diseño** y el
razonamiento detrás de cada decisión.
