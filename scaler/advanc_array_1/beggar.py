class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        #create a prefix sum with 0 velaue and A length
        psum = [0]*A
        print (psum)
        for s,e,amount in B:
            s = s-1
            e= e-1
            if e == A -1:
                psum[s] += amount
            else:
                print (s,e,B)
                psum[s] += amount
                psum[e+1] -= amount
        #process prefix sum
        ans =[]
        sum = 0
        for num in psum:
            sum += num
            ans.append(sum)
        return ans

scaler = Solution()
A = 5
B = [[1, 2, 10],[2, 3, 20],[2, 5, 25]]
print (scaler.solve(A, B))