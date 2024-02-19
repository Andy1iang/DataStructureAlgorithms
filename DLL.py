class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return self.data


class DLL:

    def __init__(self):

        self.head = None
        self.tail = None
        self.size = 0

    def add_head(self, data):

        new_node = Node(data)

        if self.size == 0:
            # if DLL is empty, instantiate head and tail node (same node)
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1

    def add_tail(self, data):

        new_node = Node(data)

        if self.size == 0:
            # if DLL is empty, instantiate head and tail node (same node)
            self.head = new_node
            self.tail = new_node

        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def insert(self, data):

        # given that the DLL is ordered

        if self.size == 0:
            self.add_head(data)

        elif data < self.head.data:
            self.add_head(data)

        elif data > self.tail.data:
            self.add_tail(data)

        else:
            temp = self.head
            while temp is not None and temp.data < data:
                temp = temp.next

            new_node = Node(data)
            new_node.next = temp
            new_node.prev = temp.prev
            temp.prev.next = new_node
            temp.prev = new_node
            self.size += 1

    def remove_head(self):

        if self.size == 0:
            return None

        elif self.size == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.size -= 1
            return temp

        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
            return temp

    def remove_tail(self):

        if self.size == 0:
            return None

        elif self.size == 1:
            temp = self.tail
            self.tail = None
            self.head = None
            self.size -= 1
            return temp

        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
            return temp

    def remove(self, target):

        if self.size == 0:
            return None

        elif target == self.head.data:
            return self.remove_head()

        elif target == self.tail.data:
            return self.remove_tail()

        else:
            temp = self.head
            while temp is not None and temp.data != target:
                temp = temp.next

            if temp is None:
                return None

            else:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                self.size -= 1
                return temp

    def traverse_forward(self):

        temp = self.head
        while temp is not None:
            print(temp)
            temp = temp.next

    def traverse_backward(self):

        temp = self.tail
        while temp is not None:
            print(temp)
            temp = temp.prev

    def reverse(self):

        if self.size > 1:

            prev = None
            curr = self.head
            self.tail = self.head

            while curr is not None:
                curr.next, curr.prev = curr.prev, curr.next
                prev = curr
                curr = curr.prev

            self.head = prev

    def __len__(self):
        return self.size

    def __repr__(self):
        res = []
        res.append(f'DLL With {self.size} Nodes, stored at {hex(id(self))}')

        temp = self.head
        idx = 1
        while temp is not None:
            res.append(f'Node {idx}: {str(temp)}')
            temp = temp.next
            idx += 1

        return '\n'.join(res)
