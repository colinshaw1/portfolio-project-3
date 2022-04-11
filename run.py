import os
SINKINGSHIP_PIC = ['''
      ______
     /     /
 ___/_____/___
 \           /
  \_________/ ''', '''

      ______
     /     /
 ___/_____/___
 \           /
  \         /''', '''

      ______
     /     /
 ___/_____/___
 \           /''', '''

      ______
     /     /
 ___/_____/___''', '''

      ______
     /     /
    /     /''', '''

     ______
    /     /''', '''

     ______''']


wordSelection = 'COLIN'
wordSelection = wordSelection.upper()
secretWord = list(len(wordSelection)*'_')
livesLeft = 6
gameState = False


def guess_letter(letter, wordSelection):
    '''
    This function checkt to see if a letter in a word from the word selection
    '''
    global secretWord 
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
    print(f'You have {livesLeft} lives left')
    print(secretWord)

def playAgian():
    '''
    Function to return true of the player wants to play again
    if not return false
    '''
    print("Would you like to play another game of SinkingShips?(yes or no)")
    return input().upper.starswith('y')

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

if gameState:
    print(f"Yes the word was {wordSelection}! You are the winnner")
else:
    print(f"You lose this round of sinking ships, the word was: {wordSelection}!")