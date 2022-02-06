class Solution:
    # @param A : list of integers
    # @return an integer
    def gcd(self,A,B):
        if A ==0:
            return B
        else:
            return self.gcd(B%A,A)

    def solve(self, A):
        N = len(A)
        ans = 0
        for i in range(N):
            skip_number = A[i]
            print ("skipping {}".format(skip_number))
            curr_gcd = 0
            for j in range(N):
                if A[j] == skip_number:
                    continue
                else:
                    #As gcd(0,A) = A
                    curr_gcd = self.gcd(curr_gcd,A[j])
                    print (curr_gcd)
            ans = max(curr_gcd,ans)
        return ans
scaler = Solution()
A=[3,9,6,8,3]
print(scaler.solve(A))