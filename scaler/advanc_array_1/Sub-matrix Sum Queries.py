'''
Sub-matrix Sum Queries
'''

class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @return a list of integers
    def pre_sum_mat(self,A):
        N = len(A)
        M = len(A[0])
        pre_sum = []
        # initialize prefix_sum_matrix
        for i in range(N):
            temp = []
            for j in range(M):
                temp.append(0)
            pre_sum.append(temp)
        # calculate row wise prefix_sum
        for i in range(N):
            sum = 0
            for j in range(M):
                sum += A[i][j]
                pre_sum[i][j] = sum
        # calculate column wise prefix_sum
        for j in range(M):
            sum = 0
            for i in range(N):
                sum += pre_sum[i][j]
                pre_sum[i][j] = sum
        return pre_sum

    def solve(self, A, B, C, D, E):
        #calulate Prefix_sum matrix
        psum=self.pre_sum_mat(A)
        queries = len(B)
        ans = []
        temp=0
        for i,j,p,q in zip(B,C,D,E):
            i=i-1
            j=j-1
            p=p-1
            q=q-1
            if i == 0 and j > 0:
                temp=psum[p][q] - psum[p][j-1]
            elif j == 0 and i > 0:
                temp=psum[p][q] - psum[i-1][q]
            elif i ==0 and j ==0:
                temp=psum[p][q]
            else:
                temp = psum[p][q] - psum[i-1][q] - psum[p][j-1] + psum[i-1][j-1]
            ans.append(temp)
        return ans



scaler = Solution()
'''
A = [   [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]   ]
B = [1, 2]
C = [1, 2]
D = [2, 3]
E = [2, 3]
'''
A = [[5, 17, 100, 11],
     [0, 0, 2, 8]]
B = [1, 1]
C = [1, 4]
D = [2, 2]
E = [2, 4]

print (scaler.solve(A,B,C,D,E))
