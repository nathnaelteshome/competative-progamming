n, m = int(input().split())
dictionary = {}

for _ in range(n):
    name, ip = str(input().split())
    dictionary[ip] = name

for _ in range(m):
    command, ip = str(input().split())
    print(f"{command} {ip} #{dictionary[ip]}")

