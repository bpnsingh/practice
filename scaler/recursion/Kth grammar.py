'''
On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row A and index B, return the Bth indexed symbol in row A. (The values of B are 1-indexed.) (1 indexed).
'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if A == 1 and B == 1:
            return 0
        length = 1 << A-1
        mid = length//2
        if B <= mid:
            return self.solve(A-1,B)
        else:
            result = self.solve(A-1,B-mid)
            if result & result:
                return 0
            else:
                return 1

scaler = Solution()
for i in range(1,9):
    print(scaler.solve(4,i))