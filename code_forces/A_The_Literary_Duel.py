n = int(input())
nums = [int(x) for x in input().split()]
Hermione = 0
Harry = 0
HermioneTurn = True
left = 0
right = n-1

while left <= right:
    highPower = 0
    if nums[right] > nums[left]:
        highPower += nums[right]
        right -= 1
    
    else:
        highPower += nums[left]
        left += 1
    if HermioneTurn:
        Hermione += highPower
        HermioneTurn = False
    else:
        Harry += highPower
        HermioneTurn = True
print(Hermione, Harry)
