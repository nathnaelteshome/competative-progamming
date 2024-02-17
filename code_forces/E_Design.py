n, q = [int(x) for x in input().split()]
res = []
output = []

 
words = [str(x) for x in input().split()]
 
for _ in range(q):
    pre, suf = [str(x) for x in input().split()]
    preLength = len(pre)
    sufLength = len(suf)
    pre_suf = pre + suf 
    res.append(pre_suf)

hashMap = {"".join(word[:preLength] + word[-sufLength:]): index for index, word in enumerate(words)}

for i in res:
    if i in hashMap:
        output.append[hashMap[i]]
 
if not output:
    print(-1)
for i in output:
    print(i, end= "")


hash{}