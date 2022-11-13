class Solution:
    def __init__(self):
        # initialise sets for saving the numbers filled in row, col, box
        self.row_num_set = set()
        self.col_num_set = set()
        self.box_num_set = set()
    def next_empty_position(self, matrix, position):
        for row in range(9):
            for col in range(9):
                # Free position is '.'
                if matrix[row][col] == '.':
                    position[0] = row
                    position[1] = col
                    return True
        # no free location found after complete iteration
        return False
    def is_valid_entry(self, row, col, num):
        box_number = (row // 3) * 3 + (col // 3)
        if (row, num) not in self.row_num_set and \
 \
                (col, num) not in self.col_num_set and \
 \
                (box_number, num) not in self.box_num_set:
            # update all the sets, add the new number to all sets
            self.row_num_set.add((row, num))
            self.col_num_set.add((col, num))
            self.box_num_set.add((box_number, num))
            return True
        else:
            return False
    def sudoku_solver(self, matrix):
        # start with row=0, col=0
        position = [0, 0]
        # base condition
        # if there are no empty positions return True
        if not self.next_empty_position(matrix, position):
            return True
        row = position[0]
        col = position[1]
        # Check with all numbers from 1-9 at the given position
        for i in range(1, 10):
            if self.is_valid_entry(row, col, i):
                # enter the number at that position
                matrix[row][col] = i
                # and check for the next position now
                if self.sudoku_solver(matrix):
                    return True
                # backtrack
                # remove the entries from all the sets
                box_number = (row // 3) * 3 + (col // 3)
                self.row_num_set.remove((row, i))
                self.col_num_set.remove((col, i))
                self.box_num_set.remove((box_number, i))
                # undo the changes for the current row, col
                matrix[row][col] = '.'
        # After checking for all numbers 1-9, didnt find a solution
        return False
    # @param A : list of list of chars
    def solveSudoku(self, A):
        # update the row, col, box sets first
        for row in range(9):
            for col in range(9):
                if A[row][col] != '.':
                    self.row_num_set.add((row, int(A[row][col])))
                    self.col_num_set.add((col, int(A[row][col])))
                    # box number 0-8 , -> 0 1 2, 3 4 5, 6 7 8
                    box_number = (row // 3) * 3 + (col // 3)
                    self.box_num_set.add((box_number, int(A[row][col])))
        self.sudoku_solver(A)
        return A