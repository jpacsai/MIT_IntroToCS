# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

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
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guess = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guess += letter
        else:
            guess += '_ '
    return guess



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    abc = string.ascii_lowercase
    available = ''
    for letter in abc:
        if letter not in lettersGuessed:
            available += letter
    
    return available
    

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
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    separator = '------------'
    print(separator)
    guessesLeft = 8
    lettersGuessed = []
    show = getGuessedWord(secretWord, lettersGuessed)
    finish = False
    abc = string.ascii_lowercase
    while guessesLeft > 0 or finish == False:
        print('You have '+ str(guessesLeft) + ' guesses left.')
        available = getAvailableLetters(lettersGuessed)
        print('Available letters: ' + available)
        guess = input("Please guess a letter: ")
        guess = guess.lower()
        if len(guess) > 1 or guess not in abc:
            print("Oops! Please guess a single letter: " + show)
            print(separator)
        elif guess in lettersGuessed:
            print("Oops! You've already guessed that letter: " + show)
            print(separator)
        else:
            lettersGuessed.append(guess)
            if guess not in secretWord:
                print("Oops! That letter is not in my word: " + show)
                guessesLeft -= 1
                print(separator)
                if guessesLeft == 0:
                    finish = True
                    print('Sorry, you ran out of guesses. The word was ' + secretWord)   
                    return 'Lost'
            else:
                show = getGuessedWord(secretWord, lettersGuessed)
                print('Good guess: ' + show)
                print(separator)
                if isWordGuessed(secretWord, lettersGuessed) == True:
                    finish = True
                    print('Congratulations, you won!')
                    return 'won'



# (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
