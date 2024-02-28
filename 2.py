names = ["Mary","John","Emma"]
heights = [180,165,170]

result = []

result += [1,2]

fdsaf= []

# # counting sort

# maximum = max(heights)
# count = [0] * maximum

# for height in heights:
#     count[height] += 1

# target = 0

# for index in range(len(count), -1, -1):
#     for i in range(count[index]):
#         names[target] = index
#         target += 1


# insertion 
# for i in range(len(names)):
#             max_idx = i
#             for j in range(i + 1, len(names)):
#                 if heights[j] > heights[max_idx]:
#                     max_idx = j
#             names[i], names[max_idx] = names[max_idx], names[i]
        
#         return names


# selection  sort

# for i in range(len(names)):
#     max_idx = i
#     for j in range(i + 1, len(names)):
#         if heights[j] > heights[max_idx]:
#             max_idx = j
#     names[i], names[max_idx] = names[max_idx], names[i]

# print(names)



# bubble sort

# name_height_pair = [[names[x], heights[x]] for x in range(len(names))]

# for i in range(len(names)):
#     flag = False
#     for j in range(len(names) - i - 1):
#         if name_height_pair[j][1] < name_height_pair[j + 1][1]:
#             name_height_pair[j], name_height_pair[j + 1] = name_height_pair[j + 1], name_height_pair[j]
#             flag = True
        
#         if not flag:
#             break

# print([x[0] for x in name_height_pair])

