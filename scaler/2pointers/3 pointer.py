'''
Given 3 sorted arrays, choose 3 values, from each array
such that, max(a,b,c) - min(a,b,c) is minimum
A=[5,10,17,20,21,24]
B = [-1,1,9,16,18,23,35]
C=[-8,-2,6,11,15,19,25]
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B,C):
        '''
        Approach to get the min diffrence of a-b , a should be minimised and b should be maximised,
        given input array is sorted, we can not get lesser value of a, so we will focus on to maximise b
        by selecting minimum from triplets
        '''
        ans = 10 ** 6 #int_max value
        P1=P2=P3 =0
        while (P1<len(A) and P2 < len(B)) and P3<(len(C)):
            max_3 = max(A[P1],B[P2],C[P3])
            min_3 = min(A[P1],B[P2],C[P3])
            temp = max_3 - min_3
            ans = min(ans,temp)
            if min_3 == A[P1]:
                P1+=1
            elif min_3 == B[P2]:
                P2+=1
            else:
                P3+=1
        return ans




scaler = Solution()
A=[5,10,17,20,21,24]
B = [-1,1,9,16,18,23,35]
C=[-8,-2,6,11,15,19,25]
print(scaler.solve(A,B,C))

