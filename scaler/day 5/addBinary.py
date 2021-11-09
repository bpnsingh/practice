def addBinary(A, B):
    result=[]
    carry_bit=0
    i=len(A)-1
    j=len(B)-1
    while (i >=0) | (j >= 0):
        if i < 0 :
            sum= 0 + int(B[j])+ carry_bit
        elif j<0:
            sum= int(A[i]) + 0 +carry_bit
        else:
            sum=int(A[i]) + int(B[j])+carry_bit
        sum_bit=sum%2
        result.append(sum_bit)
        carry_bit=sum//2
        if (carry_bit == 1) & (max(len(A),len(B))==len(result)):
            result.append(carry_bit)
        print (i,j,result)
        i-=1
        j-=1
    result_string=''.join(map(str,result))
    return result_string[::-1]

if __name__ == '__main__':
    print(addBinary('1','1'))