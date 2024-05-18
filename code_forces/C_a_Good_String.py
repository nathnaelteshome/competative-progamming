import sys

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     s = input()

#     def recursion(l, r, curr):

#         if r <= l + 1:
#             if s[l] == curr:
#                 return 0
#             else:
#                 return 1

#         else:
#             mid = (l + r) // 2
#             opt1 = recursion(l, mid, chr(ord(curr) + 1)) + sum(
#                 [1 for i in range(mid, r) if s[i] != chr(ord(curr) + 1)]
#             )
#             opt2 = recursion(mid, r, chr(ord(curr) + 1)) + sum(
#                 [1 for i in range(l, mid) if s[i] != chr(ord(curr) + 1)]
#             )

#         return min(opt1, opt2)

#     print(recursion(0, n - 1, "a"))

t = int(input())
for _ in range(t):

    length = int(input())
    string = tuple(input().strip())

    def recursion(start, end, curr):
        if start > end:
            return 0
        if start == end:
            if string[start] == curr:
                return 0
            return 1
        mid = (start + end) // 2
        left = (mid - start + 1) - string[start : mid + 1].count(curr)
        right = (end - mid) - string[mid + 1 : end + 1].count(curr)
        return min(
            recursion(start, mid, chr(ord(curr) + 1)) + right,
            recursion(mid + 1, end, chr(ord(curr) + 1)) + left,
        )

    print(recursion(0, length - 1, "a"))

a = b = 0
input()
for i in input():
    a += b == i
    b = i
print(a)
