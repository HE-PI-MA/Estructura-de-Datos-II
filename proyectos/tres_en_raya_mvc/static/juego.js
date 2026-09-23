const token = JSON.parse(document.querySelector('#token').textContent);
let datos = JSON.parse(document.querySelector('#datos').textContent);
let ocupado = false;
const botones = [...document.querySelectorAll('.casilla')];
function dibujar() {
  botones.forEach((b, i) => {
    b.textContent = datos.tablero[i];
    b.dataset.ficha = datos.tablero[i];
    b.disabled = ocupado || !!datos.resultado || !!datos.tablero[i];
    b.setAttribute('aria-label', `Fila ${Math.floor(i/3)+1}, columna ${i%3+1}: ${datos.tablero[i] || 'vacía'}`);
  });
  document.querySelector('#estado').textContent = ocupado ? 'Analizando…' : datos.resultado === 'empate' ? '¡Empate! Puedes jugar otra partida.' : datos.resultado ? (datos.resultado === 'X' ? '¡Ganaste!' : 'La computadora ganó.') : 'Tu turno: elige una casilla.';
  document.querySelector('#reiniciar').disabled = ocupado;
  document.querySelector('#comparar').disabled = ocupado;
  document.querySelector('#algoritmo').disabled = ocupado;
}
async function enviar(ruta, cuerpo = {}) {
  const r = await fetch(ruta, {method:'POST',headers:{'Content-Type':'application/json','X-CSRF-Token':token},body:JSON.stringify(cuerpo)});
  const respuesta = await r.json();
  if (!r.ok) throw new Error(respuesta.error || 'No se pudo completar la acción.');
  return respuesta;
}
async function accion(fn) {
  if (ocupado) return;
  ocupado = true; document.querySelector('#error').textContent = ''; dibujar();
  try { await fn(); } catch(e) { document.querySelector('#error').textContent = e.message; }
  finally { ocupado = false; dibujar(); }
}
botones.forEach(b => b.addEventListener('click', () => accion(async () => {
  datos = await enviar('/jugar', {casilla:Number(b.dataset.i),algoritmo:document.querySelector('#algoritmo').value});
  document.querySelector('#estados').textContent = datos.analisis?.estados ?? '—';
  document.querySelector('#cortes').textContent = datos.analisis?.cortes ?? '—';
})));
document.querySelector('#reiniciar').onclick = () => accion(async () => {
  datos = await enviar('/reiniciar');
  document.querySelector('#estados').textContent = '—'; document.querySelector('#cortes').textContent = '—';
});
document.querySelector('#comparar').onclick = () => accion(async () => {
  const r = await enviar('/comparar');
  const destino = document.querySelector('#comparacion'); destino.replaceChildren();
  const tabla = document.createElement('table');
  for (const fila of [['Algoritmo','Estados','Cortes'],['Minimax',r.minimax.estados,r.minimax.cortes],['Alfa-beta',r.alfa_beta.estados,r.alfa_beta.cortes]]) {
    const tr = document.createElement('tr');
    fila.forEach(v => {const td=document.createElement(tabla.rows.length ? 'td':'th');td.textContent=v;tr.append(td);});tabla.append(tr);
  }
  destino.append(tabla);
  const p=document.createElement('p');p.textContent=`Jugada elegida: casilla ${r.minimax.casilla+1} con Minimax y ${r.alfa_beta.casilla+1} con poda (numeradas del 1 al 9).`;destino.append(p);
});
dibujar();
