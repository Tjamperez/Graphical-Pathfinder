from queue import Queue

##Attempt to write a Breadth-First-Search algorithm

# #Assign ‘a’ as the root node and insert it into the Queue.
# Extract node ‘a’ from the queue and insert the child nodes of ‘a’, i.e., ‘b’ and ‘c’.
# Print node ‘a’.
# The queue is not empty and has node ‘b’ and ‘c’. Since ‘b’ is the first node in the queue, let’s extract it and insert the child nodes of ‘b’, i.e., node ‘d’ and ‘e’.
# Repeat these steps until the queue gets empty. Note that the nodes that are already visited should not be added to the queue again.


# maxsize – Number of items allowed in the queue.
# empty() – Return True if the queue is empty, False otherwise.
# full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
# get() – Remove and return an item from the queue. If queue is empty, wait until an item is available.
# get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
# put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
# put_nowait(item) – Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
# qsize() – Return the number of items in the queue.


class Node:
    def __init__(self, pos: int, parent, cost: int):
        self.pos = pos
        self.parent = parent
        self.cost = cost

    def __repr__(self):
        return f"Node(state={self.pos}, parent={self.parent}, pos={self.pos} cost={self.cost})"


class BreadthFirstSearch:
    def __init__(self, board: str, start: int, width: int = 10, height: int = 10):
        self.explored = []
        self.start = start
        self.width = width
        self.height = height
        self.result = self.search(board)

    def search(self, board: str):
        FINAL_STATE = "t"

        node = Node(board.index('s'), None, 0)

        self.frontier = Queue(maxsize=self.width * self.height)
        self.frontier.put(node)
        while True:
            if self.frontier.empty():
                return None
            
            candidate = self.frontier.get()
            if board[candidate.pos] == FINAL_STATE:
                solution = []
                while candidate:
                    solution.append(candidate.pos)
                    candidate = candidate.parent
                return solution[-2::-1]

            if candidate.pos not in self.explored:
                self.explored.append(candidate.pos)
                for child in self.expand(candidate):
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

initial_state = "eeeeeeeeeteseeeeeeee"
height = 4
width = 5
start = 11

bfs = BreadthFirstSearch(initial_state, start, width, height)
print(bfs.result)
