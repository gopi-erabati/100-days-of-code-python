print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

print("Day 1 - String Manipulation")
print("String Concatenation is done with the \"+\" sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

name = input('What is your name? ')
print(len(name))

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
c = b
b = a
a = c

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

#1. Create a greeting for your program.
print('Welcome to Band Name Generator')
#2. Ask the user for the city that they grew up in.
city = input('What is the name of the city you grew up?\n')
#3. Ask the user for the name of a pet.
pet = input('What is the name of your pet?\n')
#4. Combine the name of their city and pet and show them their band name.
print(f'Your new brand name is {city} {pet}')
#5. Make sure the input cursor shows on a new line: