'''
Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.



Problem Constraints

1 <= A <= 1000



Input Format

First and only argument is integer A


Output Format

Return a 2-D matrix which consists of the elements in spiral order.



Example Input

Input 1:

1
Input 2:

2


Example Output

Output 1:

[ [1] ]
Output 2:

[ [1, 2], [4, 3] ]

'''
import cnt as cnt


def solve(A):
    ans=[]
    #create an empty square matrix
    for i in range(A):
        ans.append([0]*A)
    T = 0
    B = A - 1
    L = 0
    R = A - 1
    cnt =1
    #print(T, B, L, R)
    while (B >= T):
        for k in range(L, R + 1):
            ans[T][k] = cnt
            cnt += 1
        T += 1
        for k in range(T, B + 1):
            ans[k][R] = cnt
            cnt += 1
        R -= 1
        for k in range(R, L - 1, -1):
            ans[B][k] = cnt
            cnt += 1
        B -= 1
        for k in range(B, T - 1, -1):
            ans[k][L] = cnt
            cnt += 1
        L += 1
    return ans
if __name__ == "__main__":
    A = 2
    print (solve(A))