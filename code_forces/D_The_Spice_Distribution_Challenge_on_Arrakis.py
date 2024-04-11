n, m = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

reminders = []
ans = 0

for idx ,num in enumerate(arr):
    if idx == 0:
        reminders.append(num % m)
    else:
        reminders.append((reminders[-1] + num) % m)

for num in reminders:
    if num == 0:
        ans += ans + 1

print(reminders)
print(ans)
