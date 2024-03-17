n = int(input())

for _ in range(n):
    n, m, o = [int(x) for x in input().split()]
    al = str(input()) 
    bo = str(input()) 
    ans = []

    alice = sorted(al)
    bob = sorted(bo)

    a = 0
    a_count = 0
    b_count = 0
    b = 0

    while a < len(alice) and b < len(bob):
        if a_count == o:
            ans.append(bob[b])
            b_count += 1
            b += 1
            a_count = 0
            continue
        elif b_count == o:
            ans.append(alice[a])
            a_count += 1
            a += 1
            b_count = 0
            continue

        if alice[a] < bob[b]:
            ans.append(alice[a])
            a_count += 1
            b_count = 0
            a += 1
        elif alice[a] >= bob[b]:
            ans.append(bob[b])
            b_count += 1
            a_count = 0
            b += 1

    print("".join(ans))