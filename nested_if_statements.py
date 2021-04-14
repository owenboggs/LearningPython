print("Welcome to the rollercoaster")
print("Must be over 40 inches to ride")
height = int(input("How tall are you in inches? "))
if height > 40:
    print("Welcome! You are tall enought to ride the coaster")
    age = int(input("How old are you? "))
    # nested if statement will only happen if the previous if statement is true
    if age <= 12:
        print("Ticket is $5")
    # elif will only check if true if the previous if statement is false
    elif age <= 18:
        print("Ticket is $7")
    # else will happen if both previous nested if statements are false
    else:
        print("Ticket is $12")
# if the first if statement is false it skips all the nested if statements.
else:
    print("Sorry, you are not tall enough for this ride")