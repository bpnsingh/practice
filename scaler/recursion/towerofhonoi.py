'''
Print tower of honoi movement
'''

class Solution:
    # @param A : integer
    def twh(self,N,src,dst,tmp):
        if N == 0:
            return
        self.twh(N-1,src,tmp,dst)
        print("{}-->{}".format(src,dst))
        self.twh(N - 1, tmp, dst, src)

scaler = Solution()
scaler.twh(3,'A','C','B')