#!/usr/bin/env bash
# Dependencias de sistema del Chromium de Playwright SIN root:
# descarga los .deb y los extrae locales; correr con
#   LD_LIBRARY_PATH=$PWD/root/usr/lib/x86_64-linux-gnu node validar.mjs
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p debs root
cd debs
apt-get download libnspr4 libnss3 libasound2t64
cd ..
for d in debs/*.deb; do dpkg-deb -x "$d" root; done
echo "listo: LD_LIBRARY_PATH=$PWD/root/usr/lib/x86_64-linux-gnu"
