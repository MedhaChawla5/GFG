class Solution:
    def divide(self, head):
        if not head or not head.next:
            return head 
        curr = head 
        evenh = event = None
        oddh = oddt = None 
        while(curr):
            next_node = curr.next
            curr.next = None
            if(curr.data%2==0):
                if not evenh:
                    evenh = event = curr
                else:
                    event.next = curr
                    event = curr
            else:
                if not oddh:
                    oddh = oddt = curr
                else:
                    oddt.next = curr
                    oddt = curr
            curr = next_node
            
        if event:
            event.next = oddh
        return evenh if evenh else oddh
