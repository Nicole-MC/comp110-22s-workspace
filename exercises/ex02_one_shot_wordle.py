"""One Shot Wordle."""
__author__ = "730388398"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9" 
YELLOW_BOX: str = "\U0001F7E8"


secret_word: str = "python"
length: int = len(secret_word)
guess: str = input(f"What is your {length}-letter guess? ") 
# The f-strings are meant to allow this program to do any word and length instead of just listing the int 6 

counting: int = 0
emoji: str = " "


while len(guess) != len(secret_word):
    guess = input(f"That is not {length} letters! Try again: ") 

while counting < len(secret_word): 
    if guess[counting] == secret_word[counting]:
        emoji = emoji + GREEN_BOX
    else:
        existing_character: bool = False 
        # these variables needed to be in the while loop rather with the other variables listed above. its not like this took me FOREVER to figure out :)))
        indices: int = 0 
        # meant to rep the indexs for part 3
        while not existing_character and indices < len(secret_word):
            if guess[counting] == secret_word[indices]:
                # we need to alternate the indexs to compare, so they have to go with the opposite word 
                existing_character = True
            else:
                indices = indices + 1
        if existing_character:
            # including "not" would mess up the bool 
            emoji = emoji + YELLOW_BOX 
        else:
            emoji = emoji + WHITE_BOX
    counting = counting + 1 
print(emoji)

if len(guess) == len(secret_word):
    # again best to put the length of the secret word rather than a set number 
    if str(secret_word) == str(guess):
        print("Woo! You got it! ")
    else:
        print("Not quite. Play again soon! ") 