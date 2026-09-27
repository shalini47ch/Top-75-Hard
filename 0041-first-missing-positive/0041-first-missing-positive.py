class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #this means the integer that is not present in nums 
        #means missing that is i+1 if not then n+1
        #use the concept of cyclic sort to solve this 
        n=len(nums)
        i=0
        while(i<n):
            correct=nums[i]-1
            if(1<=nums[i]<=n and nums[i]!=nums[correct]):
                #here we perform the swap
                nums[i],nums[correct]=nums[correct],nums[i]
            else:
                i+=1
        for i in range(0,n):
            if(nums[i]!=i+1):
                return i+1
        return n+1
      