for _ in range(int(input())):
    num_teams = int(input())
    team_names = [input() for _ in range(num_teams)]
    unique_names = set(team_names)
    result = ""
    for i in range(num_teams):
        current_name = team_names[i]
        for j in range(1, len(current_name)):
            prefix = current_name[:j]
            suffix = current_name[j:]
            if prefix in unique_names and suffix in unique_names:
                result += "1"
                break
        else:
            result += "0"
    print(result)
