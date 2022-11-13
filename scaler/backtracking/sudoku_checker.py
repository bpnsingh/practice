'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.'''


import collections
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        #We have to check for every number in board there is no already
        #duplicate is present in the row, col or in the 3*3 box. Easiste way to check for
        #by storing all row , col and box enteries in a set and check for duplcate
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)  #key--> r//3,c//3
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue
                if (num in rows[r] or num in cols[c] or num in squares[(r//3,c//3)]):
                    return False
                rows[r].add(num)
                cols[c].add(num)
                squares[(r//3,c//3)].add(num)
        return True
scaler = Solution()
A = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(scaler.isValidSudoku(A))

