from DLL import DLL


class Queue:

    def __init__(self):
        self.queue = DLL()

    def enqueue(self, data):
        self.queue.add_tail(data)

    def dequeue(self):
        return self.queue.remove_head()

    def peek(self):
        return self.queue.head

    def __len__(self):
        return len(self.queue)

    def __repr__(self):
        res = []
        res.append(f'{len(self)} items in queue')

        temp = self.queue.head
        count = 1
        while temp is not None:
            # adding each item to the resulting string
            res.append(f'Spot {count}: {temp.data}')
            temp = temp.next
            count += 1

        return '\n'.join(res)
