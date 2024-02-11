number_of_drinks = int(input())
juices = [int(x) for x in input().split()]
summation = 0

for juice in juices:
    summation += juice

print(summation/number_of_drinks)
    
    
