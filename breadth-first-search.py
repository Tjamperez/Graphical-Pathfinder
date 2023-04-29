from queue import Queue
from pprint import pprint


class Node:
    def __init__(self, pos: int, parent, cost: int):
        self.pos = pos
        self.parent = parent
        self.cost = cost

    def __repr__(self):
        return f"{self.pos}"


class BreadthFirstSearch:
    FINAL_STATE = "t"
    BARRIER = "b"

    def __init__(self, board: str, start: int, width: int = 10, height: int = 10):
        self.explored = ()
        self.start = start
        self.width = width
        self.height = height
        self.result = self.search(board)

    def search(self, board: str):
        node = Node(board.index('s'), None, 0)

        self.frontier = Queue(maxsize=self.width * self.height)
        self.frontier.put(node)
        result = {
            "frontier": [],
            "explored": set(),
        }
        while True:
            result["frontier"].append(self.frontier.queue.copy())
            result["explored"].add(self.explored)

            if self.frontier.empty():
                return None
            
            candidate = self.frontier.get()
            if board[candidate.pos] == self.FINAL_STATE:
                result["solution"] = []
                while candidate:
                    result["solution"].append(candidate.pos)
                    candidate = candidate.parent
                result["solution"] = result["solution"][-2::-1]
                return result

            if candidate.pos not in self.explored:
                self.explored = (*self.explored, candidate.pos)
                for child in self.expand(candidate):
                    if board[child.pos] != self.BARRIER:
                        self.frontier.put(child)
        
    def expand(self, node: Node):
        sucessors = self.sucessor(node.pos)
        children = [Node(pos, node, node.cost + 1) for pos in sucessors.values()]
        return children

    def sucessor(self, pos: int) -> dict:
        sucessors = {}

        if (pos + 1) % self.width != 0:
            sucessors["right"] = pos + 1
        
        if (pos - 1) % self.width != 0:
            sucessors["left"] = pos - 1

        if (pos - self.width) >= 0:
            sucessors["up"] = pos - self.width
        
        if (pos + self.width) < self.height * self.width:
            sucessors["down"] = pos + self.width

        return sucessors

initial_state = "eeeeeeeebeesbeeebeeeeteee"
height = 5
width = 5
start = 11

bfs = BreadthFirstSearch(initial_state, start, width, height)
pprint(bfs.result)
