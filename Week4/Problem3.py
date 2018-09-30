# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 15:48:54 2018

@author: jpacsai
"""

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    if word not in wordList:
        return False
    else:
        check = hand.copy()
        for char in word:
            try:
                if check[char] == 0:
                    return False
                else:
                    check[char] -= 1
            except KeyError:
                return False
        return True