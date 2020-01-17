# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room): # constructor
        self.name = name
        self.room = room

    def __str__(self): # __repr__ programmer friendly version of __str__
        return f'{self.name} is currently in {self.room}.'
