'''
You are given two matrices A & B of same size, you have to return another matrix which is the sum of A and B.
Problem Constraints
1 <= A.size(), B.size() <= 1000

1 <= A[i].size(), B[i].size() <= 1000

1 <= A[i][j], B[i][j] <= 1000
Input Format
First argument is vector of vector of integers representing matrix A.
Second argument is vecotor of vector of integers representing matrix B.
Output Format
You have to return a vector of vector of integers after doing required operations.

Example Input

Input 1:

A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
B = [[9, 8, 7],[6, 5, 4],[3, 2, 1]]


Example Output

Output 1:

[[10, 10, 10], [10, 10, 10], [10, 10, 10]]


Example Explanation

Explanation 1:

A + B = [[1+9, 2+8, 3+7],[4+6, 5+5, 6+4],[7+3, 8+2, 9+1]] = [[10, 10, 10], [10, 10, 10], [10, 10, 10]].
'''
def sum_matrices(A,B):
    ans=[]
    rows = len(A)
    columns = len(A[0])
    #lets iterate through both A and B
    for row in range(rows):
        column_list=[]
        for column in range(columns):
            sum = A[row][column] + B[row][column]
            column_list.append(sum)
        ans.append(column_list)
    return ans

if __name__ == '__main__':
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    A=[[6],[2],[3],[10],[1],[3]]
    B=[[6],[7],[3],[8],[1],[2]]
    print(sum_matrices(A,B))

