# Despliegue: maci.c4a.cl

Verificado el 2026-09-27: `/` responde 307 hacia la portada; 23 páginas y 30 recursos responden 200; 0 enlaces o anclas rotos.

## Cómo funciona

```
push a main (GitHub cherrera0001/MACI)
  → Vercel, proyecto "maci" (prj_lLD3lhsfxwbQFI1Q0fQB8twAunVe)
  → build: node 03_SCRIPTS/publicar_sitio.mjs   (arma public/)
  → publica solo public/
  → maci.c4a.cl (CNAME en Cloudflare → d01ed64b4defd5f7.vercel-dns-017.com)
```

`publicar_sitio.mjs` copia con la misma estructura relativa de `07_DATITO/`, así los enlaces entre carpetas siguen valiendo:

| Se publica | No se publica |
|---|---|
| `01_CONCEPTOS/visual/` (sin la plantilla) | YAML de datos (`clases`, `progreso`, `dudas`…) |
| `02_REFERENCIA/clase6_regresion.html` | transcripciones de `05_CLASES` |
| `04_EJERCICIOS/*.html`, `assets/`, `guias/`, `cuadernillos/` | `04_EJERCICIOS/entregas/`, `09_PERSONAL`, resto del repo |

Un enlace a algo que no se publica se convierte en texto con la leyenda «Disponible en la copia local del repositorio». En línea no hay 404.

## Rutas

| URL | Destino |
|---|---|
| `/` | 307 → `/01_CONCEPTOS/visual/00_index.html` |
| `/03_eda.html` (y toda `/NN_*.html`) | 308 → `/01_CONCEPTOS/visual/03_eda.html` |
| `/certamen_1.html`, `/triaje_de_problemas.html` | 308 → `/04_EJERCICIOS/…` |

Cabeceras: `X-Content-Type-Options: nosniff` y `Referrer-Policy: no-referrer`. Vercel agrega HSTS.

## Verificar

```bash
node 03_SCRIPTS/publicar_sitio.mjs                            # arma public/ en local
python -m unittest discover -s 04_CODIGO -p "test_*.py"       # incluye "sitio publicado sin enlaces rotos"
curl -sI https://maci.c4a.cl/ | head -3                       # 307 hacia la portada
curl -s -o /dev/null -w '%{http_code}\n' https://maci.c4a.cl/07_DATITO/progreso.yaml   # 404
```

## Volver atrás

Vercel guarda cada despliegue: se puede promover uno anterior desde el panel del proyecto, o hacer `git revert` del commit y `push`.

## Aviso

El repositorio de GitHub es **público**. Lo que no se publica en maci.c4a.cl sigue visible en GitHub: config, progreso y archivos personales. Para ocultarlo hay que hacer el repo privado; Vercel sigue desplegando igual.
