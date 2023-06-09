## Dictionary scores
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}


# TODO-2: Write your code below to add the grades to student_grades.👇
def scoring_criteria(score):
    if score >= 91:
        return "Outstanding"
    elif score >= 81:
        return "Exceeds Expectations"
    elif score >= 71:
        return "Acceptable"
    elif score <= 70:
        return "Fail"


for keys in student_scores:
    student_grades[keys] = scoring_criteria(student_scores[keys])

# 🚨 Don't change the code below 👇
print(student_grades)

## Nesting dict
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇
def add_new_country(country_name, num_of_visits, cities_visited):
    travel_log.append({
        "country": country_name,
        "visits": num_of_visits,
        "cities": cities_visited,
    })


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

## Bidding
# from replit import clear
# HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)

print("Welcome to bidding!")

# define a dict to store name and bid value
bids = dict()

bid_status_flag = True

while bid_status_flag:

    # ask the user for name and bid value
    name = input("What is your name?: ")
    bid = int(input("What is your bid value?: $"))

    # store the info in the dict
    bids[name] = bid

    # ask for more persons if avialble
    bid_status = input(
        "Press 'yes' to enter more bid values or press 'no' to end bidding\n")

    if bid_status == 'yes':
        import os
        os.system('clear')
    elif bid_status == 'no':
        bid_status_flag = False

# loop through dict and select highest bid
highest_bid = 0
for name in bids:
    bid_value = bids[name]
    if bid_value > highest_bid:
        highest_bid = bid_value
        highest_bidder = name

print(f"The winner is {highest_bidder} with value {highest_bid}")


