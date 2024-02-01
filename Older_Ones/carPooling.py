from typing import List


def carPooling(trips, capacity):
    locations = [[0, 0]*1001]
    for num_pass, src, dest in trips:
        locations[src][0] += num_pass
        locations[dest][1] += num_pass

    total = 0
    for i in range(len(locations)):
        total = total + locations[i][0] - locations[i][1]
        if total > capacity:
            return False
    return True


print(carPooling(trips=[[3, 2, 8], [4, 4, 6], [10, 8, 9]], capacity=11))
