# Funcion que crea los nodos
def crear_nodo(valor, izquierdo=None, derecho=None):
    return [valor, izquierdo, derecho]

# Función para verificar si es una hoja
def es_hoja(nodo):
    return nodo[1] is None and nodo[2] is None

# Recorridos del árbol #

# en preorder, recorremos el arbol empezando por la raiz, luego pasamoa al lado izquierdo y luego al derecho.
def preorden(nodo):
    if nodo is not None:
        print(nodo[0], end=' ')
        preorden(nodo[1])
        preorden(nodo[2])
# en inorden, recorremos el arbol empezando por la izquierda, luego la raiz y por ultimo la derecha.
def inorden(nodo):
    if nodo is not None:
        inorden(nodo[1])
        print(nodo[0], end=' ')
        inorden(nodo[2])
# en postorden, recorremos el arbol empezando por la izquierda, luego nos movemos a la derecha, y terminamos en la raiz.
def postorden(nodo):
    if nodo is not None:
        postorden(nodo[1])
        postorden(nodo[2])
        print(nodo[0], end=' ')

# Construcción del árbol
arbol = crear_nodo('A',         # nodo padre
    crear_nodo('B',             # nodo hijo izquierdo de A
        crear_nodo('D',         # nodo hijo izquierdo de B
            crear_nodo('H'),    # nodo hijo izquierdo de D
            None                # nodo hijo derecho de D (no tiene)
        ),
        crear_nodo('E')         # nodo hijo derecho de B
    ),
    crear_nodo('C',             # nodo hijo derecho de A
        crear_nodo('F'),        # nodo hijo izquierdo de C
        crear_nodo('G',         # nodo hijo derecho de C 
            None,               # nodo hijo izquierdo de G (no tiene)
            crear_nodo('I')     # nodo hijo derecho de G
        )
    )
)
#imprimir el recorrido preorden
print("Recorrido en preorden:")
preorden(arbol)

#imprimir el recorrido inorden
print("\nRecorrido en inorden:")
inorden(arbol)

#imprimir el recorrido postorden
print("\nRecorrido en postorden:")
postorden(arbol)