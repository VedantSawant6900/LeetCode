class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        queue = []
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j]=="*":
                    queue.append([i,j,0])
                elif grid[i][j] == 'X':
                    visited[i][j]=1
        
        def bfs(queue,visited):
            current = queue.pop(0)
            if grid[current[0]][current[1]] == "#":
                queue=[]
                return current[2]
            visited[current[0]][current[1]] = 1
            for i in [[current[0]-1,current[1]],[current[0]+1,current[1]],[current[0],current[1]-1],[current[0],current[1]+1]]:
                if (i[0]>-1 and i[0]<len(grid)) and (i[1]>-1 and i[1]<len(grid[0])) and (grid[i[0]][i[1]] == 'O' or grid[i[0]][i[1]] == '#') and visited[i[0]][i[1]]==0:
                    queue.append([i[0],i[1],current[2]+1])
                    visited[i[0]][i[1]]=1
            if queue:
                ans = bfs(queue, visited)
            else:
                return -1
            return ans
        return bfs(queue, visited)
