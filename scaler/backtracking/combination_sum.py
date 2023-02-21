'''
Count number of subsets with given some K
'''

class Solution:
    # def subset_sum(self,A,K,index,sum,temp_list,ans):
    #     if sum > K:
    #         return
    #     if sum == K:
    #         if temp_list not in ans:
    #             ans.append(temp_list[:])
    #         return
    #     if index == len(A):
    #         return
    #     sum += A[index]
    #     temp_list.append(A[index])
    #     self.subset_sum(A, K, index, sum, temp_list, ans)
    #     self.subset_sum(A,K,index+1,sum,temp_list,ans)
    #     sum -= A[index]
    #     temp_list.pop()
    #     self.subset_sum(A, K, index + 1, sum,temp_list, ans)
    def subset_sum(self,array,K,index,currentSum):
        if index == len(array):
            if K == currentSum:
                return 1
            else:
                return 0
        currentSum = currentSum + array[index]
        x = self.subset_sum(array,K,index+1,currentSum)
        currentSum = currentSum - array[index]
        y = self.subset_sum(array, K, index+1, currentSum)
        return  x+y

    def combinationSum(self,A,K):
        return  self.subset_sum(A,K,0,0)



scaler = Solution()
A = [5, 2, 7]
K = 7
print (scaler.combinationSum(A,K))