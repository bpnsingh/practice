'''
Given sorted array of N elements, find the floor of given target, K
A = [-5,2,3,6,9,10,11,14,18]
K=20   op=18
K =2   op = 2
K = 5  op = 3
K =12  op =11
'''

def get_floor(A,K):
    N = len(A)
    L = 0
    R = N-1
    while L <= R:
        mid = (L+R)//2
        if A[mid] == K:
            return A[mid]
        elif A[mid] < K:
            ans = A[mid]
            L = mid + 1
        else:
            R = mid - 1
    return ans

if __name__ == '__main__':
    A = [-5, 2, 3, 6, 9, 10, 11, 14, 18]
    print (get_floor(A,20))
    print(get_floor(A, 2))
    print(get_floor(A, 5))
    print(get_floor(A, 12))