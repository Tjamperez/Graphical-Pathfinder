from copy import deepcopy
from queue import Queue
from typing import Any


class Node:
    def __init__(self, pos: int, parent, cost: int):
        self.pos = pos
        self.parent = parent
        self.cost = cost

    def __repr__(self):
        return f"{self.pos}"


class SearchQueue:
    def __init__(self):
        self.state = Queue()
        self.trace_history = []

    def put(self, item):
        self.state.put(item)
        self._register(self.state)

    def get(self):
        item = self.state.get()
        self._register(self.state)
        return item

    def empty(self) -> bool:
        return self.state.empty()

    def history(self):
        return self.trace_history

    def _register(self, state: Queue):
        self.trace_history.append(deepcopy(state.queue))


class SearchStack:
    def __init__(self):
        self.state = []
        self.trace_history = []

    def put(self, item):
        self.state.append(item)
        self._register(self.state)

    def get(self):
        item = self.state.pop()
        self._register(self.state)
        return item

    def empty(self) -> bool:
        return len(self.state) == 0
    
    def history(self):
        return self.trace_history

    def _register(self, state: list):
        self.trace_history.append(deepcopy(state))


class TraceableSet:
    def __init__(self):
        self.state = ()
        self.trace_history = []

    def put(self, item):
        self.state = (*self.state, item)
        self._register(self.state)

    def get(self):
        item = None
        if self.state:
            item = self.state[-1]
            self.state = self.state[:-1]
            self._register(self.state)
        return item


    def history(self):
        return self.trace_history

    def _register(self, state: tuple):
        self.trace_history.append(state)

    def __iter__(self):
        return iter(self.state)
