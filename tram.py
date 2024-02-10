n = input()
num_passengers = 0
maximum = 0

for i in range(int(n)):
    exit, enter = input().split()
    num_passengers -= int(exit)
    num_passengers += int(enter)
    maximum = max(maximum, num_passengers)
    
print(maximum)