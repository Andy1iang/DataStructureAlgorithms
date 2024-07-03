class TSP:

    def __init__(self, graph):

        self.graph = graph  # adjacency matrix representation
        self.n = len(graph)

        # keeping track of vertices that's been visited
        self.visited = [False] * self.n
        self.visited[0] = True

        # keeping track of the cycles
        self.cycles = []

        # temporary paths
        self.paths = [0]*self.n

    # function to check if a path is valid
    def validPath(self, vertex, neighbor):
        if self.visited[neighbor]:
            return False

        if self.graph[vertex][neighbor] == 0:
            return False

        return True

    # recursive function to find all Hamiltonian Paths
    def calculate(self, vertex, counter=1, cost=0):

        # base case - when we come to the last vertex
        # adds current path to the cycles if the path is valid
        if counter == self.n and self.graph[0][vertex] != 0:
            self.paths.append(0)  # accounts of the last step back to the start
            self.cycles.append(
                # .copy to avoid shallow copies
                [self.paths.copy(), cost + self.graph[0][vertex]])
            self.paths.pop()
            return

        # recursive case
        # checks all vertices for valid path(s)
        # keeps check each possible path (similar to depth first search)
        for i in range(self.n):
            if self.validPath(vertex, i):
                self.visited[i] = True
                self.paths[counter] = i
                self.calculate(i, counter+1, cost + self.graph[vertex][i])
                self.visited[i] = False

    def printShortestCycle(self):
        self.calculate(0)

        if not self.cycles:
            print("No cycles found.")
            return

        shortest_cycle = min(self.cycles, key=lambda x: x[1])
        print(f"Shortest Cycle Cost: {shortest_cycle[1]}")
        print(" -> ".join(map(str, shortest_cycle[0])))
