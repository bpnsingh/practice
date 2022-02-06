class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        N = len(A)
        # replace all -ve and zero numbers with N+1
        for i in range(N):
            if A[i] < 1:
                A[i] = N + 1

        for i in range(N):
            index = abs(A[i])
            if (index >= 1) and (index <= N):
                j = index - 1
                A[j] = -1 * abs(A[j])
                #print(i,j,A[i],A[j])
                #print(A)
        #print (A)
        for i in range(N):
            if A[i] < 0:
                pass
            else:
                return i + 1

scaler = Solution()
A = [2,3,1,2]
print(scaler.firstMissingPositive(A))