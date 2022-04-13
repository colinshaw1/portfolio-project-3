import os
import random
import ship
import words


def display():
    '''
    Function to display ships and current status when a game is in progress
    '''
    # clears the terminal everytime a new game starts
    os.system("clear")
    print(ship.SINKINGSHIP_PIC[6-livesLeft])
    # converts to a string and The join() method takes all items in
    # an iterable and joins them into one string.
    print(' '.join([str(e) for e in secretWord]))
    print(f'You have {livesLeft} lives left')


def generateSecretWord(word):
    '''
    Function to generate a secret word. to return the length of the word
    from the list to the terminal
    '''
    return list(len(word)*'_')


def generateEasyRandomWord():
    '''
    Function to generate easy random word and pull the word form the
    easy word list in the word constant file
    '''
    return random.choice(words.easyWordSelection).upper()


def generateHardRandomWord():
    '''
    Function to generate hard random word and pull the word form the
    hard word list in the word constant file
    '''
    return random.choice(words.hardWordSelection).upper()


def chooseDifficulty():
    '''
    Function to choose difficulty level at the start of the game
    choose 1 to take the easyword list from the constant words.py file
    and play a game with max of 5 words. Type 2 to choose the hardword
    list from the words.py file and play a game with 8 words.
    '''
    difficulty = ''
    # whiel loop to meet conditions that user input must be 1 or 2
    while difficulty != '1' or difficulty != '2':
        difficulty = input('Type 1 for Easy, 2 for Hard \n')
        if(difficulty == '1' or difficulty == '2'):
            return difficulty


def startGame():
    '''
    Function to start the game and set conditions for the game.
    '''
    # declare global variables s
    global wordSelection
    global secretWord
    global livesLeft
    global gameState
    global gameInProgress

    # call difficulty function and set it equal to choosedifficulty
    difficulty = chooseDifficulty()
    # set diffuclty to 1 if user enters 1 and generate easy word
    if(difficulty == '1'):
        print('You have chosen an easy word')
        wordSelection = generateEasyRandomWord()
    # set diffuclty to 2 if user enters 2 and generate hard word
    elif(difficulty == '2'):
        print('You have chosen a hard word')
        wordSelection = generateHardRandomWord()

    # set game varibales
    secretWord = generateSecretWord(wordSelection)
    livesLeft = 6
    gameState = False
    gameInProgress = True
    display()

# call the starts game function so the game can run
startGame()


def guessLetter(letter, wordSelection):
    '''
    Function guessLetter checks the users guess and see if it is in the
    word selection and if it is return true and show the letter if not
    return false
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
    Functionplay again returns true if the player wants to play again
    if not return false
    '''
    playGame = ''
    while playGame.upper() != "Y" or playGame.upper() != "N":
        playGame = input("Would you like to play another game of \
             Sinking Ships? y = yes or n = no \n").upper()
        if playGame == "Y":
            return startGame()
        elif playGame == "N":
            print("Thank you for playing Sinking Ships! See you soon")
            exit()


def winGame():
    '''
    winGame function prints out the below statement if game is won
    and returns the play again function
    '''
    display()
    print(f"Yes the word was {wordSelection}! You are the winnner")
    playAgain()


def loseGame():
    '''
    loseGame function prints out the below statement if game is lost
    and returns the play again function
    '''
    print(
        f"You lose this round of sinking ships, \
            the word was: {wordSelection}!")
    playAgain()


while gameInProgress:
    '''
    While loop that call gameInProgress variable and iterates certain
    steps while the game is playing
    '''
    # if no spaces left in secret word return wingame function
    if "_" not in secretWord:
        winGame()
    # if lives equal 0 the return losegame function
    if livesLeft == 0:
        loseGame()
    # takes user input
    guess = input('Please enter a letter: ').upper()

    if len(guess) == 1 and guess in wordSelection:
        gameState = guessLetter(guess, wordSelection)
    else:
        livesLeft -= 1
    display()
