from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #here we need to return the maximum in sliding window of size k
        dq=deque()
        res=[]
        n=len(nums)
        for i in range(0,n):
            while dq and dq[0]<=i-k:
                dq.popleft()
            #prev and curr val ko comapre karo
            while dq and nums[dq[-1]]<=nums[i]:
                #matlab nums[i] bada hai toh wo order maintain nai hora hai to dq se pop karo
                dq.pop()
            dq.append(i)
            if(i>=k-1):
                res.append(nums[dq[0]])
        return res
        

        