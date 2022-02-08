'''
Given an array of size N givr that sub array from l,y-1 and y,r are sorted array.sort to subarray from l to r
A = [8,1,3,6,11,2,4,9,7,6]
l=2
y=5
r=7
OP= [8,1,2,3,4,6,9,11,7,6]
'''

def sort_subarray(A,l,y,r):
    temp = [0]*(r-l+1)
    t = 0
    a = l
    b = y
    N = y-l
    M = r-y+1
    while a < y and b < r+1:
        print (temp)
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

if __name__ == '__main__':
    A = [8, 1, 3, 6, 11, 2, 4, 9, 7, 6]
    print(sort_subarray(A,2,5,7))

