'''
Given an array of integers A. There is a sliding window of size B, moving from the very left of the array to the very right. You can only see the B numbers in the window. Each time the sliding window moves rightwards by one position. You have to find the maximum for each window.
Return an array C, where C[i] is the maximum value in the array from A[i] to A[i+B-1].
Refer to the given example for clarity.
NOTE: If B > length of the array, return 1 element with the max of the arra
Input 1:

 A = [1, 3, -1, -3, 5, 3, 6, 7]
 B = 3
Input 2:
 A = [1, 2, 3, 4, 2, 7, 1, 3, 6]
 B = 6

Example Output
Output 1:
 [3, 3, 5, 5, 6, 7]
Output 2:
 [7, 7, 7, 7]
'''


from collections import deque
class DQ:
    def __init__(self):
        self.buffer = deque()
    def top(self):
        return self.buffer[-1]
    def front(self):
        return self.buffer[0]

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        Q = DQ()
        ans = []
        N = len(A)
        for i in range(N):
            if i-B >= 0:
                if Q[0] == A[i-B]:
                    Q.popleft()
            while Q and Q[-1] < A[i]:
                Q.pop()
            Q.append(A[i])
            if i >= B-1 and Q:
                ans.append(Q[0])
        return ans



scaler = Solution()
A = [1, 3, -1, -3, 5, 3, 6, 7]
B = 3
print (scaler.slidingMaximum(A,B))


