# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 17:59:11 2018

@author: jpacsai
"""

"""
Problem 2

Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.

For example, if s = 'azcbobobegghakl', then your program should print:

Number of times bob occurs is: 2
"""

bob = 0

for x in range(0, len(s) - 2):
    if s[x:x+3] == 'bob':
        bob += 1
        
print('Number of times bob occurs is: ' + str(bob))