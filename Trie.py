class TrieNode:
    def __init__(self, val, parent=None):
        self.val = val
        self.children = {}
        self.parent = parent


class Trie:

    def __init__(self):
        self.root = TrieNode("*")

    def insert(self, key):
        # locating last matching node and rest of the input
        temp, key = self._traverse(self.root, key)

        # while there's still letters in the key
        while len(key) > 0:
            temp.children[key[0]] = TrieNode(key[0], temp)  # add the child
            temp = temp.children[key[0]]  # moving down to the child
            key = key[1::]  # shortening the key
        temp.children["*"] = TrieNode("*")  # adding end marker

    def _traverse(self, node: TrieNode, key):
        # returns last matching node of input and the rest of the string
        if len(key) == 0:
            return (node, key)

        elif key[0] not in node.children:
            return (node, key)

        elif key[0] in node.children:
            return self._traverse(node.children[key[0]], key[1::])

    def search(self, key):
        # locating last matching node and rest of the input
        temp, key = self._traverse(self.root, key)

        #only true if the last node is an end marker and the rest of the input is empty
        if len(key) == 0 and "*" in temp.children:
            return True
        return False

    def delete(self, key):
        # locating last matching node and rest of the input
        temp, key = self._traverse(self.root, key)

        # returns false if can't locate input word
        if len(key) != 0 or "*" not in temp.children:
            return False

        #calls recursive function to remove (starts from bottom up)
        return self._remove(temp, key+"*") #accounting for end marker

    def _remove(self, node: TrieNode, key):
        node.children.pop(key[-1]) #removes the child node from dictionary
        key = key[:-1:] #shortening the key

        #base case if there's no letters left or if the parent nodes has another child
        if len(node.children) != 0 or len(key) == 0:
            return True

        else:
            return self._remove(node.parent, key)
        
