num, n = input().split()

for i in range(int(n)):
    if num[-1] =='0':
        num = str(int(num)//10)
    else:
        num = str(int(num) - 1)
        
print(num)

