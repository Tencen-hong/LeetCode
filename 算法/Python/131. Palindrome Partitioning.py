class Solution:
    '''
    遇到要求所有组合、可能、排列等解集的题目，一般都是DFS + backtracking
    首先传入s="aab" path=[] res = [], 首先切割出"a"（然后是"aa" "aab" ...），然后判读它是不是回文串：
    如果不是，直接跳过
    如果是，则此时剩余的 s="ab"， path += ["a"]
    写入res的判断是，当s=""时，记录结果

    '''

    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            if s == s[::-1]:
                return True
            return False

        def helper(s, path, res):
            if not s:
                res.append(path.copy())
                return
            for i in range(1, len(s)+1):
                prefix = s[:i]
                if isPalindrome(prefix):
                    helper(s[i:], path+[prefix], res)

        if not s:
            return [[]]
        res = []
        path = []
        helper(s, path, res)
        return res
