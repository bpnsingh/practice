'''
print all number in ascending order for given N input
'''

def print_dsc(N):
    if N == 0:
        return
    print(N)
    print_dsc(N-1)


if __name__ == '__main__':
    print_dsc(10)