def max_sum_subarray(A,K):
    sum = 0
    N= len(A)
    for i in range(K):
        sum+= A[i]
    max_sum = sum
    for i in range(N-K+1):
        sum = sum - A[i] + A[K+i-1]
        if sum > max_sum:
            max_sum = sum
    return max_sum

if __name__ == '__main__':
    print (max_sum_subarray([-3,4,-2,5,3,-2,8,2,-1,4],5))