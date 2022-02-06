'''
Print a Pattern According to The Given Value of A.

Example: For A = 3 pattern looks like:

    1
  2 1
3 2 1
'''

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        for i in range(1, A + 1):
            for spaces in range(1, A - i + 1):
                print(" ", end=" ")
            for j in range(i,0,-1):
                print(j, end=" ")
            print()

scaler = Solution()
scaler.solve(5)

