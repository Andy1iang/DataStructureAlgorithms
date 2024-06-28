class node:

    def __init__(self, name=None):
        self.name = name
        self.neighbors = set()  # set containing neighboring nodes
        self.visited = False


# could also be done with recursion
def DFS(start):

    stack = []
    stack.append(start)
    start.visited = True

    # keeps iterating as long as there are nodes left on the stack
    while stack:
        vertex = stack.pop()
        print(vertex.name)

        # keeps on appending unvisited neighbors
        for neighbor in vertex.neighbors:
            if not neighbor.visited:
                neighbor.visited = True
                stack.append(neighbor)
