class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        mod = 1000003
        N = len(A)
        fact = []
        fact_num = 1
        ans = 1
        for i in range(N + 1):
            if i == 0:
                fact.append(1)
            else:
                fact_num = (fact_num * i) % mod
                fact.append(fact_num)
        print (fact)
        for i in range(N):
            cnt = 0
            for j in range(i + 1, N):
                if ord(A[i]) > ord(A[j]):
                    cnt += 1
            print (i,cnt)
            ans += (cnt * fact[N - i - 1]) % mod
        return (ans + 1) % mod

scaler = Solution()
A= 'acb'
print(scaler.findRank(A))


