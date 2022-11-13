'''
check given graph has cycle in it or not
'''
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        visited = [False] * (A+1)
        adj_mat = [[] for i in range(1,A)]
        for edge in B:
            adj_mat[edge[0]].append(edge[1])
        print (adj_mat)
        if len(adj_mat) <= 2:
            return 0
        def check_cycle(source,parent):
            visited[source] = True
            for path in adj_mat[source]:
                if parent != path and visited[path]:
                    return True
                elif not visited[path]:
                    if check_cycle(path,source):
                        return True
            return False
        return int(check_cycle(1,None))

scaler = Solution()
A = 5
B = [  [1, 2],
        [1, 3],
        [2, 3],
        [1, 4],
        [4, 5]
     ]
A = 3
B = [[1, 2],[1, 3]]
print(scaler.solve(A, B))
