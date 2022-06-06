'''
Given integer array with coins with unique denominations , and given integer with N, find number of ways
to find N.
[1,3,4,]
5
op = 3(1,1,1,1,1,  1,1,3, 4,1)
'''
def solve_recursive(A,N):
    ans = 0
    def coin_sum(index,value):
        if index < len(A):
            if value == 0:
                return 1
        else:
            return 0
        if A[index]  <= value:
            not_take = coin_sum(index+1,value)
            take = coin_sum(index,value-A[index])
            ans = not_take + take
            return ans
        else:
            return 0
    return coin_sum(0,N)

def solve_dp(A,N):
    dp = [0] * (N+1)
    dp[0] = 1
    for i in range(1,N+1):
        for j in range(0,len(A)):
            if A[j] <= i:
                dp[i] = dp[i] + dp[i-A[j]]
    return dp[N]


A = [1,3,4]
N = 5
print(solve_dp(A,N))