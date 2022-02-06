class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        r1 = 0
        r2 = 0
        r3 = 0
        r4 = 0
        ans = 0
        for num in A:
            if num % 4 == 1:
                r1 += 1
            elif num % 4 == 2:
                r2 += 1
            elif num % 4 == 3:
                r3 += 1
            else:
                r4 += 1
        #print (r1,r2,r3,r4)
        if r4 == N:
            return 0

        ans += min(r1, r3)
        r1 = r1 - ans
        r3 = r3 - ans
        r1r3 = max(r1, r3)
        if r1r3 % 2 != 0:
            return -1
        ans += r1r3//2
        r2 = r2 + r1r3 // 2
        if r2 % 2 != 0:
            return -1
        ans += r2 // 2
        return ans

scaler = Solution()
A = [ 1, 3, 3, 3, 2, 2, 2, 2, 2 ]
print(scaler.solve(A))
