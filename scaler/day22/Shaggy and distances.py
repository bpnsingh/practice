'''
Shaggy and distances
Shaggy has an array A consisting of N elements. We call a pair of distinct indices in that array as a special pair if elements at that index in the array are equal.

Shaggy wants you to find a special pair such that distance between that pair is minimum. Distance between two indices is defined as |i-j|. If there is no special pair in the array then return -1.



Problem Constraints

1 <= |A| <= 105



Input Format

First and only argument is the array A.



Output Format

Return one integer corresponding to the minimum possible distance between a special pair.



Example Input

Input 1:

A = [7, 1, 3, 4, 1, 7]
Input 2:

A = [1, 1]


Example Output

Output 1:

 3
Output 2:

 1


Example Explanation

Explanation 1:

Here we have 2 options:
1. A[1] and A[4] are both 1 so (1,4) is a special pair and |1-4|=3.
2. A[0] and A[5] are both 7 so (0,5) is a special pair and |0-5|=5.
Therefore the minimum possible distance is 3.
Explanation 2:

Only possibility is choosing A[1] and A[2].

'''


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        index_map = dict()
        N = len(A)
        ans=10**6
        for i in range(N):
            if A[i] not in index_map:
                index_map[A[i]] = [i]
            else:
                index_map[A[i]].append(i)
        for repeat_list in  index_map.values():
            if len(repeat_list) > 1:
                for i in range(1,len(repeat_list)):
                    diff = abs(repeat_list[i-1]-repeat_list[i])
                    ans=min(ans,diff)
        if ans == 10**6:
            return -1
        else:
            return ans


scaler = Solution()
A = [7, 1, 3, 4, 1, 7]
print (scaler.solve(A))
