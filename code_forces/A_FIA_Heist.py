import string
 
 
s = str(input())
 
stack = []
sList = [str(x) for x in s]
# print(sList)
 
for char in sList:
    if stack and char == "-":
        stack.pop()
 
    elif char.isalpha() or char in "!#$%&()*+,' ./:;=>?@[\]^_`{|}~" or char in '"' or char in string.whitespace:
        stack.append(char)
 
 
# print(stack)
    
print("".join(stack))