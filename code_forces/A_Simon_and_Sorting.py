hashMap = {"a": 0, "b": 1, "c": 2} 
def swapable(hashMap, s):
    for idx, word in enumerate(s):
        if hashMap[word] == idx:
            print("YES")
            return
        
    print("NO")
    return

m = int(input())
for _ in range(m):
    s = str(input())
    swapable(hashMap, s)

