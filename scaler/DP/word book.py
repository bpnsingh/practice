'''
Given a dictionary of words, and strings, check if it is possible to breakdown the complet strings in to valid words
from dictionary
'''

class Solution:
    def isValid(self,substring,dictionary):
        return substring in dictionary
    def solve(self,dictionary,input_string):
        N = len(input_string)
        #dp = [-1]*(N+1)
        def word_book(start):
            if start == N:
                return True
            for i in range(start,N):
                #dp[start] =
                if self.isValid(input_string[start:i+1],dictionary) and word_book(i+1):
                    return True
            return False
        return  word_book(0)
    def solve_dp(self,dictionary,input_string):
        N = len(input_string)
        dp = [-1]*(N+1)
        dp[N] = True
        for i in range(N-1,-1,-1):
            print (dp[i+1],input_string[i:N])
            dp[i] = self.isValid(input_string[i:N],dictionary) and dp[i+1]
        return dp

scaler = Solution()
dictionary = {'am','a','boy','girl','i'}
A = 'iamaboy'
A="catsandog"
dictionary=["cats","dog","sand","and","cat"]
print(scaler.solve(dictionary,A))
#print(scaler.solve_dp(dictionary,A))
