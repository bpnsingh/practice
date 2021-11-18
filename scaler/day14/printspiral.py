def print_spiral(A):
    T = 0
    B = len (A) - 1
    L = 0
    R= len(A[0]) -1
    print(T,B,L,R)
    while(B>=T):
        for k in range(L,R+1):
            print(A[T][k])
        T+=1
        for k in range(T,B+1):
            print(A[k][R])
        R-=1
        for k in range(R,L-1,-1):
            print(A[B][k])
        B-=1
        for k in range(B,T-1,-1):
            print(A[k][L])
        L += 1

if __name__ == '__main__':
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    A = [[1, 2, 3,4 ], [5 , 6, 7, 8 ], [9,10,11,12], [13, 14,15,16]]
    print_spiral(A)