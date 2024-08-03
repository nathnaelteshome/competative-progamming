word = input()
hello = "hello"
left = 0

for idx in range(len(word)):
    if hello[left] == word[idx]:
        left += 1
    if left == 5:
        break

print("YES" if left == 5 else "NO")
