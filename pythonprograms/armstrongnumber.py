def check_armstrong(n):
    sum = 0
    temp_num = n
    while temp_num > 0:
        reminder = temp_num % 10
        sum += reminder ** 3
        temp_num=temp_num // 10
    if sum == n:
        print (n ,"is a Armstrong number")
    else:
        print (n, "is not a Armstrong number")

if __name__ == "__main__":
    check_armstrong(153)
    check_armstrong(111)
    check_armstrong(123)
