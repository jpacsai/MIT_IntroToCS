# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 16:04:29 2018

@author: jpacsai
"""
        
def build_shift_dict(self, shift):
    '''
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a
    character shifted down the alphabet by the input shift. The dictionary
    should have 52 keys of all the uppercase letters and all the lowercase
    letters only.        
    
    shift (integer): the amount by which to shift every letter of the 
    alphabet. 0 <= shift < 26

    Returns: a dictionary mapping a letter (string) to 
             another letter (string). 
    '''
    newDict = {}
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    
    for char in lower:
        shifted = ord(char)+shift
        if shifted > 122:
            shifted -= 26
        newDict[char] = chr(shifted)
        
    for char in upper:
        shifted = ord(char)+shift
        if shifted > 90:
            shifted -= 26
        newDict[char] = chr(shifted)
    
    return newDict


def apply_shift(self, shift):
    '''
    Applies the Caesar Cipher to self.message_text with the input shift.
    Creates a new string that is self.message_text shifted down the
    alphabet by some number of characters determined by the input shift        
    
    shift (integer): the shift with which to encrypt the message.
    0 <= shift < 26

    Returns: the message text (string) in which every character is shifted
         down the alphabet by the input shift
    '''
    newDict = self.build_shift_dict(shift)
    newStr = ''
    for char in self.message_text:
        try:
            newStr += newDict[char]
        except KeyError:
            newStr += char
    return newStr