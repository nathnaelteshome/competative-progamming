from collections import defaultdict


def max_sum(monthlyPrices, k):

  left = 0
  maxSum = 0
  curSum = 0
  hashMap = defaultdict(int)  

  for right in range(len(monthlyPrices)):
    curPrices = monthlyPrices[right]

    hashMap[curPrices] += 1
    curSum += curPrices

    while hashMap[curPrices] > 1:
      hashMap[monthlyPrices[left]] -= 1
      curSum -= monthlyPrices[left]
      left += 1

    if right - left + 1 == k:
      maxSum = max(maxSum, curSum)

      hashMap[monthlyPrices[left]] -= 1
      curSum -= monthlyPrices[left]
      left += 1 
  return maxSum

# example usage
print(max_sum([1, 2, 1, 3, 4, 3, 2, 4], 3))  # 10
