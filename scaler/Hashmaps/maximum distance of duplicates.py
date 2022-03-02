'''
Count maximum distance between dulpciates elemnts
A = [1,2,3,6,1,2,3,2,qwee]
ans = 2
'''
class Solution:
    def solve(self,A):
        #create freq_map of element and recent index
        N  = len(A)
        ans =0
        freq_map = dict()
        for i in range(N):
            if A[i] not in freq_map:
                #if fist occurance then update dict with element aganist its index
                freq_map[A[i]] = i
            else:
                #if its duplicate, get the difference of current and last found index
                temp = i-freq_map[A[i]]
                ans = max(temp,ans)
                #don need to update latest index in dict
        return ans

scaler = Solution()
A= [1,2,3,6,1,2,3,2,1]
print(scaler.solve(A))
