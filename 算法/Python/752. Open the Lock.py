class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        queue = []
        queue.append('0000')
        if '0000' in visited:
            return -1
        visited.add('0000')
        steps = 0
        while queue:
            size = len(queue)
            for i in range(size):
                now = queue.pop(0)
                if now == target:
                    return steps
                for j in range(4):
                    for k in [-1, 1]:
                        digit = int(now[j])
                        digit = (digit + k + 10) % 10
                        nxt = now[:j] + str(digit) + now[j+1:]
                        if nxt not in visited:
                            visited.add(nxt)
                            queue.append(nxt)
            steps += 1
        return -1
