class Z:

    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.concat = pattern + text
        self.zed = [0] * len(self.concat)  # used for Z-boxes

    def search(self):

        self.makeZTable()

        # iterating through each letter, if Z-box is long enough, return index
        for i in range(1, len(self.concat)):
            if self.zed[i] >= len(self.pattern):
                # minus pattern length sense we are using self.concat
                return i-len(self.pattern)

    def makeZTable(self):

        # initializing first zed value & pointers
        self.zed[0] = len(self.concat)
        l, r = 0, 0

        for i in range(1, len(self.concat)):

            # case: not in Z box (searches linearly)
            if i > r:
                n = 0
                while n+i < len(self.concat) and self.concat[n] == self.concat[n+i]:
                    n += 1

                # setting zed value (how many letters match at & after current)
                self.zed[i] = n

                # moving pointers
                if n > 0:
                    l, r = i, i+n-1

            # case: in Z box
            else:
                p = i-l  # current position

                # does not need to search linearly
                if self.zed[p] < r-i+1:
                    self.zed[i] = self.zed[p]

                # search linearly
                else:
                    j = r+1
                    while j < len(self.concat) and self.concat[j] == self.concat[j-i]:
                        j += 1

                    self.zed[i] = j-i
                    l, r = i, j-1
