"""EX01 -Chardle- A cute step toward Wordle."""

__author__ = "730388398"


user_word: str = input("Enter a 5-character word: ")
if int(len(user_word)) != 5:
    print("Error: Word must contain 5 characters ")
    exit()

int(len(user_word)) == 5
character: str = input("Enter a single character: ")
counter: int = 0

if int(len(character)) != 1:
    print("Character must be a single character. ")
    exit()

if int(len(character)) == 1:
    print("Searching for " + character + " in " + user_word)
    
if str(user_word)[0] == character:
    print(character + " found at index 0")
    counter = counter + 1
if str(user_word)[1] == character:
    print(character + " found at index 1") 
    counter = counter + 1
if str(user_word)[2] == character:
    print(character + " found at index 2")
    counter = counter + 1
if str(user_word)[3] == character: 
    print(character + " found at index 3")
    counter = counter + 1
if str(user_word)[4] == character:
    print(character + " found at index 4")
    counter = counter + 1
    
if counter >= 1: 
    if counter == 1: 
        print("1 instance of " + character + " found in " + user_word)
    else: 
        print(str(counter) + " instances of " + character + " found in " + user_word) 
else: 
    print("No instances of " + character + " found in " + user_word)  