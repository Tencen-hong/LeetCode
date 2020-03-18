class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        pointer = [0]*len(primes)
        j = 1
        ans = [1]
        while j < n:
            m = min(ans[pointer[idx]] * primes[idx]
                    for idx in range(len(primes)))
            for idx in range(len(primes)):
                if m == ans[pointer[idx]] * primes[idx]:
                    pointer[idx] += 1
            ans.append(m)
            j += 1
        return ans[-1]
