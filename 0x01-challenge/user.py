#!/usr/bin/python3
"""
module that defines class user
"""


class User():
    """ Class User """

    def __init__(self):
        """ Init method """
        self.__email = None

    @email.setter
    def email(self, value):
        """ Property email check is str """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value

    @property
    def email(self):
        """ property email """
        return self.__email


if __name__ == "__main__":
    """ define name as main """
    u = User()
    u.email = "john@snow.com"
    print(u.email)
