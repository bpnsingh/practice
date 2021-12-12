'''
Given an array of positive integers A and an integer B, find and return first continuous subarray which adds to B.
If the answer does not exist return an array with a single element "-1".
First sub-array means the sub-array for which starting index in minimum.
Problem Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 10^9
1 <= B <= 10^9

Input 1:
A = [1, 2, 3, 4, 5]
 B = 5
Input 2
A = [5, 10, 20, 100, 105]
 B = 110
Example Output
Output 1:
 [2, 3]
Output 2:
 -1
'''


def solve(A, B):
    N = len(A)
    '''
    for i in range(N):
        for j in range(i+1,N):
            sum = 0
            for k in range(i,j+1):
                sum = sum + A[k]
            if sum == B:
                return A[i:j+1]
    '''
    #N2 solution
    pre_sum = []
    temp = 0
    for num in A:
        temp+=num
        pre_sum.append(temp)
    for i in range(N):
        for j in range(i+1,N):
            sum = pre_sum[j] - pre_sum[i]
            print (sum)




    return [-1]
if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    B = 5
    print (solve(A,B))