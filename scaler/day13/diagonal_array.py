def diagonal_sqaure_lr(A):
    N= len(A)
    for i in range(N):
        print (A[i][i])

def diagonal_sqaure_rl(A):
    N= len(A)
    i = 0
    j = N-1
    while (i < N) & (N-1 > 0):
        #print (i,j)
        print (A[i][j])
        i+=1
        j-=1

if __name__ == '__main__':
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    #diagonal_sqaure_lr(A)
    diagonal_sqaure_rl(A)