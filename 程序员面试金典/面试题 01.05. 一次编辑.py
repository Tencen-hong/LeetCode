class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if len(first) < len(second):
            return self.oneEditAway(second, first)
        if len(first) - len(second) > 1:
            return False
        if len(first) == len(second):
            replace_count = 0
            for i in range(len(first)):
                if first[i] != second[i]:
                    replace_count += 1
            if replace_count > 1:
                return False
            else:
                return True

        for i in range(len(first)):
            if first[:i]+first[i+1:] == second:
                return True
        return False
