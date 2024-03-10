class Node:

    def __init__(self, data, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent

    def __str__(self):
        return str(self.data)


class BST:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)

        else:
            self.insertNode(data, self.root)

    def insertNode(self, data, node: Node):
        # recursive call to traverse to the node that it should to added to, then add it in the base case
        if data < node.data:

            if node.left is not None:
                self.insertNode(data, node.left)
            else:
                node.left = Node(data, node)

        else:

            if node.right is not None:
                self.insertNode(data, node.right)
            else:
                node.right = Node(data, node)

    def remove(self, data):
        # recursively traversing to the node to remove
        temp = self.find(data, self.root)
        parent: Node = temp.parent

        # base case (when there are no nodes)
        if temp is None:
            return None

        # another base case (when node is leaf node)
        elif temp.left is None and temp.right is None:
            if parent is None:  # case when it's the root node
                self.root = None
            else:  # removing the connection
                if parent.left == temp:
                    parent.left = None
                else:
                    parent.right = None

        # case where there only is a right node
        elif temp.left is None:
            if parent is None:  # if node is the root node
                self.root = temp.right
            else:  # disconnecting the node
                if parent.left == temp:
                    parent.left = temp.right
                else:
                    parent.right = temp.right

        # case where there only is a left node
        elif temp.right is None:
            if parent is None:
                self.root = temp.left
            else:
                if parent.left == temp:
                    parent.left = temp.left
                else:
                    parent.right = temp.left

        # case where there are two child nodes
        else:
            temp.data = self.getMax(temp.left)  # getting the predecessor
            self.remove(temp.data)  # swapping and removing it

    # recursive function to find a node
    def find(self, data, node: Node):
        if node is None:
            return None

        if node.data == data:
            return node

        else:
            if data < node.data:
                return self.find(data, node.left)
            else:
                return self.find(data, node.right)

    def getMax(self, node=None):
        # default to starting from root node
        if node is None:
            if self.root is None:
                return None
            else:
                node = self.root

        if node.right is None:
            return node.data

        else:
            return self.getMax(node.right)

    def getMin(self, node=None):
        # default to starting from root node
        if node is None:
            node = self.root

        if node.left is None:
            return node.data

        else:
            return self.getMin(node.left)

    def traverse(self):
        if self.root is not None:
            self.traverseInOrder(self.root)

    # recursive call to traverse in sorted order
    def traverseInOrder(self, node: Node):
        # change the order of statements to get pre-order and post-order
        if node.left is not None:
            self.traverseInOrder(node.left)

        print(node.data)

        if node.right is not None:
            self.traverseInOrder(node.right)

    # checking for math depth
    def maxDepth(self, node: None | Node):
        if node is None:  # base case
            return 0
        else:  # return max depth on left and a right
            leftDepth = self.maxDepth(node.left)
            rightDepth = self.maxDepth(node.right)
            return max(leftDepth, rightDepth) + 1


class TreeComparator:

    # comparing if two trees are the same
    def compare(self, node1: Node, node2: Node):

        if node1 is None and node2 is None:  # base case
            return True

        elif node1 is None and node2 is not None:  # base case where one has more nodes
            return False

        elif node1 is not None and node2 is None:  # another base case where one has more nodes
            return False

        elif node1.data != node2.data:  # checking if the values are the same
            return False

        else:
            # recursive call
            return self.compare(node1.left, node2.left) and self.compare(node1.right, node2.right)
