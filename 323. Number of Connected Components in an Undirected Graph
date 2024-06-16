class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj={}
        for i in range(n):
            adj[i]=[]
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        v=[0]*n
        c=0
        for i in adj:
            print(i)
            if not v[i]:
                q=[i]
                while q:
                    current = q.pop(0)
                    for j in adj[current]:
                        if not v[j]:
                            q.append(j)
                    v[current]=1
                c+=1
        return c