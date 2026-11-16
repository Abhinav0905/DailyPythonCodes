import random

def play_number_guessing_game():
    """Simple number guessing game"""
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize attempt counter
    attempts = 0
    max_attempts = 10
    
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100")
    print(f"You have {max_attempts} attempts to guess it.\n")
    
    # Game loop
    while attempts < max_attempts:
        # Simulate user input for demonstration
        # In real game, you'd use: guess = int(input("Enter your guess: "))
        guess = random.randint(1, 100)
        attempts += 1
        
        print(f"Attempt {attempts}: Guessed {guess}")
        
        # Check if guess is correct
        if guess == secret_number:
            print(f"Congratulations! You won in {attempts} attempts!")
            return True
        # Provide hints
        elif guess < secret_number:
            print("Too low! Try a higher number.\n")
        else:
            print("Too high! Try a lower number.\n")
    
    # If max attempts reached
    print(f"Game Over! The number was {secret_number}")
    return False

# Main execution
if __name__ == "__main__":
    # Play the game
    play_number_guessing_game()
