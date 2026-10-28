# Spec de la wiki (H-6.3, T-6.3.1)

**Propósito (una frase):** que una persona que llega al repo entienda qué es
MACI, cómo se trabaja y cómo opera el tablero — sin preguntar y sin leer el repo.

## Alcance mínimo (7 páginas)

| Página | Qué responde |
|---|---|
| `Home.md` | Qué es MACI, por dónde empezar, links a las demás |
| `Que-es-MACI-y-Datito.md` | Qué es cada pieza (curso, Datito, proyecto, plataforma) |
| `Procesos.md` | Cómo se trabaja: SDD, verificación, learning loop |
| `Como-opera-el-tablero.md` | Cómo leer y mover el Project #3 |
| `Conceptos-de-GitHub-Projects.md` | Épica/historia/tarea, campos, vistas |
| `Pendientes-y-v1.0.md` | Qué falta para v1.0 y cómo se decide |

Más `_Sidebar.md` (navegación lateral de la wiki).

## Reglas

1. **Base mínima:** cada página responde UNA pregunta; si no cabe en una
   pantalla, se divide. Nada de duplicar el README.
2. **Links portables:** entre páginas SIEMPRE con `.md`
   (`[Procesos](Procesos.md)`): funcionan como archivos y en la wiki de GitHub.
3. **Estado fechado:** cada página lleva «Última revisión: AAAA-MM-DD» y el
   verificador de drift (`auditar_drift_documental.py`) la vigila como ruta
   canónica.
4. **Publicación:** la wiki de GitHub exige crear la primera página desde la
   web (github.com/cherrera0001/MACI/wiki → «Create the first page»). Después:
   `bash 03_SCRIPTS/publicar_wiki.sh` (requiere `GITHUB_TOKEN_CLASIC` en `.env`).
5. **Fuente única:** los números del curso salen de `clases.yaml` /
   `curriculum.yaml` (test_cifras_readme.py los vigila también en docs).

**Estado al 2026-10-28:** páginas construidas y con links portables; pendiente
solo el paso web manual (regla 4). Última revisión: 2026-10-28.
