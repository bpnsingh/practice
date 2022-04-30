'''
Misha loves eating candies. She has been given N boxes of Candies.
She decides that every time she will choose a box having the minimum number of candies, eat half of the candies and put the remaining candies in the other box that has the minimum number of candies.
Misha does not like a box if it has the number of candies greater than B so she won't eat from that box. Can you find how many candies she will eat?
NOTE 1: If a box has an odd number of candies then Misha will eat the floor(odd / 2).
NOTE 2: The same box will not be chosen again.
Problem Constraints
1 <= N <= 105
1 <= A[i] <= 105
1 <= B <= 106
Example Input
Input 1:
 A = [3, 2, 3]
 B = 4
Input 2:
 A = [1, 2, 1]
 B = 2
Example Output
Output 1:
 2
Output 2:
 1
'''
import heapq
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        ans = 0
        heapq.heapify(A)
        N = len(A)
        while A and A[0] <= B:
            box = heapq.heappop(A)
            ans += box//2
            rem_candies = box - (box//2)
            if A:
                temp = heapq.heappop(A)
                heapq.heappush(A,temp+rem_candies)
        return ans
scaler = Solution()
#A=[3,2,3]
#B = 4
A = [ 705 ]
B = 895

print(scaler.solve(A,B))