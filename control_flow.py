# learning control flow using if, elif and else

print("Welcome to the rollercoaster!")
height = int(input("Enter your height in inches: "))
# if height is greater then 48 then it is true and will execute the following indented line
if height > 48:
    print("You are tall enough for this ride!")
# if the statement is false then it executes the indented lines after else:
else:
    print("Sorry shorty, your not tall enough.")

# other comparison operators include:
# <= less than or equal to, if either are true then its true
# >= greater than or equal to, if either are true then its true
# > greater than
# < less than
# == this compares the values on both sides and if they match it is true
