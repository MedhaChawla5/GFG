class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        #code here
        vis = set()
        a = b = head
        while(a):
            if a in vis:
                return True
            else:
                vis.add(a)
                a = a.next 
        return False 
