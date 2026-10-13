from dataclasses import dataclass

@dataclass
class Stats:
    total_nodes: int=0             #TN: Total de nodos generados
    cut_nodes: int=0               #CN: Total de nodos podados 
    expanded_nodes: int=0          #EN: Total de nodos expandidos
    max_depth: int=0               #DF: Profundidad maxima alcanzada 
    elapsed: float=0.0             #ET: Tiempo total del algoritmo de busqueda


    def generated(self, depth : int) -> None:
        self.total_nodes += 1
        if depth > self.max_depth:
            self.max_depth = depth

    def expanded(self) -> None:
        self.expanded_nodes += 1

    def cut(self) -> None:
        self.cut_nodes += 1

    def __str__(self) -> str:
        return (f"ET: {self.elapsed:.6f}\n"
                f"TN: {self.total_nodes}\n"
                f"EN: {self.expanded_nodes}\n"
                f"CN: {self.cut_nodes}\n"
                f"DF: {self.max_depth}")