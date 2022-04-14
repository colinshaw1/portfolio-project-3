SINKING SHIPS
--
For my milestone project 3 for Code Institute Diploma in Software Development, I have chosen Project Example Idea 0. For this project, I created a command-line game called SinkingShips. The goal of the game is to guess all the letters in the word before your six lives run out. The game is a pure chance but you get the option of easy words with up to 5 letters or hard words with up to 8 letters chosen at random. 

Please click on the link to enjoy a game of Sinking Ships https://sinking-ships.herokuapp.com/


Who is this Game intended for?
--

The game is intended for anyone who has an interest in computers and likes word puzzles. The game is used through the command line so you will have to be familiar with how a command-line game works and run it before playing.

Owner
--
The owner of this game is Colin Shaw. The goal is to help people switch off and enjoy a fun interactive game.

How to play
--
Sinking ships is a variation of the classic word puzzle game Hangman. In this version, the player has an option to enter 1 for an easy word which will be no more than 5 letters in length or choose 2 for hard which is 8 letters in length. The player has 6 lives to guess the word. Each time a letter is guessed the letter appears on the display, the more you guess the easier it becomes to guess the word. The player must guess the word before the ship sinks. Once a game has ended the player has an option to select y for another game or n to end the current game. See below for pictures of how Sinking ships. 

Screenshots of Game
--

Start game

![image](https://user-images.githubusercontent.com/56481190/163455314-55c5d16b-039d-491c-a247-56bf0a0a464a.png)


Easy Game running 

![image](https://user-images.githubusercontent.com/56481190/163455899-f2f383f4-5537-4011-b632-369acf2c9d09.png)


After 4 guesses

![image](https://user-images.githubusercontent.com/56481190/163456084-f27b7a24-9299-4f28-b61d-4007f65b8555.png)


After losing a game 

![image](https://user-images.githubusercontent.com/56481190/163456219-fe18f86d-4919-4eb0-9eb3-e63b5a52f6dc.png)


Hard game running 

![image](https://user-images.githubusercontent.com/56481190/163456740-769660e9-55d5-484b-9199-4e9c74cce274.png)


After selecting y to play again

![image](https://user-images.githubusercontent.com/56481190/163456407-3482f2f8-081c-47ae-82f3-bd64ce3e0b0f.png)


After selecting n to end the game

![image](https://user-images.githubusercontent.com/56481190/163456584-8a796352-00f7-4d02-879c-9a8d8694c584.png)


Game won 

![image](https://user-images.githubusercontent.com/56481190/163457035-495013ae-9c57-4906-a8ae-02f1dfa73fc2.png)


User Experience
--

Game Player
1.	The Player will run the game
2.	The player will select difficulty 1 for easy or 2 for hard
3.	The easy game runs the player has 6 lives to guess the 5 letters
4.	The hard game runs the player has 6 lives to guess 8 letters 
5.	If player runs out of lives the game ends the word is displayed
6.	The Player has option y for a new game or n to end the game 
7.	If player selects y the game runs again 

User Experience
--

Strategy Plane

Sinking ships were designed to make an easy and challenging word puzzle that is fun and makes the user want to play multiple times. The game is easy to use and the steps are laid out well. 

Scope Plane

•	Created in HTML
•	4 inputs commands taken for the terminal y = yes, n = no,  1 = easy , and 2 = hard
•	The game takes the input of a letter for guesses


Structure Plane

The game is structured in the terminal, it is deployed and run via Heroku.


Technologies used
--

•	Python is used to implement complex functions to start, run, and end the game
•	Git for storing files and deployment 
•	Heroku is used for final deployment and playability
•	Gitpod for design

Resources
--

•	Code institute for material and ideas
•	Geeks for Geeks for information and ideas
•	W3 Schools for information and ideas
•	Slack for inspiration
•	YouTube for tutorials
•	My mentor Spencer Barbell was extremely helpful throughout the process


Testing
--
• Passed validation through PEP8 online checker

![image](https://user-images.githubusercontent.com/56481190/163461249-3ccf3dee-46f3-4394-9314-bc8a14b6c5af.png)

• Game tested through the terminal in Gitpod and heroku

Bugs

Solved

• Game kept resetting every time it was truthy in a while loop. Gem would exit because of statement after while loop gameState == False and livesLeft == 0: updated gameInprogress to play again once lives equaled 0

• WWhen putting code through PEP a lot of whitespaces and only one space after function 

Remaining Bugs

• None

Version Control
--

GitHub and GitPod to update and commit changed to my repository all commits tracked to mark progress

Deployment
--

The project was deployed using Heroku's mock terminal
• Clone repository
• Create Heroku account
• Set builds to Pyhton and set key to PORT and value to 8000
• Link Heroku account to the repository
• Click Deploy
