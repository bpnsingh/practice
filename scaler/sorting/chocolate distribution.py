'''
Given an array A of N integers where each value represents number of chocolates in a packet.

i-th can have A[i] number of chocolates.

There are B number students, the task is to distribute chocolate packets following below conditions:

1. Each student gets one packet.
2. The difference between the number of chocolates in packet with maximum chocolates and packet with minimum chocolates given to the students is minimum.
Return the minimum difference (that can be achieved) between maximum and minimum number of chocolates distributed.
'''


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        ans = 10**7
        A.sort()
        if B == 0 or N == 0 :
            return 0
        for i in range(N-B+1):
            diff = A[B+i-1] - A[i]
            if diff < ans:
                ans = diff
        return ans

scaler = Solution()
A = [3, 4, 1, 9, 56, 7, 9, 12]
B = 5
print(scaler.solve(A,B))