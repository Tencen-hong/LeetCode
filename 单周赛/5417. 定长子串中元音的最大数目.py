class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        start = 0
        numOfVowel = 0
        vowel_letters = ['a', 'e', 'i', 'o', 'u']
        res = 0
        for i in range(len(s)):
            if s[i] in vowel_letters:
                numOfVowel += 1
            if i-start + 1 > k:
                if s[start] in vowel_letters:
                    numOfVowel -= 1
                start += 1
            res = max(res, numOfVowel)
        return res
