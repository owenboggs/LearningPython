# how to get the remainder from a division problem using the modulo operator

# 2 goes into 7 three times with a remainder of 1
print(7 % 2)

# 2 goes into 3 times which is 6 with a remainder of 0
print(6 % 2)

# modulo can be useful to determine if a number is even or odd
number = int(input("Enter a number: "))
if number % 2 == 0: # the number is even
    print("This is a even number.")
else:
    print("This is an odd number.")



