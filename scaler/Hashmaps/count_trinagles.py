import cnt as cnt


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve_brute(self, A, B):
        N = len(A)
        cnt = 0
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                for k in range(N):
                    if k==i or k==j:
                        continue
                    x1,y1=A[i],B[i]
                    x2,y2=A[j],B[j]
                    x3,y3=A[k],B[k]
                    if x1 == x3 and y1==y2:
                        cnt+=1
        return cnt
    def solve_N2(self, A, B):
        cnt=0
        N = len(A)
        coordinates = set()
        for x,y in zip(A,B):
            coordinates.add((x,y))
        for i in range(N):
            for j in range(i+1,N):
                x1,y1=A[i],B[i]
                x2,y2=A[j],B[j]
                if x1 != x2 and y1 != y2:
                    if (x1,y2) in coordinates:
                        cnt+=1
                    if (x2,y1) in coordinates:
                        cnt+=1
        return cnt
    def solve(self,A,B):
        N  = len(A)
        ans = 0
        #create freq_map for x and y coordinates separately
        freq_x = dict()
        freq_y = dict()
        for x in A:
            if x not in freq_x:
                freq_x[x] = 1
            else:
                freq_x[x] += 1
        for y in B:
            if y not in freq_y:
                freq_y[y] = 1
            else:
                freq_y[y] += 1
        for i in range(N):
            x = A[i]
            y = B[i]
            ans += (freq_x[x] -1)*(freq_y[y] -1)
        return ans


scaler = Solution()
A = [1, 1, 2, 3, 3]
B = [1, 2, 1, 2, 1]
print (scaler.solve(A, B))