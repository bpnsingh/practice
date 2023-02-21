'''
Count number of subsets with given some K
'''

class Solution:
    def subset_sum(self,array,K,index,currentSum,temp_list,ans):
        if index == len(array):
            if K == currentSum:
                ans.append(temp_list[:])
                return
            else:
                return
        currentSum = currentSum + array[index]
        temp_list.append(array[index])
        self.subset_sum(array,K,index+1,currentSum,temp_list,ans)
        currentSum = currentSum - array[index]
        temp_list.pop()
        self.subset_sum(array, K, index+1, currentSum,temp_list,ans)


    def combinationSum(self,A,K):
        A.sort()
        temp_list = []
        ans = []
        self.subset_sum(A,K,0,0,temp_list,ans)
        return  ans



scaler = Solution()
A = [5, 2, 7]
K = 7
print (scaler.combinationSum(A,K))