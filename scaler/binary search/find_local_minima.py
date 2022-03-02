'''
Given an array of N distinct, wlwmwent, find any of the local minima, (number shall be smaller than, available
neighbour)
if A[i] is local minima then, A[i-1] < A[i] <A[i+1]
5 6 8 7 10
ansser = 7

'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        if A[0] < A[1]:
            return A[0]
        if A[N-1] < A[N-2]:
            return A[N-1]
        L = 1
        R = N - 2
        while L <= R:
            print (L,R)
            mid = (L+R) //2
            if (A[mid] < A[mid-1]) and (A[mid] < A[mid+1]):
                return A[mid]
            elif A[mid -1] < A[mid]:
                R = mid - 1
            else:
                L = mid + 1

scaler = Solution()
A=[9,8,3,7,6,4,1,5]
print (scaler.solve(A))
