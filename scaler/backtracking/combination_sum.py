'''
Count number of subsets with given some K
'''

class Solution:
    def subset_sum(self,A,K,index,sum,temp_list,ans):
        if sum > K:
            return
        if sum == K:
            if temp_list not in ans:
                ans.append(temp_list[:])
            return
        if index == len(A):
            return
        sum += A[index]
        temp_list.append(A[index])
        self.subset_sum(A, K, index, sum, temp_list, ans)
        self.subset_sum(A,K,index+1,sum,temp_list,ans)
        sum -= A[index]
        temp_list.pop()
        self.subset_sum(A, K, index + 1, sum,temp_list, ans)

    def combinationSum(self,A,K):
        A.sort()
        ans = []
        temp_list = []
        self.subset_sum(A,K,0,0,temp_list,ans)
        return sorted(ans)



scaler = Solution()
A = [2, 3, 6, 7]
K = 7
print (scaler.combinationSum(A,K))