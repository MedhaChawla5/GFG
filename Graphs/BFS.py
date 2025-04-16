from collections import deque 
class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        res = []
        q = deque()
        n = len(adj)
        if n==0:
            return []
        q.append(0)
        while q:
            node = q.popleft()
            res.append(node)
            for i in adj[node]:
                if i not in q:
                    q.append(i)
            print(res)
        return res 
