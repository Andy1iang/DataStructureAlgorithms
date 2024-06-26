class MaxHeap:

    def __init__(self, capacity=100):
        self.capacity = capacity  # maximum capacity of hour heap
        self.size = 0  # current size of our heap
        self.heap = [None] * self.capacity

    def insert(self, item):

        # return False if heap at max capacity
        if self.size == self.capacity:
            return False

        # insert item at the end of the heap
        self.heap[self.size] = item

        # fixing the condition of the heap
        self._fix(self.size)

        self.size += 1
        return True

    def _fix(self, index):
        parent = (index - 1) // 2  # parent index
        # if current index is valid and is larger than parent
        if index > 0 and self.heap[index] > self.heap[parent]:
            # swapping values
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._fix(parent)  # recursive call up to the root

    def getMax(self):
        return self.heap[0]

    def extractMax(self):
        maxItem = self.heap[0]
        # swapping last value of heap to front
        self.heap[0] = self.heap[self.size - 1]
        self.heap[self.size - 1] = None  # resetting the last value to None
        self.size -= 1
        self._heapify()  # fixing heap structure
        return maxItem

    def _heapify(self, idx=0):
        left = 2 * idx + 1
        right = 2 * idx + 2

        # if there's no more items to fix
        if self.heap[left] is None and self.heap[right] is None:
            return True

        # if there's only left child
        elif self.heap[right] is None:
            if self.heap[idx] < self.heap[left]:
                self.heap[idx], self.heap[left] = self.heap[left], self.heap[idx]
            return True

        # if current index has both children
        else:
            # checking if left or right is larger
            # checking if current node is less than the larger one
            # swapping & recursively calling until root node or until base case

            if self.heap[left] > self.heap[right]:
                if self.heap[idx] < self.heap[left]:
                    self.heap[idx], self.heap[left] = self.heap[left], self.heap[idx]
                    self._heapify(left)
                else:
                    return True
            else:
                if self.heap[idx] < self.heap[right]:
                    self.heap[idx], self.heap[right] = self.heap[right], self.heap[idx]
                    self._heapify(right)
                else:
                    return True

    def heapSort(self):
        # extracting elements until all elements are extracted - O(NlogN)
        result = []
        for _ in range(self.size):
            result.append(self.extractMax())
        return result


class HeapTransformer:

    # heap parameter: array representation of a heap
    def __init__(self, heap, size):
        self.heap = heap[0:size]

    def transform(self):
        # performing heapify on all internal nodes in reverse order
        for i in range(len(self.heap)//2, -1, -1):
            self._heapify(i)

    # max heap to min heap transformer
    def _heapify(self, idx):

        left = idx*2 + 1
        right = idx*2 + 2

        if left >= len(self.heap):
            return True

        elif right >= len(self.heap):
            if self.heap[idx] > self.heap[left]:
                self.heap[idx], self.heap[left] = self.heap[left], self.heap[idx]
                return True

        else:
            if self.heap[left] < self.heap[right]:
                if self.heap[idx] > self.heap[left]:
                    self.heap[idx], self.heap[left] = self.heap[left], self.heap[idx]
                    self._heapify(left)

                else:
                    return True

            else:
                if self.heap[idx] > self.heap[right]:
                    self.heap[idx], self.heap[right] = self.heap[right], self.heap[idx]
                    self._heapify(right)

                else:
                    return True
