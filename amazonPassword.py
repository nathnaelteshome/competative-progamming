def somfunc(newPasswords,oldPasswords):
    ans = []
    for i in range(len(newPasswords)):
        ans.append(helper(newPasswords[i],oldPasswords[i]))
    return ans

def isValid(a,b):
    if a == b:
        return True
    if a=="z" and b == "a":
        return True
    if ord(a)+1 == ord(b):
        return True
    return False

def helper(new,old):
    j = 0
    for i in range(len(old)):
        while j<len(new) and not isValid(new[j],old[i]):
            j += 1
        if j >= len(new):
            return "NO"
    return "YES"


newPasswords = ["baacbab", "accdb", "baacba"]
oldPasswords = ["abdbc", "ach", "abb"]
print(somfunc(newPasswords, oldPasswords))