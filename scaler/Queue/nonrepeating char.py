from collections import deque
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        Q = deque()
        ans = ''
        freq_char = {}
        for char in A:
            print (char, Q,ans)
            if char not in freq_char:
                freq_char[char] = 0
            freq_char[char] += 1
            Q.append(char)
            while Q and freq_char[Q[0]]>1 :
                Q.popleft()
                #Q.pop()
            if Q:
                ans += Q[0]
            else:
                ans += '#'
        return ans

A = "abadbc"
#A = "jyhrcwuengcbnuchctluxjgtxqtfvrebveewgasluuwooupcyxwgl"
scaler = Solution()
print (scaler.solve(A))