#Main logic
#given in questions
valid_numbers = range(1,60)
digit_len_map = {
    7: (7, 0),
    8: (6, 1),
    9: (5, 2),
    10: (4, 3),
    11: (3, 4),
    12: (2, 5),
    13: (1, 6),
    14: (0, 7)
}
def is_duplicate_present(value, arg):
    arg_cpy = list(arg)
    arg_cpy.remove(value)
    if value in arg_cpy:
        return True
    return False

def check_tkt(tkt,length):
    valid_tkt=[]
    #create combination of all 1 one diigt numbers list
    one_digit_list=[]
    for i in range(length):
        one_digit_list.append(tkt[i])
    # create combination of all  2 diigt numbers list
    two_digit_list=[]
    for i in range(length):
        two_digit_list.append(tkt[i:i+2])
    #with input lenth, possible one digit and 2 digit combinations
    single_digit_count, double_digit_count = digit_len_map[length]
    i = 0
    max_len = len(one_digit_list)
    #we will iterate through two_digit_list, taking 2 consecutive value at a time,
    #this values will be called value1 value2 where 4 combination are possible
    #case 1: value 1 is valid and value 2 is not, pick value1 only
    #case 2:value 1 is invalid and value2 is valid, pick single digit
    #case 3 : both value1 and value2 are invalid, pick correesponding single digit
    #case 4: Both value 1 and value2 are valid , In that case add another value 3,
    # If value 3 can be added then value1  and value 3. If value 3 can not be added
    # check out of 3 digit value which combination do work.

    while i < max_len :
        if ((double_digit_count > 0) and ((i + 1) < max_len)):
            value1 = two_digit_list[i]
            value2 = two_digit_list[i + 1]
            # case 1
            if (int(value1) in valid_numbers and int(value2) not in valid_numbers):
                if (value1 not in valid_tkt):
                    valid_tkt += [value1]
                    double_digit_count -= 1
                    i += 2
            #case 2
            elif (int(value1) not in valid_numbers and int(value2) in valid_numbers):
                if (one_digit_list[i] not in valid_tkt \
                        and (int(one_digit_list[i]) in valid_numbers) \
                        and value2 not in valid_tkt):
                    if (single_digit_count > 0):
                        valid_tkt += [one_digit_list[i], value2]
                        single_digit_count -= 1
                        double_digit_count -= 1
                        i += 3
            #case 3
            elif (int(value1) not in valid_numbers and int(value2) not in valid_numbers):
                if (single_digit_count >= 2):
                    if (one_digit_list[i] not in valid_tkt) \
                            and (int(one_digit_list[i]) in valid_numbers):
                        valid_tkt += [one_digit_list[i]]
                        single_digit_count -= 1
                        if (one_digit_list[i + 1] not in valid_tkt) \
                                and (int(one_digit_list[i + 1]) in valid_numbers):
                            valid_tkt += [one_digit_list[i + 1]]
                            single_digit_count -= 1
                            i += 2
            #case4
            elif (int(value1) in valid_numbers and int(value2) in valid_numbers):
                if (i + 2) < len(one_digit_list):
                    value3 = two_digit_list[i + 2]
                    if (int(value3) in valid_numbers):
                        if (value3 not in valid_tkt):
                            # if value3 is last entry with single digit ,
                            # it will still be taken care of here
                            valid_tkt += [value1]
                            double_digit_count -= 1
                            if (double_digit_count > 0 or single_digit_count > 0):
                                valid_tkt += [value3]
                                double_digit_count -= 1
                                i += 4
                    #if value3 is not valid
                    elif (int(value3) not in valid_numbers):
                        if (single_digit_count > 0):
                            # Three digits have to be split into a 2digit and 1digit\
                            # ..How to split? Compare to see if there's a duplicate
                            # in double digit list. If so , try to avoid that split.
                            if (int(one_digit_list[i]) in valid_numbers) \
                                    and (one_digit_list[i] not in valid_tkt) \
                                    and (value2 not in valid_tkt) \
                                    and (is_duplicate_present(value2, two_digit_list) == False):
                                valid_tkt += [one_digit_list[i], value2]
                                double_digit_count -= 1
                                single_digit_count -= 1
                                i += 3
                    elif (value1 not in valid_tkt) \
                            and (int(one_digit_list[i + 2]) in valid_numbers) \
                            and (one_digit_list[i + 2] not in valid_tkt) \
                            and (is_duplicate_present(value1, two_digit_list) == False):
                        valid_tkt += [value1, one_digit_list[i + 2]]
                        double_digit_count -= 1
                        single_digit_count -= 1
                        i += 3
                #check for last pair
                else:
                    if (double_digit_count > 0):
                        if value1 not in valid_tkt:
                            valid_tkt += [value1]
                            double_digit_count -= 1
                            i += 2
                        # split last two digit and see if you can add
                        else:
                            if (single_digit_count > 1) \
                                    and (single_digit_count[i] not in valid_tkt) \
                                    and (int(one_digit_list[i]) in valid_numbers) \
                                    and (one_digit_list[i + 1] not in valid_tkt) \
                                    and (int(one_digit_list[i + 1]) in valid_numbers):
                                valid_tkt += [single_digit_count[i], single_digit_count[i + 1]]
                                single_digit_count -= 2
                                i += 2
                    elif (single_digit_count > 1) \
                            and (single_digit_count[i] not in valid_tkt) \
                            and (int(one_digit_list[i]) in valid_numbers) \
                            and (one_digit_list[i + 1] not in valid_tkt) \
                            and (int(one_digit_list[i + 1]) in valid_numbers):
                        valid_tkt += [single_digit_count[i], single_digit_count[i + 1]]
                        single_digit_count -= 2
                        i += 2
        else:
            if ((single_digit_count > 0) and (int(one_digit_list[i]) in valid_numbers)):
                if one_digit_list[i] not in valid_tkt:
                    valid_tkt += [one_digit_list[i]]
                    single_digit_count -= 1
                    i += 1
    if (len(valid_tkt) != 7):
        return []
    else:
        return valid_tkt






























def WT(tickets):
    #Processing one ticket at a time with for loop
    for ticket in tickets:
        ticket_length = len(ticket)
        #given valid range are 7 digits with nt greater than 59,check ticket length to remove
        #obious not answer
        if ticket_length >= 7 and ticket_length <= 14:
            ans=check_tkt(ticket,ticket_length)
            if ans:
                print(ticket + "->"+' '.join(ans))


if __name__ == '__main__':
    n = int(input().strip())
    tickets = []
    for _ in range(n):
        tickets_item = input()
        tickets.append(tickets_item)
        WT(tickets)