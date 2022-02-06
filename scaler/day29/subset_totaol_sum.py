'''
Given N array elements , find sum of all subsets sum
'''

def subsets_sum(A):
    N = len(A)
    sum = 0
    for num in A:
        sum += num * (2 ** N-1)
    return sum

if __name__ == '__main__':
    A = [3, -1, 0, 6, 2, -3, 5]
    print(subsets_sum(A))