'''
Calculate even_prefix sum for given array
Input A= [4,1,0,-2,3,2,5]
op=[4,4,4,4,7,7,12]
'''

def even_prefix_sum(A):
    N = len(A)
    ans = [A[0],A[0]]
    for i in range(2,N):
        temp = ans[-1]
        if i %2 == 0:
            temp+=A[i]
        ans.append(temp)
    return ans

def odd_prefix_sum(A):
    N = len(A)
    ans = [0,A[1]]
    for i in range(2,N):
        temp = ans[-1]
        if i %2 != 0:
            temp+=A[i]
        ans.append(temp)
    return ans


if __name__ == '__main__':
    A = [4, 1, 0, -2, 3, 2, 5]
    print(even_prefix_sum(A))
    print(odd_prefix_sum(A))
