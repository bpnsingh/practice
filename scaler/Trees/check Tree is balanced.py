class info:
    def __init__(self,isBalance,height):
        self.isBalance = isBalance
        self.height = height
class Solution:
    def checkBalance(self,A):
        if A is None:
            return info(True,-1)
        linfo = self.checkBalance(A.left)
        rinfo = self.checkBalance(A.right)
        if linfo.isBalance and rinfo.isBalance and abs(linfo.height - rinfo.height) <= 1:
            return info(True,max(linfo.height,rinfo.height)+1)
        else:
            return info(False, max(linfo.height, rinfo.height) + 1)

    def isBalanced(self, A):
        result = self.checkBalance(A)
        if result.isBalance:
            return 1
        else:
            return 0


