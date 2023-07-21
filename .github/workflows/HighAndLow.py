import random
def High_Low(level, low, high):
    number = random.randint(low, high)
    print(f"Level {level}: Guess a number between {low} and {high}")
    
    while True:
        guess = int(input("Enter your guess: "))

        if guess < number:
            print("Try guessing higher.")
        elif guess > number:
            print("Try guessing lower.")
        else:
            print("WOW! You guessed it right^^")
            break

# levels
levels = {
    1: (1, 10),
    2: (1, 100),
    3: (1, 500),
    4: (1, 1000)
}

# choose
Level = int(input("Choose a level (1-4): "))
level_range = levels.get(Level)
if isinstance(level_range, tuple):
    High_Low(Level, level_range[0], level_range[1])
else:
    print("Invalid level!")

