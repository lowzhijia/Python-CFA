#!/user/bin/env python

import random

def main():
    """Start a guessing genre music between hip hop and rock."""
    print("Guess the music!\nPlease choose one genre music.\n(hip hop, classical, disco, rock, jazz, and kpop)\n")

    music = ["hip hop", "classical", "disco", "rock", "jazz", "kpop"]
    
    x = random.choice(music)
    guess = None
    try_again_count = 0  
    lose = False  

    while x != guess:
        guess = str(input("Pick a genre music: "))

        if x == guess:
            print("You're a genius!!!")
        else:
            try_again_count += 1  
            if try_again_count == 3:  
                lose = True
            print("Please repeat again\n" if not lose else "You lose")  

        if try_again_count == 3:  
            break

("The prompt 'Please repeat again' appeared three times!")

main()