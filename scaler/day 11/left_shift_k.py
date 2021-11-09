def swap(a,b):
    a= a^b
    b=a^b
    a=a^b
    return a,b
def reverse(A,start,end):
    while start < end :
        A[start],A[end] = swap(A[start],A[end])
        start += 1
        end -= 1
    return A

def left_shift(A,K):
    reverse(A,0,len(A)-1)
    reverse(A,0,K-1)
    reverse(A,K,len(A)-1)
    return A
if __name__ == '__main__':
    print(left_shift([3,7,1,6,8,-2,9],3))
