# from collections import Counter


# def findPermutations(n, shoe_sizes):  
#     ans = list(range(1, n + 1))
    
#     l, r = 0, 0
#     while r < n:
#         # Find contiguous equal elements
#         while r < n - 1 and shoe_sizes[r] == shoe_sizes[r + 1]:
#             r += 1

#         if l == r:  # All elements are equal, no valid permutation
#             return -1

#         # Rotate permutation (optimized for in-place modification)
#         ans = [ans[l: r + 1][-1]] + ans[l: r + 1][:len(ans[l: r + 1]) - 1]

#         l = r + 1
#         r += 1
        
                

#         l = r + 1
#         r += 1

#     return " ".join(map(str, ans)) 
    



# t = int(input())

# for _ in range(t):
#     n = int(input())
#     shoe_sizes = [int(x) for x in input().split()]
#     print(findPermutations(n, shoe_sizes))


    
        
from typing import Counter

t = int(input())
for _ in range(t):
    num_shoes = int(input())
    shoe_sizes = [int(x) for x in input().split()]
    shoe_size_counter = Counter(shoe_sizes)

    # Check if there is any shoe size that appears only once
    if list(shoe_size_counter.values()).count(1):
        print(-1)
        continue

    #  a function to calculate the new index for each shoe size
    def calculate_new_index(index):
        if index != 0 and shoe_sizes[index] == shoe_sizes[index-1]:
            return index
        else:
            return index + shoe_size_counter[shoe_sizes[index]]
    
    new_order = [calculate_new_index(index) for index in range(num_shoes)]
    print(*new_order)