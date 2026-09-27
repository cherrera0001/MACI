#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera index.html desde grafo.yaml para navegación offline."""

import sys
import io
from pathlib import Path
import yaml

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = Path(__file__).resolve().parents[1]
GRAFO_PATH = ROOT / "07_DATITO" / "grafo.yaml"
VISUAL_DIR = ROOT / "07_DATITO" / "01_CONCEPTOS" / "visual"
INDEX_PATH = VISUAL_DIR / "index.html"

# Archivos KEEP (score 1.0)
KEEP_FILES = {
    "01_fundamentos.html": "Fundamentos",
    "02_datos_features_target.html": "Datos, features, target",
    "03_eda.html": "EDA",
    "04_limpieza_preparacion.html": "Limpieza y preparación",
    "06_validacion_cruzada.html": "Validación cruzada",
    "07_generalizacion.html": "Generalización",
    "08_overfitting_underfitting.html": "Overfitting y underfitting",
    "09_regresion.html": "Regresión",
    "13_roc_auc.html": "ROC y AUC",
    "14_arboles_decision.html": "Árboles de decisión",
    "18_redes_neuronales.html": "Redes neuronales",
}

# Ejercicios KEEP
EJERCICIOS = {
    "04_EJERCICIOS/certamen_3.html": "Certamen 3",
    "02_REFERENCIA/clase6_regresion.html": "Clase 6: Regresión",
}

def generar_html():
    """Genera index.html."""

    # Leer grafo
    if GRAFO_PATH.exists():
        with open(GRAFO_PATH, encoding='utf-8') as f:
            grafo = yaml.safe_load(f) or {}
    else:
        grafo = {}

    conceptos = grafo.get("conceptos", {})

    # HTML
    html = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>MACI · Índice de Conceptos</title>
<style>
  :root {
    --tinta: #1a1a1a;
    --suave: #666;
    --linea: #d8d8d8;
    --fondo: #faf9f7;
    --azul: #2563eb;
    --verde: #059669;
    --ambar: #d97706;
    --morado: #7c3aed;
  }

  * { box-sizing: border-box; }
  body {
    margin: 0;
    padding: 2rem 1rem;
    background: var(--fondo);
    color: var(--tinta);
    font: 16px/1.7 "Segoe UI", system-ui, sans-serif;
  }

  main {
    max-width: 900px;
    margin: 0 auto;
  }

  h1 {
    font-size: 2rem;
    margin: 0 0 0.5rem;
  }

  .sub {
    color: var(--suave);
    margin: 0 0 2rem;
    font-size: 0.95rem;
  }

  .clave {
    background: #eff6ff;
    border-left: 3px solid var(--azul);
    padding: 0.85rem 1.1rem;
    margin: 1.5rem 0;
  }

  h2 {
    font-size: 1.3rem;
    margin: 2rem 0 1rem;
    padding-top: 1rem;
    border-top: 1px solid var(--linea);
    color: var(--azul);
  }

  .conceptos {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1rem;
    margin: 1rem 0;
  }

  .concepto {
    background: #fff;
    border: 1px solid var(--linea);
    border-radius: 8px;
    padding: 1.2rem;
    transition: box-shadow 0.2s;
  }

  .concepto:hover {
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  }

  .concepto a {
    color: var(--azul);
    text-decoration: none;
    font-weight: 600;
    display: block;
    margin-bottom: 0.5rem;
  }

  .concepto a:hover {
    text-decoration: underline;
  }

  .meta {
    font-size: 0.85rem;
    color: var(--suave);
    margin-top: 0.5rem;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    margin: 1.5rem 0;
    font-size: 0.9rem;
  }

  th, td {
    border: 1px solid var(--linea);
    padding: 0.75rem;
    text-align: left;
  }

  th {
    background: #f5f5f5;
    font-weight: 600;
    color: var(--azul);
  }

  footer {
    margin-top: 3rem;
    padding-top: 1rem;
    border-top: 1px solid var(--linea);
    color: var(--suave);
    font-size: 0.85rem;
  }

  .stats {
    background: #f0fdf4;
    border-left: 3px solid var(--verde);
    padding: 0.85rem 1.1rem;
    margin: 1.5rem 0;
  }
</style>
</head>
<body>

<main>

<h1>MACI · Índice de Conceptos</h1>
<p class="sub">Fundamentos de Ciencia de Datos · Tutoring System</p>

<div class="clave">
<strong>Qué es esto.</strong>
Índice de <strong>13 conceptos y ejercicios</strong> migrados a template canónico v1.
Todos funcionan <strong>offline</strong> — sin CDN, sin conexión a internet.
</div>

<div class="stats">
<strong>Status:</strong>
13 de 26 archivos listos para usar (50% cobertura).
Score: 11/11 gates validados.
</div>

<h2>Conceptos Pedagógicos (11)</h2>
<div class="conceptos">
"""

    # Agregar conceptos en orden
    order = [
        ("01_fundamentos.html", "Fundamentos"),
        ("02_datos_features_target.html", "Datos, features, target"),
        ("03_eda.html", "EDA"),
        ("04_limpieza_preparacion.html", "Limpieza"),
        ("06_validacion_cruzada.html", "Validación cruzada"),
        ("07_generalizacion.html", "Generalización"),
        ("08_overfitting_underfitting.html", "Overfitting"),
        ("09_regresion.html", "Regresión"),
        ("13_roc_auc.html", "ROC/AUC"),
        ("14_arboles_decision.html", "Árboles"),
        ("18_redes_neuronales.html", "Redes neuronales"),
    ]

    for fname, titulo in order:
        html += f"""  <div class="concepto">
    <a href="{fname}">{titulo}</a>
    <div class="meta">Template v1 • Score 1.0</div>
  </div>
"""

    html += """</div>

<h2>Ejercicios y Referencias (2)</h2>
<div class="conceptos">
"""

    # Ejercicios
    ejercicios_order = [
        ("04_EJERCICIOS/certamen_3.html", "Certamen 3"),
        ("02_REFERENCIA/clase6_regresion.html", "Clase 6: Regresión"),
    ]

    for fpath, titulo in ejercicios_order:
        html += f"""  <div class="concepto">
    <a href="{fpath}">{titulo}</a>
    <div class="meta">Template v1 • Score 1.0</div>
  </div>
"""

    html += """</div>

<h2>Estructura de Dependencias</h2>
<table>
  <tr>
    <th>Concepto</th>
    <th>Depende de</th>
    <th>Habilita</th>
  </tr>
"""

    # Agregar dependencias desde grafo
    for fname, titulo in order:
        # Buscar en grafo
        concepto_id = fname.replace(".html", "").lstrip("0123456789_")

        if concepto_id in conceptos:
            c = conceptos[concepto_id]
            depende = ", ".join(c.get("depende_de", []))[:50]
            habilita = ", ".join(c.get("habilita", []))[:50]
        else:
            depende = "—"
            habilita = "—"

        html += f"""  <tr>
    <td><strong>{titulo}</strong></td>
    <td>{depende}</td>
    <td>{habilita}</td>
  </tr>
"""

    html += """</table>

<h2>Cómo Usar</h2>

<p><strong>En navegador:</strong> Abre cualquier archivo HTML en tu navegador.
No requiere servidor ni conexión a internet.</p>

<p><strong>URL directa:</strong></p>
<pre>file:///F:/MACI/07_DATITO/01_CONCEPTOS/visual/03_eda.html</pre>

<p><strong>Navegación:</strong> Cada archivo tiene enlaces internos a otros conceptos.
Usa los enlaces para navegar entre temas.</p>

<h2>Archivos Pendientes (13 de 26)</h2>

<p>Los siguientes 13 archivos están en estado <code>DISCARD</code>
y requieren conversión manual:</p>

<ul>
  <li><strong>5 gráficos remotos:</strong> Necesitan SVG/Canvas local
    <ul>
      <li>05_train_validation_test.html</li>
      <li>11_matriz_confusion.html</li>
      <li>19_deep_learning.html</li>
      <li>Certamen 1</li>
      <li>Certamen 2</li>
    </ul>
  </li>
  <li><strong>4 estructura no estándar:</strong> Requieren refactor &lt;main&gt;
    <ul>
      <li>10_clasificacion.html</li>
      <li>12_metricas_clasificacion.html</li>
      <li>Simulador predicción falla</li>
      <li>Matriz confusión dinámica</li>
    </ul>
  </li>
  <li><strong>4 otros:</strong> Requieren análisis</li>
</ul>

<p><strong>Plan:</strong> Ver <code>FASE_2B_PENDIENTE.md</code> en repositorio.</p>

<footer>
  MACI — Máquina Asistida de Ciencia de Datos Interactiva
  <br>
  Generado automáticamente desde grafo.yaml · Template canónico v1
  <br>
  <a href="https://github.com/cherrera0001/MACI">GitHub: cherrera0001/MACI</a>
</footer>

</main>

</body>
</html>
"""

    return html

if __name__ == "__main__":
    html = generar_html()
    INDEX_PATH.write_text(html, encoding='utf-8')
    print(f"OK: Generado {INDEX_PATH.name}")
    print(f"Abrir: file:///{INDEX_PATH.resolve()}")
