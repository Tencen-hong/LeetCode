
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        counter_s1 = collections.Counter(s1)
        counter_s2 = collections.Counter(s2)
        return counter_s1 == counter_s2