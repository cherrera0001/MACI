# Suite E2E del chat — validación con navegador real

Los tests unitarios verifican el servidor; **estos viajes verifican lo que una
persona ve**. Nacieron del bug real del SyntaxError que mataba la página:
ninguna prueba de strings lo detectó, un navegador sí.

## Qué valida (`validar.mjs`)

1. La página abre con el nombre del curso y el saludo de apertura aparece.
2. Escribir y enviar produce una respuesta del tutor (que no es eco).
3. El botón de voz existe y está **habilitado** (regresión del race).
4. Los caminos de compañía (recordar, biografía, taller) están visibles.
5. «Recordar juntos» responde con una pista.
6. Cero errores de página (el JS está vivo).

## Puesta en marcha (máquina de desarrollo)

```bash
cd tests/e2e
npm install            # playwright-core (no descarga navegadores)
./setup-chrome-libs.sh # dependencias del Chromium SIN root (Ubuntu/Debian)
cd .. && pytest test_e2e_navegador.py -q
```

Sin node/chromium el test se omite (skip) y no frena CI. Contra el servidor
real en marcha también se puede correr a mano:

```bash
BASE=http://127.0.0.1:8377 SLUG=compania \
LD_LIBRARY_PATH=$PWD/root/usr/lib/x86_64-linux-gnu node validar.mjs
```

Genera `ultima-corrida.png` para revisión visual.
