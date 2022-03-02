class Solution:
    # @param A : list of integers
    # @return an integer
    def count(self, A):
        min_a = min(A)
        max_a = max(A)
        N = max_a - min_a + 1
        frq_array=[0]*(N+1)
        for num in A:
            frq_array[num+max_a] += 1
        print (frq_array)
        ans = []
        for i in range(N+1):
            while frq_array[i] > 0:
                ans.append(i-max_a)
                frq_array[i] -= 1
        return ans




scaler = Solution()
A = [1,2,1,2,1,-1,-1,1,1,2,2 ]
print (scaler.count(A))