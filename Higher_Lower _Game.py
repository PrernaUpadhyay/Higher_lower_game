from art import logo, vs
from cdata import data
import random

def format_data(account):
    account_name = account["name"]
    account_descr = account["profession"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score = 0
game_continue = True
account_b =random.choice(data) # random

while game_continue:
    # Choose two different random accounts
    account_a = account_b
    account_b = random.choice(data) #new_b

    # Ensure account_a and account_b are not the same
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n"* 20)



    a_followers = account_a["followers"]
    b_followers = account_b["followers"]
    is_correct = check_answer(guess, a_followers, b_followers)

    if is_correct:
        score += 1
        print(f"You are right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_continue = False  # End the game if the answer is wrong

# Final message when the game ends
print("Thank you for playing!")
