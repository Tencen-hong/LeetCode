class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran = collections.Counter(ransomNote)
        mag = collections.Counter(magazine)
        
        for k,v in ran.items():
            if mag[k] < v:
                return False
        return True