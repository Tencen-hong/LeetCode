import functools


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # function sorted  compare from back to front
        def compare(a, b):
            return int(b + a) - int(a + b)
        nums = sorted(map(str, nums), key=functools.cmp_to_key(compare))
        res = ''.join(nums)

        return '0' if res[0] == '0' else res
