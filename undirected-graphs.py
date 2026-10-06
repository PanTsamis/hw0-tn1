from collections import deque

class Searches:
    # BFS using adjacency list and queue (appendleft + pop = FIFO)
    # Implement queue using deque (store only node)
    # visited maps each node to its parent (the node that found that specific node)
    # visited = "discovered" (not "processed"): marking before using prevents duplicates in the queue 
    def breadthFirst(self, adj: list[list[int]], start: int):
        queue = deque([start])
        visited = {start: None}

        # Main loop, end when queue is empty
        while queue:
            # Remove node from queue and use its contents
            # Check every neighbor of node with adj list
            # If neighbor not visited -> mark it as visited and tree edge found
            # If neighbor visited + neighbor not node's parent (we use node < neig so we have no duplicates and report once)-> cross edge found
            node = queue.pop()
            print(node)
            for neig in adj[node]:
                if neig not in visited:
                    visited[neig] = node
                    print(f"Tree edge: {node}, {neig}")
                    queue.appendleft(neig)
                elif (visited[node] != neig and node < neig):
                    print(f"Cross edge: {node}, {neig}")


    # DFS using adjacency list and stack (append + pop = LIFO)
    # Implement stack using list (store both node and its parent)
    # visited maps each node to its parent (the node that found that specific node)
    # visited = "actually visited": a node is marked only when removed, so it starts empty
    def depthFirst(self, adj: list[list[int]], start: int):
        stack = [(start, None)]
        visited = {}

        # Main loop
        while stack:
            # Remove node from stack
            # If node not visited -> mark it as visited + tree edge found (for every other node found but the starting one)
            # Then we check every neighbor of node with adj list
            # If neighbor not visited -> add it to the stack (NOT TO visited YET) with node as its parent
            # If neighbor visited + neighbor is not node's parent -> backward edge found
            node, parent = stack.pop()
            if node not in visited:
                visited[node] = parent
                print(node)
                if parent is not None:
                    print(f"Tree edge: {parent}, {node}")
                for neig in adj[node]:
                    if neig not in visited:
                        stack.append([neig, node])
                    elif (visited[node] != neig):
                        print(f"Backward edge: {node}, {neig}")