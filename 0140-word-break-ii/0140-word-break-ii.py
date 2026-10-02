class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        #much similar to that of wordbreak but here we need to store the words as well
        wordset=set(wordDict)
        return self.helper(0,s,wordset)
        
    def helper(self,ind,s,wordset):
        if(ind==len(s)):
            return [""]
        res=[]
        for j in range(ind+1,len(s)+1):
            word=s[ind:j]
            if(word in wordset):
                for tail in self.helper(j,s,wordset):
                    if tail:
                        res.append(word+" "+tail)
                    else:
                        res.append(word)
        return res
        





    