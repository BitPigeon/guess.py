import time, random
from colorama import init, Fore, Back, Style

init()

def typestr(strtotype, randomrange=[0.1, 0.3], end="\n"):
    for letter in strtotype:
        print(letter, end="")
        time.sleep(random.uniform(randomrange[0], randomrange[1]))
    print(end, end="")


print("Welcome to guess.py, a Guess My Number game. See it on github https://github.com/desvasicek/guess.py. Report bugs at https://github.com/desvasicek/guess.py/issues\n")
print(f"COMPUTER:", end=" ")
typestr("I'm thinking of a number from 1 to 100. Can you guess it?", [0.01, 0.15])
number = random.randint(0, 100)
playing_game = True
in_program = True
while in_program:
    guesses = 0
    while playing_game:
        try:
            guess = input(">>> ")
            try:
                if int(guess) <= 100 and int(guess) >= 0:
                    print("YOU:", end=" ")
                    typestr(guess)
                    if int(guess) == number:
                        print(f"COMPUTER:", end=" ")
                        typestr(f"Wow! You guessed my number! It took you {str(guesses + 1)} guesses to solve this puzzle.", [0.01, 0.15], end=" ")
                        playing_game = False
                    elif int(guess) >= number:
                        print(f"COMPUTER:", end=" ")
                        typestr("Hmm... That's not it. Try lower.", [0.01, 0.15])
                        guesses += 1
                    elif int(guess) <= number:
                        print(f"COMPUTER:", end=" ")
                        typestr("Hmm... That's not it. Try higher.", [0.01, 0.15])
                        guesses += 1
                    else:
                        print(f"COMPUTER:", end=" ")
                        typestr("I think there was an error. Try restarting the program.", [0.01, 0.15])
                elif int(guess) > 100:
                    print(f"COMPUTER:", end=" ")
                    typestr("Sorry. The number has to be less than 100.", [0.01, 0.15])
                elif int(guess) < 0:
                    print(f"COMPUTER:", end=" ")
                    typestr("Sorry. The number has to be more than 0.", [0.01, 0.15])
                else:
                    print(f"COMPUTER:", end=" ")
                    typestr("I think there was an error. Try restarting the program.", [0.01, 0.15])
            except ValueError:
                print(f"COMPUTER:", end=" ")
                typestr("Your guess has to be a number.", [0.01, 0.15])     
        except:
            print(f"COMPUTER:", end=" ")
            typestr("I think there was an error. Try restarting the program.", [0.01, 0.15])
    resolved = False
    while not resolved:
        keep_playing = input("Play again? (y/n) ")
        if keep_playing == "y":
            playing_game = True
            resolved = True
        elif keep_playing == "n":
            print(f"COMPUTER:", end=" ")
            typestr("Bye for now! Play again later!", [0.01, 0.15], end="")
            in_program = False
            resolved = True
        else:
            print(f"COMPUTER:", end=" ")
            typestr("Please try again... ", [0.01, 0.15], end="")
        
