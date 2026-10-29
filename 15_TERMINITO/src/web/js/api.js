/* api.js — cliente minimo de la API local (contracts/api.md) */
const API = "";

async function api(ruta, opciones = {}) {
  const r = await fetch(API + ruta, {
    headers: opciones.body && !(opciones.body instanceof Blob)
      ? { "Content-Type": "application/json" } : {},
    ...opciones,
  });
  const datos = await r.json().catch(() => ({}));
  if (!r.ok) throw Object.assign(new Error(datos.detalle || datos.error || r.status), {
    codigo: datos.error, status: r.status, datos,
  });
  return datos;
}

const get = (ruta) => api(ruta);
const post = (ruta, cuerpo) => api(ruta, { method: "POST", body: JSON.stringify(cuerpo || {}) });
const putBlob = (ruta, blob) => api(ruta, { method: "PUT", body: blob });

function slugDe(texto) {
  return texto.normalize("NFD").replace(/[̀-ͯ]/g, "")
    .toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "")
    .slice(0, 40).replace(/-$/, "") || "mi-datito";
}

/* barra superior con estado del motor */
async function pintarEstado() {
  try {
    const s = await get("/api/salud");
    document.querySelectorAll(".estado-motor").forEach(el => {
      el.innerHTML = s.modo === "tutor"
        ? '<span class="pill tutor">' + t("pill_tutor") + " · " + s.version_modelo + "</span>"
        : '<span class="pill exploracion">' + t("pill_exploracion") + "</span>";
    });
    pintarGuia(s);
    return s;
  } catch {
    document.querySelectorAll(".estado-motor").forEach(el => {
      el.innerHTML = '<span class="pill exploracion">' + t("pill_caido") + "</span>";
    });
    return null;
  }
}

/* guía de instalación de Ollama (decisión D-7.1 «guiado»): aparece en todas
   las páginas cuando no hay LLM; se cierra por sesión de navegador y vuelve
   a comprobarse en cada carga (si instalaste Ollama, desaparece sola). */
function pintarGuia(s) {
  document.getElementById("guia-ollama")?.remove();
  if (!s || !s.guia) return;
  if (localStorage.getItem("datito-guia-ollama") === s.guia.so) return;
  const div = document.createElement("div");
  div.id = "guia-ollama";
  div.className = "nota";
  div.style.cssText = "max-width:52rem;margin:.6rem auto;padding:.7rem 1rem";
  div.innerHTML = `<b>${esc(t("guia_t"))}</b> ${esc(t("guia_instala"))}
    <ol style="margin:.35rem 0 .2rem">${s.guia.pasos.map(p =>
      `<li><code>${esc(p)}</code></li>`).join("")}</ol>
    <span class="sub">${esc(t("guia_reinicia"))}</span>
    <button class="boton alt" id="guia-cerrar"
      style="padding:.2rem .6rem;font-size:.8rem;margin-left:.6rem">${esc(t("guia_cerrar"))}</button>`;
  document.querySelector("main")?.prepend(div);
  document.getElementById("guia-cerrar").onclick = () => {
    localStorage.setItem("datito-guia-ollama", s.guia.so);
    div.remove();
  };
}

function esc(texto) {
  return String(texto ?? "").replace(/[&<>"']/g,
    c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}
