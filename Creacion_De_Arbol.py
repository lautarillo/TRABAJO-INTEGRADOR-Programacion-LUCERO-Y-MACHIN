# Función que crea los nodos
def crear_nodo(valor, izquierdo=None, derecho=None):
    return [valor, izquierdo, derecho]

# Función para verificar si es una hoja
def es_hoja(nodo):
    return nodo[1] is None and nodo[2] is None

# Funciones de recorrido del árbol:
# Preorden
def preorden(nodo):
    if nodo is not None:
        print(nodo[0], end=' ')
        preorden(nodo[1])
        preorden(nodo[2])
# Inorden
def inorden(nodo):
    if nodo is not None:
        inorden(nodo[1])
        print(nodo[0], end=' ')
        inorden(nodo[2])
# Postorden
def postorden(nodo):
    if nodo is not None:
        postorden(nodo[1])
        postorden(nodo[2])
        print(nodo[0], end=' ')

# Función recursiva para construir el árbol de forma interactiva
def construir_arbol():
    valor = input("Ingrese el valor del nodo (o deje vacío para None): ")
    if valor == "":
        return None

    nodo_izquierdo = None
    tiene_izquierdo = input(f"¿El nodo '{valor}' tiene hijo izquierdo? (s/n): ").lower()
    if tiene_izquierdo == 's':
        nodo_izquierdo = construir_arbol()

    nodo_derecho = None
    tiene_derecho = input(f"¿El nodo '{valor}' tiene hijo derecho? (s/n): ").lower()
    if tiene_derecho == 's':
        nodo_derecho = construir_arbol()

    return crear_nodo(valor, nodo_izquierdo, nodo_derecho)

# Función para imprimir la estructura del árbol
def imprimir_arbol(nodo, nivel=0, prefijo="Raíz: "):
    if nodo is not None:
        print(" " * (4 * nivel) + prefijo + str(nodo[0]))
        imprimir_arbol(nodo[1], nivel + 1, prefijo="Izq → ")
        imprimir_arbol(nodo[2], nivel + 1, prefijo="Der → ")

# Construcción del árbol por entrada del usuario
print("Construya su árbol binario:")
arbol = construir_arbol()

# Imprimir recorridos
print("\nRecorrido en preorden:")
preorden(arbol)

print("\nRecorrido en inorden:")
inorden(arbol)

print("\nRecorrido en postorden:")
postorden(arbol)

# Imprimir estructura del árbol
print("\nEstructura del árbol:")
imprimir_arbol(arbol)