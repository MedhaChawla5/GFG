class Solution:
    #Function to return list containing elements of right view of binary tree.
    def rightView(self,root):
        if root is None:
            return []
        q = []
        r = []
        q.append(root)
        currl = 0
        
        while(q):
            qlen = len(q)
            r.append([])
            
            for i in range(qlen):
                node = q.pop(0)
                r[currl].append(node.data)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            currl += 1
        res = []
        for i in range(len(r)):
            res.append(r[i][-1])
        return res
