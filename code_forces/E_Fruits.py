n, m = map(int, input().split())

fruits = list(map(int, input().split()))
fruit_names = []

for _ in range(m):
    fruit_names.append(input())

fruit_counts = []

for fruit in set(fruit_names):
    fruit_counts.append([fruit_names.count(fruit), fruit])

fruit_counts.sort()
sorted_fruit_counts = fruit_counts[::-1]
fruits.sort()

total_cost_1 = 0
total_cost_2 = 0

for i in range(len(fruit_counts)):
    total_cost_1 += sorted_fruit_counts[i][0] * fruits[i]
    total_cost_2 += sorted_fruit_counts[i][0] * fruits[-(i + 1)]

print(total_cost_1, total_cost_2)
