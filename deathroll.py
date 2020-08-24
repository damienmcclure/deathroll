import random
import time

print("""Welcome to Death Rolling.
In this game, you will start with a number,
roll 1 through that number, then the next player
will roll the resulting number. This will go back
and forth a player reaches 1. Whoever does loses!
The list of numbers rolled will be displayed
after each roll completes.""")

#filler
print(" ")

p1 = input("What is player one's name? ")

#filler
print(" ")

p2 = input("Player two's name? ")

#filler
print(" ")

min = 1
max = int(input("What is the maximum number? "))
rolls = [max]
playing = "yes"

#filler
print(" ")

while playing == "yes":
    # turn counter
    n = 1

    if (n % 2) == 1:
        print(" ")
        print(p1 + ", it is your turn.")
        input("Press ENTER to roll...")
        print("Rolling the dice...")
        time.sleep(2)
        roll = (random.randint(min, rolls[-1]))
        print("You got a " + str(roll) + "!")
        time.sleep(1)
        rolls.append(roll)
        print(rolls)

        # Loss code
        if roll == 1:
            print("Congratulations " + p2 + ", you win!")
            time.sleep(2)
            exit()

        # Change players
        else:
            n += 1

    if (n % 2) == 0:
        print(" ")
        print(p2 + ", it is your turn.")
        input('Press ENTER to roll...')
        print("Rolling the dice...")
        time.sleep(2)
        roll = (random.randint(min, rolls[-1]))
        print("You got a " + str(roll) + "!")
        time.sleep(1)
        rolls.append(roll)
        print(rolls)

        # Loss code
        if roll == 1:
            print("Congratulations " + p1 + ", you win!")
            time.sleep(2)
            exit()

        # Change players
        else:
            n += 1
