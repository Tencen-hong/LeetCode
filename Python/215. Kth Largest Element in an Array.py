class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        minHeap = []
        for num in nums:
            if len(minHeap) < k:
                heapq.heappush(minHeap, num)
            elif num < minHeap[0]:
                continue
            elif num > minHeap[0]:
                heapq.heappushpop(minHeap, num)
        return minHeap[0]
