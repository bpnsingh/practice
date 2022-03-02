class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def binary_search(self,A, B):
        N = len(A)
        L = 0
        R = N - 1
        while L <= R:
            mid = (L + R) // 2
            if B == A[mid]:
                return mid
            elif A[mid] < B:
                L = mid + 1
            else:
                R = mid - 1
        return -1

    def search(self, A, B):
        N = len(A)
        pivot = N
        L = 0
        R = N-1
        while L <= R:
            mid = (L+R)//2
            if A[mid] >= A[0]:
                L = mid+1
            else:
                pivot = mid
                R = mid - 1
        print (pivot)
        if pivot == N:
            ans = self.binary_search(A,B)
            return ans
        else:
            ans1 = -1
            ans2 = -1
            if B >= A[0] and B <= A[pivot-1]:
                ans1 = self.binary_search(A[0:pivot-1],B)
            else:
                print("checking in right part")
                ans2 = self.binary_search(A[pivot:],B)
        return max(ans2,ans1)


scaler = Solution()
#A = [4, 5, 6, 7, 0, 1, 2, 3]
#print (scaler.search(A,4))
#A=[1]
#B = 1
A=[ 180, 181, 182, 183, 184, 187, 188, 189, 191, 192, 193, 194, 195, 196, 201, 202, 203, 204, 3, 4, 5, 6, 7, 8, 9, 10, 14, 16, 17, 18, 19, 23, 26, 27, 28, 29, 32, 33, 36, 37, 38, 39, 41, 42, 43, 45, 48, 51, 52, 53, 54, 56, 62, 63, 64, 67, 69, 72, 73, 75, 77, 78, 79, 83, 85, 87, 90, 91, 92, 93, 96, 98, 99, 101, 102, 104, 105, 106, 107, 108, 109, 111, 113, 115, 116, 118, 119, 120, 122, 123, 124, 126, 127, 129, 130, 135, 137, 138, 139, 143, 144, 145, 147, 149, 152, 155, 156, 160, 162, 163, 164, 166, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177 ]
print (scaler.search(A,42))
