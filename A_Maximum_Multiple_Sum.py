t = int(input())

for _ in range(t):
  n = int(input())
  ans = 0
  best = 2

  for i in range(2, n + 1):
    mid = n // i
    cur_sum = i*(mid*( mid+1 )//2)

    if cur_sum > ans:
      ans = max(ans, cur_sum )
      best = i
  print(best)



