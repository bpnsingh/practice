'''
Given an array A of integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.
Example :
Input :
A : [1 5 3]
k : 2
Output :
1
as 3 - 1 = 2
'''

def solve(A,B):
    N = len(A)
    if N == 1:
        return 0
    set_a = set()
    for num in A:
        if num-B in set_a or num+B in set_a:
            return 1
        else:
            set_a.add(num)
    return 0


if __name__ == '__main__':
    A=[11, 85, 100, 44, 3, 32, 96, 72, 93, 76, 67, 93, 63, 5, 10, 45, 99, 35, 13]
    B=60
    print(solve(A,B))