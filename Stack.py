from DLL import DLL

# LIFO (Last in first out) structure


class Stack:

    def __init__(self):
        self.stack = DLL()

    def push(self, data):
        self.stack.add_head(data)

    def pop(self):
        return self.stack.remove_head()

    def peek(self):
        return self.stack.head

    def __len__(self):
        return len(self.stack)

    def __repr__(self):
        res = []
        res.append(f'{len(self)} items in stack')

        temp = self.stack.head
        count = 1
        while temp is not None:
            # adding each item to the resulting string
            res.append(f'Spot {count}: {temp.data}')
            temp = temp.next
            count += 1

        return '\n'.join(res)
