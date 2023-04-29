from pprint import pprint

from src.algos import BreadthFirstSearch, DepthFirstSearch


initial_state = "eeeeeeeebeesbeeebeeeeteee"
height = 5
width = 5

bfs = BreadthFirstSearch(initial_state, width, height)
print("===========BFS==============")
pprint(bfs.result)

dfs = DepthFirstSearch(initial_state, width, height)
print("\n\n\n===========DFS==============")
pprint(dfs.result)
