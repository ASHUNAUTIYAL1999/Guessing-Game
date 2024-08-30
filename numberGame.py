import random 


def generate_number():
    return random.randint(1,100)


def get_user_guess():
    while True:
        try:
            guess=int(input("number to printed"))
            return guess
        except ValueError:
            print("please enter the valid number")


def check_guess(number, guess):
    if guess < number:
        return "Too low!"
    elif guess > number:
        return "Too high!"
    else:
        return "Correct!"


def play_game(max_attempts=8):
    number = generate_number()
    attempts=0 
    while attempts<max_attempts:
        guess = get_user_guess()  # Get the user's guess
        result = check_guess(number, guess)  # Check the guess
        print(result)
        attempts=attempts + 1  # Provide feedback to the user
        if result == "Correct!":
            break 
        else:
            remaining_attempts=max_attempts-attempts
            if remaining_attempts>0:
                print("you have remaining_attempts attempts left", remaining_attempts)
            else:
                print("sorry ,out of chances",number)
                break

if __name__=="__main__":
    play_game()