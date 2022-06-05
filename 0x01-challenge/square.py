#!/usr/bin/python3
"""
module that defines class Square
"""


class Square():
    """ class square """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Init method """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.height * self.width

    def perimeter_of_my_square(self):
        """ perimeter of square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ measurements of its characteristics """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ define name as main """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
