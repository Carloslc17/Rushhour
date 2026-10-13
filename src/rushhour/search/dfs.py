# Algoritmo de busqueda DFS

from collections import deque
from rushhour.search.node import Node
from rushhour.service import question
from rushhour.service import successors
from rushhour.stats import Stats

# deque (cola de doble entrada y salida) funciona como una pila al meter y sacar elementos por el mismo lado

def run(inicio : Node, maxDepth : int, stats : Stats):

    stack = deque()
    aux = None
    visitados = {}
    nodeCount = 0

    # Activar estadisticas
    stats.generated(0)

    inicio.set_value(0)
    stack.append(inicio)

    while stack:
        aux = stack.pop()

        if question.run(aux.get_state(), "--goal", None) == True:
            break

        estado = aux.get_state()
        if estado in visitados and visitados[estado] <= aux.get_depth():
            stats.cut()
            continue

        stats.expanded()
        visitados[aux.get_state()] = aux.get_depth()

        if aux.get_depth() >= maxDepth:
            continue

        sucessors = successors.run(aux.get_state())
        nodos = []

        for element in sucessors:

            nodeCount += 1
            nuevo = Node(nodeCount, aux, element[0], element[1], aux.get_cost() + element[2], aux.get_depth() + 1, 0)
            nuevo.set_value(-nuevo.get_depth())
            nodos.append(nuevo)
            stats.generated(nuevo.get_depth)

        nodos.reverse()
        for nodo in nodos:
            stack.append(nodo)

    return aux