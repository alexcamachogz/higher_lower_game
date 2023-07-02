from random import randint
from art import logo, vs
from game_data import data
from replit import clear

def clean_display():
    """Clean the display and show the logo"""
    clear()
    print(logo)

def random_option():
    """Generate a random number between 0 and game data length"""
    return randint(0, len(data) - 1)

def print_option(person):
    """Print information about the selected option"""
    return f"{person['name']}, {person['description']}, from {person['country']}"

def choose_option():
    """Request and validate user answer"""
    while True:
        answer = input("Who has more followers? Type 'A' or B: ").lower()
        if answer == "a" or answer == "b":
            return answer
        else:
            print("Invalid option. Please try again\n")

def compare_followers(a, b):
    """Check who was more followers"""
    return 'a' if a['follower_count'] > b['follower_count'] else 'b'

score = 0
def higher_lower_game(option_a = ""):
    global score
    option_a = data[random_option()] if option_a == "" else option_a
    option_b = data[random_option()]

    print(f"Compare A: {print_option(option_a)}")
    print(vs)
    print(f"Compare B: {print_option(option_b)}")

    user_answer = choose_option()
    clean_display()
    correct_answer = compare_followers(option_a, option_b)

    if user_answer == correct_answer:
        score += 1
        print(f"You are right! Current score: {score}")
        higher_lower_game(option_a = option_b)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
  
print(logo)
higher_lower_game()
