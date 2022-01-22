"""Example of Memory Diagram Program."""

age: int = int(input("How old are you?"))
year: int = int(input("What year is it?"))
age_in_2041: int = 2041 - year + age
print("In 2041 you'll be " + str(age_in_2041))

age = age + 1
year = year + 1 
print("In " + str(year) + " you'll be " + str(age)) 
print(age)


def play():
    secret: int = 6

    print("Click 'ENTER to play")
    guess: int = int(input("Okay. guess the number I am thinking of between 1-10 "))
    if guess == (secret): 
        print("Yay! You're correct!")
        print("") 
    else: 
        print(" Sorry, you guess incorrectly :( ")
        print(" ")
    again: str = input(" Do you want to play again? Y or N ")
    if again == ("N"): 
        print("Game Over. ")
        exit()
    if again == ("Y"):
        print("Okay, Press 'ENTER' to play. ")
        play()


Question: str = (input("Would you like to play a game with me? yes or no "))
if Question == ("yes"):
    print(" ")
    play()
if Question == ("no"):
    print(' ')
    print("Okay. Goodbye. ")
    exit() 
