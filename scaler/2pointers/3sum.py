class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        ans = []
        N = len(A)
        A.sort()
        for i in range(N):
            if i > 0 and A[i] == A[i-1]:
                continue
            L = i+1
            R = N-1
            while L<R:
                threesum = A[i]+ A[L] +A[R]
                if threesum > 0:
                    R -= 1
                elif threesum < 0:
                    L +=1
                else:
                    ans.append([A[i],A[L],A[R]])
                    L+=1
                    while A[L] == A[L-1] and L<R:
                        L+=1
        return ans

scaler = Solution()
A = [ 1, -4, 0, 0, 5, -5, 1, 0, -2, 4, -4, 1, -1, -4, 3, 4, -1, -1, -3 ]
print(scaler.threeSum(A))


