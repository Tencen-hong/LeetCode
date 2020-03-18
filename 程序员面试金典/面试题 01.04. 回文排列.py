
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        m_counter = collections.Counter(s)
        odd_count = 0
        even_count = 0
        for k,v in m_counter.items():
            if v%2==1:
                odd_count += 1
            else:
                even_count += 1
        return odd_count <= 1