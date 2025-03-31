class Solution:
    def reverseLevelOrder(self,root):
        if root is None:
            return 
        q = []
        res = []
        
        q.append(root)
        curr_l = 0
        while(q):
            qlen = len(q)
            res.append([])
            for i in range(qlen):
                node = q.pop(0)
                res[curr_l].append(node.data)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            curr_l = curr_l+1
        #return res
        reslen = len(res)
        r = []
        for i in range(reslen-1 , -1 , -1):
            r.extend(res[i])
        return r
