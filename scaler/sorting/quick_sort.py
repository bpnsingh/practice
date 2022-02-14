class Solution:
    # @param A : list of integers
    # @return a list of integers
    def rearrange(self, A,l,r):
        P1 = l+1
        P2 = r
        #we are going to use 2 pointer method
        while P1 <= P2:
            if A[P1] <= A[l]:
                P1 += 1
            elif A[P2] > A[l]:
                P2 -= 1
            else:
                #swap
                A[P1],A[P2] = A[P2],A[P1]
                P1 +=1
                P2 -=1
        #swap first number
        A[l],A[P1-1] = A[P1-1],A[l]
        return P1 - 1

    def quick_sort(self,A,l,r):
        #base
        if l >=r:
            return None
        index = self.rearrange(A,l,r)
        self.quick_sort(A,l,index-1)
        self.quick_sort(A, index + 1, r)

    def solve(self, A):
        l = 0
        N = len(A)
        r = N -1
        self.quick_sort(A,l,r)
        return A




scaler = Solution()
A = [10,3,8,15,6,12,2,18,7,1]
print (scaler.solve(A))