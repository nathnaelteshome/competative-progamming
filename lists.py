if __name__ == '__main__':
    N = int(input())
    lst = []
    for x in range(N):
        command = list(map(str, input().split()))
        
        if command[0] == 'insert':
            lst.insert(int(command[1]), int(command[2]))  
        elif command[0] == 'print':
            print(lst)
        elif command[0] == 'remove':
            lst.remove(int(command[1]))
        elif command[0] == 'append':
            lst.append(int(command[1]))
        elif command[0] == 'sort':
            lst.sort()
        elif command[0] == 'pop':
            lst.pop()
        else:
            lst.reverse()
            
