'''
Given a string A of size N, find and return the longest palindromic substring in A.

Substring of string A is A[i...j] where 0 <= i <= j < len(A)

Palindrome string:
A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A.

Incase of conflict, return the substring which occurs first ( with the least starting index).



Problem Constraints

1 <= N <= 10000



Input Format

First and only argument is a string A.



Output Format

Return a string denoting the longest palindromic substring of string A.



Example Input

A = "aaaabaaa"


Example Output

"aaabaaa"
'''


class Solution:
    # @param A : string
    # @return a strings
    def check_pailndrome(self, A, i, j):
        while (i >= 0) and (j < len(A)) and (A[i] == A[j]):
            i -= 1
            j += 1
        return A[i:j]

    def longestPalindrome(self, A):
        N = len(A)
        ans = 1
        for i in range(1, N):
            if i % 2 == 0:
                ans = max(ans, self.check_pailndrome(A, i, i + 1))
            else:
                ans = max(ans, self.check_pailndrome(A, i, i))
        if ans == 1:
            return -1
        else:
            return ans


scaler=Solution()
A="aaabaaa"
print (scaler.longestPalindrome(A))

class Solution:
    # @param A : string
    # @return a strings
    def check_pailndrome(self, A, i, j):
        while (i >= 0) and (j < len(A)) and (A[i] == A[j]):
            i -= 1
            j += 1
        return A[i:j+1]

    def longestPalindrome(self, A):
        N = len(A)
        ans=''
        for i in range(1, N):
            temp_ans= self.check_pailndrome(A, i, i + 1)
            if len(temp_ans) > len(ans):
                ans=temp_ans
            temp_ans= self.check_pailndrome(A, i, i)
            if len(temp_ans) > len(ans):
                ans=temp_ans
        if ans == '':
            return -1
        else:
            return ans