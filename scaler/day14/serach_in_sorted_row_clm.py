'''
Given an araay of sorted matrices, both row and columns are sorted,
check K exsist in array if yes return 1 esle return -1
'''
def solve(A, B):
    N = len(A)
    row = 0
    col = len(A[0]) - 1
    while ((row < N) & (col > -1)):
        if A[row][col] == B:
            return 1
        elif A[row][col] < B:
            row += 1
        else:
            col -= 1
    return -1
if __name__ == '__main__':
    A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    B = 2
    C = 10
    print (solve(A,B))
    print(solve(A, C))