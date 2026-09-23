"use strict";

// Los algoritmos del árbol se ejecutan en Python. Aquí solo se dibujan
// los resultados y se controla la reproducción de los recorridos.
const $ = (id) => document.getElementById(id);
const SVG_NS = "http://www.w3.org/2000/svg";
const reglas = {
  inorden: "Izquierda → raíz → derecha. Los valores quedan ordenados.",
  preorden: "Raíz → izquierda → derecha. Se visita primero cada padre.",
  postorden: "Izquierda → derecha → raíz. Se visita cada padre al final.",
  niveles: "Nivel por nivel, de izquierda a derecha. Utiliza una cola (BFS).",
};
let datos = JSON.parse($("datos-iniciales").textContent);
let recorrido = "inorden";
let posicion = 0;
let temporizador = null;
let ocupado = false;
let zoom = 1;
let accionConfirmada = null;

function svgElemento(nombre, atributos, texto) {
  const elemento = document.createElementNS(SVG_NS, nombre);
  Object.entries(atributos).forEach(([clave, valor]) => {
    elemento.setAttribute(clave, valor);
  });
  if (texto !== undefined) elemento.textContent = texto;
  return elemento;
}

function detener() {
  if (temporizador !== null) clearInterval(temporizador);
  temporizador = null;
  $("reproducir").textContent = "Reproducir";
}

function destacar(camino = [], actual = null) {
  document.querySelectorAll(".nodo").forEach((nodo) => {
    const valor = Number(nodo.dataset.valor);
    nodo.classList.toggle("visitado", camino.includes(valor));
    nodo.classList.toggle("actual", valor === actual);
  });
  document.querySelectorAll(".arista").forEach((enlace) => {
    const desde = Number(enlace.dataset.desde);
    const hasta = Number(enlace.dataset.hasta);
    enlace.classList.toggle("visitada", camino.some((v, i) => (
      v === desde && camino[i + 1] === hasta
    )));
  });
}

function ajustarZoom(encajar = false) {
  const grafico = datos.grafico;
  if (encajar) zoom = Math.min(1, $("lienzo").clientWidth / grafico.ancho);
  const svg = $("diagrama");
  svg.style.width = `${grafico.ancho * zoom}px`;
  svg.style.height = `${grafico.alto * zoom}px`;
  if (encajar) {
    $("lienzo").scrollLeft = 0;
    $("lienzo").scrollTop = 0;
  }
}

function dibujar() {
  const { nodos, enlaces, ancho, alto } = datos.grafico;
  $("nodos").replaceChildren();
  $("enlaces").replaceChildren();
  $("diagrama").setAttribute("viewBox", `0 0 ${ancho} ${alto}`);
  $("diagrama").toggleAttribute("hidden", nodos.length === 0);
  $("vacio").hidden = nodos.length > 0;
  const posiciones = new Map(nodos.map((nodo) => [nodo.valor, nodo]));
  enlaces.forEach((enlace) => {
    const padre = posiciones.get(enlace.desde);
    const hijo = posiciones.get(enlace.hasta);
    const linea = svgElemento("line", {
      class: "arista", x1: padre.x, y1: padre.y,
      x2: hijo.x, y2: hijo.y,
      "data-desde": enlace.desde, "data-hasta": enlace.hasta,
    });
    const letra = svgElemento("text", {
      class: "lado", x: (padre.x + hijo.x) / 2 + (enlace.lado === "I" ? -9 : 9),
      y: (padre.y + hijo.y) / 2 - 5,
    }, enlace.lado);
    $("enlaces").append(linea, letra);
  });
  nodos.forEach((nodo) => {
    const grupo = svgElemento("g", {
      class: "nodo", "data-valor": nodo.valor,
      transform: `translate(${nodo.x},${nodo.y})`,
    });
    grupo.append(
      svgElemento("title", {}, `${nodo.valor}, nivel ${nodo.nivel}${nodo.hoja ? ", hoja" : ""}`),
      svgElemento("circle", { r: 25 }),
      svgElemento("text", {}, nodo.valor),
    );
    $("nodos").append(grupo);
  });
  $("diagrama-titulo").textContent = `Árbol de ${nodos.length} nodos. Raíz: ${datos.resumen.raiz ?? "vacía"}.`;
  ajustarZoom(true);
}

function actualizarRecorrido() {
  detener();
  posicion = 0;
  $("secuencia").replaceChildren();
  const secuencia = datos.recorridos[recorrido];
  if (secuencia.length === 0) {
    const aviso = document.createElement("span");
    aviso.className = "sin-valores";
    aviso.textContent = "Inserta valores para obtener un recorrido.";
    $("secuencia").append(aviso);
  } else {
    secuencia.forEach((valor) => {
      const ficha = document.createElement("span");
      ficha.textContent = valor;
      $("secuencia").append(ficha);
    });
  }
  $("regla-recorrido").textContent = reglas[recorrido];
  $("paso-actual").textContent = `0 / ${secuencia.length}`;
  document.querySelectorAll("[data-recorrido]").forEach((boton) => {
    boton.setAttribute("aria-pressed", String(boton.dataset.recorrido === recorrido));
  });
  destacar();
  habilitar();
}

function habilitar() {
  document.querySelectorAll("button, input").forEach((elemento) => {
    elemento.disabled = ocupado;
  });
  if (!ocupado) {
    const vacio = datos.resumen.vacio;
    ["abrir-vaciar", "alejar", "acercar", "encajar", "reproducir", "paso", "reiniciar"].forEach((id) => {
      $(id).disabled = vacio;
    });
  }
}

function actualizar(nuevos) {
  datos = nuevos;
  ["cantidad", "altura", "hojas", "amplitud", "raiz", "minimo", "maximo"].forEach((clave) => {
    $(clave).textContent = datos.resumen[clave] ?? "—";
  });
  $("balance").textContent = datos.resumen.vacio ? "Árbol vacío"
    : (datos.resumen.balanceado ? "Balanceado" : "Sin balancear");
  dibujar();
  actualizarRecorrido();
}

function notificar(mensaje, detalle = "", error = false) {
  $("mensaje").textContent = mensaje;
  $("camino").textContent = detalle;
  $("resultado").classList.toggle("error", error);
  document.querySelector(".resultado-icono").textContent = error ? "!" : "✓";
}

async function operar(accion, entrada = {}) {
  if (ocupado) return;
  ocupado = true;
  detener();
  habilitar();
  try {
    const respuesta = await fetch("/api/operar", {
      method: "POST",
      headers: { "Content-Type": "application/json", "X-CSRF-Token": datos.csrf },
      body: JSON.stringify({ accion, ...entrada }),
    });
    const resultado = await respuesta.json();
    if (!respuesta.ok) throw new Error(resultado.error || "No se pudo realizar la operación.");
    actualizar(resultado);
    destacar(resultado.camino, resultado.destacado);
    const ruta = resultado.camino.length ? `Camino examinado: ${resultado.camino.join(" → ")}` : "Las consultas y recorridos se actualizaron.";
    notificar(resultado.mensaje, ruta, resultado.encontrado === false);
    if (accion === "insertar") $("valores").value = "";
  } catch (error) {
    const mensaje = error instanceof TypeError
      ? "No se pudo conectar. Comprueba que Flask siga abierto en PowerShell."
      : error.message;
    notificar(mensaje, "El árbol mostrado conserva el último resultado recibido.", true);
  } finally {
    ocupado = false;
    habilitar();
  }
}

function avanzar() {
  const secuencia = datos.recorridos[recorrido];
  if (!secuencia.length) return;
  if (posicion >= secuencia.length) posicion = 0;
  posicion += 1;
  const visitados = secuencia.slice(0, posicion);
  destacar(visitados, secuencia[posicion - 1]);
  [...$("secuencia").children].forEach((ficha, indice) => {
    ficha.classList.toggle("visto", indice < posicion);
    ficha.classList.toggle("activo", indice === posicion - 1);
  });
  $("paso-actual").textContent = `${posicion} / ${secuencia.length}`;
  if (posicion === secuencia.length) detener();
}

function confirmar(accion) {
  if (datos.resumen.vacio) {
    operar(accion);
    return;
  }
  accionConfirmada = accion;
  const ejemplo = accion === "ejemplo";
  $("titulo-confirmacion").textContent = ejemplo ? "¿Cargar el ejemplo?" : "¿Vaciar el árbol?";
  $("texto-confirmacion").textContent = ejemplo
    ? "El ejemplo reemplazará los valores del árbol actual."
    : "Se quitarán todos los valores del árbol actual.";
  $("confirmar-accion").textContent = ejemplo ? "Cargar ejemplo" : "Vaciar árbol";
  $("confirmar").showModal();
}

$("form-insertar").addEventListener("submit", (evento) => {
  evento.preventDefault();
  operar("insertar", { valores: $("valores").value });
});
$("form-consultar").addEventListener("submit", (evento) => {
  evento.preventDefault();
  operar(evento.submitter?.value || "buscar", { valor: Number($("valor").value) });
});
document.querySelectorAll("[data-consulta]").forEach((boton) => {
  boton.addEventListener("click", () => operar(boton.dataset.consulta));
});
document.querySelectorAll("[data-recorrido]").forEach((boton) => {
  boton.addEventListener("click", () => {
    recorrido = boton.dataset.recorrido;
    actualizarRecorrido();
  });
});
$("reproducir").addEventListener("click", () => {
  if (temporizador !== null) {
    detener();
    return;
  }
  avanzar();
  if (posicion < datos.recorridos[recorrido].length) {
    temporizador = setInterval(avanzar, 700);
    $("reproducir").textContent = "Pausar";
  }
});
$("paso").addEventListener("click", () => { detener(); avanzar(); });
$("reiniciar").addEventListener("click", actualizarRecorrido);
$("cargar-ejemplo").addEventListener("click", () => confirmar("ejemplo"));
$("abrir-vaciar").addEventListener("click", () => confirmar("vaciar"));
$("cancelar").addEventListener("click", () => $("confirmar").close());
$("confirmar-accion").addEventListener("click", () => {
  $("confirmar").close();
  operar(accionConfirmada);
});
$("encajar").addEventListener("click", () => ajustarZoom(true));
$("acercar").addEventListener("click", () => { zoom = Math.min(2, zoom * 1.25); ajustarZoom(); });
$("alejar").addEventListener("click", () => { zoom = Math.max(0.1, zoom / 1.25); ajustarZoom(); });
window.addEventListener("resize", () => ajustarZoom(true));
actualizar(datos);
