# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None
sum = -10**10
class Solution:
    # @param A : root node of tree
    # @return an integer
    def pathsum(self,root):
        if root == None:
            return 0
        global sum
        l = max(0,self.pathsum(root.left))
        r = max(0,self.pathsum(root.right))
        l = max(0,l)
        r = max(0,r)
        sum = max(sum,l+r+root.val)
        return root.val+max(l,r)

    def maxPathSum(self, A):
        global sum
        ans = self.pathsum(A)
        return sum
