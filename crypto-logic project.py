#This is defining functions and variables and pullings data from the wordList.txt file

import random # import random module to use its functions 
def convert(lst):    #This function will convert our letter list back into a string
    str1=""
    return(str1.join(lst))

file1= open(r"C:/Users/johnc/Documents/JSU Important/JSU Fall 2020/CS 230/Python/Project 1/wordList.txt", "r") # opens the word list file---This function was not discussed in class!!
word_list=file1.readlines()            #reads the lines of word list file, and return it as a list stored in the variable word_list

seceret_word=random.choice(word_list)    #picks random word from word_list and stores it in variable secret word

seceret_word_list=list(seceret_word)   #seperates word into a list of letter
del seceret_word_list[-1]             #deletes the "\n" at end of the list

seceret_word_shuffled_list= list(seceret_word)   #creates another copy of the letter list to be shuffled in line 19
del seceret_word_shuffled_list[-1]     #deletes the "\n" at end of the list

random.shuffle(seceret_word_shuffled_list)     # shuffles the letter list stored in seceret_word-shuffled_list

seceret_word_shuffled= convert(seceret_word_shuffled_list) # puts the shuffled letter list back together into a string

'''
print(seceret_word)
print(seceret_word_list)
print(seceret_word_shuffled_list)
print(seceret_word_shuffled)
'''
'''
print(seceret_word)
'''

#this is the beginning of the game logic

print("Welcome to CRYTO-LOGIC!!") #intro and instructions
print("Try to guess the scrambled word, one letter at a time!")

incorrect_guesses=0 #initial values for incorrect guesses and letters guessed
letters_already_guessed=[]
i=0    # set initial value to i, i controls the loop

while i < len(seceret_word)-1:                 #Game logic

    print("Scrambled word: ", seceret_word_shuffled)

    guessed_letter=input("Enter your Guess...")
    if guessed_letter == seceret_word_list[i]:
        letters_already_guessed.append(guessed_letter.capitalize()) #adds the guessed letter to letters_already_guessed list if the letter is correct/ and then capitolizes the letter
        i+=1
    else:
        incorrect_guesses+=1
    print("Incorrect guesses: ", incorrect_guesses)
    print("Letters already guessed: ", convert(letters_already_guessed))
    print()

if incorrect_guesses == 1:       #controls whether the word is guess or guesses based of the number of incorrect guesses
    guess_guesses="guess"
else:
    guess_guesses="guesses"        


print("Congradulations you found the correct answer after ", incorrect_guesses, "incorrect",guess_guesses )