'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
Given an integer A, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
The final list should be generated in such a way that the indices of the queens in each list should be in reverse lexicographical order.
Problem Constraints
1 <= A <= 10



Input Format
First argument is an integer n denoting the size of chessboard



Output Format
Return an array consisting of all distinct solutions in which each element is a 2d char array representing a unique solution.



Example Input
Input 1:

A = 4
Input 2:

A = 1


Example Output
Output 1:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],
["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Output 1:

[
 [Q]
]

'''

class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        column = set()
        left_dia = set() #r+c
        right_dia = set() #r-c
        result = []
        board = [["."]*A for i in range(A)]

        def backtrack(row):
            if row == A:
                copy = ["".join(r) for r in board]
                result.append(copy)
                return
            for c in range(A):
                if c in column or (row+c) in left_dia or (row - c) in right_dia:
                    continue
                column.add(c)
                left_dia.add(c+row)
                right_dia.add(row - c)
                board[row][c] = "Q"
                backtrack(row+1)
                column.remove(c)
                left_dia.remove(row+c)
                right_dia.remove(row-c)
                board[row][c] = "."
        backtrack(0)
        return result

scaler = Solution()
A = 4
print(scaler.solveNQueens(A))

