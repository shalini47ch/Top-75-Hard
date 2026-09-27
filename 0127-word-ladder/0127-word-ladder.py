from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #here we will use the concept of bfs to solve this 
        wordset=set(wordList)
        queue=deque()
        queue.append([beginWord,1])
        while(queue):
            ele=queue.popleft()
            word=ele[0]
            steps=ele[1]
            if(word==endWord):
                return steps 
            for i in range(0,len(word)):
                for ch in range(ord("a"),ord("z")+1):
                    newword=word[:i]+chr(ch)+word[i+1:]
                    if newword in wordset:
                        wordset.discard(newword)
                        queue.append([newword,steps+1])
        return 0
       