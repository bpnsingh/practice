from _ast import If


def to_lower( A):
    N = len(A)
    #print (ord('A'),ord('Z'),ord('a'),ord('z'))
    for i in range(N):
        if ord(A[i]) in range(ord('A'), ord('Z') + 1):
            A[i] = chr(ord(A[i]) ^ 32)
    return A


if __name__ == '__main__':
    print (to_lower(['S', 'c', 'A', 'l', 'e', 'r', 'A', 'c', 'a', 'D', 'e', 'm', 'y']))