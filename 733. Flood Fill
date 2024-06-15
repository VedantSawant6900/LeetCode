class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = [0] * len(image[0])
        visited = [visited] * len(image)
        old_color = image[sr][sc]
        queue=[[sr,sc]]
        if image[sr][sc] == color:
             return image
        image = self.dfs(visited=visited,image=image,queue=queue,color=color,old_color=old_color)
        return image
    

    def dfs(self, visited, image, queue,color,old_color):
        current = queue.pop(-1)
        image[current[0]][current[1]] = color
        for i in [[current[0]+1,current[1]],[current[0]-1,current[1]],[current[0],current[1]+1],[current[0],current[1]-1]]:
            if  (i[0]>-1 and i[0]<len(image)) and (i[1]>-1 and i[1] < len(image[0])) and (not visited[i[0]][i[1]]) and image[i[0]][i[1]] == old_color:
                queue.append([i[0],i[1]])
        visited[current[0]][current[1]] = 1
        if not len(queue):
            return image
        else:
            image = self.dfs(visited=visited,image=image,queue=queue,color=color,old_color=old_color)
        return image