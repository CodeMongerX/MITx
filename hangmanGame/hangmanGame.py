# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 00:04:05 2018

@author: Rajeev
"""
import string

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    flag = False 
    for i in lettersGuessed:
        if i in secretWord:
            flag = True
        else:
            flag = False
        
    return flag
    


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    str1 = []
    for i in secretWord:
        if i in lettersGuessed:
            str1.append(i)
        else:
            str1.append("_ ")
    joined = "".join(str1)
    return joined
    
    
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    str1 = []
    for i in string.ascii_lowercase:
        if i not in lettersGuessed:
            str1.append(i)
        else:
            continue
    return "".join(str1)
    

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
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long")
    numGuess = 8
    lettersGuessed = []
    print("Available Letters: " + str(string.ascii_lowercase))
    while(numGuess > 0):
        print("You have "+ str(numGuess) + " guesses left")
        guess = input("Please guess a letter:")
        lettersGuessed.append(guess)
        a1 = isWordGuessed(secretWord, lettersGuessed)
        print(str(a1))
        a2 = getGuessedWord(secretWord, lettersGuessed)
        print(str(a2))
        a3 = getAvailableLetters(lettersGuessed)
        print(str(a3))
        numGuess -= 1
        if ("_ " not in a2):
            print("Congrats you have guessed the word")
            break
    print("the word is "+str(secretWord))
    return None