'''
Given an array of N elements, rearrange the array such that, A[0] should go to its sorted postion in array.
All the elements less than or equal should be in right side and all the elements, grater should be on left side
After arrangement return index of A[0]
A = [10,3,8,15, 6, 12,2,18,7,1]
l = 2
r = 6
Op= [10,3,6,2,8,15,12,18,7,1]
'''
class Solution:
    # @param A : list of integers
    def solve(self, A,l,r):
        P1 = l+1
        P2 = r
        #we are going to use 2 pointer method
        while P1 <= P2:
            print(P1,P2)
            if A[P1] <= A[l]:
                P1 += 1
            elif A[P2] > A[l]:
                P2 -= 1
            else:
                #swap
                A[P1],A[P2] = A[P2],A[P1]
                P1 +=1
                P2 -=1
        #swap first number
        A[l],A[P1-1] = A[P1-1],A[l]
        return P1 - 1

scaler = Solution()
A = [10,3,8,15,6,12,2,18,7,1]
print (scaler.solve(A,2,6))