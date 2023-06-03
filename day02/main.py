## sum of two digit number
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇
print(int(two_digit_number[0]) + int(two_digit_number[1]))

## BMI
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = int(float(weight)/float(height)**2)
print(bmi)

## Life in Weeks
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
current_age = int(age)
final_age = 90

years_left = final_age - current_age
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")

## Tip calculator
#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to tip calculator")
total_bill = float(input("What was the total bill? "))
tip = float(input("What percentage of tip you would like to give? "))
num_people = int(input("How many people to split the bill? "))

bill_per_person = (total_bill * (1 + tip / 100)) / num_people

print(f"Each person should pay: {bill_per_person:.2f}")