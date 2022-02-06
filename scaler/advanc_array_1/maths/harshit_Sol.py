# Enter your code here. Read input from STDIN. Print output to STDOUT
import copy

# lottery_list = ["1", "42", "100848", "4938532894754", "1234567", "472844278465445", "5698157156"]
result = []


def solve(input, index, arrrayresult):
    # base
    if index >= len(input):
        # print(len(arrrayresult))
        if len(arrrayresult) != 7:
            return
        if len(set(arrrayresult)) != 7:
            return
        # print (arrrayresult)
        temp = copy.deepcopy(arrrayresult)
        result.append(temp)
        # print (result)
        return
    num = ord(input[index]) - ord('0')
    arrrayresult.append(num)
    solve(input, index + 1, arrrayresult)
    arrrayresult.pop()
    if (index + 1) >= len(input):
        return
    num = num * 10 + (ord(input[index + 1]) - ord('0'))

    if num <= 59:
        arrrayresult.append(num)
        solve(input, index + 2, arrrayresult)
        arrrayresult.pop()


if __name__ == '__main__':
    n = int(input().strip())
    tickets = []
    for _ in range(n):
        tickets_item = input()
        tickets.append(tickets_item)
    # result=[]
    # global result
    res = []

    res = []
    for input_str in tickets:
        solve(input_str, 0, res)
        result.sort()
        if result:
            for each in result:
                print(input_str + " -> " + ' '.join(str(elem) for elem in each))
        result = []
