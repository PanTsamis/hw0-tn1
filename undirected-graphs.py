from collections import deque

class Searches:
    def breadthFirst(self, adj: list[list[int]], start: int):
        queue = deque([start])
        visited = {start: None}
        while queue:
            node = queue.pop()
            print(node)
            for neig in adj[node]:
                if neig not in visited:
                    visited[neig] = node
                    print(f"Tree edge: {node}, {neig}\n")           # tree edge
                    queue.appendleft(neig)
                elif (visited[node] != neig and node < neig):  
                    print(f"Cross edge: {node}, {neig}\n")          # cross edge

    def depthFirst(self, adj: list[list[int]], start: int):
        stack = [start]
        visited = {start: None}
        while stack:
            node = stack[-1]
            for neig in adj[node]:
                
                
            
