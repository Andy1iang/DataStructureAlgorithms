class Node:

    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        self.height = 0


class AVLTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self._insert(data, self.root)

    # recursive insertion helper function
    def _insert(self, data, node):
        if data < node.data:
            if node.left:
                self._insert(data, node.left)
            else:
                node.left = Node(data, node)
                node.height = max(self.getHeight(node.left),
                                  self.getHeight(node.right))+1
        else:
            if node.right:
                self._insert(data, node.right)
            else:
                node.right = Node(data, node)
                node.height = max(self.getHeight(node.left),
                                  self.getHeight(node.right))+1

        self.balance(node)

    def remove(self, data):
        if self.root:
            self._remove(data, self.root)

    # recursive removal helper function
    def _remove(self, data, node):
        if node is None:
            return None

        if data < node.data:
            self._remove(data, node.left)
        elif data > node.data:
            self._remove(data, node.right)
        else:
            # leaf nodes
            if node.left is None and node.right is None:
                parent = node.parent

                if parent is None:
                    self.root = None

                elif parent.left == node:
                    parent.left = None
                elif parent.right == node:
                    parent.right = None

                self.balance(parent)

            # no left nodes
            elif node.left is None and node.right is not None:
                parent = node.parent

                if parent is None:
                    self.root = node.right

                else:
                    if parent.left == node:
                        parent.left = node.right
                    if parent.right == node:
                        parent.right = node.right

                node.right.parent = parent

                self.balance(parent)

            # no right nodes
            elif node.right is None and node.left is not None:
                parent = node.parent

                if parent is None:
                    self.root = node.left

                else:
                    if parent.left == node:
                        parent.left = node.left
                    if parent.right == node:
                        parent.right = node.left

                node.left.parent = parent

                self.balance(parent)

            # two child nodes
            else:
                # switching node and predecessor data, then deleting predecessor node
                predecessor = self.getPredecessor(node.left)
                predecessor.data, node.data = node.data, predecessor.data
                self._remove(data, predecessor)

    def getPredecessor(self, node):
        if node.right:
            return self.getPredecessor(node.right)

        return node

    # recursive searching function
    def find(self, data, node):
        if node is None:
            return None

        if node.data == data:
            return node

        else:
            if data < node.data:
                return self.find(data, node.left)
            else:
                return self.find(data, node.right)

    def balance(self, node):

        # keep rotating until we reach the root node
        while node is not None:
            node.height = max(self.getHeight(node.left),
                              self.getHeight(node.right))+1
            self.rotate(node)
            node = node.parent

    def rotate(self, node):

        balance = self.getBalance(node)

        # left heavy
        if balance > 1:

            # left-right heavy
            if self.getBalance(node.left) < 0:
                self.leftRotate(node.left)

            self.rightRotate(node)

        # right heavy
        if balance < -1:

            # right-left heavy
            if self.getBalance(node.right) > 0:
                self.rightRotate(node.right)

            self.leftRotate(node)

    def getHeight(self, node):

        if node is None:
            return -1

        return node.height

    def getBalance(self, node):

        if node is None:
            return 0

        return self.getHeight(node.left) - self.getHeight(node.right)

    def leftRotate(self, node):
        right = node.right
        t = right.left
        parent = node.parent

        right.left = node
        node.right = t

        if t is not None:
            t.parent = node

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

        # updating the height of the nodes after they have been rotated
        node.height = max(self.getHeight(node.left),
                          self.getHeight(node.right)) + 1
        right.height = max(self.getHeight(right.left),
                           self.getHeight(right.right)) + 1

    def rightRotate(self, node):
        left = node.left
        t = left.right
        parent = node.parent

        left.right = node
        node.left = t

        if t is not None:
            t.parent = node

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

        # updating the height of the nodes after they have been rotated
        node.height = max(self.getHeight(node.left),
                          self.getHeight(node.right)) + 1
        left.height = max(self.getHeight(left.left),
                          self.getHeight(left.right)) + 1

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
