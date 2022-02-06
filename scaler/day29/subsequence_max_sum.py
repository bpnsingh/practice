'''
Given N array elements, calculate sum of max of every subseequence
A = [0,-2,8,4,3]
'''

def sub_max_sum(A):
    A.sort()
    N = len(A)
    sum = 0
    for i in range(N):
        print (A[i])
        sum += A[i] * (2 ** i)
    return sum

if __name__ == '__main__':
    A = [3, -1, 0, 6, 2, -3, 5]
    print(sub_max_sum(A))