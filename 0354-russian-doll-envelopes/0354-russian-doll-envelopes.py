class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        #here we need to return the maximum no of envelopes we will use the concept of lis to solve this along with binary search
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        def lowerbound(nums,target):
            n=len(nums)
            start=0
            end=n-1
            res=n
            while(start<=end):
                mid=start+(end-start)//2
                if(nums[mid]>=target):
                    res=mid
                    end=mid-1
                else:
                    start=mid+1
            return res 
        res=[]
        for w,h in envelopes:
            ind=lowerbound(res,h)
            if(ind==len(res)):
                res.append(h)
            else:
                res[ind]=h
        return len(res)
        