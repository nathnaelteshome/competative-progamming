#User function Template for python3

def isSubset( a1, a2, n, m):
    
    for num in range(m):
        if a2[num] in a1:
            a1.remove(a2[num])
        else:
            return "No"
            
    return "Yes"
            
    