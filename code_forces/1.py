#  function that takes a string and returns if it is palindrome or not
def isPalindrome(s):
    return s == s[::-1]

# fizzbuzz function
def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

