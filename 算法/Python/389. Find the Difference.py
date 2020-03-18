class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for tt in t:
            if t.count(tt) > s.count(tt):
                return tt
        return ""
