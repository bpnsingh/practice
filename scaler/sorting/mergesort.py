'''
Impement merge sort
'''

def merge(A,l,y,r):
    temp = [0]*(r-l+1)
    t = 0
    a = l
    b = y
    N = y-l
    M = r-y+1
    while a < y and b < r+1:
        if A[a] < A[b]:
            temp[t] = A[a]
            t+=1
            a+=1
        else:
            temp[t] = A[b]
            t+=1
            b+=1
    while a < y:
        temp[t] = A[a]
        a += 1
        t += 1
    while b < r+1:
        temp[t] = A[b]
        t += 1
        b += 1

    for i in range(r-l+1):
        A[i+l] = temp[i]

    return A

def merge_sort(A,l,r):
    if l == r:
        return None
    mid = (l+r) // 2
    merge_sort(A,l,mid)
    merge_sort(A,mid+1,r)
    merge(A,l,mid+1,r)
    return A

if __name__ == '__main__':
    A = [3,10,6,8,15,2,12,18,17]
    merge_sort(A,0,len(A)-1)
    print (A)
