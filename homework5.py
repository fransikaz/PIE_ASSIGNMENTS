'''
HOMEWORK #5: Basic Loops
A program that generates numbers from 1 to 100 but prints;
'Fizz' for multiples of 3
'Buzz' for multiples of 5
'FizzBuzz' for multiples of both 3 and 5 and
'Prime' for prime numbers
'''


for n in range(1, 101):
    count = 0
    for i in range(1, n + 1):  # iteration to be used for checking prime numbers
        if (n % i) == 0:
            count += 1
    if n % 3 == 0 and n % 5 == 0:  # checking divisibility by both 3 and 5
        print("{:<3} {:<3}".format(n, " FizzBuzz"))
    elif n % 3 == 0:  # checking divisibility by 3
        print("{:<3} {:<3}".format(n, " Fizz"))
    elif n % 5 == 0:  # Checking divisibiltiy by 5
        print("{:<3} {:<3}".format(n, " Buzz"))
    elif count == 2:  # Checking if number is a prime
        print("{:<3} {:<3}".format(n, " prime"))
    else:
        print(n)  # printing other numbers


# Actual numbers from range have been printed to the left of the words for ease of verification
