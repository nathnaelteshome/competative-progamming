from collections import Counter

n = input().split()
boxes = [int(x) for x in input().split()]
dictionary = Counter(boxes)
output = 1

for value in dictionary.values():
    if output < value:
        output = value

print(output)

