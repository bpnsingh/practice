def string_mod(A,B):
    ans = 0
    mod = B
    n = len(A)
    curr = 1
    for i in range(n - 1, -1, -1):
        dig = ord(A[i]) - 48
        term = (dig * curr) % mod
        ans = (ans + term) % mod
        curr = (curr * 10) % mod
    return ans

if __name__ == '__main__':
    A = "43535321"
    B = 47
    #A = "143"
    #B =2
    print(string_mod(A,B))
