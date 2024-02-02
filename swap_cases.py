def swap_case(s):
    res = ""
    for i in s:
        if i.isupper():
            word = i.lower()    
        else:
            word = i.upper()
        res += word    
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)