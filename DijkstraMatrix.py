class Dijkstra:

    def __init__(self, matrix, start):
        self.matrix = matrix  # adjacency matrix representation (undirected)
        self.start = start
        self.n = len(matrix)  # number of vertices
        self.visited = [False] * self.n
        # distance from start to each vertex
        self.distance = [float('inf')] * self.n
        self.distance[start] = 0  # distance from start to itself is 0

    # runtime can be reduced to O(logV) with heaps
    def getMinVertex(self):

        minVertex = float('inf')
        minIndex = 0

        # finding the current minimum value vertex (excepted visited ones)
        for idx in range(self.n):
            if not self.visited[idx] and self.distance[idx] < minVertex:
                minVertex = self.distance[idx]
                minIndex = idx

        return minIndex

    def calculate(self):

        # nested loop to get neighbors of the current minimum vertex at each iterations
        for i in range(self.n):
            vertex = self.getMinVertex()
            self.visited[vertex] = True

            # checking neighbors
            for other in range(self.n):

                # checking if neighbor has been visited and has connection
                if self.matrix[vertex][other] > 0 and not self.visited[other]:
                    newDistance = self.distance[vertex] + \
                        self.matrix[vertex][other]

                    # updating distance if shorter one is present
                    if newDistance < self.distance[other]:
                        self.distance[other] = newDistance

    # function returns all distances from start (defined in init)
    def getDistances(self):
        return self.distance
