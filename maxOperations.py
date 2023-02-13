from operator import index
from typing import Counter, List


def maxOperations(nums: List[int], k: int) -> int:
    nums.sort()
    counter = 0
    dictn = Counter(nums)
    for i in dictn:
        reverse = k-i
        if reverse == i:
            counter += int(i/2)
        elif reverse in dictn and dictn[k-i] != 0 and dictn[i] != 0:
            minim = min(dictn[i], dictn[k-i])
            counter += minim
            dictn[i] -= minim
            dictn[k-i] -= minim
    return list(dictn)


maxOperations([4, 4, 1, 3, 1, 3, 2, 2, 5, 5, 1, 5, 2, 1, 2, 3, 5, 4], 2)
