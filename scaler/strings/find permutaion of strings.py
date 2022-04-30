'''
You are given two strings A and B of size N and M respectively.
You have to find the count of all permutations of A present in B as a substring. You can assume a string will have only lowercase letters.
'''

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def frq_map(self,A):
        map_f = dict()
        for c in A:
            if c not in map_f:
                map_f[c] = 1
            else:
                map_f[c] += 1
        return map_f
    def solve(self, A, B):
        cnt = 0
        M  = len(A)
        N  = len(B)
        req_map = self.frq_map(A)
        current_map = self.frq_map(B[0:M])
        if req_map == current_map:
            cnt += 1
        for i in range(1,N-M+1):
            
        return cnt

scaler = Solution()
A = "abc"
B = "abcbacabc"
print (scaler.solve(A,B))