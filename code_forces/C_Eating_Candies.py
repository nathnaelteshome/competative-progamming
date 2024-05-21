for _ in range(int(input())):
    n = int(input())
    num = list(map(int,input().split()))
    l , r = -1,n
    s , t = 0,0
    r = 0
    while l-r:

        if s == t:
            r = (l+1) + (n-r)
            l += 1
            s += num[l]
        elif s < t:
            l += 1
            s += num[l]
        else:
            r-=1
            t += num[r]
    print(r)