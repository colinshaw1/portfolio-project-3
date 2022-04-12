import os
import random
import ship

# words taken from Random word generator 50 in total
wordSelection = '''
goalkeeper
improve
stimulation
deprive
school
theft
language
pull
file
couple
rape
forecast
site
call
therapist
joy
dish
chair
obligation
president
cemetery
formation
simplicity
affair
vague
calm
black
contain
departure
blade
cancel
subject
powder
cast
mean
sustain
course
ideology
flatware
sum
outlook
brown
conservative
lean
tongue
lung
roll
dollar
communist
contraction'''.split()

def display():
    '''
    Function to display ships and current status
    '''
    os.system("clear")
    print(ship.SINKINGSHIP_PIC[6-livesLeft])
    # converts to a string and The join() method takes all items in an iterable and joins them into one string.
    print(' '.join([str(e) for e in secretWord]))
    print(f'You have {livesLeft} lives left')

def generateSecretWord(word):
    return list(len(word)*'_')

def generateRandomWord():
    return random.choice(wordSelection).upper()

def startGame():
    global wordSelection
    global secretWord
    global livesLeft
    global gameState
    global gameInProgress

    wordSelection = generateRandomWord()
    secretWord = generateSecretWord(wordSelection)
    livesLeft = 6
    gameState = False
    gameInProgress = True
    display()

startGame()

def checkUserInput(userInput):
    while userInput != "y" or userInput != "n":
        if userInput == "y":
            return startGame()
        elif userInput == "n":
            print("Thank you for playing Sinking Ships! See you soon")
            exit()


def guess_letter(letter, wordSelection):
    '''
    This function checkt to see if a letter in a word from the word selection
    '''
    global secretWord
    letter
    for i in range(0, len(wordSelection)):
        letter = wordSelection[i]
        if guess == letter:
            secretWord[i] = guess
    if '_' not in secretWord:
        return True
    else:
        return False

def playAgain():
    '''
    Function to return true of the player wants to play again
    if not return false
    '''
    playGame = ''
    while playGame.upper() != "Y" or playGame() != "N":
        playGame = input("Would you like to play another game of Sinking Ships? y = yes or n = no \n").upper()
        if playGame == "Y":
            return startGame()
        elif playGame == "N":
            print("Thank you for playing Sinking Ships! See you soon")
            exit()


while gameInProgress:
    if livesLeft == 0:
        playAgain()

    guess = input('Please enter a letter: ').upper()

    if guess == wordSelection:
        gameState = True
        secretWord = wordSelection
    if len(guess) == 1 and guess in wordSelection:
        gameState = guess_letter(guess, wordSelection)
    else:
        livesLeft -= 1
    display()

if gameState:
    print(f"Yes the word was {wordSelection}! You are the winnner")
else:
    print(
        f"You lose this round of sinking ships, the word was: {wordSelection}!")
    playAgain()