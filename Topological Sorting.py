def topoSort( V, adj):
        # Code here
        def dfs():
            current = queue.pop(-1)
            if current in adj:
                for i in adj[current]:
                    if not visited[i]:
                        queue.append(i)
                        visited[i]=1
            ans.append(current)
            print(ans)
            if queue:
                dfs()
        visited = [i for i in [0]*V]
        queue = []
        fans=[]
        for i in range(V):
            if (not visited[i]) and (i in adj):
                queue.append(i)
                visited[i]=1
                ans=[]
                dfs()
                if ans:
                    fans=ans+fans
        print(fans)
        return fans

topoSort(7, {5:[1],1:[4],4:[6],6:[3],0:[2,3]})