from src.algos.models import Node, SearchQueue, SearchStack, TraceableSet


class BaseBlindSearch:
    FINAL_NODE = "t"
    BARRIER = "b"

    def __init__(self, board: str, width: int, height: int, frontier):
        self._explored = TraceableSet()
        self._start_pos = board.index("s")
        self._width = width
        self._height = height
        self._frontier = frontier
        self.result = self.search(board)

    def search(self, board: str):
        node = Node(self._start_pos, None, 0)

        self._frontier.put(node)
        while True:
            if self._frontier.empty():
                return None
            
            candidate = self._frontier.get()
            if board[candidate.pos] == self.FINAL_NODE:
                solution = {
                    "frontier": self._frontier.history(),
                    "explored": self._explored.history(),
                    "path": self._get_solution_path(candidate),
                }
                return solution

            if candidate.pos not in self._explored:
                self._explored.put(candidate.pos)
                for child in self._expand(candidate):
                    if board[child.pos] != self.BARRIER:
                        self._frontier.put(child)

    def _get_solution_path(self, node: Node):
        path = []
        while node:
            path.append(node.pos)
            node = node.parent
        return path[-2::-1]
        
    def _expand(self, node: Node):
        sucessors = self._sucessor(node.pos)
        children = [Node(pos, node, node.cost + 1) for pos in sucessors.values()]
        return children

    def _sucessor(self, pos: int) -> dict:
        sucessors = {}

        if (pos + 1) % self._width != 0:
            sucessors["right"] = pos + 1
        
        if (pos - 1) % self._width != 0:
            sucessors["left"] = pos - 1

        if (pos - self._width) >= 0:
            sucessors["up"] = pos - self._width
        
        if (pos + self._width) < self._height * self._width:
            sucessors["down"] = pos + self._width

        return sucessors


class DepthFirstSearch(BaseBlindSearch):
    def __init__(self, board: str, width: int, height: int):
        super().__init__(board, width, height, SearchStack())

class BreadthFirstSearch(BaseBlindSearch):
    def __init__(self, board: str, width: int, height: int):
        super().__init__(board, width, height, SearchQueue())
