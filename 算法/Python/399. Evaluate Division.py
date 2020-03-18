class Solution:
    '''
    1.等式A/B=k 相当于有向图的边 A->B, queries['a','c']就是找一条从a到c的路径,并将沿路的权重累乘
    2.根据所给参数创建有向权重图
    3.从图中取3个点做全排列，如果这3个点是连接的则更新图
    '''

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        quot = collections.defaultdict(dict)
        for (num, den), val in zip(equations, values):
            quot[num][num] = quot[den][den] = 1.0
            quot[num][den] = val
            quot[den][num] = 1/val

        for k, i, j in itertools.permutations(quot, 3):
            if k in quot[i] and j in quot[k]:
                quot[i][j] = quot[i][k] * quot[k][j]

        return [quot[num].get(den, -1.0)for num, den in queries]
