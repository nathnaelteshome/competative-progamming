for _ in range(int(input())):
    num_strings = int(input())
    strings = [input() for _ in range(num_strings)]
    unique_strings = set(strings)
    result = ""
    for i in range(num_strings):
        for j in range(1, len(strings[i])):
            if strings[i][:j] in unique_strings and strings[i][j:] in unique_strings:
                result += "1"
                break
        else:
            result += "0"
    print(result)
