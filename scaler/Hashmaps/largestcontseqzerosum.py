class Solution:
    # @param A : list of integers
    # @return a list of integers
    def get_max_distance_duplicate(self, A):
        N = len(A)
        ans = -10**6
        freq_map = dict()
        start = -1
        end = -1
        for i in range(N):
            if A[i] not in freq_map:
                # if fist occurance then update dict with element aganist its index
                freq_map[A[i]] = i
            else:
                # if its duplicate, get the difference of current and last found index
                temp = i - freq_map[A[i]]
                if temp > ans:
                    ans = temp
                    end = i
                    start = freq_map[A[i]]
                # don need to update latest index in dict
        return [start, end]


    def lszero(self, A):
        N = len(A)
        end1 = 0
        start1 = 0
        # create prefix_sum
        psum = [0] * N
        psum[0] = A[0]
        for i in range(1, N):
            psum[i] = psum[i - 1] + A[i]
        # if psum has zero , than Array starting from 0 to that index is zero
        print (psum)
        for i in range(N):
            if psum[i] == 0:
                end1 = i
        #if 0 in psum:
        #    i = psum.index(0)
        #    start1 = 0
        #    end1 = i
        print(start1, end1)
        start2, end2 = self.get_max_distance_duplicate(psum)
        print (start2,end2)
        if start1 == -1:
            return
        if (end2 - start2) > (end1 - start1+ 1):
            return A[start2 + 1:end2 + 1]
        else:
            return A[:end1 + 1]


#A = [ -1, 1, 1, -1, -1, 1, 1, -1 ]
#A=[ -8, 8, -1, -16, -28, -27, 15, -14, 14, -27, -5, -6, -25, -11, 28, 29, -3, -25, 17, -25, 4, -20, 2, 1, -17, -10, -25 ]
A=[ 10, 13, -1, 8, 29, 1, 24, 8, 21, 20, 21, -23, -21, 0 ]
scaler = Solution()
print (scaler.lszero(A))