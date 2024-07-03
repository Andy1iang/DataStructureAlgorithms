class KnuthMorrisPratt:

    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        # pre-computed table to make search O(n)
        self.piTable = self.makePiTable(pattern)

    def makePiTable(self, pattern):
        pi = [0] * len(pattern)
        prefixCounter = 0  # first letter always has value 0
        i = 1

        # pi table keeps track of how many letter it matches with the start of the pattern
        while i < len(pattern):
            if pattern[i] == pattern[prefixCounter]:
                prefixCounter += 1
                pi[i] = prefixCounter
                i += 1
            else:
                if prefixCounter != 0:
                    prefixCounter = pi[prefixCounter-1]
                else:
                    pi[i] = 0
                    i += 1

        return pi

    def search(self):
        i = 0  # used to iterate the text
        j = 0  # used to iterate the pi table

        # iterates through every letter of the text
        while i < len(self.text):

            # increments both points
            if self.text[i] == self.pattern[j]:
                i += 1
                j += 1

            # if letters don't match
            else:
                # pushes pi table pointer back if not at 0
                if j != 0:
                    j = self.piTable[j-1]

                # if at 0, increment text pointer
                else:
                    i += 1

            # found substring if pi table pointer reaches the end
            if j == len(self.pattern):
                return i-j
