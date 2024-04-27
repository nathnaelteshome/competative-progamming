# The first line of the input contains a single integer t
#  (1≤t≤104
# ) — the number of test cases. Then the descriptions of the test cases follow.

# The first line of each test case contains three integers n
# , x
# , and y
#  (2≤n≤2⋅105
# , 1≤x,y≤109
# ) — the size of the array and Polycarp's favorite integers.

# The second line of each test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤109
# ) — the elements of the array.

# It is guaranteed that the sum of n
#  over all test cases does not exceed 2⋅105
# .

# Output
# For each test case, output a single integer — the number of beautiful pairs in the array a
# .
def count_beautiful_pairs():
    t = int(input())
    for _ in range(t):
        n, x, y = [int(x) for x in input().split()]
        A = [int(x) for x in input().split()]
        ans = calculate_pairs(A, x, y)
        print(ans)

def calculate_pairs(A, x, y):
    d = dict()
    ans = 0
    for e in A:
        dx, dy = e % x, e % y
        ans += d.get(((x - dx) % x, dy), 0)
        d[(dx, dy)] = d.get((dx, dy), 0) + 1
    return ans

count_beautiful_pairs()