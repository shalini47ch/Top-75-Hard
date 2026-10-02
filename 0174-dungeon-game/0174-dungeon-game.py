class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        #use the concept of 2d dp to solve this we will move from 0,0 till m-1,n-1
        #here we need to return the minimum health to rescue the princess
        m=len(dungeon)
        n=len(dungeon[0])
        #as the princess is located at m-1,n-1
        dp=[[-1 for i in range(n+1)]for j in range(m+1)]
        return self.helper(0,0,m,n,dungeon,dp)

    def helper(self,i,j,m,n,dungeon,dp):
        if(i>=m or j>=n):
            #means it moves out of bound
            return sys.maxsize 
        if(i==m-1 and j==n-1):
            return max(1,1-dungeon[i][j])
        if(dp[i][j]!=-1):
            return dp[i][j]
        #now there are two options either down or right
        down=self.helper(i+1,j,m,n,dungeon,dp)
        right=self.helper(i,j+1,m,n,dungeon,dp)
        #now before entering the next cell
        neednext=min(down,right)
        needcurr=max(1,neednext-dungeon[i][j])
        dp[i][j]=needcurr
        return dp[i][j]






    








    







    

       