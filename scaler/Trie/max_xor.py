'''
Problem Description
Given an array of integers A, find and return the maximum result of A[i] XOR A[j], where i, j are the indexes of the array.
Problem Constraints
1 <= length of the array <= 100000
0 <= A[i] <= 109
Input Format
The only argument given is the integer array A.
Output Format
Return an integer denoting the maximum result of A[i] XOR A[j].
Example Input
Input 1:
 A = [1, 2, 3, 4, 5]
Input 2:
 A = [5, 17, 100, 11]
Example Output
Output 1:
 7
Output 2:
 117
Example Explanation
Explanation 1:
 Maximum XOR occurs between element of indicies(0-based) 1 and 4 i.e. 2 ^ 5 = 7.
Explanation 2:
 Maximum XOR occurs between element of indicies(0-based) 1 and 2 i.e. 17 ^ 100 = 117.
'''
class Trie:
    def __init__(self):
        self.hashmap = {}
        self.end = False

class Solution:
    # @param A : list of integers
    # @return an integer
    def get_set_bit(self,num,pos):
        mask = 1<<pos
        if bool(num & mask):
            return 1
        else:
            return 0
    def insert(self,root,num):
        curr = root
        for i in range(31,-1,-1):
            bit = self.get_set_bit(num,i)
            if bit not in curr.hashmap:
                new_node = Trie()
                curr.hashmap[bit] = new_node
            curr = curr.hashmap[bit]
        curr.end = True
    def find_xor(self,root,num):
        curr = root
        ans = 0
        for i in range(31,-1,-1):
            bit = self.get_set_bit(num, i)
            c_bit = 1^bit
            if c_bit in curr.hashmap:
                ans += (1 << i)
                curr = curr.hashmap[c_bit]
            else:
                curr = curr.hashmap[bit]
        return ans

    def solve(self, A):
        ans = -10**9
        root = Trie()
        for num in A:
            self.insert(root,num)
        for num in A:
            temp = self.find_xor(root,num)
            ans = max(temp,ans)
        return ans
scaler = Solution()
A = [1, 2, 3, 4, 5]
A = [5, 17, 100, 11]
print(scaler.solve(A))

