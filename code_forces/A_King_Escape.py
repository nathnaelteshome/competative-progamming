n = int(input())

queen_x, queen_y = [int(x) for x in input().split()]
king_x, king_y = [int(x) for x in input().split()]
cord_x, cord_y = [int(x) for x in input().split()]

if (queen_x < king_x and queen_y < king_y) and (queen_x < cord_x and queen_y < cord_y):
    print("YES")
elif (queen_x < king_x and queen_y > king_y) and (
    queen_x < cord_x and queen_y > cord_y
):
    print("YES")
elif (queen_x > king_x and queen_y < king_y) and (
    queen_x > cord_x and queen_y < cord_y
):
    print("YES")
elif (queen_x > king_x and queen_y > king_y) and (
    queen_x > cord_x and queen_y > cord_y
):
    print("YES")
else:
    print("YES")
