class Solution:
	# @param A : list of integers
	# @return an integer
    def check_set_bit(self,N, pos):
        if (N >> pos) & 1 == 1:
            return True
        else:
            return False

    def solve(self, A):
        N = len(A)
        sum = 0
        for i in range(0,8):
            temp_list = []
            for j in range(0,N):
                print (i,j)
                if self.check_set_bit(i,j):
                    temp_list.append(A[j])
            print (temp_list)
            if len(temp_list) >= 2:
                sum += max(temp_list) - min(temp_list)
        return sum

scaler = Solution()
A= [5,4,2]
print (scaler.solve(A))
