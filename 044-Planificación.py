from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start, goal):
        queue = deque([(start, [start])])
        visited = set([start])

        while queue:
            node, path = queue.popleft()
            if node == goal:
                return path
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return None

# Ejemplo de uso
graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('B', 'E')
graph.add_edge('C', 'F')
graph.add_edge('E', 'G')

start_node = 'A'
goal_node = 'G'
path = graph.bfs(start_node, goal_node)

if path:
    print("Camino encontrado:", path)
else:
    print("No se encontró camino desde {} hasta {}".format(start_node, goal_node))
