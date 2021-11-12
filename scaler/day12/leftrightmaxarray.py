'''
Given an array of size N, return 2 array, left and right max for every index of
left_max[i] = max(0-i)
right_max[i] = max(i-N-1)
A= -3 6 2 4 5 2 8 -9 3 1
lm= -3 6 6 6 6 6 8 8 8 8
rm =                 8 3 3 1
'''
def lef_right_max_array(A):
    N = len(A)
    left_max = []
    right_max = [0 for i in range(N)]
    left_max.append(A[0])
    right_max[-1] = A[-1]
    for i in range(1,N):
        left_max.append(max(left_max[i-1],A[i]))
    for i in range(N-2,-1,-1):
        right_max[i] = max(right_max[i+1],A[i])
    print (left_max)
    print (right_max)

if __name__ == '__main__':
    lef_right_max_array([-3,6,2,4,5,2,8,-9,3,1])