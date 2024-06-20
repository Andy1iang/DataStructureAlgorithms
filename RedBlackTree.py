# TODO: Implement Delete Operation


class Color:
    BLACK = 0
    RED = 1


class Node:

    def __init__(self, data, parent=None, color=Color.RED):
        self.data = data
        self.parent = parent
        self.color = color
        self.left = None
        self.right = None


class RedBlackTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            self.root.color = Color.BLACK  # root is always black
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data <= node.data:
            if node.left is None:
                node.left = Node(data, node)
                self.fix(node.left)  # fixing possible violations
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data, node)
                self.fix(node.right)  # fixing possible violations
            else:
                self._insert(node.right, data)

    def traverse(self):
        if self.root is not None:
            self.traverseInOrder(self.root)

    def traverseInOrder(self, node: Node):
        if node.left is not None:
            self.traverseInOrder(node.left)

        print(node.data)

        if node.right is not None:
            self.traverseInOrder(node.right)

    def leftRotate(self, node):
        right = node.right
        rightLeft = right.left
        parent = node.parent

        right.left = node
        node.right = rightLeft

        if rightLeft is not None:
            rightLeft.parent = node

        node.parent = right
        right.parent = parent

        # updating parent link if needed
        if parent is not None:
            if parent.left == node:
                parent.left = right
            else:
                parent.right = right

        if node == self.root:
            self.root = right

    def rightRotate(self, node):
        left = node.left
        leftRight = left.right
        parent = node.parent

        left.right = node
        node.left = leftRight

        if leftRight is not None:
            leftRight.parent = node

        node.parent = left
        left.parent = parent

        # updating parent link if needed
        if parent is not None:
            if parent.left == node:
                parent.left = left
            else:
                parent.right = left

        if node == self.root:
            self.root = left

    def isRed(self, node):
        if node is None:
            return False  # null counts as black node
        return node.color == Color.RED

    def fix(self, node):

        # fixing violations from node up to root node
        while node != self.root and self.isRed(node) and self.isRed(node.parent):

            parent = node.parent
            grandParent = parent.parent

            if parent == grandParent.left:
                uncle = grandParent.right

                # case 1: uncle is red
                if self.isRed(uncle):
                    parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    grandParent.color = Color.RED
                    node = grandParent

                # case 2: uncle is black (or null)
                else:
                    # case 2.1: node is right child of parent (left rotation)
                    if node == parent.right:
                        self.leftRotate(parent)
                        # updating pointers after the rotation
                        node = parent
                        parent = node.parent

                    # case 2.2: node is left child of parent (also when case 2.1 has been rotated)
                    parent.color = Color.BLACK
                    grandParent.color = Color.RED
                    self.rightRotate(grandParent)

            else:
                uncle = grandParent.left

                # these are symmetric cases to the above cases

                if self.isRed(uncle):
                    parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    grandParent.color = Color.RED
                    node = grandParent

                else:
                    if node == parent.left:
                        self.rightRotate(parent)
                        # updating pointers after the rotation
                        node = parent
                        parent = node.parent

                    parent.color = Color.BLACK
                    grandParent.color = Color.RED
                    self.leftRotate(grandParent)

        if self.isRed(self.root):
            self.root.color = Color.BLACK
