secretNumber = 0
computerGuess = 50
low = 1
high = 100
guessCorrect = False
higher = False
median = (high+low)//2
choice = "y"
statement = "h"
invalid = True

def findMedian():
    global high, low
    return (high+low)//2


while invalid == True:
    secretNumber = int(input('What do you want the secret number to be? '))
    if (1 <= secretNumber <= 100):
        print('Valid')
        invalid = False
    elif (secretNumber < 1) or (secretNumber > 100):
        print('Invalid')
        invalid = True
    
    
def changeRange():
    global computerGuess, low, high, median
    if higher == True:
        low = median
    else:
        high = median
    
while guessCorrect == False:
    choice = input('Is this your secret number? ' + str(computerGuess) + ' y or n ')
    if choice == "y":
        guessCorrect = True
        print('Yes, I was correct!')
    elif choice == "n":
        guessCorrect = False
        statement = input('Is your number higher or lower? h or l ')
    if (computerGuess == 99) and (statement == "h"):
        computerGuess = (99 + 1)
        choice = input('Is this your secret number? ' + str(computerGuess) + ' y or n ')
        if choice == 'y':
            guessCorrect = True
            print('Yes, I was correct!')
    if statement == "h":
        higher = True
    elif statement == "l":
        higher = False
    changeRange()
    median = findMedian()
    computerGuess = median
    