class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        '''
        N = len(A)
        ans=[]
        for start_index,end_index in B:
            xor = None
            cnt = 0
            for i in range(start_index-1,end_index):
                if xor is None:
                    xor = A[i]
                else:
                    xor ^= A[i]
                if A[i] == 0:
                    cnt+=1
            ans.append([xor,cnt])
        return ans
        '''
        N = len(A)
        pre_list = [A[0]]
        for i in range(1,N):
            pre_list.append(pre_list[i-1]+A[i])
        print (pre_list)
        ans = []
        for start_index,end_index in B:
            no_of_ones = pre_list[end_index-1] - pre_list[start_index-1]
            if no_of_ones % 2 == 0:
                xor = 0
            else:
                xor = 1
            no_of_unset_bits = end_index - start_index + 1 - no_of_ones
            ans.append([xor,no_of_unset_bits])
        return ans

scaler = Solution()
A = [1,0,0,0,1]
B=[ [2,4],
    [1,5],
    [3,5] ]
print (scaler.solve(A,B))