class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        #code here
        set_a = {x for x in a}
        set_b = {x for x in b}
        output = set_a | set_b
        
        return len(output)
