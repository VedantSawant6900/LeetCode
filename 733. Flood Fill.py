class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = [0] * len(image[0])
        visited = [visited] * len(image)
        old_color = image[sr][sc]
        queue=[[sr,sc]]
        if image[sr][sc] == color:
             return image
        while queue:
            current = queue.pop(0)
            image[current[0]][current[1]] = color
            for i in [[current[0]+1,current[1]],[current[0]-1,current[1]],[current[0],current[1]+1],[current[0],current[1]-1]]:
                print(i)
                if  (i[0]>-1 and i[0]<len(image)) and (i[1]>-1 and i[1] < len(image[0])) and (not visited[i[0]][i[1]]) and image[i[0]][i[1]] == old_color:
                    queue.append([i[0],i[1]])
            visited[current[0]][current[1]] = 1
        return image