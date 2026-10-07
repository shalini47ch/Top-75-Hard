class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        #lets use the concept of dfs along with dp to solve this 
        m=len(matrix)
        n=len(matrix[0])
        dp=[[0 for i in range(n+1)]for j in range(m+1)]
        dirs=[(-1,0),(0,1),(1,0),(0,-1)]
        def dfs(i,j):
            if(dp[i][j]!=0):
                return dp[i][j]
            best=1
            for dr,dc in dirs:
                nrow=i+dr
                ncol=j+dc
                if(nrow>=0 and nrow<m and ncol>=0 and ncol<n and 
                matrix[nrow][ncol]>matrix[i][j]):
                #means its increasing form
                   best=max(best,1+dfs(nrow,ncol))
            dp[i][j]=best
            return dp[i][j]
        #now at last we need to return the length of longest increasing path
        maxi=0
        for i in range(0,m):
            for j in range(0,n):
                maxi=max(maxi,dfs(i,j))
        return maxi



        