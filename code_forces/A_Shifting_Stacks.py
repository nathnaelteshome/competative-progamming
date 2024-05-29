for _ in range(int(input())):
    num_elements = int(input())
    elements = list(map(int, input().split()))
    result = "YES"
    sum_elements = 0
    for i in range(num_elements):
        sum_elements += elements[i]
        if sum_elements < i * (i + 1) // 2:
            result = "NO"
    print(result)
