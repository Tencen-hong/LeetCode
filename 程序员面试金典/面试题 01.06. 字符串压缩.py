class Solution:
    def compressString(self, S: str) -> str:
        if S == "":
            return S
        x = S[0]
        cnt = 0
        new_s = ''
        S += '$'
        for ch in S:
            if ch == x:
                cnt += 1
            else:
                new_s += x+str(cnt)
                cnt = 1
                x = ch
        S = S[:-1]
        if len(new_s) < len(S):
            return new_s
        else:
            return S
