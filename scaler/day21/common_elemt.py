'''
Given two integer array A and B of size N and M respectively. Your task is to find all the common elements in both the array.
NOTE:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.


Problem Constraints

1 <= N, M <= 105

1 <= A[i] <= 109



Input Format

First argument is an integer array A of size N.

Second argument is an integer array B of size M.



Output Format

Return an integer array denoting the common elements.



Example Input

Input 1:

 A = [1, 2, 2, 1]
 B = [2, 3, 1, 2]
Input 2:

 A = [2, 1, 4, 10]
 B = [3, 6, 2, 10, 10]


Example Output

Output 1:

 [1, 2, 2]
Output 2:

 [2, 10]
 '''

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def get_freq_map(self,A):
        ans ={}
        for num in A:
            if num not in ans:
                ans[num] = 1
            else:
                ans[num]+=1
        return ans

    def solve(self, A, B):
        frq_a=self.get_freq_map(A)
        frq_b=self.get_freq_map(B)
        ans=[]

        for num in frq_b:
            common_count=0
            #checking elemnt inside a list is O(n), and checking element in hasmap is O(1)
            if num in frq_a:
                common_count = min(frq_a[num],frq_b[num])
            for i in range(common_count):
                ans.append(num)
        return ans
if __name__ == '__main__':
    A = [1, 2, 2, 1]
    B = [2, 3, 1, 2]
    scaler=Solution()
    print(scaler.solve(A,B))