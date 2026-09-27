class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #here we need to return the max profit we can achieve 
        #we can complete atmost 2 transactions 
        n=len(prices)
        dp=[[[-1 for i in range(3)]for j in range(2)]for s in range(n+1)]
        return self.helper(0,1,2,prices,n,dp)

    def helper(self,ind,buy,cap,prices,n,dp):
        if(ind==n):
            return 0
        if(cap==0):
            return 0
        if(dp[ind][buy][cap]!=-1):
            return dp[ind][buy][cap]
        if(buy):
            profit=max(-prices[ind]+self.helper(ind+1,0,cap,prices,n,dp),
            0+self.helper(ind+1,1,cap,prices,n,dp))
        else:
            profit=max(prices[ind]+self.helper(ind+1,1,cap-1,prices,n,dp),
            0+self.helper(ind+1,0,cap,prices,n,dp))
        dp[ind][buy][cap]=profit
        return dp[ind][buy][cap]
        
        