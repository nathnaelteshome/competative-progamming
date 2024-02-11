number_of_people = input()
arr = [int(x) for x in input().split()]
difficulty = "EASY"

for i in arr:
    if i == 1:
        difficulty = "HARD"
        
print(difficulty)
    
    
    
