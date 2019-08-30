class Solution:
    def maximumSwap(self, num: int) -> int:
        num = str(num)
        num_c = list(num)
        for i in range(len(num)-1):
            max_num = max(num[i+1:])
            if num[i] < max_num:
                max_index = num.rindex(max_num)
                num_c[max_index], num_c[i] = num_c[i], num_c[max_index]
                return int(''.join(num_c))

        return int(''.join(num_c))
