# single_winner, team_winner = 0, 0
row1 = [str(x) for x in input()]
row2 = [str(x) for x in input()]
row3 = [str(x) for x in input()]

col1 = set([row1[0], row2[0], row3[0]])
col2 = set([row1[1], row2[1], row3[1]])
col3 = set([row1[2], row2[2], row3[2]])

diag1 = set([row1[0], row2[1], row3[2]])
diag2 = set([row1[2], row2[1], row3[0]])

all_set = [set(row1), set(row2), set(row3), col1, col2, col3, diag1, diag2]


single_winner = {next(iter(x)) for x in all_set if len(x) == 1}
team_winner = {"".join(sorted(x)) for x in all_set if len(x) == 2}


print(single_winner)
print(team_winner)

