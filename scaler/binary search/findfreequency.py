'''
Givrn an array of  N elements sorted in ascneding order, find the frequency of givn number K
'''
#optimal approach will be find the start and index of K and then calculate, the freq of it

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def find_start_index(self,A,B):
        N = len(A)
        L = 0
        R = N -1
        ans = -1
        while L <= R :
            mid = (L+R)//2
            if A[mid] == B:
                ans = mid
                R = mid - 1
            elif A[mid] < B :
                L = mid +1
            else:
                R = mid -1
        return ans

    def find_end_index(self, A, B):
        N = len(A)
        L = 0
        R = N - 1
        ans = -1
        while L <= R:
            mid = (L + R) // 2
            if A[mid] == B:
                ans = mid
                L = mid + 1
            elif A[mid] < B:
                L = mid + 1
            else:
                R = mid - 1
        return ans

    def searchRange(self, A, B):
        start_index=self.find_start_index(A,B)
        if start_index >= 0:
            end_index = self.find_end_index(A,B)
            return end_index -start_index + 1
        else:
            return -1






scaler = Solution()
A = [-5,-5,-3,0,0,1,1,1,5,5,5,5,5,5,9,10]
#print(scaler.searchRange(A,5))
#print(scaler.searchRange(A,10))
print(scaler.searchRange(A,-5))
#print(scaler.searchRange(A,2))

