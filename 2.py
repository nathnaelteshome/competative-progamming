names = ["Mary","John","Emma"]
heights = [180,165,170]

name_height_pair = [[names[x], heights[x]] for x in range(len(names))]

for i in range(len(names)):
    for j in range(len(names) - i - 1):
        if name_height_pair[j][1] < name_height_pair[j + 1][1]:
            name_height_pair[j], name_height_pair[j + 1] = name_height_pair[j + 1], name_height_pair[j]

print([x[0] for x in name_height_pair])

