# Algoritmo de busqueda BFS

import queue
from rushhour.search.node import Node
from rushhour.service import question
from rushhour.service import successors
from rushhour.stats import Stats

def run(inicio : Node, stats : Stats):

    q = queue.Queue()
    aux = None
    visitados = set()
    nodeCount = 0

    # Activar estadisticas
    stats.generated(0)

    inicio.set_value(0)
    q.put(inicio)

    while q.empty() == False:
        aux = q.get()

        if question.run(aux.get_state(), "--goal", None) == True:
            break

        if aux.get_state() in visitados:
            stats.cut() # Nodo podado
            continue

        stats.expanded() # Nodo expandido
        visitados.add(aux.get_state())
        sucessors = successors.run(aux.get_state())

        for element in sucessors:

            nodeCount += 1
            nuevo = Node(nodeCount, aux, element[0], element[1], aux.get_cost() + element[2], aux.get_depth() + 1, 0)
            nuevo.set_value(nuevo.get_depth())
            q.put(nuevo)
            stats.generated(nuevo.get_depth())

    return aux


