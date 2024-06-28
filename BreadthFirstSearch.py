class node:

    def __init__(self, name=None):
        self.name = name
        self.neighbors = set() # set containing neighboring nodes
        self.visited = False


def BFS(start):
    queue = []
    start.visited = True
    queue.append(start)

    # will continue to execute as long as there at nodes in the queue
    while queue: 
        vertex = queue.pop(0) # could be more time efficient if done with linked list
        print(vertex.name)

        # keeps appending unvisited neighbors to queue
        for neighbor in vertex.neighbors:
            if not neighbor.visited:
                neighbor.visited = True
                queue.append(neighbor)
