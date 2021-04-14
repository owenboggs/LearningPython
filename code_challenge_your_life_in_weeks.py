# calculate days weeks and months left if your life expectancy was 90 years
# first determine current age
current_age = int(input("How old are you? "))
# subtract current age from 90
time_left = 90 - current_age
# 365 days in a year, 52 weeks in a year, 12 months in a year
days = time_left * 365
weeks = time_left * 52
months = time_left * 12
print(f"You have {days} days, {weeks} weeks and {months} months left.")

