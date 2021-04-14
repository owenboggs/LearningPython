num_char = len(input("What is your name? "))

# we convert the variable num_char to str for concatenation.
# len returns type int normally
print("Your name has " + str(num_char) + " characters")

# using the type function to tell us what data type we have
a = float(123)
print(type(a))

# using the str to change the data type from int
print(str(70) + str(100))

# challenge: take the input of 2 consecutive numbers and add them together
two_digit_number = input("Type a two digit number: ")
# slice the input str and assign to variables
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
# covert the slices to type int
sum_of_two_numbers = int(first_digit) + int(second_digit)
print(f"the two numbers add up to {sum_of_two_numbers}.")
