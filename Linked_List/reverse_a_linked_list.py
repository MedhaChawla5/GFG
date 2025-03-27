class Solution:
    def reverseList(self, head):
        a = head
        b = head.next
        a.next = None
        while(a):
            a = b 
            b = b.next
            a.next = head
            head = a
            if b==None:
                return head
