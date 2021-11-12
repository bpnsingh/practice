'''
For in put array give an equilibrium index
i/p= 1,2,3,4,8,10
o/p = 4
'''
def solve(A):
    N = len(A)
    prefix_sum = []
    prefix_sum.append(A[0])
    for i in range(1,N):
        prefix_sum.append(A[i]+prefix_sum[i-1])
    if N in [1,2]:
        return N
    for i in range(1,N):
        sum_left = prefix_sum[i-1]
        sum_right = prefix_sum[N-1] - prefix_sum[i]
        if sum_left == sum_right:
            return i
if __name__ == '__main__':
    print(solve([1,3,6,8,10]))
    print(solve([-7,1,5,2,-4,3,0]))

