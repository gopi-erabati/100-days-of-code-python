## Heads or Tails
import random

choice = random.randint(0, 1)

if choice == 0:
    print("Tails")
elif choice == 1:
    print("Heads")

## Random choice
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
import random

choice = random.choice(names)
print(f"{choice} is going to buy the meal today!")

## Treasure Map
# 🚨 Don't change the code below 👇
row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
col_pos = int(position[0]) - 1
row_pos = int(position[1]) - 1

map[row_pos][col_pos] = 'X'

# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

## Rock, Paper and Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
import random

choices = [rock, paper, scissors]

my_choice = int(
    input("What do you choose ? 0 for Rock, 1 for Paper and 2 for Scissors"))

if my_choice < 0 or my_choice >= 35:
    print("You type an invalid number so you Lose")
else:
    print("You choose:")
    print(choices[my_choice])

    comp_choice = random.choice([0, 1, 2])
    print("Computer chooses")
    print(choices[comp_choice])

    if my_choice == comp_choice:
        print("Draw")
    elif my_choice == 0 and comp_choice == 1:
        print("Computer Won")
    elif my_choice == 0 and comp_choice == 2:
        print("You Won")
    elif my_choice == 1 and comp_choice == 0:
        print("You Won")
    elif my_choice == 1 and comp_choice == 2:
        print("Computer Won")
    elif my_choice == 2 and comp_choice == 0:
        print("Computer Won")
    elif my_choice == 2 and comp_choice == 1:
        print("You Won")
