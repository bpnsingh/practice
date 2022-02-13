class Solution:
    # @param A : list of integers
    # @return an integer
    def swap(self,A,B):
        A = A^B
        B = A^B
        A = A^B
    def indrtion_sort(self, A):
        N = len(A)
        for i in range(1,N):
            j = i-1
            while j >= 0 and A[j] > A[j+1] :
                self.swap(A[j],A[j+1])
                j -= 1
        return A

scaler = Solution()
A = [ 45, 10, 15, 25, 50 ]
print (scaler.indrtion_sort(A))