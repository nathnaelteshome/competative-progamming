from collections import Counter

# single_winner, team_winner = 0, 0
row1 = [str(x) for x in input()]
row2 = [str(x) for x in input()]
row3 = [str(x) for x in input()]

col1 = [row1[0], row2[0], row3[0]]
col2 = [row1[1], row2[1], row3[1]]
col3 = [row1[2], row2[2], row3[2]]

diag1 = [row1[0], row2[1], row3[2]]
diag2 = [row1[2], row2[1], row3[0]]

count_row1 = Counter(row1)
count_row2 = Counter(row2)
count_row3 = Counter(row3)

count_col1 = Counter(col1)
count_col2 = Counter(col2)
count_col3 = Counter(col3)

count_diag1 = Counter(diag1)
count_diag2 = Counter(diag2)

total_row = list(count_row1.values()) + list(count_row2.values()) + list(count_row3.values())
total_col = list(count_col1.values()) + list(count_col2.values()) + list(count_col3.values())
total_diag = list(count_diag1.values()) + list(count_diag2.values())

single_winner = total_row.count(3) + total_col.count(3) + total_diag.count(3)
team_winner = total_row.count(2) + total_col.count(2) + total_diag.count(2)

print(single_winner)
print(team_winner)

