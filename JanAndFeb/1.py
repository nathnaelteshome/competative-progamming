title = "Transpose Matrix"

arr = title.split(" ")
res = ""
for word in arr:
    res += word.lower() + "_"
    name = res[:-1] + ".py"

print(res[:-1] + ".py")

file = open(name , 'w')
file.close()

