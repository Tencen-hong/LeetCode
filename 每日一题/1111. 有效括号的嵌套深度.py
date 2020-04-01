class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ans = [0]*len(seq)
        for i in range(1, len(seq)):
            if seq[i] == seq[i-1]:  # 前后"()"相同，分到不同组
                ans[i] = 1 - ans[i-1]
            else:  # 前后"()"不同,分到相同组
                ans[i] = ans[i-1]
        return ans
