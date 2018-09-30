# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 16:03:38 2018

@author: jpacsai
"""

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    length = 0
    for num in hand.items():
        length += num[1]
    return length