import random
def High_Low(level, low, high):
    number = random.randint(low, high)
    print(f"Level {level}: Guess a number between {low} and {high}")
    guesses = 1
    #number_loop
    while True:
        guess = low + (high-low)//2
        answer = int(input("Enter your guess: "))

        if answer < guess:
            print("Please enter higher number.")
            low = guess + 1
        elif answer > guess:
            print("Please enter lower number.")
            high = guess - 1
        elif answee == guess: 
            print("Good job! you've done it right^^")
            break
        else:
            print("(Invalid option!)")
            break

# levels
levels = {
    1: (1, 10),
    2: (1, 100),
    3: (1, 500),
    4: (1, 1000)
}

# choose_level
Level = int(input("Choose a level (1-4): "))
level_range = levels.get(Level)
if isinstance(level_range, tuple):
    High_Low(Level, level_range[0], level_range[1])
else:
    print("Invalid level!")

