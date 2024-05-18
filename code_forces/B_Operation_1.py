import math


a, m = [int(x) for x in input().split()]

min_operation = math.ceil(a/2)
valid_operation = min_operation if min_operation % m == 0 else min_operation + m - (min_operation % m )

print(valid_operation if valid_operation <= a else -1)