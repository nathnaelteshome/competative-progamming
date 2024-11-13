num = int(input())
prime_count = [0] * (num + 1)
for i in range(2, num):
  if prime_count[i] == 0:
    for j in range(2 * i, num + 1, i):
      prime_count[j] += 1
print(prime_count.count(2))