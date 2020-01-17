from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"), Item("Rock"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""), Item("Candlestick"),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""), Item("Pebble"),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""), Item("Gold"),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""), Item("Treasure"),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main

# Make a new player object that is currently in the 'outside' room.
player = Player('Elliot', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# Day 2 mvp
# Make rooms able to hold multiple items
# Make the player able to carry multiple items
# Add items to the game that the user can carry around
# Add get [ITEM_NAME] and drop [ITEM_NAME] commands to the parser

move = None

while move != 'q':
    # print current room name, description
    print(player.room)

    # user input
    move = input('Enter n, s, e, w to enter a room or q to quit the game:')

    # error
    error = 'This move is not allowed.'

    # movements
    if move == 'n':
        if player.room.n_to:
            player.room = player.room.n_to
        else:
            print(error)
    elif move == 's':
        if player.room.s_to:
            player.room = player.room.s_to
        else:
            print(error)
    elif move == 'e':
        if player.room.e_to:
            player.room = player.room.e_to
        else:
            print(error)
    elif move == 'w':
        if player.room.w_to:
            player.room = player.room.w_to
        else:
            print(error)
    elif move == 'q':
        print('Game over!')
        break
