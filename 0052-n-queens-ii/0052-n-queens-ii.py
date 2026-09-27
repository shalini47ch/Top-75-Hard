class Solution:
    def totalNQueens(self, n: int) -> int:
        #here we need to return the no of distinct puzzles
        colset=set()
        posdiag=set()
        negdiag=set()
        board=[["."]*n for i in range(n)]
        res=[]
        def backtrack(r):
            if(r==n):
                copy=["".join(row) for row in board]
                res.append(copy)
                return 
            for c in range(0,n):
                if(c in colset or (r+c) in posdiag or (r-c) in negdiag):
                    continue
                colset.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)
                board[r][c]="Q"
                backtrack(r+1)
                colset.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
                board[r][c]="."
        backtrack(0)
        return len(res)
            
            
        