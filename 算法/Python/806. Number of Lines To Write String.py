class Solution:
    '''
        按顺序累加每个字符的长度，如果超过了最大长度就再起一行
    '''
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        line = 1
        max_width = 100
        temp_width = 0
        for s in S:
            if temp_width + widths[ord(s)-ord('a')] <= max_width:
                temp_width += widths[ord(s)-ord('a')]
            else:
                line += 1
                temp_width = 0 + widths[ord(s)-ord('a')]

        return [line, temp_width]
