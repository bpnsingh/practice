'''Problem Description
Given a set of distinct integers A, return all possible subsets.
NOTE:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Also, the subsets should be sorted in ascending ( lexicographic ) order.
The list is not necessarily sorted.
Problem Constraints
1 <= |A| <= 16
INTMIN <= A[i] <= INTMAX
Input Format
First and only argument of input contains a single integer array A.
Output Format
Return a vector of vectors denoting the answer.
Example Input
Input 1:
A = [1]
Input 2:
A = [1, 2, 3]
Example Output
Output 1:
[
    []
    [1]
]
Output 2:
[
 []
 [1]
 [1, 2]
 [1, 2, 3]
 [1, 3]
 [2]
 [2, 3]
 [3]
]
Example Explanation
Explanation 1:
 You can see that these are all possible subsets.
Explanation 2:
You can see that these are all possible subsets.
'''
import copy
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def generate_subsets(self,A,index,curr_list,ans_list):
        if index == len(A):
            ans_list.append(copy.deepcopy(curr_list))
            return
        curr_list.append(A[index])
        self.generate_subsets(A,index+1,curr_list,ans_list)
        curr_list.pop()
        self.generate_subsets(A,index + 1, curr_list, ans_list)

    def subsets(self, A):
        curr_list = []
        ans_list = []
        index =0
        self.generate_subsets(A, index, curr_list, ans_list)
        return sorted(ans_list)

A = [1, 2, 2]
scaler = Solution()
print (scaler.subsets(A))




