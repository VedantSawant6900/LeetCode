class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        d={
            4:0,
            3:1,
            1:3,
            0:4,
            2:2
        }
        perimeter=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    surrond=0
                    for k in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                        if (k[0]>-1 and k[0]<len(grid)) and (k[1]>-1 and k[1]<len(grid[i])) and grid[k[0]][k[1]] == 1:
                            surrond+=1
                    perimeter+=d[surrond]
        return perimeter

