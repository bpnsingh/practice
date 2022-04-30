# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def inorderTraversal(self, A):
        stack = []
        ans = []
        node = A
        while len(stack) > 0 or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                ans.append(node.val)
                node = node.right
        return ans

    def solve(self, A, B):
        lista = []
        listb = []
        lista = self.inorderTraversal(A)
        listb = self.inorderTraversal(B)
        print(lista)
        print(listb)

        set_b = set(listb)
        ans = 0
        for num in lista:
            if num in set_b:
                ans += num
        return ans



