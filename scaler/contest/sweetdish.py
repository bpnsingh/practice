class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def check_prime(self, N):
        if N in range(2):
            return False
        i = 2
        while i * i <= N:
            if N % i == 0:
                return False
        return True

    def check_set_bit(self, N, pos):
        if ((N >> pos) & 1) == 1:
            return True
        else:
            return False

    def solve(self, A, B, C):
        cnt = 0
        N = len(A)
        prime_array = []
        for i in range(N):
            prime_array.append(self.check_prime(A[i]))
        for i in range(1 << N):
            sum = 0
            prime_flag = False
            for j in range(1, N):
                if self.check_set_bit(i, j):
                    if prime_array[i]:
                        prime_flag = True
                    sum += A[j]
                if sum in range(B, C + 1) and prime_flag:
                    cnt += 1
        return cnt


scaler = Solution()
A = [2, 2, 4, 5]
B = 3
C = 7
print (scaler.solve(A,B,C))