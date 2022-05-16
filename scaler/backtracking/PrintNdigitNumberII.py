'''
Print All N digit numbers using {1,2,3,4,5}
'''
import copy
class Solution:
    def generate(self,N,number,index):
        if N == 0:
            print (number)
            return
        for digit in range(1,6):
            number[index] = digit
            self.generate(N-1,copy.deepcopy(number),index+1)

    def solve(self,N):
        number = [0]*N
        index = 0
        self.generate(N,number,index)

scaler = Solution()
scaler.solve(3)