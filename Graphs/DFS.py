class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        n = len(adj)
        vis=set()
        res = []
        def helper(adj , node):
            vis.add(node)
            res.append(node)
            for i in adj[node]:
                if i not in vis:
                    helper(adj , i)
        helper(adj , 0)
        return res 
