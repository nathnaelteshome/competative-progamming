t = int(input())

for _ in range(t):
    string = input()
    a, b, c = [i for i in string.split()]
    if a == b:
        print(c)
    elif a == c:
        print(b)
    else:
        print(a)
