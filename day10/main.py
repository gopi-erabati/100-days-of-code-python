## Days in month

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month != 2:
        return month_days[month - 1]
    else:
        leap = is_leap(year)
        if leap:
            return 29
        else:
            return 28


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


## Calculator

# Calculator

# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def sub(n1, n2):
    return n1 - n2


# Multiply
def mul(n1, n2):
    return n1 * n2


# Divide
def div(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
}

from art import logo

print(logo)

print("Welcome to calculator!")


def calculator():
    continue_flag = True
    a = float(input("What's the first number: "))

    for symbol in operations:
        print(symbol)

    while continue_flag:
        operator = input('Pick an operator: ')
        b = float(input("What's the next number: "))

        f_name = operations[operator]
        result = f_name(a, b)

        print(f"{a} {operator} {b} = {result}.")

        is_continue = input(
                f"Type 'y' to continue with {result}, or type 'n' to start a new calculation: ")

        if is_continue == 'n':
            continue_flag = False
            calculator()
        elif is_continue == 'y':
            a = result


calculator()
