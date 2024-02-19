class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class SLL:

    def __init__(self):

        self.head = None
        self.tail = None
        self.size = 0

    def add_head(self, data):

        newNode = Node(data)

        if self.size == 0:
            self.head = newNode
            self.tail = newNode

        else:
            newNode.next = self.head
            self.head = newNode

        self.size += 1

    def add_tail(self, data):

        newNode = Node(data)

        if self.size == 0:
            self.head = newNode
            self.tail = newNode

        else:
            self.tail.next = newNode
            self.tail = newNode

        self.size += 1

    # given that the SLL is ordered
    def insert(self, data):

        newNode = Node(data)

        if self.size == 0:
            self.add_head(data)

        elif data <= self.head.data:
            self.add_head(data)

        elif data >= self.tail.data:
            self.add_tail(data)

        else:
            temp = self.head
            while temp.next is not None and temp.next.data < data:
                temp = temp.next

            newNode.next = temp.next
            temp.next = newNode
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
            self.size -= 1
            return temp

    def remove(self, data):

        if self.size == 0:
            return None

        elif self.head.data == data:
            self.size -= 1
            return self.remove_head()

        else:
            prev = None
            temp = self.head
            while temp is not None and temp.data != data:
                prev = temp
                temp = temp.next

            if temp is None:
                return None
            else:
                self.size -= 1
                prev.next = temp.next
                return temp

    def traverse(self):

        temp = self.head
        while temp is not None:
            print(temp)
            temp = temp.next

    def reverse(self):

        curr = self.head
        prev = None
        next = None
        while curr is not None:
            # setting next node variable to the next node
            next = curr.next
            # setting the actual current node's next link to the previous node (reverse)
            curr.next = prev
            # sitting previous node variable to current node
            prev = curr
            # sitting current node variable to the next node
            curr = next

        # setting the head node variable to the last node (current node is None, prev is last node)
        self.head = prev

    def __len__(self):
        return self.size

    def __repr__(self):

        res = []
        res.append(f'SLL With {self.size} Nodes, stored at {hex(id(self))}')
        temp = self.head
        idx = 1
        while temp is not None:
            res.append(f'Node {idx}: {str(temp)}')
            temp = temp.next
            idx += 1

        return '\n'.join(res)
