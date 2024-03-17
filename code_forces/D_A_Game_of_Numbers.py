n = int(input())

for _ in range(n):
    n , m = [int(x) for x in input().split()]
    frodoCollection = [int(x) for x in input().split()]
    samCollection = [int(x) for x in input().split()]

    frodoCollection.sort()
    samCollection.sort()

    ans = 0
    # result = []
    l, r = 0, len(frodoCollection) - 1
    left, right = 0, len(samCollection) - 1

    while l <= r:
        a = abs(frodoCollection[l] - samCollection[left])
        b = abs(frodoCollection[l] - samCollection[right])
        c = abs(frodoCollection[r] - samCollection[left])
        d = abs(frodoCollection[r] - samCollection[right])

        # print("hello", a,b,c,d)
        
        if a >= max(b, c, d):
            result.append([a, "a" , n])
            ans += a
            l += 1
            left += 1
        elif b >= max(a, c, d):
            result.append([b, "b" , n])
            ans += b
            l += 1
            right -= 1
        elif c >= max(a, b, d):
            result.append([c, "c", n])
            ans += c
            r -= 1
            left += 1
        else:
            result.append([d, "d", n])
            ans += d
            r -= 1
            right -= 1

    print(result)
    print(ans)
