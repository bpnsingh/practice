'''
Given an array of size n, find the majority element. The majority element is the element that appears more than floor(n/2) times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example :

Input : [2, 1, 2]
Return  : 2 which occurs 2 times which is greater than 3/2.
'''

def majority(A):
    N = len(A)
    maj = None
    freq = 0
    for i in range(N):
        if maj == None:
            maj = A[i]
            freq = 1
        elif A[i] == maj:
            freq += 1
        else:
            freq -= 1
            if freq == 0:
                maj = None
    cnt = 0
    for num in A:
        if num == maj:
            cnt += 1
    if cnt > (N//2):
        return maj

if __name__ == '__main__':
    A=[2, 1, 2]
    print (majority(A))