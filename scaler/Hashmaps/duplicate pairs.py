'''
Given a array of  N elements, conunt number of duplicate pairs.
A[I] == A[j]
A= [1,2,1,4,1,2,3,4,1,6]
Ans = 8
pairs 1,1

'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A):
        ans = 0
        #create freq_map
        freq_map = dict()
        for num in A:
            if num not in freq_map:
                freq_map[num] = 1
            else:
                ans += freq_map[num]
                freq_map[num] += 1
        return ans
A= [1,2,1,4,1,2,3,4,1,6]
scaler = Solution()
print (scaler.solve(A))


