# BMI Formula: weight (lb) / [height (in)]2 x 703.

# convert the input to type int
weight = int(input("what is your weight in lbs? "))
height = int(input("what is your height in inches? "))
# height squared then divided by weight then multiplied by 703, convert it to int
bmi = int((weight / height ** 2) * 703)
print("BMI Categories:\nUnderweight = <18.5\nNormal weight = 18.5–24.9\nOverweight = 25–29.9\nObesity = BMI of 30 or greater")
print(f"your BMI: {bmi}")
