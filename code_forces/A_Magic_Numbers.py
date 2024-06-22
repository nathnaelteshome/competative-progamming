n = input()
total_count = len(n)

if n.count("1") + n.count("144") + n.count("14") == total_count:
    print("YES")
else:
    print("NO")
