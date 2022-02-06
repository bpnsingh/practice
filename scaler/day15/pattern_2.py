'''
1 0 0

1 2 0

1 2 3


'''

def solve(A):
    for i in range(1, A + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        for zeros in range(1,A-i+1):
            print (0, end=" ")
        print()

if __name__ == '__main__':
    A = 3
    solve(A)
