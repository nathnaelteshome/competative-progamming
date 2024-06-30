# Given a limit n find all pair prime elements that are less than n and their sum is equal to n.

# input: n = 18
# output: [(5, 13), (7, 11)]

# ans of test
# def findPairs(n):
#     # Plan
#     """
#     Create a set and a list to hold all elements
#     iterate through the list and find the target
#     target = n - i
#     if target is found append to res and remove it from the set
#     then optimize by going through the list and deleting any multiple of i
#     """

#     numbers = [i for i in range(2, n)]
#     set_of_numbers = {i for i in range(2, n)}

#     res = []

#     for i in numbers:
#         target = n - i

#         if target in set_of_numbers:
#             res.append([i, target])
#             set_of_numbers.remove(target)

#         temp = i

#         while temp < n:
#             set_of_numbers.discard(temp)
#             temp += temp

#     return res


# # findPairs(18)  # [(5, 13), (7, 11)]


def findPairs(n):
    numbers = [i for i in range(n)]  # 0, 1, 2, 3, 4, 5
    set_of_numbers = {i for i in range(2, n)}  # 2, 3, 4, 5

    for idx, num in enumerate(numbers):
        if num in set_of_numbers:
            for i in range(num * num, n, num):
                set_of_numbers.discard(i)

    return list(set_of_numbers)


print(findPairs(18))
