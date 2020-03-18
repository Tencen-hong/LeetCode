class Solution:
    '''
    对于target而言，其正负由于对称性，所走的步数是一样的。比如，-1和+1都是只走一步，区别是往左还是往右而已。所以该问题可以简化为只考虑target为正的情况。
现在我们来考虑如何分步解决该问题。如果要得到最小的步数，必须尽量一直往右走，任何的后退都会让步数增多。假定存在k，S=1+2+...+k，有如下几种情况：

S==target，则k为最小步数。
S<target，需要继续往右走，直到情况1或3。
S>target，需要往左走才能到达target。具体该如何走我们来详细讨论。

往左走的步数越少越好，能否往左只走一步呢？假定第n步往左走（1<=n<=k）,一共会走1+2+...+n-1 - n + n+1+...+k=(1+2+...+n-1 + n + n+1 + ... + k) - 2n= S-2n=target，即S-target=2n。也就是说，如果S与target之间的差值为偶数，才能保证调整n的方向，就可以在k步走到target。如果差值为奇数，我们需要继续往前走一步，使差值变为偶数。
    '''

    def reachNumber(self, target: int) -> int:
        target_ = abs(target)
        sum_, step = 0, 0

        while sum_ < target_ or (sum_ - target_) & 1 != 0:
            step += 1
            sum_ += step

        return step
