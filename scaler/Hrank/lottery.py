def brute_force(tickets):
    ans = 0
    num_of_tickets = len(tickets)
    for i in range(num_of_tickets):
        for j in range(i + 1, num_of_tickets):
            cnt_flag = 0
            for num in range(10):
                if str(num) in tickets[i] + tickets[j]:
                    cnt_flag += 1
            if cnt_flag == 10:
                ans += 1
    return ans


def winningLotteryTicket(tickets):
    # Write your code here
    # get the toatal length of tkts combination
    total_size = (1<<10) - 1
    encoded_array = [0]*(total_size+1)
    #create binary encoded array
    for lot_num in tickets:
        mask = 0
        for digit in lot_num:
            mask = mask | 1 << (ord(digit) -ord('0'))
        encoded_array[mask] += 1
    ans = 0
    for i in range(total_size+1):
        for j in range(i+1,total_size+1):
            if i | j == total_size:
                ans += encoded_array[i]*encoded_array[j]
    #if any lottery number has all the digits it self
    number = encoded_array[total_size]

    ans += number*(number-1)//2
    return ans


if __name__ == '__main__':
    A=["129300455","5559948277","012334556","56789","123456879","012345678912","012345678912"]
    print(winningLotteryTicket(A))
