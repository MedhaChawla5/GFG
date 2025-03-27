class Solution:
    
    def deleteAllOccurances(self,head,x):
        curr = head
        prev = None
        while(curr):
            if curr.data == x:
                if prev is None:
                    head = curr.next
                else:
                    prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return head
