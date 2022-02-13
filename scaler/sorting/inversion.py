class Solution:
    # @param A : list of integers
    # @return an integer
    def merge(self,A, l, y, r):
        temp = [0] * (r - l + 1)
        t = 0
        a = l
        b = y
        count = 0
        while a < y and b < r + 1:
            if A[a] < A[b]:
                temp[t] = A[a]
                t += 1
                a += 1
            else:
                temp[t] = A[b]
                t += 1
                b += 1
                count += (y - a)
        while a < y:
            temp[t] = A[a]
            a += 1
            t += 1
        while b < r + 1:
            temp[t] = A[b]
            t += 1
            b += 1
        print(count)
        return count

    def inv_count(self, A, l, r):
        if l == r:
            return 0
        mid = (l + r) // 2
        x = self.inv_count(A, l, mid)
        y = self.inv_count(A, mid + 1, r)
        z = self.merge(A, l, mid + 1, r)
        print (A)
        return x + y + z

    def solve(self, A):
        l = 0
        r = len(A) - 1
        ans = self.inv_count(A, l, r)
        return ans

scaler = Solution()
A = [ 45, 10, 15, 25, 50 ]
scaler.solve(A)