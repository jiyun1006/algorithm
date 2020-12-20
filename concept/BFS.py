from collections import deque


graph = {'A': ['B', 'C'],
         'B': ['A', 'D'],
         'C': ['A', 'G', 'H', 'I'],
         'D': ['B', 'E', 'F'],
         'E': ['D'],
         'F': ['D'],
         'G': ['C'],
         'H': ['C'],
         'I': ['C', 'J'],
         'J': ['I']}


# B C D G H I

def bfs(graph, start_node):
    visited = deque()
    need_visit = deque()

    need_visit.appendleft(start_node)
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extendleft(graph[node])
    return visited


print(bfs(graph, 'A'))