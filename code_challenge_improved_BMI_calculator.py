# BMI Formula: weight (lb) / [height (in)]2 x 703.

# convert the input to type int
weight = int(input("what is your weight in lbs? "))
height = int(input("what is your height in inches? "))
# height squared then divided by weight then multiplied by 703, convert it to int
bmi = int((weight / height ** 2) * 703)

print(f"your BMI: {bmi}")
# using conditional statements to print out the results of the BMI
if bmi <= 18.5:
    print("You are underweight.")
elif bmi <= 24.9:
    print("You are Normal weight.")
elif bmi <= 29.9:
    print("You are Overweight.")
else:
    print("You are Obese.")