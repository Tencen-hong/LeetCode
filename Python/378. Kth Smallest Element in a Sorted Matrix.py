class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return sorted(n for row in matrix for n in row)[k-1]
