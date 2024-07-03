import heapq


class Edge:

    def __init__(self, weight, src, dst):
        self.weight = weight
        self.src = src  # source
        self.dst = dst  # destination


class Node:

    def __init__(self, value):
        self.value = value
        self.visited = False
        self.predecessor = None
        self.edges = []
        self.min = float('inf')  # infinity

    # overloading method for leap
    def __lt__(self, other):
        return self.min < other.min


class Dijkstra:

    def __init__(self):
        self.heap = []

    def calculate(self, start):
        start.min = 0
        heapq.heappush(self.heap, start)

        # keeps going as long as heap is not empty
        while self.heap:
            vertex = heapq.heappop(self.heap)

            # does not do the following if the vertex has been considered
            if vertex.visited:
                continue

            # check all neighboring nodes
            # if we discover a shorter path:
            # update the neighboring nodes & push it to the heap
            for edge in vertex.edges:
                u = edge.src
                v = edge.dst
                distance = u.min + edge.weight
                if distance < v.min:
                    v.predecessor = u
                    v.min = distance
                    heapq.heappush(self.heap, v)

            vertex.visited = True

    # printing the shortest path given out start (defined in init) and target
    def getShortestPath(self, target):
        print(f"Shortest path to {target.value}: {target.min}")
        node = target
        nodes = []
        while node:
            nodes.append(node)
            node = node.predecessor

        nodes.reverse()
        print(" -> ".join([str(node.value) for node in nodes]))
