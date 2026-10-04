# src/rushhour/cli.py
from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from enum import Enum

from rushhour.parsing.errors import InvalidLevelError


class Strategy(str, Enum):
    BFS = "BFS"
    DFS = "DFS"
    UCS = "UCS"
    GBF = "GBF"
    ASTAR = "AStar"

def _position(text: str) -> tuple[int, int]:
    """Convierte 'fila,columna' en (fila, columna)."""
    try:
        row, col = (int(n) for n in text.split(","))
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"posición inválida '{text}', se esperaba FILA,COLUMNA (ej. 2,3)"
        )
    return row, col


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="rushhour",
        description="Rush Hour: verificación, sucesores y resolución de niveles.",
    )

    sub = parser.add_subparsers(dest="command", required=True, metavar="<comando>")

    def add_level(p: argparse.ArgumentParser) -> None:
        p.add_argument("-s", "--level", required=True, metavar="CADENA",
                       help="cadena que describe el nivel")

    # verify
    p = sub.add_parser("verify", help="comprueba que el nivel es válido")
    add_level(p)
    p.set_defaults(handler=cmd_verify)

    # successors
    p = sub.add_parser("successors", help="lista los estados sucesores")
    add_level(p)
    p.set_defaults(handler=cmd_successors)

    # question
    p = sub.add_parser("question", help="consultas sobre el nivel")
    add_level(p)
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument("--whereis", metavar="ID", help="posiciones que ocupa un vehículo")
    group.add_argument("--what", metavar="FILA,COL", type=_position, help="qué hay en una casilla")
    group.add_argument("--size", metavar="ID", help="longitud de un vehículo")
    group.add_argument("--howmany", action="store_true", help="número de vehículos del nivel")
    group.add_argument("--goal", action="store_true", help="posicion objetivo")
    p.set_defaults(handler=cmd_question)

    # solver
    p = sub.add_parser("solver", help="resuelve el nivel")
    add_level(p)
    p.add_argument("--strategy", required=True, choices=[s.value for s in Strategy])
    p.add_argument("--depth", type=int, help="profundidad máxima (solo DFS)")
    p.add_argument("--heuristic", type=int, help="heurística (solo GBF y AStar)")
    p.add_argument("--stats", action="store_true", help="muestra estadísticas")
    p.set_defaults(handler=cmd_solver)

    return parser


# --- Handlers: solo traducen args -> servicio -> salida ---------------------

def cmd_verify(args: argparse.Namespace) -> int:
    from rushhour.service import verify
    print(verify.run(args.level))
    return 0


def cmd_successors(args: argparse.Namespace) -> int:
    from rushhour.service import successors
    for level in successors.run(args.level):
        print(level)
    return 0

def cmd_question(args: argparse.Namespace) -> int:
    from rushhour.service import question

    for nombre in ("whereis", "what", "size", "howmany", "goal"):
        valor = getattr(args, nombre)
        if valor is not None and valor is not False:
            quest, arg = f"--{nombre}", valor
            break

    print(question.run(args.level, quest, arg))
    return 0


def cmd_solver(args: argparse.Namespace) -> int:
    from rushhour.service import solver
    result = solver.run(
        args.level,
        Strategy(args.strategy),
        max_depth=args.depth,
        heuristic=args.heuristic,
    )
    print(result.solution_text())
    if args.stats:
        print(result.stats)
    return 0


# --- Validación cruzada y punto de entrada ---------------------------------

def _validate(parser: argparse.ArgumentParser, args: argparse.Namespace) -> None:
    if args.command != "solver":
        return
    strategy = Strategy(args.strategy)
    if args.depth is not None and strategy is not Strategy.DFS:
        parser.error("--depth solo se admite con DFS")
    if args.heuristic is not None and strategy not in (Strategy.GBF, Strategy.ASTAR):
        parser.error("--heuristic solo se admite con GBF y AStar")


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    _validate(parser, args)
    try:
        return args.handler(args)
    except InvalidLevelError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1