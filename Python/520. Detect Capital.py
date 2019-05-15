class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.upper() == word:
            return True
        if word.lower() == word:
            return True
        if len(word) > 1 and word[0] == word[0].upper() and word[1:] == word[1:].lower():
            return True
        return False
