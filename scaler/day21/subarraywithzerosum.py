'''
Given an array of integers A, find and return whether the given array contains a non-empty subarray with a sum equal to 0.

If the given array contains a sub-array with sum zero return 1 else return 0.
Problem Constraints

1 <= |A| <= 100000

-10^9 <= A[i] <= 10^9



Input Format

The only argument given is the integer array A.



Output Format

Return whether the given array contains a subarray with a sum equal to 0.



Example Input

Input 1:

 A = [1, 2, 3, 4, 5]
Input 2:

 A = [-1, 1]


Example Output

Output 1:

 0
Output 2:

 1


Example Explanation

Explanation 1:

 No subarray has sum 0.
Explanation 2:

 The array has sum 0.
'''


class Solution:
    # @param A : list of integers
    # @return an integer
    '''
    We know that, If prefix sum of any number repeat itself , them middle elemnet sum must be zero.
    So first calculate prefix sum, and check if number is duplicate in it , if yes, return 1.
    Abovwe apporach has 2 edge case.
    if input Array has 0 in middle, then prefix sum wont repeat , to handle it , if input array has 0
    element, raise it as 1 as 0 will also counte as valid subarray
    2. If ptrfix sum has one or other element = 0 ehen also return 1.
    '''
    def get_pre_sum(self,A):
        sum = 0
        pre_sum = []
        for i in range(len(A)):
            sum += A[i]
            pre_sum.append(sum)
        return pre_sum
    def solve(self, A):
        '''if input Array has 0 in middle, then prefix sum wont repeat , to handle it , if input array has 0
    element, raise it as 1 as 0 will also counte as valid subarray
        '''
        if 0 in A:
            return 1
        pre_sum = self.get_pre_sum(A)
        '''If ptrfix sum has one or other element = 0 ehen also return 1.'''
        if 0 in pre_sum:
            return 1
        freq_map = {}
        for num in pre_sum:
            if num not in freq_map:
                freq_map[num] = 1
            else:
                freq_map[num] += 1
        '''If prefix sum of any number repeat itself , them middle elemnet sum must be zero.
    So first calculate prefix sum, and check if number is duplicate in it , if yes, return 1.'''
        for freq in freq_map.values():
            if freq > 1:
                return 1
        return 0
A = [ 1, 2, -3, 3 ]
scaler=Solution()
print(scaler.solve(A))