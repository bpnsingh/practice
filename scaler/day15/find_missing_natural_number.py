def find(A):
    '''
    sum = 0
    N = len(A) + 1
    #sum based approach
    for num in A:
        sum+=num
    total_sum = int((N*(N+1))/2)
    print(sum,total_sum)
    return total_sum - sum
    '''
    #XOR based
    ans = 0
    N = len(A) + 1
    for num in A:
        ans^=num
    for count in range(N+1):
        ans ^= count
    return ans
if __name__ == '__main__':
    A=[1,2,5,4]
    print(find(A))