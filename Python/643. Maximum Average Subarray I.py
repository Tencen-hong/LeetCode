class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        prefixSum = [0]+list(itertools.accumulate(nums))
        return max(map(operator.sub, prefixSum[k:], prefixSum[:-k]))/k
