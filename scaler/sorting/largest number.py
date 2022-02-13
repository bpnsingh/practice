from functools import cmp_to_key

def fun(x,y):
    if x+y <= y+x:
        return 1
    return -1

class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        B = list(map(str,A))
        B = sorted(B,key=cmp_to_key(fun))
        largestNumber = ''.join(B)
        if largestNumber[0] == '0':
            return '0'
        else:
            return largestNumber

scaler = Solution()
A = [3, 30, 34, 5, 9]
print (scaler.largestNumber(A))