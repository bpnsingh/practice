'''
Given an array and number K , return true if theier exists a pair i,j such that i!=j
A[i] + A[j] = k
input =
2,9,11,9,15 ,K = 18
'''


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return 1 or 0
    def solve(self, A, B):
        set_a = set()
        for num in A:
            if B - num not in set_a:
                set_a.add(num)
            else:
                return True
        return False


A=[5, 10, 20, 100, 105]
B= 110
scaler = Solution()
print (scaler.solve(A,B))
A=[2,5,7]
B= 10
scaler = Solution()
print (scaler.solve(A,B))