def count_special(word):
    """
    Returns the number of special characters in `word`.
    A character c is special if:
      1. c appears in both lowercase and uppercase forms in word.
      2. Every lowercase occurrence of c appears before the first uppercase occurrence of c.
    """
    n = len(word)
    last_lower = [-1] * 26       # last index of each lowercase character
    first_upper = [n] * 26       # first index of each uppercase character
    
    for i, ch in enumerate(word):
        if 'a' <= ch <= 'z':
            idx = ord(ch) - ord('a')
            last_lower[idx] = i
        elif 'A' <= ch <= 'Z':
            idx = ord(ch) - ord('A')
            if first_upper[idx] > i:
                first_upper[idx] = i
    
    # Count letters that satisfy: seen in both forms, and all lowers come before the first upper.
    count = 0
    for idx in range(26):
        if last_lower[idx] != -1 and first_upper[idx] != n and last_lower[idx] < first_upper[idx]:
            count += 1
    return count


print(count_special("XxYYyZz"))