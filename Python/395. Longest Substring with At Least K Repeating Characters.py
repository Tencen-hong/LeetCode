class Solution:
    '''
    先遍历整个string，并记录最小的character的出现次数。
    如果最小character出现次数都不小于k，那么说明整个string就是满足条件的longest substring，返回原string的长度即可；
    如果character的出现次数小于k，假设这个character是c，因为满足条件的substring永远不会包含c，所以满足条件的substring一定是在以c为分割参考下的某个substring中。所以我们需要做的就是把c当做是split的参考，在得到的String[]中再次调用我们的method，找到最大的返回值即可。
    '''

    def longestSubstring(self, s: str, k: int) -> int:
        def helper(s, k):
            if len(s) < k:
                return 0
            ch = min(set(s), key=s.count)
            if s.count(ch) >= k:
                return len(s)
            else:
                return max(helper(t, k) for t in s.split(ch))
        return helper(s, k)
