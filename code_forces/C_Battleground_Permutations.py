# 2 4 5 6 8 9
# 1 1 3 4 5 6

# 3*3*3*2*2*1

# 2*2*2*2*2*1

n = int(input())

for _ in range(n):
    size = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    
    def unn(a,b,size):
        a.sort(reverse=True)
        b.sort(reverse=True)
        idx = 0
        count = 0
        result = 1
        countLength = 0

        for num in b:
            while idx < size and a[idx] > num:
                count += 1
                idx += 1

            result *= (count - countLength)
            if (count - countLength) == 0:
                return 0
                
            countLength += 1
        
        
        return result % ((10**9) + 7)

    print(unn(a,b,size))


