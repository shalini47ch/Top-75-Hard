class Solution:
    def trap(self, height: List[int]) -> int:
        #here we need to return the sum we will create two helpers ngr and ngl
        n=len(height)
        su=0
        left=self.ngl(height)
        right=self.ngr(height)
        for i in range(0,n):
            area=min(left[i],right[i])-height[i]
            su+=area
        return su

    def ngr(self,height):
        n=len(height)
        right=[0 for i in range(n)]
        right[n-1]=height[n-1]
        #move from right to left
        for i in range(n-2,-1,-1):
            right[i]=max(right[i+1],height[i])
        return right 
    
    #now do for ngl
    def ngl(self,height):
        n=len(height)
        left=[0 for i in range(n)]
        left[0]=height[0]
        for i in range(1,n):
            left[i]=max(left[i-1],height[i])
        return left



      