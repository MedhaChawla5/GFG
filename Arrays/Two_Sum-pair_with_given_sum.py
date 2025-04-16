class Solution:
	def twoSum(self, arr, target):
	    s = set()
	    for i in arr:
	        com = target-i
	        if com in s:
	            return True
	        s.add(i)
	    return False 
