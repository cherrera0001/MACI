/* datito:nucleo:v2 — fuente: 03_SCRIPTS/plantillas/nucleo_v2.js (no editar la copia embebida;
   correr 03_SCRIPTS/sincronizar_nucleo.py). REQ-TUT-012, 013, 014, 017.

   Marcado que entiende:
     <div class="predice" data-predice="p1"> ... <textarea></textarea> <button>Registrar</button></div>
         predicción escrita; desbloquea todo [data-requiere="p1"]
     <div data-requiere="p1"> ... </div>            controles bloqueados hasta predecir
     <details class="nivel" data-nivel="1|2">       nivel de abstracción; el 2 arranca cerrado
     <div class="intento" data-intento="q1"><textarea></textarea></div>
     <details class="resp" data-intento="q1">       se abre tras el intento, o con .pedir
     <button class="pedir" data-intento="q1">       "dame la respuesta" (G11): abre y lo registra
     [data-enlace="k"]                              hover ilumina todos los [data-enlace="k"]
     <pre id="datito-export"></pre>                 bloque DATITO-EVENTOS para pegar en el chat
   API: Datito.observa(id, texto), Datito.evento(tipo, datos), Datito.desbloqueado(id)
*/
(function () {
  "use strict";
  var MIN = 3;
  var pagina = (location.pathname.split("/").pop() || "visual").replace(/\.html$/, "");
  var CLAVE = "datito:v2:" + pagina;
  var estado = { pred: {}, intentos: {}, pedidas: {}, eventos: [] };

  function cargar() {
    try {
      var s = JSON.parse(localStorage.getItem(CLAVE) || "null");
      if (s && s.eventos) estado = s;
    } catch (e) { /* sin almacenamiento: la página funciona igual */ }
  }
  function guardar() {
    try { localStorage.setItem(CLAVE, JSON.stringify(estado)); } catch (e) { /* idem */ }
  }
  function todos(sel, raiz) { return Array.prototype.slice.call((raiz || document).querySelectorAll(sel)); }

  function evento(tipo, datos) {
    var ev = { tipo: tipo, pagina: pagina, ts: new Date().toISOString().slice(0, 19) };
    for (var k in datos) if (Object.prototype.hasOwnProperty.call(datos, k)) ev[k] = datos[k];
    estado.eventos.push(ev);
    if (estado.eventos.length > 60) estado.eventos.shift();
    guardar();
    pintarExport();
    return ev;
  }

  function exportar() {
    var lineas = ["DATITO-EVENTOS v1 · " + pagina];
    estado.eventos.forEach(function (e) {
      var r = {};
      for (var k in e) if (k !== "pagina") r[k] = e[k];
      lineas.push(JSON.stringify(r));
    });
    return lineas.join("\n");
  }
  function pintarExport() {
    var pre = document.getElementById("datito-export");
    if (pre) pre.textContent = estado.eventos.length ? exportar() : "(todavía no registras nada en esta página)";
  }

  function desbloqueado(id) { return !!estado.pred[id]; }

  function aplicarCandados() {
    todos("[data-requiere]").forEach(function (el) {
      var ok = el.getAttribute("data-requiere").split(/\s+/).every(desbloqueado);
      el.classList.toggle("bloqueado", !ok);
      todos("input, select, button, textarea", el).forEach(function (c) { c.disabled = !ok; });
      if (el.tagName === "DETAILS" && !ok) el.open = false;
    });
    todos(".predice[data-predice]").forEach(function (box) {
      var id = box.getAttribute("data-predice");
      if (estado.pred[id]) {
        box.classList.add("hecha");
        var ta = box.querySelector("textarea");
        if (ta) { ta.value = estado.pred[id]; ta.readOnly = true; }
      }
    });
  }

  function intentoHecho(id) { return !!(estado.intentos[id] || estado.pedidas[id]); }

  function iniciar() {
    cargar();

    todos(".predice[data-predice]").forEach(function (box) {
      var id = box.getAttribute("data-predice");
      var ta = box.querySelector("textarea");
      var b = box.querySelector("button");
      if (!b || !ta) return;
      b.addEventListener("click", function () {
        var v = ta.value.trim();
        if (v.length < MIN) { ta.focus(); box.classList.add("falta"); return; }
        box.classList.remove("falta");
        if (!estado.pred[id]) { estado.pred[id] = v; evento("prediccion", { id: id, texto: v }); }
        aplicarCandados();
      });
    });

    todos(".intento[data-intento] textarea").forEach(function (ta) {
      var id = ta.closest(".intento").getAttribute("data-intento");
      if (estado.intentos[id]) ta.value = estado.intentos[id];
      ta.addEventListener("change", function () {
        var v = ta.value.trim();
        if (v.length >= MIN && v !== estado.intentos[id]) {
          estado.intentos[id] = v;
          evento("intento", { id: id, texto: v });
        }
      });
    });

    todos("details.resp[data-intento]").forEach(function (d) {
      var id = d.getAttribute("data-intento");
      d.addEventListener("toggle", function () {
        if (d.open && !intentoHecho(id)) {
          d.open = false;
          var aviso = d.parentNode.querySelector('.aviso-intento[data-intento="' + id + '"]');
          if (!aviso) {
            aviso = document.createElement("p");
            aviso.className = "aviso-intento";
            aviso.setAttribute("data-intento", id);
            aviso.textContent = "Primero escribe tu intento arriba, o pide la respuesta.";
            d.parentNode.insertBefore(aviso, d);
          }
        } else if (d.open) {
          var a = d.parentNode.querySelector('.aviso-intento[data-intento="' + id + '"]');
          if (a) a.remove();
        }
      });
    });

    todos("button.pedir[data-intento]").forEach(function (b) {
      var id = b.getAttribute("data-intento");
      b.addEventListener("click", function () {
        if (!estado.pedidas[id]) { estado.pedidas[id] = true; evento("pidio_respuesta", { id: id }); }
        var d = document.querySelector('details.resp[data-intento="' + id + '"]');
        if (d) d.open = true;
      });
    });

    todos('details.nivel[data-nivel="2"]').forEach(function (d) { d.open = false; });
    todos("details.nivel").forEach(function (d) {
      d.addEventListener("toggle", function () {
        if (d.open) evento("nivel", { id: d.id || "", nivel: +d.getAttribute("data-nivel") });
      });
    });

    // delegado: sirve tambien para elementos que el lab crea despues
    function enlace(e, on) {
      var el = e.target && e.target.closest ? e.target.closest("[data-enlace]") : null;
      if (!el) return;
      var k = el.getAttribute("data-enlace");
      todos('[data-enlace="' + k + '"]').forEach(function (x) { x.classList.toggle("enlazado", on); });
    }
    document.addEventListener("mouseover", function (e) { enlace(e, true); });
    document.addEventListener("mouseout", function (e) { enlace(e, false); });
    document.addEventListener("focusin", function (e) { enlace(e, true); });
    document.addEventListener("focusout", function (e) { enlace(e, false); });

    var copiar = document.getElementById("datito-copiar");
    if (copiar) copiar.addEventListener("click", function () {
      var txt = exportar();
      try { navigator.clipboard.writeText(txt); copiar.textContent = "Copiado: pégalo en el chat con Datito"; }
      catch (e) { copiar.textContent = "Selecciona el bloque y cópialo a mano"; }
    });
    var borrar = document.getElementById("datito-borrar");
    if (borrar) borrar.addEventListener("click", function () {
      estado = { pred: {}, intentos: {}, pedidas: {}, eventos: [] };
      guardar();
      location.reload();
    });

    aplicarCandados();
    pintarExport();
  }

  window.Datito = {
    evento: evento,
    observa: function (id, texto) { return evento("observacion", { id: id, texto: String(texto) }); },
    desbloqueado: desbloqueado,
    exportar: exportar,
    alCambiar: aplicarCandados
  };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", iniciar);
  else iniciar();
})();
