class Solution:
    def isValid(self, row, col, board,num,rows,cols,boxes):
        boxidx=(row//3)*3+(col//3)
        if num in rows[row]:
            return False
        if num in cols[col]:
            return False
        if num in boxes[boxidx]:
            return False
        return True

    def solve(self,board,empty,index,rows,cols,boxes):
        if index==len(empty):
            return True
        row,col=empty[index]
        boxidx=(row//3)*3+(col//3)
        for num in "123456789":
            # first check for the valid case
            if self.isValid(row,col,board,num,rows,cols,boxes):
                # here its add
                board[row][col]=num
                rows[row].add(num)
                cols[col].add(num)
                boxes[boxidx].add(num)
                # explore
                if self.solve(board,empty,index+1,rows,cols,boxes):
                    return True
                # here you do undo
                board[row][col]= "."
                rows[row].remove(num)
                cols[col].remove(num)
                boxes[boxidx].remove(num)
        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]
        empty=[]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxidx = (i//3)*3+(j//3)
                    boxes[boxidx].add(num)
                else:
                    empty.append((i,j))
        self.solve(board,empty,0,rows,cols,boxes)