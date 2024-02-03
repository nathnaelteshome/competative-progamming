def split_and_join(line):
    # write your code here
    splitted_line = line.split(" ")
    joined_line = "-".join(splitted_line)
    
    return joined_line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)