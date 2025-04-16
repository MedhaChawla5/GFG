class Solution:
    def transitiveClosure(self, N, graph):
        reach = [i[:] for i in graph]
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if i==j:
                        reach[i][j] = 1
                    reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
        return reach
