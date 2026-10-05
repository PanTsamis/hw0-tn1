""""

class Searches:
    def __init__(self):
        self.stack = [None]
        self.visited = {}

    def depthFirst(self, AdjacencyList: list[list[int]], node: int):
        if node in self.visited: return
        self.stack.append(node)
        self.visited{node} = node

        for i in AdjacencyList[node]:
            if i in self.visited: continue # backward edges!!!
            # tree edges!!!
            self.depthFirst(AdjacencyList, i)
       
        self.stack.pop()



        BFS: insert stin arxi kai delete apo telos

""""



from collections import deque

class Searches:
    def breadthFirst(self, adj: list[list[int]], start: int):
        queue = deque([start])
        visited = set([start])
        while queue:
            node = queue.pop()
            print(node)
            for neig in adj[node]:
                if neig not in visited:
                    visited.add(neig)
                    # tree edge
                    queue.appendleft(neig)
                else if neig != node:
                    # cross edge
                    continue