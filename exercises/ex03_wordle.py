"""Wordle."""

__author__ = "730388398"


GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
WHITE_BOX: str = "\U00002B1C"


def contains_char(search: str, single: str) -> bool:
    """Function will look through search index to find single."""
    assert len(single) == 1 
    index: int = 0 
    while index < len(search):
        if search[index] == single: 
            return True 
            # The "index" int type will start at the [0] place of the "search" str to match with the "single" character. If it does not match, the while loop continues and goes on to [1][2]... etc until the end of the str, or "single" is found.
        else: 
            index += 1
    return False 
    # This return type satisfies the function def return "bool". The while loop will either return as a "True" bool statement or a "False" bool statement.


def emojified(guess_word: str, secret_word: str) -> str:
    """Call contains_char function to test for yellow or white box codification."""
    assert len(guess_word) == len(secret_word)
    index: int = 0 
    # like in the contains_char function, "index" will cycle through each index in the str of "guess_word" to match and mark characters in the "secret_word" str. 
    emoji: str = ""
    # emoji is an empty string so it can be redined later to either the green, white, or yellow boxes. 
    while index < len(guess_word):
        if guess_word[index] == secret_word[index]:
            emoji += GREEN_BOX
            # Green_box means that a character in the guess_word str is in the same place as the secret_word str.
        else: 
            if contains_char(secret_word, guess_word[index]):
                emoji += YELLOW_BOX
                # Yellow_box means that a character in the guess_word str is in the secret_word str but not in the right place. This singles the user to try a new str with that char in a different place.
            else: 
                emoji += WHITE_BOX
                # White_box means that the char in the guess_word str is not in the secret_word str at all. 
        index += 1
    return emoji
    # This return statement satisfies the the function def return "str" since "emoji" starts as an empty str and changes to one of the box str statments.


def input_guess(expected_length: int) -> str:
    """Ask user for a word and continue prompting till input matched expected word length."""
    user_guess: str = input(f"Enter a {expected_length} character word: ")
    while len(user_guess) != expected_length: 
        user_guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return user_guess 
    # The reason why this works even tho function def return type is a str and the para is an int is bc we tell the user the para int my prompting them with a word of that length. The user's input str is then returned. 


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    # This can change, but "codes" is the secret word we are told to use
    N: int = 1 
    # This variable keeps track of the current turns the user is on. It starts at one instead of zero bc the first guess happens once the function starts.
    turns: int = 6 
    # This can change too, but we are told that there are 6 turns for this game
    Won = False
    # This bool statement will turn True in the function once the user has guessed the word correctly, ending the while loop and thus ending the function.
    guesser: str = ""
    # Guesser is first defined as an empty str until it is redefinded as the user's input till the user "wins" or their turns are over.

    while N <= turns and Won is False:
        print(f"=== Turn {N}/{turns} ===")
        guesser = input_guess(len(secret))
        print(emojified(guesser, secret)) 
        if guesser == secret:
            print(f"You won in {N}/{turns} turns! ")
            Won = True
        else:
            N += 1
    if guesser != secret: 
        print(f"X/{turns} - Sorry, try again tomorrow!")
# X is used in the print statement above bc the turns can be subjected to change and X is just a character to stand in for that number of turns that have been reached. 


if __name__ == "__main__":
    main()
    # This if statement allows this module to run when "python -m exercises.ex03_wordle" is called in terminal.