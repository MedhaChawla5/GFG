class Solution:
    def getKthFromLast(self, head, k):
        count = 0
        a = head
        while(a):
            count = count+1
            a = a.next
        tar = count-k
        if(tar<0):
            return -1
        a = head
        for i in range(tar):
            a = a.next
        return a.data 
