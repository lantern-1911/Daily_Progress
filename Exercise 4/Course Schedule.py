def canFinish(numCourses, prerequisites):
        premap = {i:[] for i in range(numCourses)}
        for i,j in prerequisites:
            #print(i,j)
            premap[i].append(j)
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if premap[crs] == []:
                return True
            visited.add(crs)
            for pre in premap[crs]:
                if not dfs(pre):return False
            visited.remove(crs)
            premap[crs] = []
            return True
        for i in range(numCourses):
            if not dfs(i):return False
        return True    
numCourses = 2
prerequisites = [[1,0],[0,1]]
print(canFinish(numCourses,prerequisites))           