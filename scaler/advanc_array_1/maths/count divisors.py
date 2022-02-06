class Solution:
    # @param A : list of integers
    # @return a list of integers
    def brute_force(self, A):
        ans = []
        for num in A:
            if num >= 2:
                cnt = 2
                i = 2
                while i * i <= num:
                    if num % i == 0:
                        cnt += 2
                    if i * i == num:
                        cnt -= 1
                    i += 1
            else:
                cnt = 1
            ans.append(cnt)
        return ans

    def spf_array(self, N):
        prime = []
        for i in range(N + 1):
            if i < 2:
                prime.append(0)
            else:
                prime.append(i)
        i = 2
        while i <= N:
            if i == prime[i]:
                j = i * i
                while j <= N:
                    prime[j] = min(i, prime[j])
                    j += i
            i += 1
        return prime

    def count_divisor(self, N):
        ans = 1
        spf = self.spf_array(N)
        while N > 1:
            x = spf[N]
            cnt = 0
            while (N % x == 0):
                N = N // x
                cnt += 1
            ans *= (cnt + 1)
        return ans

    def solve(self, A):
        # brute force O(N2)
        # return self.brute_force(A)
        ans = []
        for num in A:
            if num == 1:
                ans.append(1)
            else:
                ans.append(self.count_divisor(num))
        return ans

scaler = Solution()
A = [2,3,4,5]
print(scaler.solve(A))