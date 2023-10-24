#!/usr/bin/python3
import math
""" Creates class called MagicClass
"""




class MagicClass:

    """Class that stores the properties
    of a circumference"""
    def __init__(self, radius=0):
       """
        Returns the self
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    """ Method that calculates the area of the circumference """
    def area(self):
        """
        Returns the area of the magicClass
        """
        return ((self.__radius ** 2) * math.pi)

    """ Method that calculates the perimeter of a circumference """
    def circumference(self):
        """
        Returns the cicumference
        """
        return (2 * math.pi * self.__radius)
