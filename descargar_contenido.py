#!/usr/bin/env python3
"""
Script para descargar contenido de Canvas y alumnos.udec.cl

Uso:
  python descargar_contenido.py

Lee credenciales de F:\MACI\.env
Descarga todo a F:\MACI\descargas_udec\
"""

import os
import sys
import json
from pathlib import Path
from dotenv import load_dotenv
import requests
from datetime import datetime

# Cargar .env
env_path = Path(__file__).parent / ".env"
load_dotenv(env_path)

USER_UDEC = os.getenv("User_udec")
PASS_UDEC = os.getenv("Pass_udec")

if not USER_UDEC or not PASS_UDEC:
    print("❌ Error: credenciales no encontradas en .env")
    print("   Asegúrate de que .env tenga:")
    print("   User_udec=...")
    print("   Pass_udec=...")
    sys.exit(1)

# Configuración
BASE_DIR = Path(__file__).parent / "descargas_udec"
BASE_DIR.mkdir(exist_ok=True)

# URLs de Canvas
CANVAS_COURSES = [
    {"id": 80714, "name": "Curso 1"},
    {"id": 83707, "name": "Curso 2"},
    {"id": 80038, "name": "Curso 3"},
    {"id": 80014, "name": "Curso 4"},
    {"id": 83706, "name": "Curso 5"},
    {"id": 83703, "name": "Curso 6"},
]

CANVAS_API = "https://udec.instructure.com/api/v1"
ALUMNOS_URL = "https://alumnos.udec.cl"

print(f"📁 Descargando a: {BASE_DIR}")
print(f"👤 Usuario: {USER_UDEC}")
print("")

# ============================================================================
# PASO 1: Obtener token de Canvas
# ============================================================================
print("⏳ Conectando a Canvas...")
try:
    # Canvas requiere token, no user/pass
    # Para obtenerlo manualmente:
    # 1. Ingresa a https://udec.instructure.com
    # 2. Configuración → Tokens de acceso → Generar nuevo token
    # 3. Cópialo aquí o en un CANVAS_TOKEN en .env

    CANVAS_TOKEN = os.getenv("CANVAS_TOKEN")
    if not CANVAS_TOKEN:
        print("⚠️  Necesitas CANVAS_TOKEN en .env")
        print("   Pasos:")
        print("   1. Ingresa a https://udec.instructure.com")
        print("   2. Configuración → Tokens de acceso")
        print("   3. Genera nuevo token")
        print("   4. Agrega a .env: CANVAS_TOKEN=<tu-token>")
        print("")
        print("   Mientras tanto, descargando de alumnos.udec.cl...")
    else:
        print("✅ Token de Canvas encontrado")
except Exception as e:
    print(f"❌ Error: {e}")

# ============================================================================
# PASO 2: Descargar de alumnos.udec.cl
# ============================================================================
print("")
print("⏳ Ingresando a alumnos.udec.cl...")

session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
})

try:
    # Login
    login_url = f"{ALUMNOS_URL}/user/login"
    payload = {
        "name": USER_UDEC,
        "pass": PASS_UDEC,
        "form_id": "user_login",
        "op": "Log in"
    }

    resp = session.post(login_url, data=payload, allow_redirects=True)
    if "Log out" in resp.text or "Salir" in resp.text:
        print("✅ Login exitoso en alumnos.udec.cl")

        # Descargar página de cursos
        cursos_url = f"{ALUMNOS_URL}/?q=node/5"
        resp = session.get(cursos_url)

        # Guardar HTML
        output_file = BASE_DIR / "alumnos_udec_cursos.html"
        output_file.write_text(resp.text, encoding='utf-8')
        print(f"💾 Guardado: {output_file.relative_to(Path.cwd())}")

    else:
        print("❌ Login fallido en alumnos.udec.cl")

except Exception as e:
    print(f"❌ Error al acceder alumnos.udec.cl: {e}")

# ============================================================================
# PASO 3: Descargar de Canvas (si hay token)
# ============================================================================
if CANVAS_TOKEN:
    print("")
    print("⏳ Descargando de Canvas...")

    headers = {
        "Authorization": f"Bearer {CANVAS_TOKEN}",
        "User-Agent": "Mozilla/5.0"
    }

    for course in CANVAS_COURSES:
        course_id = course["id"]
        course_name = course["name"]
        course_dir = BASE_DIR / f"canvas_curso_{course_id}_{course_name}"
        course_dir.mkdir(exist_ok=True)

        try:
            # Obtener información del curso
            url = f"{CANVAS_API}/courses/{course_id}"
            resp = requests.get(url, headers=headers)
            if resp.status_code == 200:
                course_info = resp.json()
                # Guardar JSON de curso
                (course_dir / "course_info.json").write_text(
                    json.dumps(course_info, indent=2, ensure_ascii=False),
                    encoding='utf-8'
                )
                print(f"✅ Curso {course_id}: {course_info.get('name', course_name)}")

                # Obtener módulos
                url = f"{CANVAS_API}/courses/{course_id}/modules"
                resp = requests.get(url, headers=headers)
                if resp.status_code == 200:
                    modules = resp.json()
                    (course_dir / "modules.json").write_text(
                        json.dumps(modules, indent=2, ensure_ascii=False),
                        encoding='utf-8'
                    )
                    print(f"   └─ {len(modules)} módulos")

            else:
                print(f"❌ Curso {course_id}: Error {resp.status_code}")

        except Exception as e:
            print(f"❌ Curso {course_id}: {e}")

# ============================================================================
# RESUMEN
# ============================================================================
print("")
print("=" * 60)
print(f"✅ Descarga completada en: {BASE_DIR}")
print("")
print("📁 Estructura creada:")
print("   descargas_udec/")
print("   ├── alumnos_udec_cursos.html")
print("   ├── canvas_curso_80714_Curso 1/")
print("   │   ├── course_info.json")
print("   │   └── modules.json")
print("   └── ...")
print("")
print("⚠️  NOTAS:")
print("   • Los archivos grandes deben descargarse manualmente desde Canvas")
print("   • Para videos y documentos: usa opción Descargar en Canvas")
print("   • Los .json contienen referencias a recursos")
print("")
