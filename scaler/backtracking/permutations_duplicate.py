'''
Given an array A of size N denoting collection of numbers that might contain duplicates, return all possible unique permutations.
NOTE: No 2 entries in the permutation sequence should be the same.
WARNING: DO NOT USE LIBRARY FUNCTION FOR GENERATING PERMUTATIONS. Example : next_permutations in C++ / itertools.permutations in python.
If you do, we will disqualify your submission retroactively and give you penalty points.
Problem Constraints
1 <= |A| <= 9
0 <= A[i] <= 10
Input Format
Only argument is an integer array A of size N.
Output Format
Return a 2-D array denoting all possible unique permutation of the array.
Example Input
Input 1:
A = [1, 1, 2]
Input 2:
A = [1, 2]
Example Output
Output 1:
[ [1,1,2]
  [1,2,1]
  [2,1,1] ]
Output 2:
[ [1, 2]
  [2, 1] ]
Example Explanation
Explanation 1:
 All the possible unique permutation of array [1, 1, 2].
Explanation 2:
 All the possible unique permutation of array [1, 2].
'''
class Solution:
    def permute(self, A):
        freq = {n:0 for n in range(11)}
        temp_list = []
        ans = []
        for num in A:
            freq[num] += 1
        def generate():
            if len(temp_list) == len(A):
                ans.append(temp_list.copy())
            for num in freq:
                if freq[num] > 0:
                    temp_list.append(num)
                    freq[num] -= 1
                    generate()
                    temp_list.pop()
                    freq[num] += 1
        generate()
        return ans


A = [1,1,2]
scaler = Solution()
print (scaler.permute(A))