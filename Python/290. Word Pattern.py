class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        wordstr = str.split()
        # print(wordstr)
        if len(wordstr) != len(pattern):
            return False
        return list(map(pattern.find, pattern)) == list(map(wordstr.index, wordstr))
