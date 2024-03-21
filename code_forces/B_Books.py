n, t = [int(x) for x in input().split()]
 
books = [int(x) for x in input().split()]
 
left = 0
right = 0
answer = 0
summation = 0


for r in range(n):
    summation += books[r]
    while summation > t:
        summation -= books[left]
        left += 1
    answer = max(answer, r - left + 1)

 
print(answer)
   