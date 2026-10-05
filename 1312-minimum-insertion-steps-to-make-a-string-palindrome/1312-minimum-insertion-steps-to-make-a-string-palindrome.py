class Solution:
    def minInsertions(self, s: str) -> int:
        s1=s[::-1]
        m=len(s)
        n=len(s1)
        dp=[[-1 for i in range(n+1)]for j in range(m+1)]
        y=self.helper(m-1,n-1,s,s1,m,n,dp)
        return m-y

    def helper(self,ind1,ind2,s1,s2,m,n,dp):
        if(ind1<0 or ind2<0):
            return 0
        if(dp[ind1][ind2]!=-1):
            return dp[ind1][ind2]
        if(s1[ind1]==s2[ind2]):
            dp[ind1][ind2]=1+self.helper(ind1-1,ind2-1,s1,s2,m,n,dp)
            return dp[ind1][ind2]
        else:
            ele1=self.helper(ind1-1,ind2,s1,s2,m,n,dp)
            ele2=self.helper(ind1,ind2-1,s1,s2,m,n,dp)
            dp[ind1][ind2]=max(ele1,ele2)
            return dp[ind1][ind2]

        
       