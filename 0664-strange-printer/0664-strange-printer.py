class Solution:
    def strangePrinter(self, s: str) -> int:
        n=len(s)
        dp=[[-1 for i in range(n+1)]for j in range(n+1)]
        return self.helper(0,n-1,s,dp)

    def helper(self,i,j,s,dp):
        if(i>j):
            return 0
        if(i==j):
            return 1
        if(dp[i][j]!=-1):
            return dp[i][j]
        ans=1+self.helper(i+1,j,s,dp)
        for k in range(i+1,j+1):
            if(s[i]==s[k]):
                ans=min(ans,self.helper(i+1,k-1,s,dp)+self.helper(k,j,s,dp))
        dp[i][j]=ans
        return dp[i][j]


        