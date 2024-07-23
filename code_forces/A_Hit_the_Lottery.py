withDrawl = int(input())

notes = [100, 20, 10, 5, 1]
count = 0

for note in notes:
    count += withDrawl // note
    withDrawl %= note

print(count)
