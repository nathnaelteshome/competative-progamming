powerLevel = [int(x) for x in input().split()]
armySize = [int(x) for x in input().split()]
alliance1 = 0
alliance2 = 0
for idx in range(3):
    alliance1 += powerLevel[idx] * armySize[idx]

for idx in range(3, len(powerLevel)):
    alliance2 += powerLevel[idx] * armySize[idx]

# print(alliance1,alliance2)

if alliance1 > alliance2:
    print("WIN")
elif alliance1 < alliance2:
    print("LOSE")
else:
    print("DRAW")


