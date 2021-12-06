#n3 solution
def all_sum(A):
    N = len (A)
    sum=0
    for i in range(N):
        for j in range(i+1,N):
            sum = 0
            for k in range(i,j+1):
                sum+=A[k]
            print (sum)
    #print (sum)

#n2 solution
def all_sum_2(A):
    N = len (A)
    sum=0
    for i in range(N):
        for j in range(i,N):
            print (A[j])
    print (sum)
def all_sum_opt(A):
    N = len (A)
    sum=0
    for i in range(N):
        s = i+1
        e=  N-i
        sum+=(A[i]*(s*e))
    print (sum)

if __name__ == '__main__':
    all_sum([ 1, 2, -3, 3 ])
    #all_sum_2([1, 2, 3])
    #all_sum_opt([1, 2, 3])