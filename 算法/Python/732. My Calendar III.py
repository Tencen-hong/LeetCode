class MyCalendarThree:

    def __init__(self):
        self.timeline = collections.defaultdict(int)

    def book(self, start: int, end: int) -> int:
        self.timeline[start] += 1
        self.timeline[end] -= 1
        res = 0
        ongoing = 0
        for k, v in sorted(self.timeline.items()):
            ongoing += v
            res = max(res, ongoing)
        return res


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
