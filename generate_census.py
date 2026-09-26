import subprocess
import json
from pathlib import Path

html_files = [
    "07_DATITO/01_CONCEPTOS/visual/00_index.html",
    "07_DATITO/01_CONCEPTOS/visual/01_fundamentos.html",
    "07_DATITO/01_CONCEPTOS/visual/02_datos_features_target.html",
    "07_DATITO/01_CONCEPTOS/visual/03_eda.html",
    "07_DATITO/01_CONCEPTOS/visual/04_limpieza_preparacion.html",
    "07_DATITO/01_CONCEPTOS/visual/05_train_validation_test.html",
    "07_DATITO/01_CONCEPTOS/visual/06_validacion_cruzada.html",
    "07_DATITO/01_CONCEPTOS/visual/07_generalizacion.html",
    "07_DATITO/01_CONCEPTOS/visual/08_overfitting_underfitting.html",
    "07_DATITO/01_CONCEPTOS/visual/09_regresion.html",
    "07_DATITO/01_CONCEPTOS/visual/10_clasificacion.html",
    "07_DATITO/01_CONCEPTOS/visual/11_matriz_confusion.html",
    "07_DATITO/01_CONCEPTOS/visual/12_metricas_clasificacion.html",
    "07_DATITO/01_CONCEPTOS/visual/13_roc_auc.html",
    "07_DATITO/01_CONCEPTOS/visual/14_arboles_decision.html",
    "07_DATITO/01_CONCEPTOS/visual/18_redes_neuronales.html",
    "07_DATITO/01_CONCEPTOS/visual/19_deep_learning.html",
    "07_DATITO/02_REFERENCIA/clase6_regresion.html",
    "07_DATITO/03_CASOS_ESTUDIO/cancer_mama/matriz_confusion_dinamica.html",
    "07_DATITO/04_EJERCICIOS/certamen_1.html",
    "07_DATITO/04_EJERCICIOS/certamen_2.html",
    "07_DATITO/04_EJERCICIOS/certamen_3.html",
    "07_DATITO/04_EJERCICIOS/simulador_prediccion_falla.html",
    "07_DATITO/04_EJERCICIOS/triaje_de_problemas.html",
]

with open("07_DATITO/07_BITACORA/learning_loop/census.tsv", "w") as f:
    f.write("path\tscore\tkeep_eligible\tstatus\n")
    for html in html_files:
        try:
            result = subprocess.run(
                ["python", "03_CODIGO/datito_loop_eval.py", "--path", html, "--json"],
                capture_output=True, text=True, timeout=5
            )
            if result.returncode == 0:
                data = json.loads(result.stdout)
                score = data["score"]
                keep = int(data["keep_eligible"])
                status = "PASS" if score == 1.0 else ("PRE" if score >= 0.8 else "BROKEN")
                f.write(f"{html}\t{score}\t{keep}\t{status}\n")
        except Exception as e:
            print(f"Error {html}: {e}")

print("census.tsv created")
