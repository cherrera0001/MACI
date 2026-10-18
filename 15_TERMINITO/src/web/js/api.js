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
    .slice(0, 40).replace(/-$/, "") || "mi-termito";
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
    return s;
  } catch {
    document.querySelectorAll(".estado-motor").forEach(el => {
      el.innerHTML = '<span class="pill exploracion">' + t("pill_caido") + "</span>";
    });
    return null;
  }
}

function esc(texto) {
  return String(texto ?? "").replace(/[&<>"']/g,
    c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}
