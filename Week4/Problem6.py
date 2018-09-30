# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 23:30:07 2018

@author: jpacsai
"""

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    todo = ''
    hand = None
    play = True
    allowedInput = ['n', 'r', 'e']
    while play == True:
        while todo not in allowedInput:
            todo = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
            if todo not in allowedInput:
                print(todo + ' Invalid command.')
        if todo == 'n' or todo == 'r':
            if todo == 'n':
                hand = dealHand(HAND_SIZE)
            elif hand == None:
                print('You have not played a hand yet. Please play a new hand first!')
                todo = ''
                continue
            playHand(hand, wordList, HAND_SIZE)
            todo = ''
        else:
            play = False
            todo = ''