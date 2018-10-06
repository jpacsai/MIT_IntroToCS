# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 23:14:23 2018

@author: jpacsai
"""

def decrypt_story():
    '''
    get_story_string() that returns the encrypted version of the story
    as a string
    
    creating a CiphertextMessage object using the story string and 
    use decrypt_message to return the appropriate shift value and 
    unencrypted story string
    '''
    story = get_story_string()
    unencrypted = CiphertextMessage(story)
    return unencrypted.decrypt_message()