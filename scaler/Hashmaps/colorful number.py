class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        lista = []
        N = A
        while N:
            lista.append(N%10)
            N = N//10
        product_set = set()
        lista = lista[::-1]
        for i in range(len(lista)):
            product = 1
            for j in range(i,len(lista)):
                product = product * lista[j]
                if product in product_set:
                    return 0
                product_set.add(product)
                print(product_set)
        return 0
scaler = Solution()
print (scaler.colorful(23))