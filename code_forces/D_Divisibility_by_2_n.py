test_cases = int(input())

for _ in range(test_cases):
    size = int(input())
    numbers = list(map(int, input().split()))

    count = 0
    for num in numbers:
        while num % 2 == 0:
            count += 1
            num //= 2

    count_array = []
    count3 = 0
    if size >= 2:
        for i in range(2, size + 1, 2):
            count2 = 0
            while i % 2 == 0:
                count2 += 1
                count3 += 1
                i //= 2

            count_array.append(count2)

    if count + count3 < size:
        print(-1)
        continue

    count_array.sort(reverse=True)
    cc = 0
    if count >= size:
        print(0)
    else:
        for i in count_array:
            count += i
            cc += 1
            if count >= size:
                print(cc)
                break
