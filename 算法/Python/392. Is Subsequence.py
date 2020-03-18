class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        queue = collections.deque(s)
        for c in t:
            if not queue:
                return True
            if c == queue[0]:
                queue.popleft()
        return not queue
