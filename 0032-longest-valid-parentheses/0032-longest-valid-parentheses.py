class Solution:
    def longestValidParentheses(self, s: str) -> int:
        #here we need to return the length of the longest valid parentheses
        stack=[-1]
        maxi=0
        #traverse through the given string
        for ind,ch in enumerate(s):
            if(ch=="("):
                #here we add ind to stack
                stack.append(ind)
            else:
                stack.pop()
                if(len(stack)==0):
                    #matlab restart karo phirse
                    stack.append(ind)
                else:
                    maxi=max(maxi,ind-stack[-1])
        return maxi
            

       