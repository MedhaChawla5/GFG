class Solution:
    def isValid(self, s):
        #code here
        sub = s.split(".")
        if len(sub)!=4:
            return False
        for subs in sub:
            if not subs.isdigit():
                return False 
            if len(subs)>1 and subs[0]=="0":
                return False 
            if not 0<=int(subs)<=255:
                return False 
        return True 
