'''
Given an array of integers A of size N. Find the longest subsequence of A which is odd-even.

A subsequence is said to odd-even in the following cases:

The first element of the subsequence is odd, second element is even, third element is odd and so on. For example: [5, 10, 5, 2, 1, 4], [1, 2, 3, 4, 5]

The first element of the subsequence is even, second element is odd, third element is even and so on. For example: [10, 5, 2, 1, 4, 7], [10, 1, 2, 3, 4]

Return the maximum possible length of odd-even subsequence.

Note: An array B is a subsequence of an array A if B can be obtained from A by deletion of several (possibly, zero or all) elements.
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        odd_list = []
        even_list = []
        odd_flag = True
        for num in A:
            if num % 2 == 1:
                if odd_flag:
                    odd_list.append(num)
                    odd_flag = False
            else:
                if not odd_flag:
                    odd_list.append(num)
                    odd_flag = True
        even_flag = True
        for num in A:
            if num % 2 == 0 and even_flag:
                    even_list.append(num)
                    even_flag = False
            elif not even_flag:
                    even_list.append(num)
                    even_flag = True
        return max(len(odd_list),len(even_list))

scaler = Solution()
A=[1,2,2,5,6]
A = [12,10,28,37,43,40,14,12,48]
print (scaler.solve(A))