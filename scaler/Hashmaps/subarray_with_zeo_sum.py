class Solution:
    # @param A : list of integers
    # @return an integer
    def is_duplicate_elements(self,input:list)-> bool :
        return (len(input) != len(set(input)))
    def solve(self, A):
        '''
        we take input as a list, and create prefix sum, if prefix sum array
        has any duplicate in it, means it has subarrays with zero sum.
        Also if prefix_sum has 0 , then also
        @param A:
        @return:
        '''
        prefix_sum = [0]*len(A)
        prefix_sum[0] = A[0]
        for index,num in A:
            if index == 0:
                continue
            prefix_sum[index] = prefix_sum[index-1] + num
        if 0 in prefix_sum:
            return 1

        if self.is_duplicate_elements(prefix_sum):
            return 1
        else:
            return 0

