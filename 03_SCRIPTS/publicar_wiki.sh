#!/usr/bin/env bash
# Publica docs/wiki/ en la wiki de GitHub. La wiki queda igual que la carpeta.
#
#   bash 03_SCRIPTS/publicar_wiki.sh
#
# Requisito de una sola vez: GitHub no crea el repositorio de la wiki hasta que
# alguien guarda la primera página desde la web
# (https://github.com/cherrera0001/MACI/wiki → «Create the first page» → Save).
set -euo pipefail

RAIZ="$(cd "$(dirname "$0")/.." && pwd)"
REPO="cherrera0001/MACI"
TOKEN="$(grep -E '^GITHUB_TOKEN_CLASIC=' "$RAIZ/.env" | cut -d= -f2- | tr -d '\r"')"
[ -n "$TOKEN" ] || { echo "Falta GITHUB_TOKEN_CLASIC en .env" >&2; exit 1; }

# El token viaja en una cabecera, nunca en la URL del remoto.
AUTH="Authorization: Basic $(printf 'x-access-token:%s' "$TOKEN" | base64 -w0)"
git_wiki() { git -c credential.helper= -c http.extraHeader="$AUTH" "$@"; }

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

if ! git_wiki clone -q "https://github.com/$REPO.wiki.git" "$TMP/wiki" 2>/dev/null; then
  echo "La wiki aún no existe. Guarda la primera página en https://github.com/$REPO/wiki y vuelve a correr." >&2
  exit 2
fi

find "$TMP/wiki" -maxdepth 1 -name '*.md' -delete
cp "$RAIZ"/docs/wiki/*.md "$TMP/wiki/"
cd "$TMP/wiki"
git add -A
if git diff --cached --quiet; then
  echo "La wiki ya está al día."
  exit 0
fi
git -c user.name="$(git -C "$RAIZ" config user.name)" -c user.email="$(git -C "$RAIZ" config user.email)" \
  commit -q -m "Wiki desde docs/wiki ($(git -C "$RAIZ" rev-parse --short HEAD))"
git_wiki push -q origin HEAD
echo "Publicado: https://github.com/$REPO/wiki"
