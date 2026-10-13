# Comando solver

import time
from rushhour.cli import Strategy
from rushhour.search.node import Node
from rushhour.search import bfs
from rushhour.search import dfs
from rushhour.search import ucs
from rushhour.search import gbf
from rushhour.search import astar
from rushhour.stats import Stats

def run(cadenaNivel, strategy, maxDepth=None, heuristic=None):

    Inicio = Node(0,None,"___",cadenaNivel,0,0,0)
    Solucion = None
    statsSearch = Stats()

    start = time.perf_counter()
    match strategy:
        case Strategy.BFS:  
            Solucion = bfs.run(Inicio, statsSearch)

        case Strategy.DFS:
            Solucion = dfs.run(Inicio, maxDepth, statsSearch)

        case Strategy.UCS:
            Solucion = ucs.run(Inicio, statsSearch)

        case Strategy.GBF:
            Solucion = gbf.run(Inicio, heuristic, statsSearch)

        case Strategy.ASTAR:
            Solucion = astar.run(Inicio, heuristic, statsSearch)

    statsSearch.elapsed = time.perf_counter() - start
    Camino = []

    # Construir camino solucion
    while Solucion:
        Camino.append(Solucion)
        Solucion = Solucion.get_parent()

    Camino.reverse()
    return (Camino, statsSearch)
