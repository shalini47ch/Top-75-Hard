#so here we can return the edge that can be removed so that its a graph
class DisjointSet:
    def __init__(self,n):
        self.parent=[i for i in range(n+1)]
        self.rank=[0 for i in range(n+1)]
    
    def findparent(self,node):
        if(node==self.parent[node]):
            return self.parent[node]
        self.parent[node]=self.findparent(self.parent[node])
        return self.parent[node]
    
    def unionbyrank(self,u,v):
        upu=self.findparent(u)
        upv=self.findparent(v)
        if(self.rank[upu]<self.rank[upv]):
            self.parent[upu]=upv
        elif(self.rank[upv]<self.rank[upu]):
            self.parent[upv]=upu
        else:
            self.parent[upv]=upu
            self.rank[upu]+=1
    
class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n=len(edges)
        res=[]
        ds=DisjointSet(n)
        #if they have the same parent we add the nodes else return [-1,-1]
        for u,v in edges:
            if(ds.findparent(u)==ds.findparent(v)):
                res.extend([u,v])
            ds.unionbyrank(u,v)
        if(len(res)==0):
            return [-1,-1]
        return res
        