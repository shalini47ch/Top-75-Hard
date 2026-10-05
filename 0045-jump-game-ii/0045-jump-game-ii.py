class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest=0
        currend=0
        jumps=0
        #traverse through nums array
        for i in range(0,len(nums)-1):
            farthest=max(farthest,nums[i]+i)
            if(i==currend):
                jumps+=1
                currend=farthest
        return jumps
        