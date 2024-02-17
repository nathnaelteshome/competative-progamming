n = int(input())
countFile = {}
result = ""

for _ in range(n):
    char = str(input())
    if char not in countFile:
        countFile[char]= 1
        print("OK")
    else:
        print(f"{char}{countFile[char]}")
        countFile[char] = countFile[char]  + 1
        
