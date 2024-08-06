print("<-----------------------Task 1----------------------->")
from collections import deque


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbour):
        if node not in self.graph:
            self.graph[node] = []
        if neighbour not in self.graph:
            self.graph[neighbour] = []
        self.graph[node].append(neighbour)

    def breadth_first_search(self, start, goal):
        visited = set()
        queue = deque([start])

        visited.add(start)

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            if node == goal:
                print("\nFound target")
                return

            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

        print("\nTarget not found")
        return


dataGraph = {
    '0': {'1', '4'},
    '1': {'0', '2', '3', '4'},
    '2': {'1', '3'},
    '3': {'1', '2', '4'},
    '4': {'0', '1', '3'}
}

graph = Graph()

for node, neighbours in dataGraph.items():
    for neighbour in neighbours:
        graph.add_edge(node, neighbour)

graph.breadth_first_search('0', '3')

print("<-----------------------Task 2----------------------->")

from collections import deque


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbour):
        if node not in self.graph:
            self.graph[node] = []
        if neighbour not in self.graph:
            self.graph[neighbour] = []
        self.graph[node].append(neighbour)

    def breadth_first_search(self, start, goal):
        visited = set()
        queue = deque([start])

        visited.add(start)

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            if node == goal:
                print("\nFound target")
                return

            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

        print("\nTarget not found")
        return


dataGraph = {
    'A': {'B', 'C', 'D'},
    'B': {'E', 'F'},
    'C': {'G'},
    'D': {},
    'E': {},
    'F': {},
    'G': {}
}

graph = Graph()
for node, neighbours in dataGraph.items():
    for neighbour in neighbours:
        graph.add_edge(node, neighbour)

graph.breadth_first_search('A', 'G')

print("<-----------------------Task 3----------------------->")
import heapq


def priority_queue():
    queue = []

    heapq.heappush(queue, (1, 'B'))
    heapq.heappush(queue, (0, 'A'))
    heapq.heappush(queue, (2, 'C'))

    while queue:
        priority, node = heapq.heappop(queue)
        print("Priority:", priority, "Node:", node)


priority_queue()

