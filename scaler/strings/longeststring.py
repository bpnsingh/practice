import current as current


class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        char_set = set()
        P1 = 0
        P2 = 0
        N = len(A)
        current_len = 0
        max_length  = 0
        while  P2 < N:
            if A[P2] not in char_set:
                char_set.add(A[P2])
                current_len  = P2 - P1 + 1
                max_length = max(current_len,max_length)
                P2+=1
            else:
                while A[P1] != A[P2]:
                    char_set.remove(A[P1])
                    P1+=1
                char_set.remove(A[P1])
                P1+=1
        return max_length



scaler = Solution()
A='abcabcbb'
print (scaler.lengthOfLongestSubstring(A))