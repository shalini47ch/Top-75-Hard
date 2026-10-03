class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        #use the concept of mah to solve this
        n=len(matrix)
        m=len(matrix[0])
        #this will befor cols
        heights=[0 for i in range(m)]
        maxarea=0
        for i in range(0,n):
            for j in range(0,m):
                if(matrix[i][j]=="1"):
                    heights[j]+=1
                else:
                    heights[j]=0
            area=self.mah(heights)
            maxarea=max(maxarea,area)
        return maxarea

    def mah(self,heights):
        n=len(heights)
        left=self.nsl(heights)
        right=self.nsr(heights)
        maxarea=0
        for i in range(0,n):
            area=(right[i]-left[i]-1)*heights[i]
            maxarea=max(maxarea,area)
        return maxarea

    #create two helpers one for nsl and other is nsr
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


        