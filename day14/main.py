from art import logo, vs
from game_data import data
import random

data_len = len(data)


def get_two_choices(len):
    ch1 = random.randint(0, len - 1)
    ch2 = random.randint(0, len - 1)
    while ch2 == ch1:
        ch2 = random.randint(0, len - 1)
    return ch1, ch2


score = 0
is_game_over = False
ch1, ch2 = get_two_choices(data_len)


def user_is_correct(user_choice, ch1_score, ch2_score):
    if ch1_score > ch2_score:
        return user_choice == 'a'
    else:
        return user_choice == 'b'


while not is_game_over:
    print(logo)

    if score > 0:
        print(f"You're right! Current score: {score}.")

    print(
        f"Compare A: {data[ch1]['name']}, a {data[ch1]['description']}, from {data[ch1]['country']}")
    ch1_score = data[ch1]['follower_count']
    print(vs)
    print(
        f"Against B: {data[ch2]['name']}, a {data[ch2]['description']}, from {data[ch2]['country']}")
    ch2_score = data[ch2]['follower_count']

    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    is_user_correct = user_is_correct(user_choice, ch1_score, ch2_score)

    if is_user_correct:
        score += 1
        ch1 = ch2
        _, ch2 = get_two_choices(data_len)
        while ch2 == ch1:
            _, ch2 = get_two_choices(data_len)
    else:
        is_game_over = True
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")


