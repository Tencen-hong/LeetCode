class Solution:
    '''
    我们从0开始以其为起点实验，累加 restGas += gas[i] - cost[i]，一旦在 i 处遇到restGas<0，那么就说明当前选择的起点start不行，
    需要重新选择，此时我们不应该回去使用 start+1 作为新起点，因为start+1 到 i 处的总gas一定<总的cost，选择其中任何一个作为起点还是不行的，所以应该跳过这些点，
    以 i+1 作为新起点，遍历到 size-1 处就可以结束了，如果找到了可能的起点，我们还要进行验证，走一遍(total)，
    total>=0 保证总gas>=总cost 说明存在解，反之，总油量<总消耗，无解
    '''
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        rest, total = 0, 0
        for i in range(len(gas)):
            rest += gas[i]-cost[i]
            total += gas[i]-cost[i]
            if rest < 0:
                start = i+1
                rest = 0

        return start if total >= 0 else -1
