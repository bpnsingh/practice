'''
Given a 2D matrix of 1s and 0s, where each row is sorted , find which row has max 1s.

'''

def solve(A):
    N = len(A)
    M = len(A[0])
    i=0
    j=M-1
    ans = -1
    #print(N,M,i,j)
    while((i < N ) & (j > -1)):
        #print(i,j)
        if A[i][j]==1:
            j=j-1
            ans = i
        if A[i][j] == 0:
            i = i+1
    return ans+1

if __name__ == '__main__':
    A = [[0, 0, 0, 1, 1, 1],[0,0, 0, 1, 1, 1],[0, 0, 1, 1, 1, 1]]
    print (solve(A))

