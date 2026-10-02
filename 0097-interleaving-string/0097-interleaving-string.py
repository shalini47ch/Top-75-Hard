class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #here s3 should be s1+s2
        m=len(s1)
        n=len(s2)
        N=len(s3)
        #applying memoization to the existing code
        dp=[[[-1 for i in range(N+1)]for j in range(n+1)]for k in range(m+1)]
        return self.helper(0,0,0,s1,s2,s3,dp)

    def helper(self,i,j,k,s1,s2,s3,dp):
        m=len(s1)
        n=len(s2)
        N=len(s3)
        if(i==m and j==n and k==N):
            return True
        if(k>=N):
            #means out of bound case
            return False
        if(dp[i][j][k]!=-1):
            return dp[i][j][k]
        res=False
        if(i<m and s1[i]==s3[k]):
            res=self.helper(i+1,j,k+1,s1,s2,s3,dp)
        if(res==True):
            return True
        if(j<n and s2[j]==s3[k]):
            res=self.helper(i,j+1,k+1,s1,s2,s3,dp)
        dp[i][j][k]=res
        return dp[i][j][k]

        