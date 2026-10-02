class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #here we need to return the area of the largest rectangle in histogram
        #create two helpers one is nsl and other is nsr
        maxarea=0
        left=self.nsl(heights)
        right=self.nsr(heights)
        #traverse through the heights array and find the area 
        n=len(heights)
        for i in range(0,n):
            area=(right[i]-left[i]-1)*heights[i]
            #its basically width*height
            maxarea=max(maxarea,area)
        return maxarea

    def nsl(self,heights):
        n=len(heights)
        stack=[]
        ans=[]
        for i in range(0,n):
            while(stack and heights[stack[-1]]>=heights[i]):
                stack.pop()
            if(len(stack)==0):
                ans.append(-1)
            else:
                ans.append(stack[-1])
            stack.append(i)
        return ans 
    
    #now similarly do for nsr
    def nsr(self,heights):
        n=len(heights)
        stack=[]
        ans=[]
        for i in range(n-1,-1,-1):
            while(stack and heights[stack[-1]]>=heights[i]):
                stack.pop()
            if(len(stack)==0):
                ans.append(n)
            else:
                ans.append(stack[-1])
            stack.append(i)
        return ans[::-1]
            
       