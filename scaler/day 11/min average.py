def solve(A, B):
    N = len(A)

    sum = 0
    for i in range(B):
        sum += A[i]
    least_sum = sum
    ans = 0
    print (sum)
    for i in range(1, N - B + 1):
        print (sum,least_sum)
        sum = sum - A[i - 1] + A[B + i - 1]
        if sum < least_sum:
            least_sum = sum
            ans = i
    return ans

if __name__ == '__main__':
    A= [5, 15, 7, 6, 3, 4, 18, 14, 13, 7, 3, 7, 2, 18]
    B= 6
    print (solve(A, B))
