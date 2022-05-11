class nodeinfo:
    def __init__(self,isBST,maxima,minima):
        self.isBST = isBST
        self.maxima = maxima
        self.minima = minima

class Solution:
    def isBSTUtil(self, root,maxima,minima):
        if root is None:
            return nodeinfo(True,float('-inf'),float('inf'))
        linfo = self.isBSTUtil(root.left,maxima,minima)
        rinfo = self.isBSTUtil(root.right,maxima,minima)
        if linfo.isBST and rinfo.isBST and (root.val > linfo.maxima and root.val < rinfo.minima):
            return nodeinfo(True,max(root.val,linfo.maxima,rinfo.maxima),min(root.val,linfo.minima,rinfo.minima))
        else:
            return nodeinfo(False, max(root.val, linfo.maxima, rinfo.maxima), min(root.val, linfo.minima, rinfo.minima))

    def isValidBST(self, A):
        res = self.isBSTUtil(A,float('inf'),float('-inf'))
        return int(res.isBST)