import heapq


n = int(input())
ans = []
q = []

for i in range(n):
    word = input()
    order, val = word.split()

    if order == "insert":
        heapq.heappush(q, int(val))
    elif order == "getMin":
        while q and q[0] < int(val):
            heapq.heappop(q)
            ans.append("removeMin")
        if not q or q[0] > val:
            heapq.heappush(q, val)
            ans.append("insert " + str(val))
        ans.append("getMin " + str(val))

print(len(ans))
print("\n".join(ans))
