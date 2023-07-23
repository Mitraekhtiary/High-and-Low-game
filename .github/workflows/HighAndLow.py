import random

def High_Low(level, low, high):
 number = random.randint(low, high)
 print(f"level {level}: Guess a number between {low} and {high}" )
 guesses=1
 while True:
    guess = low + (high - low)//2
    answer = int(input("enter your number:"))
    if answer < guess:
        print ("please enter higher number!")
        low = guess + 1
    elif answer > guess:
        print ("please enter lower number!")
        high = guess - 1
    elif answer == guess:
        print ("good job! you entered true answer!")
        break
    else:
        print ("you entered invalid number!")
        break
#levels
levels = {1: (1, 10),
          2: (1, 100),
          3: (1, 500),
          4: (1, 1000),
          }
Level = int(input("Choose you level (1-4):"))
level_range = levels.get(Level)

if isinstance (level_range, tuple):
    High_Low (Level, level_range [0], level_range [1])
else:
    print ("Invalid level")

