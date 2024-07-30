from cmath import inf


n = int(input())
fruits = [int(x) for x in input().split()]

sorted_fruits = sorted(fruits)
out_of_place = 0

for idx in range(len(fruits)):
    if fruits[idx] != sorted_fruits[idx]:
        out_of_place += 1

print(out_of_place - 1 if out_of_place > 0 else 0)
