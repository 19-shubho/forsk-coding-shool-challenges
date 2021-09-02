print('Welcome to the Guess Your Number Game!!!')
print('INSTRUCTIONS: \n1. Computer will ask you to guess a number between 1 to 10. \n2. If your guess is correct you win the game. \n3. To finish press F.')

while(True):
    import random
    n=random.randint(1,10)
    x=input('What is your take? ')
    if(not x):
        print('Invalid input, try again.')
        continue

    elif(x=='F'):
        break
    
    x=int(x)
    if(x>10 or x<1):
        print('Invalid input, try again.')
        continue
    
    elif(n==x):
        print('Computer generated random number is: ',n)
        print('You win, computer loses.')
    else:
        print('Computer generated random number is: ',n)
        print('You lose, computer wins.')