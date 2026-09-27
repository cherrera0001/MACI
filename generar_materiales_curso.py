#!/usr/bin/env python3
"""
A6 · Docente Explicador: Generar PPTX + DOCX + TRAZABILIDAD.md desde clases.yaml
"""

import yaml
import os
from datetime import datetime
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from docx import Document
from docx.shared import Inches as DocInches, Pt as DocPt, RGBColor as DocRGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement


def load_clases():
    """Carga clases.yaml"""
    with open("docs/curso-gestion/clases.yaml", "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data["clases"], data["metadata"]


def set_background_color(slide, color_rgb):
    """Establece color de fondo en un slide"""
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(*color_rgb)


def create_title_slide(prs, titulo, subtitulo):
    """Crea slide de portada"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank layout

    # Fondo azul oscuro
    set_background_color(slide, (25, 50, 100))

    # Título
    title_box = slide.shapes.add_textbox(Inches(0.5), Inches(2), Inches(9), Inches(1.5))
    title_frame = title_box.text_frame
    title_frame.word_wrap = True
    title_para = title_frame.paragraphs[0]
    title_para.text = titulo
    title_para.font.size = Pt(54)
    title_para.font.bold = True
    title_para.font.color.rgb = RGBColor(255, 255, 255)
    title_para.alignment = PP_ALIGN.CENTER

    # Subtítulo
    subtitle_box = slide.shapes.add_textbox(Inches(0.5), Inches(3.8), Inches(9), Inches(1))
    subtitle_frame = subtitle_box.text_frame
    subtitle_para = subtitle_frame.paragraphs[0]
    subtitle_para.text = subtitulo
    subtitle_para.font.size = Pt(28)
    subtitle_para.font.color.rgb = RGBColor(200, 200, 200)
    subtitle_para.alignment = PP_ALIGN.CENTER

    # Fecha
    fecha_box = slide.shapes.add_textbox(Inches(0.5), Inches(5.5), Inches(9), Inches(0.5))
    fecha_frame = fecha_box.text_frame
    fecha_para = fecha_frame.paragraphs[0]
    fecha_para.text = f"Septiembre 27, 2026"
    fecha_para.font.size = Pt(16)
    fecha_para.font.color.rgb = RGBColor(150, 150, 150)
    fecha_para.alignment = PP_ALIGN.CENTER


def add_text_box(slide, left, top, width, height, text, font_size=24, bold=False, color=(0,0,0)):
    """Agrega caja de texto a slide"""
    textbox = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    frame = textbox.text_frame
    frame.word_wrap = True
    para = frame.paragraphs[0]
    para.text = text
    para.font.size = Pt(font_size)
    para.font.bold = bold
    para.font.color.rgb = RGBColor(*color)
    return textbox


def create_clase_slide_1(slide, numero, titulo, objetivo, pregunta):
    """Slide 1: Objetivo + Activación"""
    set_background_color(slide, (245, 245, 250))

    # Encabezado
    header = add_text_box(slide, 0.5, 0.3, 9, 0.6, f"Clase {numero}: {titulo}",
                         font_size=36, bold=True, color=(25, 50, 100))

    # Pregunta de activación (rojo)
    add_text_box(slide, 0.5, 1.2, 9, 0.8, f"❓ {pregunta}",
                font_size=26, bold=True, color=(200, 30, 30))

    # Objetivo
    add_text_box(slide, 0.5, 2.3, 9, 1.2, f"Objetivo:\n{objetivo}",
                font_size=20, color=(60, 60, 60))


def create_clase_slide_2(slide, numero, bloom_nivel, evidencia):
    """Slide 2: Nivel Bloom + Evidencia"""
    set_background_color(slide, (240, 248, 255))

    # Encabezado
    add_text_box(slide, 0.5, 0.3, 9, 0.5, f"Clase {numero}: Nivel Bloom",
                font_size=32, bold=True, color=(25, 50, 100))

    # Nivel Bloom (mapear a colores)
    bloom_colors = {
        "Comprender": (70, 130, 180),
        "Aplicar": (34, 139, 34),
        "Analizar": (218, 165, 32),
        "Evaluar": (220, 20, 60),
        "Crear": (148, 0, 211)
    }
    color = bloom_colors.get(bloom_nivel, (100, 100, 100))

    add_text_box(slide, 1, 1.5, 8, 0.8, f"Nivel: {bloom_nivel}",
                font_size=28, bold=True, color=color)

    # Evidencia
    add_text_box(slide, 0.5, 2.8, 9, 2, f"Evidencia:\n{evidencia}",
                font_size=18, color=(60, 60, 60))


def create_clase_slide_3(slide, numero, practica):
    """Slide 3: Práctica"""
    set_background_color(slide, (255, 250, 240))

    # Encabezado
    add_text_box(slide, 0.5, 0.3, 9, 0.5, f"Clase {numero}: Práctica",
                font_size=32, bold=True, color=(25, 50, 100))

    # Práctica
    add_text_box(slide, 0.5, 1.2, 9, 3.5, f"✋ {practica}",
                font_size=18, color=(40, 40, 40))


def create_navigation_slide(prs, clases):
    """Crea slide final de navegación"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_background_color(slide, (25, 50, 100))

    add_text_box(slide, 0.5, 0.5, 9, 0.8, "Mapa de Navegación del Curso",
                font_size=36, bold=True, color=(255, 255, 255))

    # Listar clases en 2 columnas
    y_start = 1.5
    col_width = 4.5
    items_per_col = 7

    for i, clase in enumerate(clases):
        col = i // items_per_col
        row = i % items_per_col

        x = 0.5 + (col * col_width)
        y = y_start + (row * 0.4)

        texto = f"Clase {clase['numero']}: {clase['concepto']}"
        add_text_box(slide, x, y, col_width - 0.3, 0.35, texto,
                    font_size=14, color=(220, 220, 220))


def generate_pptx(clases, metadata):
    """Genera presentación en PPTX"""
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)

    # Portada
    create_title_slide(prs,
                      metadata["titulo"],
                      "GitHub Projects para MACI")

    # 14 clases × 3 slides
    for clase in clases:
        numero = clase["numero"]
        titulo = clase["concepto"]
        objetivo = clase["objetivo"]
        pregunta = clase["pregunta"]
        bloom = clase["bloom"]
        evidencia = clase["evidencia"]
        practica = clase["practica"]

        # Slide 1: Objetivo + Activación
        slide1 = prs.slides.add_slide(prs.slide_layouts[6])
        create_clase_slide_1(slide1, numero, titulo, objetivo, pregunta)

        # Slide 2: Bloom + Evidencia
        slide2 = prs.slides.add_slide(prs.slide_layouts[6])
        create_clase_slide_2(slide2, numero, bloom, evidencia)

        # Slide 3: Práctica
        slide3 = prs.slides.add_slide(prs.slide_layouts[6])
        create_clase_slide_3(slide3, numero, practica)

    # Mapa de navegación
    create_navigation_slide(prs, clases)

    # Guardar
    output_path = "Curso_Gestion_GitHubProjects.pptx"
    prs.save(output_path)
    print(f"✓ PPTX generado: {output_path} ({len(prs.slides)} slides)")
    return output_path


def generate_docx(clases, metadata):
    """Genera guía de autoestudio en DOCX"""
    doc = Document()

    # Portada
    title = doc.add_paragraph()
    title_run = title.add_run(metadata["titulo"])
    title_run.font.size = DocPt(36)
    title_run.font.bold = True
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    subtitle = doc.add_paragraph("Guía de Autoestudio")
    subtitle_run = subtitle.runs[0]
    subtitle_run.font.size = DocPt(24)
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.add_paragraph()

    metadata_para = doc.add_paragraph(f"Versión: {metadata['version']} | {metadata['fecha_diseño']}")
    metadata_para.alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.add_page_break()

    # Índice (manual)
    doc.add_heading("Índice", level=1)
    for clase in clases:
        doc.add_paragraph(f"Clase {clase['numero']}: {clase['concepto']}", style="List Number")

    doc.add_page_break()

    # 14 capítulos
    for clase in clases:
        numero = clase["numero"]
        titulo = clase["concepto"]
        objetivo = clase["objetivo"]
        pregunta = clase["pregunta"]
        bloom = clase["bloom"]
        evidencia = clase["evidencia"]
        practica = clase["practica"]
        prerequisitos = clase["prerequisitos"]
        habilita = clase["habilita"]
        tiempo = clase["tiempo_minutos"]

        # Encabezado de clase
        heading = doc.add_heading(f"Clase {numero}: {titulo}", level=1)

        # Metadata
        meta_para = doc.add_paragraph()
        meta_para.add_run("Duración: ").bold = True
        meta_para.add_run(f"{tiempo} min | ")
        meta_para.add_run("Nivel Bloom: ").bold = True
        meta_para.add_run(f"{bloom}\n")

        # Objetivo
        doc.add_heading("Objetivo", level=2)
        doc.add_paragraph(objetivo)

        # Pregunta de activación
        doc.add_heading("Pregunta Activadora", level=2)
        doc.add_paragraph(pregunta)

        # Práctica
        doc.add_heading("Práctica", level=2)
        doc.add_paragraph(practica)

        # Evidencia
        doc.add_heading("Evidencia Esperada", level=2)
        doc.add_paragraph(evidencia)

        # Prerequisitos
        if prerequisitos:
            doc.add_heading("Prerequisitos", level=2)
            prereq_text = ", ".join([f"Clase {p}" for p in prerequisitos])
            doc.add_paragraph(prereq_text)

        # Habilita
        if habilita:
            doc.add_heading("Habilita", level=2)
            habilita_text = ", ".join([f"Clase {h}" for h in habilita])
            doc.add_paragraph(habilita_text)

        doc.add_page_break()

    # Glosario
    doc.add_heading("Glosario: Términos de GitHub Projects", level=1)

    glossary_terms = {
        "Epic": "Un gran resultado o iniciativa que agrupa varias historias. Ejemplo: E-3 (Curso confiable)",
        "Historia": "Descripción de una característica desde la perspectiva del usuario. Formato: H-N",
        "Tarea": "Unidad de trabajo concreta de 1-8 horas. Formato: T-N.N.N",
        "Issue": "Registro en GitHub Projects que representa trabajo, bug o tarea.",
        "Criterios de Aceptación": "Condiciones verificables usando formato Dado/Cuando/Entonces",
        "DoD (Definition of Done)": "Checklist que define cuándo un trabajo está completamente terminado",
        "Sub-issue": "Descomposición de una tarea en pequeños pasos (<1 hora cada uno)",
        "WIP (Work In Progress)": "Límite de tareas simultáneas en un tablero para mantener flujo",
        "Throughput": "Cantidad de trabajo completado por unidad de tiempo",
        "Cycle Time": "Tiempo desde que inicia hasta que se completa una tarea",
        "ADR": "Architecture Decision Record: documento que justifica decisiones técnicas",
        "INVEST": "Criterios para historias: Independiente, Negociable, Valiosa, Estimable, Pequeña, Verificable"
    }

    for term, definition in glossary_terms.items():
        p = doc.add_paragraph(style="List Bullet")
        p.add_run(term).bold = True
        p.add_run(f": {definition}")

    doc.add_page_break()

    # Anexo: Mapa conceptual (Bloom progression)
    doc.add_heading("Anexo: Progresión de Bloom", level=1)

    bloom_progression = {
        "Comprender": ["Clase 1: Proyecto y problema", "Clase 2: Spec y constitución", "Clase 10: Roles y ceremonias"],
        "Aplicar": ["Clase 3: Épica", "Clase 4: Historia", "Clase 5: Criterios de aceptación",
                    "Clase 6: Issue y etiquetas", "Clase 11: Iteraciones e hitos", "Clase 12: Automatización"],
        "Analizar": ["Clase 7: Tarea y sub-issue", "Clase 9: Tablero y límite WIP"],
        "Evaluar": ["Clase 8: Definición de Terminado", "Clase 13: Métricas e Insights"],
        "Crear": ["Clase 14: ADR, deuda y retrospectiva"]
    }

    for nivel, clases_en_nivel in bloom_progression.items():
        doc.add_heading(nivel, level=2)
        for clase_info in clases_en_nivel:
            doc.add_paragraph(clase_info, style="List Bullet")

    # Guardar
    output_path = "Guia_Autoestudio_Gestion_GitHubProjects.docx"
    doc.save(output_path)
    print(f"✓ DOCX generado: {output_path}")
    return output_path


def generate_trazabilidad(clases):
    """Genera TRAZABILIDAD.md"""
    md = "# Trazabilidad: Clases → Issues → Materiales\n\n"
    md += "Mapeo de cada clase a su issue correspondiente, slides en PPTX y capítulo en DOCX.\n\n"
    md += "## Tabla de Trazabilidad\n\n"

    md += "| Clase | Concepto | Issue | Slides PPTX | Capítulo DOCX | Bloom |\n"
    md += "|-------|----------|-------|-------------|---------------|---------|\n"

    for clase in clases:
        numero = clase["numero"]
        concepto = clase["concepto"]

        # Mapeo de issue (convención)
        if numero <= 3:
            issue = f"E-{numero}" if numero == 3 else f"H-{numero}"
        else:
            issue = f"H-{numero}"

        # Slides: portada=1, clase 1 inicia en slide 2 (1+3*0+2)
        slide_start = 2 + (numero - 1) * 3
        slide_end = slide_start + 2

        # Capítulo
        capitulo = numero

        bloom = clase["bloom"]

        md += f"| {numero} | {concepto} | `{issue}` | {slide_start}-{slide_end} | {capitulo} | {bloom} |\n"

    md += "\n## Notas\n\n"
    md += "- **Portada (Slide 1)**: Información del curso\n"
    md += "- **Slides 2-43**: 14 clases × 3 slides (objetivo+activación, Bloom+evidencia, práctica)\n"
    md += "- **Slide 44**: Mapa de navegación\n"
    md += "- **Issues**: Convención E-N (épicas) y H-N (historias). Completar en GitHub Projects.\n"
    md += "- **Capítulos DOCX**: Numerados 1-14, uno por clase, con índice automático en portada.\n\n"

    md += "## Progresión de Bloom\n\n"
    md += "```\nComprender (1,2,10)\n  ↓\nAplicar (3,4,5,6,11,12)\n  ↓\nAnalizar (7,9)\n  ↓\nEvaluar (8,13)\n  ↓\nCrear (14)\n```\n"

    output_path = "docs/curso-gestion/TRAZABILIDAD.md"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"✓ TRAZABILIDAD.md generado: {output_path}")
    return output_path


def main():
    """Función principal"""
    print("🔧 A6 · Docente Explicador: Generando materiales del curso...\n")

    # Cargar datos
    clases, metadata = load_clases()
    print(f"✓ Cargadas {len(clases)} clases desde clases.yaml\n")

    # Generar PPTX
    print("📊 Generando PPTX...")
    pptx_path = generate_pptx(clases, metadata)

    # Generar DOCX
    print("📖 Generando DOCX...")
    docx_path = generate_docx(clases, metadata)

    # Generar TRAZABILIDAD
    print("🔗 Generando TRAZABILIDAD.md...")
    traz_path = generate_trazabilidad(clases)

    print("\n✅ F5 COMPLETADO: Todos los materiales generados")
    print(f"   - {pptx_path}")
    print(f"   - {docx_path}")
    print(f"   - {traz_path}")


if __name__ == "__main__":
    main()
