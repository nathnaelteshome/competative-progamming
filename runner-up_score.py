if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    sorted_arr = sorted(arr)
    non_identical = {x for x in sorted_arr}
    non_identical_list = list(non_identical) 
    
    print(non_identical_list[-2])
    