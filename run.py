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
secretWord = list(len(wordSelection)*'_')


livesLeft = 6
gameState = False

while gameState == False and livesLeft > 0:
    print(secretWord)
    guess = input('Please enter a letter: ')
    guess = guess.upper()

    if guess == wordSelection:
        gameState = True
    if len(guess) == 1 and guess in wordSelection:
        for i in range(0, len(wordSelection)):
          letter = wordSelection[i]
          if guess == letter:
            wordSelection[i] = guess
        if '_' not in secretWord:
            gameState = True
    else:
        livesLeft -= 1

if gameState:
    print(f"Yes the word was {wordSelection}! You are the winnner")
else:
    print(f"You lose the word was: {wordSelection}!")