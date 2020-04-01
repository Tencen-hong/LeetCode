class Solution:
    def findLucky(self, arr: List[int]) -> int:
        m_dict = collections.Counter(arr)
        res = [-1]
        for k, v in m_dict.items():
            if k == v:
                res.append(k)
        return max(res)
