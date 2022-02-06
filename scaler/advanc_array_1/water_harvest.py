class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        N = len(A)
        ans = 0
        left_max = [0]
        right_max = []
        for i in range(N):
            right_max.append(0)
        for i in range(1,N):
            num = max(left_max[i-1],A[i-1])
            left_max.append(num)
        for i in range(N-2,-1,-1):
            right_max[i] = max(A[i+1],right_max[i+1])

        for hight,left,right in zip(A,left_max,right_max):
            dimension = min(left,right)
            building_sum = dimension - hight
            if building_sum > 0:
                ans += building_sum
        return ans

scaler = Solution()
A = [7,0,4,2,5,0,6,4,0,5]
print (scaler.trap(A))


