import sys

INSTRUCCIONES = ("Uso:  python rushhour.jar verify -s <cadena nivel>\n" +
                       "python rushhour.jar question -s <cadena nivel> <parametros>\n" + 
                       "python rushhour.jar successors -s <cadena nivel>\n" +
                       "python rushhour.jar solver -s <cadena nivel> --strategy <estrategia busqueda>")


def main():

    args = sys.argv[1:]


    if len(args) < 3:
        print(INSTRUCCIONES);
        return

# Comando introducido por el usuario. 4 opciones.
    comando = args[0]

    if args[1] != "-s":
        print("Uso: java -jar rushhour.jar <comando> -s")
        return

    level = args[2]
    quest = ""
    x = ""
    strategy = ""
    maxDepth = -1
    stats = False
    heuristic = -1

    # QUESTION. Parsear argumentos extra.

    if comando == "question":

        if len(args) >= 4:
            quest = args[3]

        if len(args) == 5:
            x = args[4]

    # SOLVER. Parsear profundidad maxima si DFS. Parsear heuristica si GBF o A*
    elif comando == "solver":

        if len(args) < 5:
            print("Uso: java -jar rushhour.jar solver -s <cadena nivel> --strategy <estrategia>")
            return

        strategy = args[4]

        if len(args) > 5:

            if strategy == "DFS" and args[5] == "--depth":
                maxDepth = int(args[6])
            elif (strategy == "GBF" or strategy == "AStar") and args[5] == "--heuristic":
                heuristic = int(args[6])


    match comando:

        # VERIFY
        case "verify":
            print("Verify")

        # QUESTION
        case "question":
            print("Question")

        # SUCCESSORS
        case "successors":
            print("Successors")

        # SOLVER
        case "solver":
            print("Solver")

        
        case _:
            print("Opcion no valida")
            return

        


if __name__ == "__main__":
    main()