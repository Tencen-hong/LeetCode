class Solution:
    '''
    1.由于相同的元素需要隔离n个时间。那么我们找到tasks中出现最多次数的元素，该元素的出现次数为 t。那么总时间至少(t-1)(n+1)+1，若最多元素不止一个总有s个，那么总时间最少为(t-1)(n+1)+s。
    2.还有一种情况，当所有相同元素造成的间隔都被填满的情况下，这时总时间应该是task任务的长度。
    '''

    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = [0]*26
        for task in tasks:
            counter[ord(task)-ord('A')] += 1

        counter.sort()
        i = 25
        while i >= 0 and counter[i] == counter[25]:
            i -= 1
        return max(len(tasks), (counter[25]-1)*(n+1)+(25-i))
