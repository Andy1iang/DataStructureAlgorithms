class Vertex:

    def __init__(self, name):
        self.name = name
        self.node = None  # node for disjoint set


class Edge:

    def __init__(self, weight, src, dst):
        self.weight = weight
        self.src = src  # source vertex
        self.dst = dst  # destination vertex

    # overloaded less than function (based on edge weight)
    def __lt__(self, other):
        return self.weight < other.weight


class Node:

    def __init__(self, rank, parent=None):
        self.rank = rank  # height of tree
        self.parent = parent


class DisjointSet:

    # Disjoint Sets
    # Keeping track of the nodes of vertices
    # Once an edge is part of the minimum spanning tree, the connecting vertices will be merged (union)
    # The root of a set will always be the parent of that set
    # The height of the tree at each node will be stored in the rank

    def __init__(self, vertices):
        self.vertices = vertices
        self.rootNodes = []  # all root nodes
        self.makeSets()

    def makeSets(self):
        # all disjoint sets at first
        for vertex in self.vertices:
            node = Node(0)
            vertex.node = node
            self.rootNodes.append(node)

    def find(self, node):
        curr = node
        while curr.parent is not None:
            curr = curr.parent

        root, curr = curr, node

        # path compression (node can have multiple children)
        while curr is not root:
            temp = curr.parent
            curr.parent = root
            curr = temp

        return root

    def union(self, node1, node2):

        root1 = self.find(node1)
        root2 = self.find(node2)

        # does not merge if it's the same set
        if root1 is root2:
            return False

        if root1.rank < root2.rank:
            root1.parent = root2

        elif root1.rank > root2.rank:
            root2.parent = root1

        else:
            root2.parent = root1
            root1.rank += 1  # increase rank by 1 only when both sets have same rank

        return True


class Kruskal:

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges

    def calculate(self):

        disjointSet = DisjointSet(self.vertices)
        minSpanTree = []

        # going through all sorted edges
        # until all vertices have been merged into one set
        # requires there has a spanning tree present in the graph
        self.edges.sort()
        for edge in self.edges:
            src = edge.src
            dst = edge.dst

            if disjointSet.find(src.node) is not disjointSet.find(dst.node):
                minSpanTree.append(edge)
                disjointSet.union(src.node, dst.node)

        return minSpanTree

    def printMinSpanTree(self):
        minSpanTree = self.calculate()
        for edge in minSpanTree:
            print(f"{edge.src.name} - {edge.dst.name}: {edge.weight}")
