# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for i in secretWord:
        if i in lettersGuessed:
            pass
        else:
            return False
        

    return True


def getGuessedWord(secretWord, lettersGuessed):
    
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessedWord = list("_"*len(secretWord))
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            guessedWord[i] = secretWord[i]
    str_guessedWord = ""
    for i in guessedWord:
        str_guessedWord += i
    return str_guessedWord
            
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    lexical_order = "abcdefghijklmnopkrstuvwxyz"
    list_alphabets = list(lexical_order)
    for i in lettersGuessed:
        if i in list_alphabets:
            try:
              list_alphabets.remove(i)
            except Exception as e:
                print(f"The {e} has been thrown")
    
    str_alphabets = "" 
    for i in list_alphabets:
        str_alphabets += i
    return str_alphabets
          


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    sw = secretWord
    print("-"*10)
    print(f"Welcome to Hangman, the computer has chosen a word of {len(sw)} letters. You have 8 guesses to reveal the word.")
    lettersGuessed = []
    numGuesses = 0

    while numGuesses<8 and (not isWordGuessed(secretWord, lettersGuessed)): # game loop

        letter_input = input("Enter a letter:")

        # adding letter to list of letters
        while letter_input in lettersGuessed:
            print("Letter already guessed, try again")
            letter_input = input("Enter a letter:")
        lettersGuessed.append(letter_input)

        # returning if valid guess or not
        if letter_input in secretWord:
            print("That was a good guess! :)")
            print(8-numGuesses,"guesses left.")
        else:
            print("That was an incorrect guess. :(")
            numGuesses +=1
            print(8-numGuesses,"guesses left.")
        
        print("Current word you've formed:",getGuessedWord(secretWord, lettersGuessed))
        print("Words not used:",getAvailableLetters(lettersGuessed))
    # printing the end conditions
    if numGuesses == 8:
        print("You ran out of guesses.")
    else: 
        print(f"You won. The word was {secretWord}")



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

#secretWord = chooseWord(wordlist).lower()
secretWord = "testing secret word"
hangman(secretWord)
