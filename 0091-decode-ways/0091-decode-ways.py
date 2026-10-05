class Solution:
    def numDecodings(self, s: str) -> int:
        #use recursion+memo to solve this 
        n=len(s)
        dp=[-1 for i in range(n+1)]
        return self.helper(0,s,n,dp)

    def helper(self,ind,s,n,dp):
        if(ind==n):
            return 1
        if(s[ind]=="0"):
            return 0
        if(dp[ind]!=-1):
            return dp[ind]
        #there are two options onlyindex and newindex
        onlyindex=self.helper(ind+1,s,n,dp)
        newindex=0
        if(ind+1<n):
            if(s[ind]=="1" or (s[ind]=="2" and s[ind+1]<="6")):
                newindex=self.helper(ind+2,s,n,dp)
        dp[ind]=(onlyindex+newindex)
        return dp[ind]
      