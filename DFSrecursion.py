def dfs(node,visited,adj,ls):
    visited[node]=1
    ls.append(node)
    for i in adj[node]:
        if not visited[i]:
            dfs(i,visited,adj,ls)
ls=[]
dfs(0,[0,0,0,0,0,0],{0:[2,3],3:[1,0],1:[3,5],5:[1],2:[0,4],4:[2]},ls)
print(ls)