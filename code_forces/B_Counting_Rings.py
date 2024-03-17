s = str(input())
shapes = [str(x) for x in s]
result , idx = 0, 0

while idx < len(shapes):
    count = 0

    while idx < len(shapes) and shapes[idx] == "O":
        count += 1
        idx += 1

    result = max(result, count)
    idx += 1 

print(result)

