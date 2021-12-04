'''
given an array count the number of distinct element:

'''
def count_distinct(A):
    ans=set()
    for item in A:
        ans.add(item)
    return len(ans)


if __name__ == '__main__':
    A=[7,3,2,1,3,7,0]
    print (count_distinct(A))