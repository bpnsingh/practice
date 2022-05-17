'''
Given an integer array A of size N denoting collection of numbers , return all possible permutations.
NOTE:
No two entries in the permutation sequence should be the same.
For the purpose of this problem, assume that all the numbers in the collection are unique.
Return the answer in any order
WARNING: DO NOT USE LIBRARY FUNCTION FOR GENERATING PERMUTATIONS. Example : next_permutations in C++ / itertools.permutations in python.
If you do, we will disqualify your submission retroactively and give you penalty points.
Problem Constraints
1 <= N <= 9
Input Format
Only argument is an integer array A of size N.
Output Format
Return a 2-D array denoting all possible permutation of the array.
Example Input
A = [1, 2, 3]
Example Output
[ [1, 2, 3]
  [1, 3, 2]
  [2, 1, 3] 
  [2, 3, 1] 
  [3, 1, 2] 
  [3, 2, 1] ]
Example Explanation
All the possible permutation of array [1, 2, 3].
'''
import copy


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def generate(self,A,temp_list,taken_map,ans):
        if len(temp_list) == len(A):
            ans.append(temp_list[:])
            return
        for num in A:
            if not taken_map[num]:
                taken_map[num] = True
                temp_list.append(num)
                self.generate(A, temp_list, taken_map, ans)
                temp_list.pop()
                taken_map[num] = False

    def permute(self, A):
        temp_list = []
        taken_map = dict()
        for num in A:
            taken_map[num] = False
        ans = []
        self.generate(A,temp_list,taken_map,ans)
        return ans

scaler = Solution()
A = [1, 2, 3]
print(scaler.permute(A))