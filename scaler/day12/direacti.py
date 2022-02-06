class Solution:
    # @param A : list of integers
    # @return an integer
    def psum_even(self, A):
        N = len(A)
        ans = [A[0], A[0]]
        for i in range(2, N):
            temp = ans[-1]
            if i % 2 == 0:
                temp += A[i]
            ans.append(temp)
        return ans

    def psum_odd(self, A):
        N = len(A)
        ans = [0, A[1]]
        for i in range(2, N):
            temp = ans[-1]
            if i % 2 != 0:
                temp += A[i]
            ans.append(temp)
        return ans

    def solve(self, A):
        # After removing any elemt from any index, odd indexed element shall become even indexed and vice versa
        # letcaulate prefix_sum for odd and even indexed elemnts
        N = len(A)
        even_index_sum = self.psum_even(A)
        odd_index_sum = self.psum_odd(A)
        print (even_index_sum)
        print (odd_index_sum)
        cnt = 0
        for i in range(N):
            if i == 0:
                even_sum = odd_index_sum[-1]
                odd_sum = even_index_sum[-1] - even_index_sum[0]
            else:
                even_sum = even_index_sum[i - 1] + odd_index_sum[-1] - odd_index_sum[i]
                odd_sum = odd_index_sum[i - 1] + even_index_sum[-1] - even_index_sum[i]
            if even_sum == odd_sum:
                cnt += 1
        return cnt

scaler = Solution()
A = [4,3,2,7,6,-2]
print (scaler.solve(A))