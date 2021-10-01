# CryptoLogic
- Simple Word Guessing Game Built with Python
- This game is ran in the command line


# Game Description
The Player is given a random word selected from a list. The letters of this word have
been scrambled and it is the players goal to unscramble the word letter by letter with the
fewest amount of incorrect guesses

# Game Play Example
![Game_example1](https://user-images.githubusercontent.com/89806393/135562052-6d45b021-f625-4f52-9728-c7750200f023.jpg)

# Design
This program stores all the words that can be used within within a seperate text file
named wordList.txt . The python script "crypto-logic project.py" reads all the words into a list.
From this list one random word is choosen with the "random.choice" method. This randomly selected word is then
seperated letter by letter into a another list named "seceret_word_list". The letters contained in this list are scrambled 
using the "random.shuffle" method and then appended to a string variable "secret_word_shuffled".
The introduction message is then printed to the console and the main game loop is instantiated.
The player is shown the scrambled version of the selected word and is asked to input their gues for the first letter.
If the player guesses corectly then the letter is displayed and the player tries to guess the next letter. If the guess is incorrect
then the incorrect guesses counter is incremented by one and the player must retry until they select
the correct letter. This continues until all the letters 
are guessed. When all the letters are guessed then the loop while terminate and the results will be displayed.
A congradulatory message will be displayed along with the amount of guesses that it took to unscramble the letter.

# Contact Information
For inquiries or suggestions for the program please contact jcarter20@stu.jsu.edu
