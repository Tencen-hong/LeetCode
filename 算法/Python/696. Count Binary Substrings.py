class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # 遍历一遍字符串，记录每次重复的0和1的数量，比如："00110011"，遍历后记录为：“2222”。“00011”遍历后记录为：“32”。然后再对这个新的记录，遍历，并取两个相邻数中较小的那一个，这实际上就是看每次响铃的0串和1串中会有的附和要求的子串数量了，速度快多了。
        res, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur += 1
            else:
                res += min(prev, cur)
                prev, cur = cur, 1

        return res + min(prev, cur)
