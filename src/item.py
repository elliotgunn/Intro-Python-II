# Implement a class to hold item information. This should have name and
# description attributes.

class Item:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name}'
