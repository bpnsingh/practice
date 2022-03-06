'''
Given a sorted array of integers (not necessarily distinct) A and an integer B, find and return how many pair of integers ( A[i], A[j] ) such that i != j have sum equal to B.
Since the number of such pairs can be very large, return number of such pairs modulo (109 + 7).

'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve_opt(self, A, B):
        N = len(A)
        P1 = 0
        P2 = N-1
        cnt = 0
        while P1 < P2:
            if A[P1] + A[P2] == B:
                if A[P1] == A[P2]:
                    length = P2 - P1 +1
                    cnt += (length*(length -1))//2
                    break
                else:
                    cnt_p1 = 1
                    cnt_p2 = 1
                    P1+=1
                    P2-=1
                    while P1<N and A[P1] == A[P1-1]:
                        cnt_p1+=1
                        P1+=1
                    while P2>=0 and A[P2] == A[P2+1]:
                        cnt_p2+=1
                        P2-=1
                    cnt += cnt_p1*cnt_p2
            elif A[P1] + A[P2] < B:
                P1+=1
            else:
                P2-=1
        return cnt
    def solve(self,A,B):
        cnt = 0
        map_a = dict()
        for num in A:
            if num not in map_a:
                map_a[num] = 1
            else:
                map_a[num]+=1
        print (map_a)
        for num in A:
            map_a[num] -= 1
            if B - num in map_a:
                cnt += map_a[B-num]
            map_a[num] += 1
        return cnt // 2



scaler = Solution()
#A = [ 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 9, 10 ]
#B = 5
A = [ 2, 2, 3, 4, 4, 5, 6, 7, 10 ]
B = 8
print (scaler.solve_opt(A,B))
