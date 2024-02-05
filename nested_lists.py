if __name__ == '__main__':
    lst = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append((name, score))  # Store name-score pairs as tuples (hashable)
        scores.append(score)
        
    second_lowest = sorted(list(set(scores)))[1]
    lst.sort(key=lambda x: (x[1], x[0]))


    for name, score in lst:
        if score == second_lowest:
            print(name)


