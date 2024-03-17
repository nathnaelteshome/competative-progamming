m = int(input())
array = [int(x) for x in input().split()] 
set_ = set(i % 2 for i in array)

if len(set_) != 1:
    array = sorted(array)
    
print(*array)