'''
Given an array A of size N, groot wants you to pick 2 indices i and j such that

1 <= i, j <= N
A[i] % A[j] is maximum among all possible pairs of (i, j).
Help Groot in finding the maximum value of A[i] % A[j] for some i, j.

Problem Constraints
1 <= N <= 100000
0 <= A[i] <= 100000'''
#brute force, time complexity is O(n^2)
def solve (A):
    mod_list = []
    j = 0
    i = 1
    for j in range(0, len(A)):
        for i in range(0,len(A)):
            mod_list.append(A[i] % A[j])
    return   max(mod_list)

# A% B is maxmimum when A<B,
#edge case, whwn N=1, return 0
#when all array elemnts are same then return 0
#Nlog(N)
def solve_sort(A):
    if len(A) == 1 or (A.count(A[0]) == len(A)):
        return 0
    else:
        return sorted(A)[-2]


def solve_opt(A):
    first=second=0
    for i in range(len(A)):
        if first < A[i]:
            second=first
            first = A[i]
        elif second < A[i] and A[i] != first:
            second = A[i]

    if second !=0:
        return second
    else:
        return 0

if __name__ == "__main__":
    print (solve_opt([ 927, 707, 374, 394, 279, 799, 878, 937, 431, 112 ]))
    print(solve_opt([927]))
    print(solve_opt([927, 927])))

