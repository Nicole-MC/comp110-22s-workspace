"""Demonstrates asking the user for input."""


import random 
Import = random 
a = random.randint(1, 10)
Import = random
b = random.randint(1, 10)
Import = random
c = random.randint(1, 10)
user_name: str = input("What is your name? ")
print('    ')
print(user_name + ", that is a pretty snazzy name. ")
print(" Well hello " + user_name + ", nice to meet you! ") 
print("       ")
color: str = input(" What is your favorite color? ")
print(" I like " + color + " too! ") 
print("           ")
Answer = input(" I have an idea. Would you like to play a game with me? YES or NO ")
print("       ")
if Answer == ("no"):
    print("Okay, Goodbye!")
    exit()

if Answer == ("yes"):
    print("Great, pick a number between 1-10 and I'll try to guess it.")  
okay: str = input("Once you have your number type 'OKAY' to continue. ")   
print(" Is this...")                      
print(a)
Question = input("... your number? YES or NO ")
if Question == ("yes"): 
    print("Yay! Good game. ")
if Question == ("no"): 
    print("Dang! Better luck next time. ")
again = input("Do you want to play again? YES or NO ") 
if again == ("no"): 
    print("Okay, thanks for playing with me!")
    exit()
if again == ("yes"):
    print("Yay! Lets play again.")
okay: str = input("Once you have your number type 'OKAY' to continue. ")   
print(" Is this...")                      
print(b)
Question = input("... your number? YES or NO ")
if Question == ("yes"): 
    print("Yay! Good game. ") 
if Question == ("no"): 
    print("Dang! Better luck next time.") 
last = input(" Do you wanna play again? YES or NO ") 
if last == ("no"): 
    print(" Okay, thanks for playing with me!")
    exit() 
if last == ("yes"): 
    print("Okay, third times a charm. Pick a number between 1-10. ") 
okay: str = input("Once you have your number type 'OKAY' to continue. ") 
print(" Is this...")                      
print(c)
Question3 = input("... your number? YES or NO ")
if Question3 == ("no"): 
    print(" Dang! better luck next time. Thanks for playing with me.")
    exit() 
if Question3 == ("yes"): 
    print("Yay! Good game. Thanks for playing with me. ")
    exit() 