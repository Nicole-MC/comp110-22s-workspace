
import random
Import = random 
random.randint(1, 69)
Import = random
random.randint(1, 27) 


def play():

    print("  ")
    print("Your white numbers are: ")  
    print("     ")
    print(random.randint(1, 69),)    
    print("     ")

    print(random.randint(1, 69),) 
    print("     ")

    print(random.randint(1, 69))
    print("     ")

    print(random.randint(1, 69),)
    print("     ")
    print("Your red number is: ")
    print("     ")

    print(random.randint(1, 27))
    print("     ") 


user_name: str = input("What is your name? ")
print('    ')
print("Well hello " + user_name + ", it is nice to meet you! ") 
print("       ")
Answer = input("Would you like me to randomly select your PowerBall numbers? YES or NO ")
if Answer == ("no"): 
    print("  ")
    print("Okay, Goodbye!")
    print("  ")
    exit() 
if Answer == ("yes"): 
    print("   ")
    print("Great, I hope you are feeling lucky!")
okay: str = input("Press'ENTER' to continue. ")
play() 
print("   ")

z = True 
while True:
    i = input("Here are your numbers. Would you like me to pick again? YES or NO ")
    if i == ("yes"):
        print("  ")
        print("Great, I hope you are feeling lucky!")
        okay: str = input("Press 'ENTER' to continue. ")

        play()
    elif i == ("no"):
        print("  ")
        print("Okay, Goodbye!")
        exit() 
    else: 
        print(" Please type YES or NO. ") 