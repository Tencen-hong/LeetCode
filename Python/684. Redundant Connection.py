class Solution:
    '''
    由题意，去掉一个边，剩下的就形成树，说明图中只有一个环
    并查集，当边的2个节点属于同一个根节点时，便是最后那个多出来的边
    '''

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        fa = [-1]*(len(edges)+1)
        for edge in edges:
            a = self.findRoot(edge[0], fa)
            b = self.findRoot(edge[1], fa)
            if a != b:
                fa[a] = b
            else:
                return edge

    def findRoot(self, x, fa):
        if fa[x] == -1:
            return x
        else:
            root = self.findRoot(fa[x], fa)
            fa[x] = root
            return root
