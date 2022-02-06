'''
Given N array elements, check if there exist a subset with sum K
A= [3,-1,0,6,2,-3,5]
K = 10
Output: True

'''

def check_set_bit(N,pos):
    if (N>>pos) & 1 == 1:
        return True
    else:
        return False

def subset_sum(A,K):
    N = len(A)
    for i in range(1<<N):
        temp_sum = 0
        for j in range(1,N):
            if check_set_bit(i,j):
                temp_sum += A[j]
        if temp_sum == K:
            return True
    return False

if __name__ == '__main__':
    A = [3, -1, 0, 6, 2, -3, 5]
    K = 10
    K1= 100
    print(subset_sum(A,K))
    print(subset_sum(A, K1))
