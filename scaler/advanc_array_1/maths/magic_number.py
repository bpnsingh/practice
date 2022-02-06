class Solution:
    # @param A : integer
    # @return an integer
    def brute_force(self, A):
        # create prime array
        if A <= 5:
            return 0
        prime = []
        for i in range(A + 1):
            if i > 1:
                prime.append(True)
            else:
                prime.append(False)
        i = 2
        while i <= A:
            if prime[i]:
                j = i * i
                while j < A:
                    prime[j] = False
                    j = i + j
            i += 1

        # logic to get the ans
        ans = 0
        for i in range(6, A + 1):
            cnt = 0
            for j in range(2, i):
                if prime[j] and i % j == 0:
                    cnt += 1
            if cnt == 2:
                ans += 1
        return ans

    def solve(self, A):
        # create pf_array
        ans_array = [0] * (A + 1)
        i = 2
        while i <= A:
            #print(i)
            if ans_array[i] == 0:
                j = 2 * i
                while j <= A:
                    ans_array[j] += 1
                    j = i + j
            i = i + 1

        cnt = 0
        #print(ans_array)
        for value in ans_array:
            if value == 2:
                cnt += 1
        return cnt


scaler = Solution()
A =12
print (scaler.solve(A))
