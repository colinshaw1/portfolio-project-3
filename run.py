import os
import random
SINKINGSHIP_PIC = ['''
         \\
      ____\\_____
      \\        \\
_______\\        \\______
\\                      /
 \\                    /
  \\__________________/
~~~~~~~~~~~~~~~~~~~~~~~~''', '''
         \\
      ____\\_____
      \\        \\
_______\\        \\______
\\                      /
 \\                    /
~~~~~~~~~~~~~~~~~~~~~~~~''', '''
         \\
      ____\\_____
      \\        \\
_______\\        \\______
\\                      /
~~~~~~~~~~~~~~~~~~~~~~~~''', '''
         \\
      ____\\_____
      \\        \\
_______\\        \\______
~~~~~~~~~~~~~~~~~~~~~~~~''', '''
         \\
      ____\\_____
      \\        \\
~~~~~~~~~~~~~~~~~~~~~~~~''', '''
         \\
      ____\\_____
~~~~~~~~~~~~~~~~~~~~~~~~''', '''
         \\
~~~~~~~~~~~~~~~~~~~~~~~~''']

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


wordSelection = random.choice(wordSelection)
wordSelection = wordSelection.upper()
secretWord = list(len(wordSelection)*'_')
livesLeft = 6
gameState = False


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


def display():
    '''
    Funtcion to display ships and current status
    '''
    os.system("clear")
    print(SINKINGSHIP_PIC[6-livesLeft])
    # converts to a string and The join() method takes all items in an iterable and joins them into one string.
    print(' '.join([str(e) for e in secretWord]))
    print(f'You have {livesLeft} lives left')


def playAgian():
    '''
    Function to return true of the player wants to play again
    if not return false
    '''
    # print("Would you like to play another game of SinkingShips?(yes or no)")
    # return input().upper.startswith('y')
    global playGame
    playGame = input("Would you like to play another game of Sinking Ships? y = yes or n = no \n")
    while playGame not in ["y", "Y", "n", "N"]:
        playGame = input("Would you like to play another game of Sinking Ships? y = yes or n = no \n")
    if playGame == "y":
        secretWord = True
    elif playGame == "n":
        print("Thank you for playing Sinking Ships! See you soon")
        exit()

while gameState == False and livesLeft > 0:
    guess = input('Please enter a letter: ')
    guess = guess.upper()

    if guess == wordSelection:
        gameState = True
        secretWord = wordSelection
    if len(guess) == 1 and guess in wordSelection:
        gameState = guess_letter(guess, wordSelection)
    else:
        livesLeft -= 1
    display()
    
   
    # if gameState:
    #     if playAgian():
    #         wordSelection = random.choice(wordSelection)
    #         wordSelection = wordSelection.upper()
    #         secretWord = list(len(wordSelection)*'_')
    #         gameState = False
    #     else:
    #         break

if gameState:
    print(f"Yes the word was {wordSelection}! You are the winnner")
else:
    print(
        f"You lose this round of sinking ships, the word was: {wordSelection}!")
    playAgian()



