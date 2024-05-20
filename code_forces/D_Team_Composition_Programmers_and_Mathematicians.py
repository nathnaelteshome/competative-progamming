# t = int(input())

# for _ in range(t):
#     programmer, mathematician = [int(x) for x in input().split()]
#     if programmer * 3 < mathematician:
#         print(programmer)  # 10

#     elif mathematician * 3 < programmer:
#         print(mathematician)

#     else:
#         print((programmer + mathematician) // 4)

for _ in range(int(input())):
    a, b = map(int, input().split())
    totalPeople = a + b
    teamFormed = (a + b) // 4

    if min(a, b) < teamFormed:
        print(min(a, b))
    else:
        print(teamFormed)
# team has to have 4 members
# each team has to have aleast on prof and mathematician
# teamFormed p + m = 10
t = int(input())

for _ in range(t):
    p, m = int(input()), int(input())
