'''
Given a binary string A. It is allowed to do at most one swap between any 0 and 1. Find and return the length of the longest consecutive 1’s that can be achieved.

'''

def solve(A):
    input_array = [int(i) for i in A]
    count_ones = 0
    for num in input_array:
        if num == 1:
            count_ones += 1

    N = len(input_array)
    pre_sum = []
    pre_sum.append(input_array[0])
    suf_sum = []
    for i in range(N):
        suf_sum.append(0)
    sum = input_array[0]
    suf_sum[-1]=input_array[-1]
    for i in range(1,N):
        if input_array[i] == 0:
            sum = 0
        sum = sum + input_array[i]
        pre_sum.append(sum)
    for i in range(N-2,-1,-1):
        if input_array[i] == 0:
            sum = 0
        sum = sum + input_array[i]
        suf_sum[i] = sum
    temp = 0
    ans = 0
    for i in range(N-1):
        if input_array[i] == 0:
            temp = pre_sum[i-1] + suf_sum[i+1]
            if count_ones > temp:
                temp+=1
        ans = max(temp,ans)
    return ans



if __name__ == '__main__':
    A='111011101'
    A='1101001100101110'
    print (solve(A))
