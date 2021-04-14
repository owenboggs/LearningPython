print("welcome to the tip calculator.")
bill_total = float(input("What was the total bill? "))
tip_percentage = int(input("What percentage tip would you like to give? "))
total_people = int(input("How many people to split the bill?"))

# first we calculate the tip percentage
# tip_percentage = tip_percentage / 100 gives us the percentage as a floating point number
tip_percentage /= 100
# multiply the floating point number by the cost of the bill and round to two decimal places
total_tip = round(tip_percentage * bill_total, 2)
# add the cost of the total_tip to the bill_total
bill_total += total_tip
# divide the bill_total by the number people splitting the bill
# round down to two decimal places
individual_cost = round(bill_total / total_people, 2)
# using the format function to hard code in the two decimal places for the cents
individual_cost = "{:.2f}".format(individual_cost)
print(f"Each person should pay {individual_cost}")
