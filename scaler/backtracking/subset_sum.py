'''
Count number of subsets with given some K
'''

class Solution:
    def subset_sum(self,A,K,index,sum):
        if index == len(A):
            if sum == K:
                return 1
            else:
                return 0
        sum += A[index]
        x = self.subset_sum(A,K,index+1,sum)
        sum -= A[index]
        y = self.subset_sum(A, K, index + 1, sum)
        return x+y

    def solve(self,A,K):
        ans = self.subset_sum(A,K,0,0)
        return ans



scaler = Solution()
A = [5,2,7,4,3,1,6,-2]
K = 7
print (scaler.solve(A,K))