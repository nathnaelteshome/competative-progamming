title = "Smallest Even Multiple"

arr = title.split(" ")
res = ""
for word in arr:
    res += word.lower() + "_"

print(res[:-1] + ".py")