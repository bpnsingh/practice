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
        for i in range(ord('a'),ord('z')+1):
            map_f[chr(i)] = 0
        for c in A:
            map_f[c] += 1
        return map_f

    def remove_ch(self,ch,map_f):
        map_f[ch] -= 1

    def add_ch(self,ch,map_f):
        if ch not in map_f:
            map_f[ch] = 1
        else:
            map_f[ch] += 1

    def solve(self, A, B):
        cnt = 0
        M  = len(A)
        N  = len(B)
        #if length of strings which has to be checked is less than input string
        if N < M:
            return -1
        req_map = self.frq_map(A)
        current_map = self.frq_map(B[0:M])
        if req_map == current_map:
            cnt += 1
        for i in range(1,N-M+1):
            self.remove_ch(B[i-1],current_map)
            self.add_ch(B[i+M-1],current_map)
            #print (current_map)
            if req_map == current_map:
                cnt+=1

        return cnt

scaler = Solution()
A = "abc"
B = "abcbacabc"
#A = "p"
#B = "pccdpeeooadeocdoacddapacaecb"
print (scaler.solve(A,B))