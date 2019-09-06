class Solution:
    '''
    以邻接表形式重新存储边 adj
    q为最小堆（time,node）存储到node需要的时间，以(0,K)为起点，每次从q中取出的元素即为到q最近的节点，
    若此节点未收录则加入到答案中，以此节点为中间节点继续遍历adj[node]，押入到q中 
    '''
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        q = [(0, K)]
        t = {}
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        while q:
            time, node = heapq.heappop(q)
            if node not in t:
                t[node] = time
                for v, w in adj[node]:
                    heapq.heappush(q, (time+w, v))

        return max(t.values()) if len(t) == N else -1
