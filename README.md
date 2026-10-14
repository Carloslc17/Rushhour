# Rush Hour

Resolutor y herramienta de análisis de niveles del puzzle **Rush Hour**, escrito en Python y ejecutable desde la terminal.

Permite verificar niveles, consultar su contenido, generar los estados sucesores y resolverlos con distintas estrategias de búsqueda (BFS, DFS, UCS, GBF y A*), mostrando estadísticas de cada ejecución.

## Origen del proyecto

Este proyecto nació como una práctica de la asignatura **Sistemas Inteligentes**, que implementé en Java el curso pasado.

Ahora lo rehago por mi cuenta, en Python y con un funcionamiento mejorado, para aplicar lo que entonces no supe resolver bien.

## Requisitos

- Python **3.10 o superior**.
- No hay dependencias de ejecución: solo se usa la biblioteca estándar.

Para desarrollar (tests, linter y tipos):

```bash
python -m venv .venv
source .venv/bin/activate        # en Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Formato de los niveles

Un nivel es una **cadena de 36 caracteres** que describe un tablero de 6x6 leído fila por fila, de arriba abajo y de izquierda a derecha:

- `o` representa una casilla vacía.
- Cada letra representa un vehículo; las casillas con la misma letra forman ese vehículo.
- Un vehículo ocupa 2 o 3 casillas contiguas, en horizontal o en vertical, y solo se mueve en la dirección de su eje.
- `A` es el vehículo objetivo, que debe llegar a la salida, situada a la derecha de su fila.

Ejemplo: `IBBoooIoooDDJAAoooJoKEEMooKooMGGHHHM`

```
I B B o o o
I o o o D D
J A A o o o
J o K E E M
o o K o o M
G G H H H M
```

## Uso

Desde la raíz del repositorio:

```bash
python -m rushhour <comando> -s "<cadena nivel>" [opciones]
```

Escribe siempre la cadena entre comillas. Si empieza por `-`, usa `-s=<cadena>` o `--level=<cadena>`.

Ayuda general y por comando:

```bash
python -m rushhour -h
python -m rushhour solver -h
```

### `verify`

Comprueba si el nivel es válido.

```bash
python -m rushhour verify -s "IBBoooIoooDDJAAoooJoKEEMooKooMGGHHHM"
```

### `successors`

Lista los niveles que se obtienen al aplicar un movimiento válido, uno por línea.

```bash
python -m rushhour successors -s "IBBoooIoooDDJAAoooJoKEEMooKooMGGHHHM"
```

### `question`

Consultas sobre un nivel. Se indica exactamente una pregunta:

| Opción | Descripción |
|---|---|
| `--whereis ID` | Posiciones que ocupa el vehículo `ID` |
| `--what FILA,COL` | Contenido de la casilla indicada (base 0) |
| `--size ID` | Longitud del vehículo `ID` |
| `--howmany` | Número de vehículos del nivel |

```bash
python -m rushhour question -s "IBBoooIoooDDJAAoooJoKEEMooKooMGGHHHM" --howmany
python -m rushhour question -s "IBBoooIoooDDJAAoooJoKEEMooKooMGGHHHM" --whereis A
python -m rushhour question -s "IBBoooIoooDDJAAoooJoKEEMooKooMGGHHHM" --what 2,1
```

### `solver`

Resuelve el nivel con la estrategia indicada.

```bash
python -m rushhour solver -s "<cadena nivel>" --strategy <estrategia> [opciones]
```

| Opción | Descripción |
|---|---|
| `--strategy` | `BFS`, `DFS`, `GBF` o `AStar` (obligatoria) |
| `--depth N` | Profundidad máxima. Solo con `DFS` |
| `--heuristic N` | Heurística a usar. Solo con `GBF` y `AStar` |
| `--stats` | Muestra las estadísticas de la búsqueda |

Ejemplos:

```bash
python -m rushhour solver -s "<nivel>" --strategy BFS --stats
python -m rushhour solver -s "<nivel>" --strategy DFS --depth 30
python -m rushhour solver -s "<nivel>" --strategy AStar --heuristic 1 --stats
```

## Estrategias de búsqueda

| Estrategia | Descripción | Estructura de la frontera |
|---|---|---|
| `BFS` | Búsqueda en anchura. Encuentra la solución con menos movimientos | Cola FIFO |
| `DFS` | Búsqueda en profundidad, con límite opcional | Pila |
| `UCS` | Búsqueda por coste: expande el nodo con menor coste | Cola de prioridad por coste |
| `GBF` | Búsqueda voraz: expande el nodo con menor heurística | Cola de prioridad por `h` |
| `AStar` | A*: prioriza por `g + h`. Óptima con heurísticas admisibles | Cola de prioridad por `g + h` |

## Estadísticas

Con `--stats` se muestran los datos de la ejecución:

| Sigla | Significado |
|---|---|
| `ET` | Tiempo de ejecución de la búsqueda |
| `TN` | Total de nodos generados |
| `CN` | Nodos descartados |
| `EN` | Nodos expandidos |
| `DF` | Máxima profundidad alcanzada |

## Estructura del proyecto

```
rushhour-py/
├── README.md
├── requirements.txt
├── rushhour/
│   ├── __main__.py        # python -m rushhour
│   ├── cli.py             # argumentos y salida; sin lógica de juego
│   ├── stats.py           # SearchStats
│   ├── model/             # Vehicle, Board, Move
│   ├── parsing/           # cadena <-> Board y excepciones propias
│   ├── search/            # Node, estrategias y heurísticas
│   ├── services/          # verify, successors, question, solver
│   └── structures/        # pila, cola y cola de prioridad
└── tests/
```

Flujo de dependencias: `cli -> services -> search / model / parsing`. El modelo y la búsqueda no hacen entrada/salida: devuelven valores y solo la CLI imprime.

## Desarrollo

```bash
python -m pytest        # tests
ruff check .            # linter
mypy rushhour           # comprobación de tipos
```

## Estado del proyecto

- [ ] `Vehicle` y `Board`
- [ ] Parser de niveles y `verify`
- [ ] Sucesores y `successors`
- [ ] BFS y `solver`
- [ ] DFS
- [ ] UCS
- [ ] Heurísticas, GBF y A*
- [ ] `question`
- [ ] Estadísticas
- [ ] Pruebas, CI y benchmark de estrategias
