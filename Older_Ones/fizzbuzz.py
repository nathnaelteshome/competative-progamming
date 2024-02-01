def fizzBuzz(n: int):
    answer = []
    i = 1
    while(i <= n):
        if (i % 3 == 0 and i % 5 == 0):
            answer.append('FizzBuzz')
        elif(i % 3 == 0):
            answer.append('Fizz')
        elif(i % 5 == 0):
            answer.append('Buzz')
        else:
            answer.append(i)
    i += 1
    return answer


fizzBuzz(5)


# divisors =[[3,'Fizz'],[5,'Buzz']]

# output=[]
# i=1
# while i <= n:
#    newString =''
#    for j in divisors:
#     if i% divisors[j][0] ==o:
#         newString += divisors[j][1]

# output.push()
