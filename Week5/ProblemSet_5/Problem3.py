# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 23:05:09 2018

@author: jpacsai
"""

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        self.message_text = text
        self.valid_words = Message.get_valid_words(self)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        best = {'counter' : 0, 'shift' : 0, 'message' : ''}
        
        for i in range(0, 27):
            tryShift = i
            validCounter = 0
            decripted = Message.apply_shift(self, tryShift).split(' ')
            for word in decripted:
                if word in self.valid_words:
                    validCounter += 1
            if validCounter > best['counter']:
                best['counter'] = validCounter
                best['shift'] = i
                best['message'] = ' '.join(decripted)
        return (best['shift'], best['message'])