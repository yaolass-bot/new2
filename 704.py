from collections import deque
def bfs(graph, start, goal):
  visited = set()
  queue = deque([(start, [start])])

  while queue:
    node, path = queue.popleft()

    if node == goal:
      return path

    if node not in visited:
      visited.add(node)
    for neighbor in graph[node]:
        queue.append((neighbor, path + [neighbor]))

  return []


# Example usage:
graph = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F'],
  'D': [],
  'E': ['F'],
  'F': []
}





























































