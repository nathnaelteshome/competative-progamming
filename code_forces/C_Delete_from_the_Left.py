string1 = input()
string2 = input()
i = len(string1)
j = len(string2)
while i * j * (string1[i - 1] == string2[j - 1]):
    i -= 1
    j -= 1
print(i + j)
