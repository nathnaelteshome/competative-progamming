def longestCommonPrefix( strs):
        first_str = strs[0]
        for i in range(len(first_str)):
            for j in range(1, len(strs)):
                curr_str = strs[j]
                if first_str[:i+1] != curr_str[:i+1]:
                    return first_str[:i]
        return first_str

