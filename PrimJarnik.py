import heapq


class Vertex:

    def __init__(self, name):
        self.name = name
        self.edges = []

# Edges should be undirected (make two edges for each)


class Edge:

    def __init__(self, weight, src, dst):
        self.weight = weight
        self.src = src
        self.dst = dst

    def __lt__(self, other):
        return self.weight < other.weight


class PrimJarnik:

    def __init__(self, vertices):
        self.unvisited = set(vertices)
        self.minSpanTree = []  # edges of the minimum spanning tree
        self.cost = 0
        self.heap = []

    def calculate(self, start):
        self.unvisited.remove(start)
        vertex = start

        # continues executing while there's still unvisited vertices
        while self.unvisited:

            # checks all edges of the current vertex
            for edge in vertex.edges:
                if edge.dst in self.unvisited:
                    heapq.heappush(self.heap, edge)

            # gets the minimum weight edge
            minEdge = heapq.heappop(self.heap)

            # adds that edge to the minimum spanning tree & make according adjustments
            if minEdge.dst in self.unvisited:
                self.minSpanTree.append(minEdge)
                self.cost += minEdge.weight
                self.unvisited.remove(minEdge.dst)
                vertex = minEdge.dst

    def printMinSpanTree(self):
        print(f"Total Cost: {self.cost}\n")
        for edge in self.minSpanTree:
            print(f"{edge.src.name} -> {edge.dst.name} : {edge.weight}")
