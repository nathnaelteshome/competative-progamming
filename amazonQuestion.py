from bisect import bisect_left


def getSmallerItems(items, start, end, query):
    results = []
    
    for i in range(len(query)):
        arr = []
        for j in range(len(start)):
            for k in range(start[j], end[j] + 1):
                arr.append(items[k])
        
        arr.sort()  # Sort the arr
        
        count = bisect_left(arr, query[i])
        results.append(count)
    
    return results

# Example usage:
items = [1, 2, 5, 4, 5]
start = [0, 0, 1]
end = [1, 2, 2]
prefix = [2,3,3,0,0]
query = [2, 4]
print(getSmallerItems(items, start, end, query))  # Output: [2, 5]


