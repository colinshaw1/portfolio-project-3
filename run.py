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


word = 'COLIN'
secretWord = list(len(word)*'_')


lives = 6
gameWon = False

while gameWon == False and lives > 0:
    print(secretWord)
    guess = input('Please enter a letter:')
    guess = guess.upper()

    if guess == word:
        gameWon = True
    if len(guess) == 1 and guess in word:
        for i in range(0, len(word)):
          letter = word[i]
          if guess == letter:
            secretWord[i] = guess
        if '_' not in secretWord:
            gameWon = True


    else:
        lives -= 1

if gameWon:
    print("Yes the word was +word+! You are the winnner")
else:
    print("You lose the word was: "' + word + '"!")