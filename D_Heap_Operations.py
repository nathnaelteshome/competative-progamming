from heapq import *
 
n = int(input())
logs = []
finalLogs = []
heap = []
 
for _ in range(n):
    logs.append(input().split())
 
for log in logs:
    if log[0] == "insert":
        heappush(heap, int(log[1]))
    elif log[0] == "removeMin":
        if heap:
            heappop(heap)
        else:
            finalLogs.append(["insert", 1])
    else:
        while heap and heap[0] < int(log[1]):
            heappop(heap)
            finalLogs.append(["removeMin"])
 
        if not heap or heap[0] != int(log[1]):
            heappush(heap, int(log[1]))
            finalLogs.append(["insert", int(log[1])])
 
    finalLogs.append(log)
 
print(len(finalLogs))
for log in finalLogs:
    print(*log)