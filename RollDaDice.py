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
    

