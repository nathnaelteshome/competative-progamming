from collections import defaultdict
import random

def findPermutations(n, shoe_sizes):  
    ans = [0] * n 
    # make a dictionary of shoe sizes
    shoe_hash = defaultdict(list)
    for idx, size in enumerate(shoe_sizes):
        shoe_hash[size].append(idx)

    #check everyone has a shoe_size pair
    for key, val in shoe_hash.items():
        if len(val) == 1:
            return -1
    
    # make a permutation and append to the ans
    for key in shoe_hash.keys():
        permutation_hash = {}
        same_sizes_index = shoe_hash[key]
        #randomize it so it can be any permutation other than every element is different from the orginal
        random.shuffle(same_sizes_index)
        for idx, element in enumerate(same_sizes_index):
            if idx == 0:
                val = same_sizes_index[-1]
            else:
                val = same_sizes_index[idx - 1]
            permutation_hash[element] = val
        
        for idx in range(n):
            if idx in permutation_hash:
                ans[idx] = permutation_hash[idx] + 1

    return " ".join(map(str,ans))


t = 1

for _ in range(t):
    n = 5
    shoe_sizes = [1,1,1,1,1]
    print(findPermutations(n, shoe_sizes))


    
        


