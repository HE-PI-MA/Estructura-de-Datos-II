"""Árbol M-vías de búsqueda sin balanceo, inspirado en la unidad 2."""

from bisect import bisect_left
from collections import deque

if __package__:
    from .nodo_mvias import NodoMVias
else:
    from nodo_mvias import NodoMVias


class ArbolMVias:
    """Mantiene claves comparables y únicas; el orden 2 equivale a un ABB."""

    def __init__(self, orden=4):
        NodoMVias.validar_orden(orden)
        self.__orden = orden
        self.__raiz = None

    def get_orden(self):
        return self.__orden

    def set_orden(self, orden):
        NodoMVias.validar_orden(orden)
        if not self.esta_vacio():
            raise ValueError("Cambiar el orden requiere un árbol vacío")
        self.__orden = orden

    def get_raiz(self):
        return self.__raiz

    def set_raiz(self, nodo):
        """Acepta únicamente una estructura M-vías válida del mismo orden."""
        if nodo is not None and not isinstance(nodo, NodoMVias):
            raise TypeError("La raíz debe ser NodoMVias o None")
        if not self._estructura_valida(nodo):
            raise ValueError("La estructura del árbol M-vías no es válida")
        self.__raiz = nodo

    def raiz(self):
        """Devuelve las claves de la raíz, o [] si el árbol está vacío."""
        return [] if self.esta_vacio() else self.__raiz.get_claves()

    def esta_vacio(self):
        return self.__raiz is None

    def vaciar(self):
        self.__raiz = None

    @staticmethod
    def es_hoja(nodo):
        if nodo is None:
            return False
        if not isinstance(nodo, NodoMVias):
            raise TypeError("Se esperaba un objeto NodoMVias o None")
        return nodo.es_hoja()

    def insertar(self, clave):
        """Devuelve True al insertar y False si la clave ya existe."""
        NodoMVias.validar_clave(clave)
        if self.esta_vacio():
            self.__raiz = NodoMVias(self.__orden, [clave])
            return True
        actual = self.__raiz
        while True:
            claves = actual.get_claves()
            indice = bisect_left(claves, clave)
            if indice < len(claves) and claves[indice] == clave:
                return False
            # Un nodo interno puede quedar incompleto tras una eliminación.
            # Solo llenamos hojas para conservar los rangos de sus hijos.
            if actual.es_hoja() and not actual.esta_lleno():
                claves.insert(indice, clave)
                actual.set_claves(claves)
                return True
            hijo = actual.get_hijo(indice)
            if hijo is None:
                actual.set_hijo(indice, NodoMVias(self.__orden, [clave]))
                return True
            actual = hijo

    def obtener_nodo(self, clave):
        """Devuelve el nodo que contiene la clave, o None."""
        NodoMVias.validar_clave(clave)
        actual = self.__raiz
        while actual is not None:
            claves = actual.get_claves()
            indice = bisect_left(claves, clave)
            if indice < len(claves) and claves[indice] == clave:
                return actual
            actual = actual.get_hijo(indice)
        return None

    def buscar(self, clave):
        """Devuelve un booleano, como buscar() en el ejemplo del ingeniero."""
        return self.obtener_nodo(clave) is not None

    def eliminar(self, clave):
        """Elimina una clave sin reconstruir el árbol; informa si existía."""
        if not self.buscar(clave):
            return False
        self.__raiz = self._eliminar(self.__raiz, clave)
        return True

    def _eliminar(self, nodo, clave):
        claves = nodo.get_claves()
        indice = bisect_left(claves, clave)
        if indice == len(claves) or claves[indice] != clave:
            nodo.set_hijo(
                indice, self._eliminar(nodo.get_hijo(indice), clave)
            )
            return nodo

        izquierdo = nodo.get_hijo(indice)
        derecho = nodo.get_hijo(indice + 1)
        if derecho is not None:
            # El sucesor conserva la separación entre los dos subárboles.
            reemplazo = self._minimo(derecho)
            nodo.set_clave(indice, reemplazo)
            nodo.set_hijo(indice + 1, self._eliminar(derecho, reemplazo))
        elif izquierdo is not None:
            reemplazo = self._maximo(izquierdo)
            nodo.set_clave(indice, reemplazo)
            nodo.set_hijo(indice, self._eliminar(izquierdo, reemplazo))
        else:
            # Ambos rangos adyacentes están vacíos: se juntan en uno vacío.
            claves.pop(indice)
            hijos = nodo.get_hijos()
            hijos.pop(indice + 1)
            nodo.set_claves(claves)
            nodo.set_hijos(hijos)
            if not claves:
                return None
        return nodo

    @staticmethod
    def _minimo(nodo):
        while nodo.get_hijo(0) is not None:
            nodo = nodo.get_hijo(0)
        return nodo.get_clave(0)

    @staticmethod
    def _maximo(nodo):
        while nodo.get_hijo(nodo.cantidad_claves()) is not None:
            nodo = nodo.get_hijo(nodo.cantidad_claves())
        return nodo.get_clave(nodo.cantidad_claves() - 1)

    def minimo(self):
        return None if self.esta_vacio() else self._minimo(self.__raiz)

    def maximo(self):
        return None if self.esta_vacio() else self._maximo(self.__raiz)

    def _nodos_con_nivel(self):
        """Genera pares (nodo, nivel) en amplitud utilizando una cola."""
        if self.esta_vacio():
            return
        pendientes = deque([(self.__raiz, 0)])
        while pendientes:
            nodo, nivel = pendientes.popleft()
            yield nodo, nivel
            for hijo in nodo.get_hijos():
                if hijo is not None:
                    pendientes.append((hijo, nivel + 1))

    def altura(self):
        """Altura en aristas: vacío -1; una sola raíz 0."""
        return max((nivel for _, nivel in self._nodos_con_nivel()), default=-1)

    def cantidad(self):
        """Cantidad de nodos físicos, consistente con Cantidad() del ABB."""
        return sum(1 for _ in self._nodos_con_nivel())

    def cantidad_claves(self):
        return sum(n.cantidad_claves() for n, _ in self._nodos_con_nivel())

    def __len__(self):
        return self.cantidad_claves()

    def cantidad_hojas(self):
        return sum(n.es_hoja() for n, _ in self._nodos_con_nivel())

    def amplitud(self):
        """Máximo número de nodos físicos en un nivel."""
        cantidades = {}
        for _, nivel in self._nodos_con_nivel():
            cantidades[nivel] = cantidades.get(nivel, 0) + 1
        return max(cantidades.values(), default=0)

    def en_orden(self):
        resultado = []
        self._recorrer(self.__raiz, resultado, "in")
        return resultado

    def pre_orden(self):
        resultado = []
        self._recorrer(self.__raiz, resultado, "pre")
        return resultado

    def post_orden(self):
        resultado = []
        self._recorrer(self.__raiz, resultado, "post")
        return resultado

    def _recorrer(self, nodo, resultado, modo):
        if nodo is None:
            return
        claves = nodo.get_claves()
        if modo == "post":
            self._recorrer(nodo.get_hijo(0), resultado, modo)
            for i, clave in enumerate(claves):
                self._recorrer(nodo.get_hijo(i + 1), resultado, modo)
                resultado.append(clave)
        else:
            for i, clave in enumerate(claves):
                if modo == "pre":
                    resultado.append(clave)
                self._recorrer(nodo.get_hijo(i), resultado, modo)
                if modo == "in":
                    resultado.append(clave)
            self._recorrer(nodo.get_hijo(len(claves)), resultado, modo)

    def por_niveles(self):
        """BFS agrupado por nodo, igual al ejemplo M-vías del docente."""
        return [nodo.get_claves() for nodo, _ in self._nodos_con_nivel()]

    def niveles(self):
        """Agrupa los nodos por profundidad: niveles[nivel][nodo][clave]."""
        resultado = []
        for nodo, nivel in self._nodos_con_nivel():
            if nivel == len(resultado):
                resultado.append([])
            resultado[nivel].append(nodo.get_claves())
        return resultado

    def es_balanceado(self):
        """Comprueba diferencia de alturas <= 1; no realiza rotaciones."""
        def comprobar(nodo):
            if nodo is None:
                return True, -1
            alturas = []
            for hijo in nodo.get_hijos()[:nodo.cantidad_claves() + 1]:
                balanceado, altura = comprobar(hijo)
                if not balanceado:
                    return False, 0
                alturas.append(altura)
            return max(alturas) - min(alturas) <= 1, 1 + max(alturas)

        return comprobar(self.__raiz)[0]

    def validar(self):
        """Comprueba orden, capacidad, rangos y referencias sin ciclos."""
        return self._estructura_valida(self.__raiz)

    def _estructura_valida(self, raiz):
        pendientes = [(raiz, None, None)]
        vistos = set()
        try:
            while pendientes:
                nodo, inferior, superior = pendientes.pop()
                if nodo is None:
                    continue
                if not isinstance(nodo, NodoMVias) or id(nodo) in vistos:
                    return False
                vistos.add(id(nodo))
                claves = nodo.get_claves()
                hijos = nodo.get_hijos()
                if nodo.get_orden() != self.__orden:
                    return False
                if not 1 <= len(claves) < self.__orden:
                    return False
                if len(hijos) != self.__orden:
                    return False
                for clave in claves:
                    NodoMVias.validar_clave(clave)
                    if inferior is not None and not inferior < clave:
                        return False
                    if superior is not None and not clave < superior:
                        return False
                if any(not a < b for a, b in zip(claves, claves[1:])):
                    return False
                if any(h is not None for h in hijos[len(claves) + 1:]):
                    return False
                limites = [inferior] + claves + [superior]
                for i in range(len(claves) + 1):
                    pendientes.append((hijos[i], limites[i], limites[i + 1]))
        except (TypeError, ValueError):
            return False
        return True

    def imprimir(self):
        if self.esta_vacio():
            print("(árbol vacío)")
        for nivel, nodos in enumerate(self.niveles()):
            print(f"Nivel {nivel}: " + " | ".join(map(str, nodos)))

    # Compatibilidad con los nombres usados en las tareas anteriores.
    Insertar = insertar
    InsertarNodo = insertar
    Buscar = obtener_nodo
    BuscarX = obtener_nodo
    Eliminar = eliminar
    EsHoja = es_hoja
    EsVacio = esta_vacio
    EstaVacio = esta_vacio
    Raiz = raiz
    Minimo = minimo
    Maximo = maximo
    Altura = altura
    Cantidad = cantidad
    CantidadClaves = cantidad_claves
    CantidadHojas = cantidad_hojas
    Amplitud = amplitud
    InOrden = en_orden
    PreOrden = pre_orden
    PostOrden = post_orden
    PorNiveles = por_niveles
    EsBalanceado = es_balanceado
