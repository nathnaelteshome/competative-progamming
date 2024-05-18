test_cases = int(input())
# [-34 -56 1 2 23 3 5 6 40]
# [-56 -34 1 2 3 5 6 23 40]

def findmax(n, array, maxmimum):
  array.sort()
  left_product = array[0] * array[1]
  right_product = array[-1] * array[-2]

  return maxmimum

for _ in range(test_cases):
  n = int(input())
  array = [int(x) for x in input().split()]
  print(findmax(n, array, maxmimum))


