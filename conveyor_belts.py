m = int(input())

for _ in range(m):
    n, x1,y1,x2,y2 = [int(x) for x in input().split()]

    print(abs(min(x1-1,n-x1,y1-1,n-y1)-min(x2-1,n-x2,y2-1,n-y2)))