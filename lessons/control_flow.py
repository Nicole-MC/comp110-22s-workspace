"""Eight Ball."""

from random import randint

input("Ask a yes or no question: ")

response: int = randint(0, 3)

if response == 0: 
    print("Yes, most definitely. ")
elif response == 1: 
    print("looking hopeful. ")
elif response == 2:
    print("Ask again later. ")
else: 
    print("No way. Not a chance. ")