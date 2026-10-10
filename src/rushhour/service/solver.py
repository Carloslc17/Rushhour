# Comando solver

from rushhour.cli import Strategy
from rushhour.search.node import Node
from rushhour.search import bfs
from rushhour.search import dfs
from rushhour.search import ucs
from rushhour.search import gbf
from rushhour.search import astar

def run(cadenaNivel, strategy, maxDepth=None, heuristic=None):

    Inicio = Node(0,None,"___",cadenaNivel,0,0,0)
    Solucion = None

    match strategy:
        case Strategy.BFS:  
            Solucion = bfs.run(Inicio)

        case Strategy.DFS:
            Solucion = dfs.run(Inicio, maxDepth)

        case Strategy.UCS:
            Solucion = ucs.run(Inicio)

        case Strategy.GBF:
            Solucion = gbf.run(Inicio, heuristic)

        case Strategy.ASTAR:
            Solucion = astar.run(Inicio, heuristic)

    Camino = []
    while Solucion:
        Camino.append(Solucion)
        Solucion = Solucion.get_parent()

    Camino.reverse()
    return Camino