class FreqStack:

    def __init__(self):
        self.freq = collections.Counter()
        self.list = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, x: int) -> None:
        self.freq[x] += 1
        if self.freq[x] > self.maxfreq:
            self.maxfreq = self.freq[x]
        self.list[self.freq[x]].append(x)

    def pop(self) -> int:
        if self.maxfreq != 0:
            x = self.list[self.maxfreq].pop()
            self.freq[x] -= 1
            if not self.list[self.maxfreq]:
                self.maxfreq -= 1
            return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
