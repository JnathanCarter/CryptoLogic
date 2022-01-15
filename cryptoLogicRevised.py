#not working :(
from cmath import pi
import random
class Word():
        def __init__(self):
                self.randomword = ""
                self.randomwordList = "" 
                self.randomwordScrambled = ""
                self.randomwordScrambledList = ""
        
                
#Open word list file
file1= open(r"C:/Users/johnc/Documents/JSU Important/JSU Fall 2020/CS 230/Python/Project 1/wordList.txt", "r")

# converts list of characters to string
def convert(lst):
        tempstring = ""
        return(tempstring.join(lst))

def pickRandomWord():
        wordList = file1.readlines()
        secretWord = random.choice(wordList)
        return secretWord

def creatListofSecretWord(randomWord):
        seceretWord = randomWord
       
        return list(seceretWord)

def scrambleword(wordToBeScrambled):
        del wordToBeScrambled[-1]  
        return random.shuffle(wordToBeScrambled)


def returnWordObject():
        myWord = Word()
       
        myWord.randomword = pickRandomWord()
       
        myWord.randomwordList = creatListofSecretWord(myWord.randomword)
       
        myWord.randomwordScrambledList = scrambleword(myWord.randomwordList)
        
        myWord.randomwordScrambled = convert(myWord.randomwordScrambledList)
       
        return myWord 
        
        
def main():
        gameWord = returnWordObject() 
       
       
        
        #this is the beginning of the game logic

        print("Welcome to CRYTO-LOGIC!!") #intro and instructions
        print("Try to guess the scrambled word, one letter at a time!")

        incorrect_guesses=0 #initial values for incorrect guesses and letters guessed
        letters_already_guessed=[]
        i=0    # set initial value to i, i controls the loop

        while i < len(gameWord.randomword)-1:                 #Game logic

                print("Scrambled word: ", gameWord.randomwordScrambled)

                guessed_letter=input("Enter your Guess...")
                if guessed_letter == gameWord.randomwordList[i]:
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


if __name__ == "__main__":
        main()