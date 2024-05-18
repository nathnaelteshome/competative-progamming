t = int(input())


for _ in range(t):
    k, q = [int(x) for x in input().split()]
    kickedSequence = [int(x) for x in input().split()]
    players_number = [int(x) for x in input().split()]
    ans = []
    frontKicker = kickedSequence[0] - 1
    for noOfPlayer in players_number:
        if noOfPlayer < frontKicker:
            ans.append(noOfPlayer)
        else:
            ans.append(frontKicker)
    print(*ans)
