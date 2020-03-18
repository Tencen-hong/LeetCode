class Solution:
    '''
        在Course Schedule I的基础上 记录路径
    '''

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        inDegree = [0]*numCourses
        for prerequest in prerequisites:
            graph[prerequest[1]].append(prerequest[0])
            inDegree[prerequest[0]] += 1

        q = []
        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                q.append(i)

        res = []
        while q:
            temp = q.pop(0)
            res.append(temp)
            for j in graph[temp]:
                inDegree[j] -= 1
                if inDegree[j] == 0:
                    q.append(j)

        for i in range(len(inDegree)):
            if inDegree[i] != 0:
                return []
        return res
