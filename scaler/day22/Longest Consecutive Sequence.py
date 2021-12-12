def solve(A):
    #create a set variable to stor unique numbers of input array
    set_a = set(A)
    ans = 1
    for num in set_a:
        #skip numbers of set if any number less than 1 already exists in
        #set map, for example if num is 4 , and if 3 exist in set, than we
        #can not get max length with num
        if num -1 in set_a:
            pass
        else:
        #once we got number , assuming its the lenght 1, and keep looking for num+1
        #exist in set, if yes keep incrementing ans_len
            temp_len = 1
            while ((num + 1) in set_a):
                temp_len+=1
                num+=1
            ans = max(ans,temp_len)
    return ans






if __name__ == '__main__':
    A=[100, 4, 200, 1, 3, 2]
    B=[2, 1]
    print (solve(A))
    print(solve(B))