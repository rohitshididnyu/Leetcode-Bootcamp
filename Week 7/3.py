class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        graph = {i: [] for i in range(numCourses)}
        cycle =[False]
        visited = [0] * numCourses

        for src, dest in prerequisites:
            graph[dest].append(src)

        print(graph)

        def dfs (node):
            if visited[node] == 1:
                cycle[0] = True
            if visited[node] == 2:
                return

            visited[node] =1
            for neig in graph[node]:
                if cycle[0]:
                    return
                dfs(neig)
            visited[node]=2
            order.append(node)

        for i in range(0,numCourses):
            if visited[i]==0:
                dfs(i)
                if cycle[0]:
                    return[]
            
        
        order.reverse()
        return order


            