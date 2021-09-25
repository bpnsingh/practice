def powerofnum(base,exp):
    assert  exp >= 0 and int(exp) == exp, "Exponenet should be positive integer"
    if exp == 0:
        return 1
    elif exp == 1:
        return  base
    else:
        return   base * powerofnum(base,exp-1)

if __name__ == '__main__':
    print (powerofnum(2,3))
    print(powerofnum(7, 3))