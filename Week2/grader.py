# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 15:35:28 2018

@author: jpacsai
"""

"""
Grader

A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is: 
The perimeter of a polygon is: length of the boundary of the polygon
Write a function called polysum that takes 2 arguments, n and s. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.
"""

import math

def polysum(n, s):
   area = (0.25 * n * s**2) / (math.tan( math.pi / n))
   perimeter = n * s
   return round(area + perimeter**2, 4)

polysum(7, 2)