class HashTable:

    # Less Collisions when our capacity is a prime number
    # Primes taken from https://planetmath.org/goodhashtableprimes
    primeHashes = [53, 97, 193, 389, 769, 1543, 3079, 6151, 12289, 24593, 49157, 98317, 196613, 393241, 786433,
                   1572869, 3145739, 6291469, 12582917, 25165843, 50331653, 100663319, 201326611, 402653189, 805306457, 1610612741]

    def __init__(self, loadFactor=0.66):

        self.capacityIdx = 0  # index of the current prime capacity we're at
        self.capacity = HashTable.primeHashes[self.capacityIdx]
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        self.size = 0
        # whether our capacity is max (can't be resized again)
        self.atMax = False
        # capacity will resize when the size is >= (loadFactor*capacity)
        self.loadFactor = loadFactor

    def _hash(self, key):
        # getting the sum of the ascii values then converting it to an valid integer
        return sum(ord(i) for i in key) % self.capacity

    def clear(self):
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        self.size = 0

    def _resize(self):
        if self.atMax:
            print("Hash Table Capacity at Maximum. Errors May Occur")
            return

        tempKeys = []
        tempValues = []

        # storing the keys and values temporarily
        for i in range(self.capacity):
            if self.keys[i] is not None:
                tempKeys.append(self.keys[i])
                tempValues.append(self.get(self.keys[i]))

        self.capacityIdx += 1
        if self.capacityIdx == len(HashTable.primeHashes)-1:
            self.atMax = True

        self.capacity = HashTable.primeHashes[self.capacityIdx]

        self.clear()

        # re-entering all the previously stored values
        for i in range(len(tempKeys)):
            self.insert(tempKeys[i], tempValues[i])

    def insert(self, key, value):
        hash_value = self._hash(key)

        # linear probing to deal with collisions
        while self.keys[hash_value] is not None:

            # when we find an empty slot
            if self.keys[hash_value] == key:
                self.values[hash_value] = value
                return True

            hash_value = (hash_value + 1) % self.capacity

        self.keys[hash_value] = key
        self.values[hash_value] = value
        self.size += 1

        if self.size >= int(self.capacity * self.loadFactor):
            self._resize()

    def get(self, key):
        hash_value = self._hash(key)
        while self.keys[hash_value] is not None:
            if self.keys[hash_value] == key:
                return self.values[hash_value]
            hash_value = (hash_value + 1) % self.capacity

        return None

    def delete(self, key):
        # this is a soft delete (the space is still taken up)
        hash_value = self._hash(key)
        while self.keys[hash_value] is not None:
            if self.keys[hash_value] == key:
                value = self.values[hash_value]
                self.values[hash_value] = None
                return value
            hash_value = (hash_value + 1) % self.capacity

        return False
