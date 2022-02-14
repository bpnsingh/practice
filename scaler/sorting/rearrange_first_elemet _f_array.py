'''
Given an array of N elements, rearrange the array such that, A[0] should go to its sorted postion in array.
All the elements less than or equal should be in right side and all the elements, grater should be on left side
After arrangement return index of A[0]
A = [10,3,8,15, 6, 12,2,18,7,1]
op = 6
'''
class Solution:
    # @param A : list of integers
    def solve(self, A):
        N = 10
        P1 = 1
        P2 = 9
        #we are going to use 2 pointer method
        while P1 <= P2:
            print(P1,P2)
            if A[P1] <= A[0]:
                P1 += 1
            elif A[P2] > A[0]:
                P2 -= 1
                print (P2)
            else:
                #swap
                A[P1],A[P2] = A[P2],A[P1]
                P1 +=1
                P2 -=1
        #swap first number
        A[0],A[P1-1] = A[P1-1],A[0]
        return A

scaler = Solution()
A = [10,3,8,15,6,12,2,18,7,1]
print (scaler.solve(A))