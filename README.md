# Dice-Roll-Simulator
# A simple dice roll simulator written in Python 3.5.2 with a play again prompt.
# It runs within the Python Shell - simply run the document with the following pasted within:

import random

def rollingD():
    print('Your roll is:')
    print(random.randint(1, 6), random.randint(1, 6))
    print()

rollAgain = 'yes'
while rollAgain == 'yes' or rollAgain == 'y':
    rollingD()
    print('Roll again? (yes or no)')
    rollAgain = input()
    
# Super simple
