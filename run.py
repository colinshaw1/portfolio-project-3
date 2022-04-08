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

# gamesWords = 'sign vat insure illustrate management sport praise comfort experienced insistence side lonely shine monk soldier
# restrict rubbish fraud warrant hand image revoke execute cycle functional burst rehabilitation herb grandmother'


wordSelection = 'COLIN'
wordSelection = wordSelection.upper()
secretWord = list(len(wordSelection)*'_')
livesLeft = 6
gameState = False


def guess_letter(letter, wordSelection):
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
    print(SINKINGSHIP_PIC[6-livesLeft])
    print(secretWord)

while gameState == False and livesLeft > 0:
    print(secretWord)
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
    print(f"You lose the word was: {wordSelection}!")