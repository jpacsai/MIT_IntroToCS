# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 18:05:06 2018

@author: User
"""

"""
Problem 3

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. 

For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""

longest = s[0:1]
i = 0

while i < len(s) - 1:
    j = i + 1
    while j < len(s):
        if ord(s[j]) >= ord(s[j - 1]):
            j += 1
            long = s[i:j]
            if len(long) > len(longest):
                longest = long
        else:
            break
    if j == len(s):
        break
    i += 1
    
print('Longest substring in alphabetical order is: ' + longest)