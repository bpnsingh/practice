'''
Given an array with q queries, for every query you get start and end index .
you have to give some for all the queries
'''
def sum_array(A,start,end):
    sum = 0
    for i in range(start,end+1):
        sum += A[i]
    return sum

def opt_sum(A,start,end):
    prefix_sum=[]
    prefix_sum.append(A[0])
    for i in range(1,len(A)):
        prefix_sum.append(A[i]+prefix_sum[i-1])
    return prefix_sum[end] - prefix_sum[start-1]


if __name__ == '__main__':
    #print (sum_array([3,6,2,4,5,2,8,-9,3,1],1,3))
    #print(sum_array([3, 6, 2, 4, 5, 2, 8, -9, 3, 1], 2, 7))
    print(opt_sum([3, 6, 2, 4, 5, 2, 8, -9, 3, 1], 1, 3))