class Node:

    def __init__(self, value):
        self.value = value
        self.edges = []
        self.distance = float('inf')
        self.predecessor = None


class Edge:

    def __init__(self, weight, src, dest):
        self.src = src
        self.dest = dest
        self.weight = weight


class BellmanFord:

    def __init__(self, vertices, edges, start):
        self.vertices = vertices
        self.edges = edges
        self.start = start
        self.start.distance = 0
        self.cycle = False  # boolean value to detect negative cycle

        self.calculate()  # automatically calculate

    def calculate(self):

        # iterating V-1 times (Can be optimized via Yen Optimization)
        for _ in range(len(self.vertices)-1):

            for edge in self.edges:
                u = edge.src
                v = edge.dest
                w = edge.weight

                # checking if there is a shorter path
                if u.distance + w < v.distance:
                    v.distance = u.distance + w
                    v.predecessor = u

        # if a path can be shortened after V-1 iterations, there is a negative cycle
        for edge in self.edges:
            u = edge.src
            v = edge.dest
            w = edge.weight

            if u.distance + w < v.distance:
                self.cycle = True
                break

    def getShortestPath(self, target):

        if self.cycle:
            print("Negative cycle detected")
            return

        print(f"Shortest path to {target.value}: {target.distance}")
        node = target
        nodes = []
        while node:
            nodes.append(node)
            node = node.predecessor

        nodes.reverse()
        print(" -> ".join([str(node.value) for node in nodes]))
