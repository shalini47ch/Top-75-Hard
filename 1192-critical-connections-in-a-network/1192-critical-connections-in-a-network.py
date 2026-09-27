class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        #if the connection is removed it makes some servers unreachable 
        #this is solved using the concept of tarjans algo with a condition of low[neigh]>dis[node]
        #here the first step is to build the graph
        graph=[[] for i in range(n)]
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
        low=[-1 for i in range(n)]
        dis=[-1 for i in range(n)] #here dis stands for discovery
        timer=0
        bridges=[]
        def dfs(node,parent):
            nonlocal timer
            #lets first populate low and dis
            low[node]=timer
            dis[node]=timer
            timer+=1
            #now the next step is to check for neighbor nodes 
            for neigh in graph[node]:
                if(neigh==parent):
                    continue
                if(dis[neigh]==-1):
                    #means its already visited
                    dfs(neigh,node)
                    low[node]=min(low[node],low[neigh])
                    #now check the case for bridge
                    if(low[neigh]>dis[node]):
                        bridges.append([node,neigh])
                else:
                    low[node]=min(low[node],dis[neigh])
        for node in range(n):
            if(dis[node]==-1):
                dfs(node,-1)
        return bridges

                



       