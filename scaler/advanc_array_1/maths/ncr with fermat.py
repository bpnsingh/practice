class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    global cache
    cache = {}
    def pow(self, A, B, C):
        # any power of 0 is alwys zero
        if A == 0:
            return 0
        # its to check if power becomes zero
        if B == 0:
            return 1
        A = A % C
        # deviding A ^ B into 2 halfs
        half_power = self.pow(A, B // 2, C)
        half_ansr = ((half_power * half_power) % C)
        if B % 2 != 1:
            return (half_ansr % C)
        else:
            return ((half_ansr * A) % C)

    def fact(self, A):
        if A in cache:
            return cache[A]
        if A == 0:
            value = 1
        else:
            value = A * self.fact(A - 1)
        cache[A] = value
        return value

    def solve(self, A, B, C):

        # n! % P 1st
        first_term = self.fact(A) % C
        # fact(n-r)^C-2
        second_term = self.pow(self.fact(A - B), C - 2, C)
        third_term = self.pow(self.fact(B), C - 2, C)
        return (first_term * second_term * third_term) % C

scaler = Solution()
A = 5
B = 2
C = 13
print (scaler.solve(A, B, C))