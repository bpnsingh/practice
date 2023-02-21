'''
Count minimum distance between dulpciates elemnts
A = [1,2,3,6,1,2,3,2,1]
ans = 2
'''
class Solution:
    def solve(self,A):
        #create freq_map of element and recent index
        N  = len(A)
        ans =N
        freq_map = dict()
        for index,num in enumerate(A):
            if num not in freq_map:
                #if fist occurance then update dict with element aganist its index
                freq_map[num] = index
            else:
                #if its duplicate, get the difference of current and last found index
                temp = index-freq_map[num]
                ans = min(temp,ans)
                #update latest index in dict
                freq_map[num] = index
        return ans

scaler = Solution()
A= [1,2,3,6,1,2,3,2,1]
print(scaler.solve(A))
