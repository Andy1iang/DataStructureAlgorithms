class RabinKarp:

    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.expo = 26  # exponent used in hashing
        self.mod = 53  # modulo value used in hashing

    def hash(self, string, stringLen):
        hash = 0
        for i in range(stringLen):
            # hashing with polynomials to avoid spurious matches
            hash += ord(string[i])*(26**(stringLen-i-1))
        return hash % self.mod

    # rolling hash to avoid recomputing the hash from scratch each time
    def rollingHash(self, prevHash, prevChar, nextChar, patternLen):
        nextHash = (prevHash - (ord(prevChar)*26**(patternLen-1))
                    ) * 26 + ord(nextChar)
        return nextHash % self.mod

    def search(self):

        n = len(self.text)
        m = len(self.pattern)

        # pre-computing the hash value of the pattern
        patternHash = self.hash(self.pattern, m)

        # pre-computing the hash value of the first window of the text
        textHash = self.hash(self.text[0:m], m)

        # checking all substrings
        for i in range(n-m+1):

            if textHash == patternHash:
                # checking letter by letter
                if self.text[i:i+m] == self.pattern:
                    return i

            # as long as we're not on the last iteration
            if i < n-m:
                textHash = self.rollingHash(
                    textHash, self.text[i], self.text[i+m], m)
