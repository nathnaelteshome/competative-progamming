for _ in range(int(input())):
    num_lights, color = input().split()
    sequence = (input() * 2)[::-1]
    max_length = current_length = 0
    for light in sequence:
        current_length += 1
        if light == "g":
            current_length = 0
        if light == color:
            max_length = max(max_length, current_length)
    print(max_length)
