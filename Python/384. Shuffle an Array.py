class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """

        return self.original

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        self.new = self.original.copy()
        random.shuffle(self.new)
        return self.new


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
