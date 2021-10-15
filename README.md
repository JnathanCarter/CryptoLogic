<!--
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
This program stores all the words that can be used within a separate text file named wordList.txt . The python script "crypto-logic project.py" reads all the words into a list. From this list one random word is chosen with the "random.choice" method. This randomly selected word is then separated letter by letter into another list named "seceret_word_list". The letters contained in this list are scrambled using the "random.shuffle" method and then appended to a string variable "secret_word_shuffled". The introduction message is then printed to the console and the main game loop is instantiated. The player is shown the scrambled version of the selected word and is asked to input their guess for the first letter. If the player guesses correctly then the letter is displayed, and the player tries to guess the next letter. If the guess is incorrect then the incorrect guesses counter is incremented by one and the player must retry until they select the correct letter. This continues until all the letters are guessed. When all the letters are guessed then the loop while terminate and the results will be displayed. A congratulatory message will be displayed along with the number of guesses that it took to unscramble the letter.

# Contact Information
For inquiries or suggestions for the program please contact jcarter20@stu.jsu.edu
-->
# Introduction
This was my Introduction to Computer Programming in Python's final project. The project's goal was to create a simple, command-line interfaced word game named "Crypto-Logic." In this game, the player will be presented with a random word in which all the letters are scrambled. The player then attempts to unscramble the word letter by letter while making the fewest possible errors. When the word is successfully unscrambled, the player will be shown how many incorrect guesses they made.
# Materials and Method
The source code for this game is written in the programming language of Python. This code was developed within Microsoft's Visual Studio Code text editor on a Windows 10 machine. This text editor had many extensions installed to aid in developing the code, including syntax highlighting, debugging support, and auto-formatting. The program is designed to use the terminal for displaying information to the user and for user input. There is no graphical user interface, and the game is played strictly within the terminal. Since the source code is written in Python, this program can be run on any machine no matter the operating system if the device has an installed Python Interpreter.

The algorithm for the program begins with selecting a random word from a large text file that contains the possible words to use in the game. The individual letters are then added to a list, a second copy of this list is instantiated then scrambled. This scrambled list is passed to a function that returns a string of all the scrambled letters. This string will be displayed to the user as the scrambled word. The main game loop is then started. This loop is a while loop controlled by the "gameOver" flag. The loop displays the scrambled word, prompts the player to take a guess, receives the user's input, and determines whether that letter is the following letter in the word. It does so by checking the user's input to the corresponding index in the word's unscrambled list of letters. When the player guesses the correct letter, the index is incremented to check for the next letter of the word. If the player guesses all the letters, then the "gameOver" flag is changed to true, which causes the game loop to end. Then a congratulatory message is printed on the screen.

# Game Play Example
![Game_example1](https://user-images.githubusercontent.com/89806393/135562052-6d45b021-f625-4f52-9728-c7750200f023.jpg)

# Results and Discussion
The program begins with a welcome message and, in this specific instance, displays the scrambled word "rrusci." When the player enters the guess of the letter "r," the incorrect guess counter's value changes from zero to one since this guess was not correct. The user then entered the letter 'I,' which was correct, and the incorrect guess value stayed at one. Then the user entered the letter 'r,' which was correct, then entered the letter 'r' again, which was also correct. The counter, as expected, remained at zero. Then the user entered the letters "u" and "r," which were correct. The game then displayed the message, "Congratulations, you unscrambled the word in with only one incorrect guess."
# Conclusion
After many rounds of the game were played, with each round behaving as expected when giving appropriate input, it was concluding that the program met all the requirements of the lab. The program correctly validated the user's input to the word and perfectly kept track of the number of incorrect guesses while also exiting at the correct time. The game met the requirements but could still be improved. Since there was no input validation, if the user input the entire word unscrambled, the guess would still be considered incorrect. There was no functionality in the game to guess the entire word at once and win the game early. Even though this was not required for the lab, it would be an excellent improvement to the game. Another improvement to be considered would be adding an optional maximum number of incorrect guesses the player could make to make the game more challenging. If the player exceeds this limit, they will lose the game and be shown a losing message and the unscrambled word.
