/* Validación E2E real: los viajes del usuario en Chromium headless.
 *
 * Variables de entorno:
 *   BASE       URL del servidor (default http://127.0.0.1:8377)
 *   SLUG       curso a abrir (default compania)
 *   CHROME     binario de Chromium (default: cache de Playwright)
 *   HEADLESS   "0" para ver el navegador (default 1)
 *
 * Salida: un línea "VIAJE ok/fallo: <nombre>" por viaje y exit code != 0
 * si algún viaje falla. Comportamiento, no strings: cada aserción toca la
 * página como la tocaría una persona.
 */
import { chromium } from 'playwright-core';

const BASE = process.env.BASE || 'http://127.0.0.1:8377';
const SLUG = process.env.SLUG || 'compania';
const CHROME = process.env.CHROME
  || `${process.env.HOME}/.cache/ms-playwright/chromium-1248/chrome-linux64/chrome`;
const HEADLESS = process.env.HEADLESS !== '0';
const URL_ = `${BASE}/chat.html?curso=${encodeURIComponent(SLUG)}`;

const fallos = [];
const ok = (nombre, cond, detalle = '') => {
  console.log(`VIAJE ${cond ? 'ok  ' : 'FALLO'}: ${nombre}${detalle ? ' — ' + detalle : ''}`);
  if (!cond) fallos.push(nombre);
};

const navegador = await chromium.launch({ executablePath: CHROME, headless: HEADLESS });
const pagina = await navegador.newPage({ viewport: { width: 1280, height: 900 } });
const errores = [];
pagina.on('pageerror', e => errores.push(e.message));

try {
  // ---- viaje 1: la página abre y el compañero toma la iniciativa ----------
  await pagina.goto(URL_, { waitUntil: 'networkidle', timeout: 30000 });
  await pagina.waitForTimeout(2500);
  const titulo = (await pagina.textContent('#titulo')) || '';
  ok('pagina carga con nombre del curso', titulo.trim().length > 3, titulo.slice(0, 40));
  const bienvenida = await pagina.waitForSelector('#mensajes .tutor',
    { timeout: 15000 }).catch(() => null);
  ok('saludo de apertura visible', !!bienvenida);

  // ---- viaje 2: escribir y recibir respuesta ------------------------------
  await pagina.click('#texto');
  await pagina.fill('#texto', 'Hola, ¿me escuchas?');
  await pagina.click('#enviar');
  const huboRespuesta = await pagina.waitForFunction(
    () => {
      const els = document.querySelectorAll('#mensajes .tutor');
      const u = els[els.length - 1];
      return u && u.textContent.trim().length > 3 && !/thinking|pensando/i.test(u.textContent);
    },
    { timeout: 60000 },
  ).then(() => true).catch(() => false);
  const respuesta = await pagina.$$eval('#mensajes .tutor',
    els => els.at(-1)?.textContent.trim() || '');
  ok('respuesta del tutor tras escribir', huboRespuesta, respuesta.slice(0, 60));
  ok('respuesta no es eco del mensaje',
    respuesta.toLowerCase() !== 'hola, ¿me escuchas?');

  // ---- viaje 3: el micrófono existe y está habilitado ---------------------
  const voz = await pagina.textContent('#voz').catch(() => null);
  const deshab = await pagina.getAttribute('#voz', 'disabled').catch(() => null);
  ok('boton de voz habilitado', !!voz && deshab === null, (voz || '').slice(0, 40));

  // ---- viaje 4: los caminos de compañía están a un click ------------------
  for (const [sel, nombre] of [['#recordar', 'recordar juntos'],
    ['#btn-biografia', 'mi historia de vida'], ['#btn-taller', 'aprender paso a paso']]) {
    const visible = await pagina.isVisible(sel).catch(() => false);
    ok(`boton visible: ${nombre}`, visible);
  }

  // ---- viaje 5: recordar juntos responde con una pista --------------------
  const antes = (await pagina.$$('#mensajes .tutor')).length;
  await pagina.click('#recordar');
  const pista = await pagina.waitForFunction(
    (n) => {
      const els = document.querySelectorAll('#mensajes .tutor');
      const u = els[els.length - 1];
      return els.length > n && u && u.textContent.trim().length >= 10;
    },
    antes,
    { timeout: 30000 },
  ).then(() => true).catch(() => false);
  ok('recordar juntos entrega una pista', pista);

  // ---- el script de la página está vivo (sin SyntaxError) ------------------
  ok('sin errores de pagina (JS vivo)', errores.length === 0,
    errores.join(' | ').slice(0, 120));

  await pagina.screenshot({ path: new URL('./ultima-corrida.png', import.meta.url).pathname });
} finally {
  await navegador.close();
}

console.log(fallos.length ? `\n${fallos.length} viaje(s) fallaron` : '\ntodos los viajes ok');
process.exit(fallos.length ? 1 : 0);
