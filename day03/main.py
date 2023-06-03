## If else example
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride rollarcoaster")
    age = int(input("What's your age?"))
    if age <= 5:
        bill = 5
        print("Child pay $5")
    elif age <= 18:
        bill = 7
        print("Youth pay $7")
    else:
        bill = 12
        print("Adult pay $12")
    wants_photo = input("Wants photos? Y or N: ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is {bill}")
else:
    print("You have to be more than 120 cm, sorry!")


## Even /odd number test
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check odd/even? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

## BMI 2.0 Interpretation
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

## Leap year
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

## Pizza bill
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bill = 0

if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
elif size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")

# Love calc
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()

count_t = name1.count('t')
count_t += name2.count('t')

count_r = name1.count('r')
count_r += name2.count('r')

count_u = name1.count('u')
count_u += name2.count('u')

count_e = name1.count('e')
count_e += name2.count('e')

true_score = count_t + count_r + count_u + count_e

# print(f"T occurs {count_t} times")
# print(f"R occurs {count_r} times")
# print(f"U occurs {count_u} times")
# print(f"E occurs {count_e} times")
# print(f"Total = {true_score})

count_l = name1.count('l')
count_l += name2.count('l')

count_o = name1.count('o')
count_o += name2.count('o')

count_v = name1.count('v')
count_v += name2.count('v')


love_score = count_l + count_o + count_v + count_e

# print(f"L occurs {count_l} times")
# print(f"O occurs {count_o} times")
# print(f"V occurs {count_v} times")
# print(f"E occurs {count_e} times")
# print(f"total = {love_score}")

total_score = int(str(true_score)+str(love_score))

if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif 40 < total_score < 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")