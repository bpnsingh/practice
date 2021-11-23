'''
Given a column title as appears in an Excel sheet, return its corresponding column number.



Problem Constraints

1 <= length of the column title <= 5



Input Format

Input a string which represents the column title in excel sheet.



Output Format

Return a single integer which represents the corresponding column number.



Example Input

Input 1:

 AB
Input 2:

 ABCD


Example Output

Output 1:

 28
Output 2:

 19010


Example Explanation

Explanation 1:

 A -> 1
 B -> 2
 C -> 3
 ...
 Z -> 26
 AA -> 27
 AB -> 28

'''
def excel_clm(A):
    N = len(A)
    ans = 0
    multi = 1
    for i in range(N-1,-1,-1):
        digit = ord(A[i]) - 64
        ans = ans + digit*multi
        multi = multi*26
    return ans

if __name__ == '__main__':
    A="ABCD"
    print(excel_clm(A))
