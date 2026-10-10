# Algoritmo de busqueda GBF

import heapq
import itertools
from rushhour.search.node import Node
from rushhour.service import question
from rushhour.service import successors
from rushhour.search import heuristics

def run(inicio : Node, h : int):

    pq = []
    counter = itertools.count()
    aux = None
    visitados = set()
    nodeCount = 0

    inicio.set_heuristic(heuristics.calcular(inicio.get_state(), h))
    inicio.set_value(inicio.get_heuristic() + inicio.get_cost())
    heapq.heappush(pq, (inicio.get_value(), next(counter), inicio))

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
            nuevo = Node(nodeCount, aux, element[0], element[1], aux.get_cost() + element[2], aux.get_depth() + 1, heuristics.calcular(element[1],h))
            nuevo.set_value(nuevo.get_heuristic() + nuevo.get_cost())
            heapq.heappush(pq, (nuevo.get_value(), next(counter), nuevo))

    return aux