'''
abc 8626
bcd 8714
cde 8802
def 8890
eff 8947
fff 8976
ffa 8821
fab 8712
abc 8626
bcd 8714
cdd 8771
ddf 8862
dff 8918
fff 8976
ffg 9007
fga 8849
gab 8741
abc 8626

'''

class Solution:
    global P
    P = 29
    def string_to_integer(self,strings):
        #print ('calculating for {}'.format(strings))
        N = len(strings)
        int_string = 0
        for i in range(N):
            int_string += ord(strings[i])*(29**i)
        return int_string%37

    def rabin_krap_search(self,input_string,pattern):
        M = len(pattern)
        N = len(input_string)
        cnt = 0
        global P
        prime_multiplier = P ** (M-1)
        pattern_int = self.string_to_integer(pattern)
        int_string = self.string_to_integer(input_string[0:M])
        #print(pattern_int)
        if pattern_int == int_string:
            cnt+=1
        for i in range(1,N-M+1):
            remove_char = ord(input_string[i-1])
            add_char = ord(input_string[M+i-1])*prime_multiplier
            next_str_int = ((int_string - remove_char)//P + add_char)%37
            if pattern_int == next_str_int:
                cnt+=1
            int_string = next_str_int
        return cnt

scaler = Solution()
A = "abcdefffabcddfffgabc"
B= "abc"
print (scaler.rabin_krap_search(A,B))
