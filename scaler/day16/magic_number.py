''''''

def to_binary(N):
    ans=""
    while N > 0:
        temp = N % 2
        ans = ans + str(temp)
        N = N //2
    return ans[::-1]

def solve(A):
    binary_repr = to_binary(A)
    M = 5
    N = len(binary_repr)
    sum = 0
    for index in range(N-1,-1,-1):
        sum = sum + (int(binary_repr[index])*M)
        M = M * 5
    return sum

if __name__ == "__main__":
    A = 3
    B = 10
    C=  73
    #print (to_binary(8))
    print (solve(A))
    print (solve(B))
    #print(solve(C))
