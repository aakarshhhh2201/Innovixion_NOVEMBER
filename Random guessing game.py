import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Set the number of attempts
attempts = 5

print("Welcome to the Number Guessing Game!")
print(f"Guess the secret number between 1 and 100. You have {attempts} attempts.")

# Main game loop
for attempt in range(1, attempts + 1):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))
    
    if guess < secret_number:
        print("Too low! Try a higher number.")
    elif guess > secret_number:
        print("Too high! Try a lower number.")
    else:
        print(f"Congratulations! You've guessed the secret number ({secret_number}) in {attempt} attempts.")
        break
else:
    print(f"Out of attempts! The secret number was {secret_number}. Better luck next time.")
