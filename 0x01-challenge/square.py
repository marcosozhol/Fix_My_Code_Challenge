#!/usr/bin/python3
"""Defines class square"""


class square():
    """Class square"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """init method"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.height * self.width

    def permiter_of_my_square(self):
        """ Perimeter of square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Str representation """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    """check if main"""
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
