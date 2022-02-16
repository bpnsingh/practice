'''
Given a sorted array check input integer is present in array or not
A = [3,6,9,12,14,19,20,23,25]
B = 25
B = 2
'''
def binary_search(A,B):
    N = len(A)
    L = 0
    R = N-1
    while L <= R:
        mid = (L+R) // 2
        if B == A[mid]:
            return mid
        elif A[mid] < B:
            L = mid + 1
        else:
            R = mid -1
    return -1

if __name__ == '__main__':
    A = [3, 6, 9, 12, 14, 19, 20, 23, 25]
    B = 25
    print(binary_search(A,B))
    B = 2
    print(binary_search(A, B))