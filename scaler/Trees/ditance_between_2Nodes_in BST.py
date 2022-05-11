'''
Given a binary search tree.
Return the distance between two nodes with given two keys B and C. It may be assumed that both keys exist in BST.
NOTE: Distance between two nodes is number of edges between them.
Problem Constraints
1 <= Number of nodes in binary tree <= 1000000
0 <= node values <= 109
Input Format
First argument is a root node of the binary tree, A.
Second argument is an integer B.
Third argument is an integer C.
Output Format
Return an integer denoting the distance between two nodes with given two keys B and C
Example Input
Input 1:
    
         5
       /   \
      2     8
     / \   / \
    1   4 6   11
 B = 2
 C = 11
Input 2:
    
         6
       /   \
      2     9
     / \   / \
    1   4 7   10
 B = 2
 C = 6
Example Output
Output 1:
 3
Output 2:
 1
Example Explanation
Explanation 1:
 Path between 2 and 11 is: 2 -> 5 -> 8 -> 11. Distance will be 3.
Explanation 2:
 Path between 2 and 6 is: 2 -> 6. Distance will be 1
Approach:
Caculate the LCA of B and C and then find the distance between LCA to B and LCA to C

'''
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def get_distance(self,root,A):
        if A is None:
            return None
        if root.val == A:
            return 0
        if A < root.val:
            return 1 + self.get_distance(root.left,A)
        else:
            return 1 + self.get_distance(root.right, A)

    def LCA(self,root,A,B):
        if A is None:
            return None
        if A < root.val and B < root.val:
            self.LCA(root.left,A,B)
        elif A > root.val and B > root.val:
            self.LCA(root.right, A, B)
        else:
            return self.get_distance(root,A) + self.get_distance(root,B)
    def solve(self, A, B, C):
        return self.LCA(A,B,C)

