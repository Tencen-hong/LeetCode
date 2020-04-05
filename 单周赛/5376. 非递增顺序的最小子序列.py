class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        t_list = list(enumerate(nums))
       # print(t_list)
        t_list = sorted(t_list,key = lambda x: -x[1])
       # print(t_list)
        s = sum(nums)
        ans = []
        t_s = 0
        for it in t_list:
            t_s += it[1]
            ans.append(it[1])
            if t_s > s - t_s:
                break
        #ans = sorted(ans, key = lambda x: x[0] )
        #ans = [ it[1] for it in ans]
        return ans
            
        
        