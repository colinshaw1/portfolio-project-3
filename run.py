import os
import random
import ship
import words

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

def generateEasyRandomWord():
    return random.choice(words.easyWordSelection).upper()

def generateHardRandomWord():
    return random.choice(words.hardWordSelection).upper()

def chooseDifficulty():
    difficulty = ''
    while difficulty != '1' or difficulty != '2':
        difficulty = input('Type 1 for Easy, 2 for Hard \n')
        if(difficulty == '1' or difficulty == '2'):
            return difficulty

def startGame():
    global wordSelection
    global secretWord
    global livesLeft
    global gameState
    global gameInProgress

    difficulty = chooseDifficulty()

    if(difficulty == '1'):
        print('You have chosen an easy word')
        wordSelection = generateEasyRandomWord()

    elif(difficulty == '2'):
        print('You have chosen a hard word')
        wordSelection = generateHardRandomWord()


    secretWord = generateSecretWord(wordSelection)
    livesLeft = 6
    gameState = False
    gameInProgress = True
    display()

startGame()


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
    while playGame.upper() != "Y" or playGame.upper() != "N":
        playGame = input("Would you like to play another game of Sinking Ships? y = yes or n = no \n").upper()
        if playGame == "Y":
            return startGame()
        elif playGame == "N":
            print("Thank you for playing Sinking Ships! See you soon")
            exit()


while gameInProgress:
    if livesLeft == 0:
        print(
            f"You lose this round of sinking ships, the word was: {wordSelection}!")
        playAgain()

    guess = input('Please enter a letter: ').upper()

    if guess == wordSelection:
        secretWord = wordSelection
        display()
        print(f"Yes the word was {wordSelection}! You are the winnner")
        playAgain()
    if len(guess) == 1 and guess in wordSelection:
        gameState = guess_letter(guess, wordSelection)
    else:
        livesLeft -= 1
    display()