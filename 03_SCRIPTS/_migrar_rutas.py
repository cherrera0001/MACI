"""Reescribe las rutas de los scripts tras la reestructuracion del repositorio.

Se ejecuto una sola vez (15-09-2026). Se conserva como registro auditable del
cambio: cada reemplazo esta declarado y el script imprime que toco.

    python _migrar_rutas.py
"""
import glob
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# (patron, reemplazo). Orden significativo: primero rutas absolutas, luego relativas.
REEMPLAZOS = [
    # --- carpeta del proyecto del curso ---
    (r"F:\MACI\Fundamentos de ciencia de datos", r"F:\MACI\02_PROYECTO_FCD"),
    ("Fundamentos de ciencia de datos/Hito1", "02_PROYECTO_FCD/Hito1"),

    # --- datos ---
    (r"F:\MACI\housing_dashai_2016_2017.csv", r"F:\MACI\04_DATOS\housing_dashai_2016_2017.csv"),

    # --- resultados (rutas absolutas) ---
    (r"F:\MACI\resultados_temporal.json", r"F:\MACI\05_RESULTADOS\resultados_temporal.json"),
    (r"F:\MACI\comparacion_estadistica.json", r"F:\MACI\05_RESULTADOS\comparacion_estadistica.json"),
    (r"F:\MACI\predicciones_2017.csv", r"F:\MACI\05_RESULTADOS\predicciones_2017.csv"),
    (r"F:\MACI\auditoria_dashai_vs_crudo.json", r"F:\MACI\05_RESULTADOS\auditoria_dashai_vs_crudo.json"),
    (r"F:\MACI\correlacion_dashai.json", r"F:\MACI\05_RESULTADOS\correlacion_dashai.json"),
    (r"F:\MACI\dashai_resultados.json", r"F:\MACI\05_RESULTADOS\dashai_resultados.json"),
    (r"F:\MACI\dashai_split_indices.json", r"F:\MACI\05_RESULTADOS\dashai_split_indices.json"),
    (r"F:\MACI\dashai_state.json", r"F:\MACI\05_RESULTADOS\dashai_state.json"),
    # variantes con backslash escapado en literales de Python
    (r"F:\\MACI\\correlacion_dashai.json", r"F:\\MACI\\05_RESULTADOS\\correlacion_dashai.json"),
    (r"F:\\MACI\\resultados_temporal.json", r"F:\\MACI\\05_RESULTADOS\\resultados_temporal.json"),
    (r"F:\\MACI\\viz_", r"F:\\MACI\\06_ENTREGABLES\\visualizaciones\\viz_"),

    # --- resultados (nombres relativos, scripts con os.chdir a la raiz) ---
    ('"resultados_temporal.json"', '"05_RESULTADOS/resultados_temporal.json"'),
    ('"comparacion_estadistica.json"', '"05_RESULTADOS/comparacion_estadistica.json"'),
    ('"dashai_resultados.json"', '"05_RESULTADOS/dashai_resultados.json"'),
    ('"dashai_state.json"', '"05_RESULTADOS/dashai_state.json"'),
    ('"correlacion_dashai.json"', '"05_RESULTADOS/correlacion_dashai.json"'),

    # --- entregables ---
    ('"INFORME_MODELO_FCD_P3.md"', '"06_ENTREGABLES/INFORME_MODELO_FCD_P3.md"'),
    ('"PITCH_HITO2_REVISION.md"', '"06_ENTREGABLES/PITCH_HITO2_REVISION.md"'),
    ('"Pitch_Hito2_v2.pptx"', '"06_ENTREGABLES/Pitch_Hito2_v2.pptx"'),
]


def main():
    total = 0
    for ruta in sorted(glob.glob(os.path.join(HERE, "*.py"))):
        nombre = os.path.basename(ruta)
        if nombre.startswith("_migrar_rutas"):
            continue
        with open(ruta, encoding="utf-8") as fh:
            original = fh.read()
        texto = original
        tocados = []
        for patron, destino in REEMPLAZOS:
            if patron in texto:
                n = texto.count(patron)
                texto = texto.replace(patron, destino)
                tocados.append(f"{n}x {patron}")
        if texto != original:
            with open(ruta, "w", encoding="utf-8") as fh:
                fh.write(texto)
            total += 1
            print(f"[OK] {nombre}")
            for t in tocados:
                print(f"       {t}")
        else:
            print(f"[--] {nombre}  (sin rutas que migrar)")
    print(f"\nArchivos modificados: {total}")


if __name__ == "__main__":
    main()
