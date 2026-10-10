# Algoritmo de busqueda UCS

import heapq
import itertools
from rushhour.search.node import Node
from rushhour.service import question
from rushhour.service import successors

def run(inicio : Node):

    pq = []
    counter = itertools.count()
    aux = None
    visitados = set()
    nodeCount = 0

    inicio.set_value(0)
    heapq.heappush(pq, (inicio.get_value(),next(counter), inicio))

    while pq:
        _, _, aux = heapq.heappop(pq)

        if question.run(aux.get_state(), "--goal", None) == True:
            break

        if aux.get_state() in visitados:
            continue

        visitados.add(aux.get_state())
        sucessors = successors.run(aux.get_state())

        for element in sucessors:

            nodeCount += 1
            nuevo = Node(nodeCount, aux, element[0], element[1], aux.get_cost() + element[2], aux.get_depth() + 1, 0)
            nuevo.set_value(nuevo.get_cost())
            heapq.heappush(pq, (nuevo.get_value(), next(counter), nuevo))

    return aux