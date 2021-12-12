'''
print all number in ascending order for given N input
'''

def print_asc(N):
    if N == 0:
        return None
    print_asc(N-1)
    print(N)

if __name__ == '__main__':
    print_asc(10)