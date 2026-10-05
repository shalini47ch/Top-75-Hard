class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #here we need to return the minimum no of operations to convert word1 to word2
        m=len(word1)
        n=len(word2)
        dp=[[-1 for i in range(n+1)]for j in range(m+1)]
        return self.helper(m-1,n-1,m,n,word1,word2,dp)


    def helper(self,i,j,m,n,s1,s2,dp):
        if(i<0):
            return j+1
        if(j<0):
            return i+1
        if(dp[i][j]!=-1):
            return dp[i][j]
        if(s1[i]==s2[j]):
            dp[i][j]=self.helper(i-1,j-1,m,n,s1,s2,dp)
            return dp[i][j]
        else:
            #there are three options insert,delete and replace 
            insert=self.helper(i,j-1,m,n,s1,s2,dp)
            delete=self.helper(i-1,j,m,n,s1,s2,dp)
            replace=self.helper(i-1,j-1,m,n,s1,s2,dp)
            dp[i][j]=1+min(insert,delete,replace)
            return dp[i][j]

      