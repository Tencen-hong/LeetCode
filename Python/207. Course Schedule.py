class Solution:
    '''
    其实这道题的本质即给定一个图，让我们判断该图是否是拓扑有序。

    这里我们需要用到一个图里入度的概念，在初始的图中，入度为0的点，即是课程中最基础的课程（需要先修，比如数据结构、C语言基础），在找到图中所有入度为0的点以后，将它们依次放入一个队列中，每次循环从队列头提取一个点，然后将这个点放入图中查询，查出哪些点被这个点所指向，并依次将这些点的入度减1，直观上的看的话，即是一个删除一个入度为0的点的操作，每次减1时，检测其他节点的入度，若出现新的入度为0的点，将其加入队列，循环往复，直到队列为空为止。

    循环结束后，再次检查每个节点的入度，若该图是拓扑有序的，则在循环操作中，所有的入度都会变为0。若不是拓扑有序的，则还会有入度不为0的点，即存在环。

    '''

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        inDegree = [0]*numCourses
        for prerequest in prerequisites:
            graph[prerequest[1]].append(prerequest[0])
            inDegree[prerequest[0]] += 1

        q = []
        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                q.append(i)

        while q:
            temp = q.pop(0)
            for j in graph[temp]:
                inDegree[j] -= 1
                if inDegree[j] == 0:
                    q.append(j)

        for i in range(len(inDegree)):
            if inDegree[i] != 0:
                return False
        return True
