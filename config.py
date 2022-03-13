""" Initialises layers for use in the program.
    Make sure to type the exact directory name into the folder value.

    Rarity weights are based on the order of the images in each folder, typically
    alphabetical.
"""
layers = [
    {
        'id': 1,
        'folder': 'Background',
        'rarities': [5, 10, 1, 2, 7, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        'required': True,

    },

    {
        'id': 2,
        'folder': 'Body',
        'rarities': [7, 7, 7, 7, 1, 1, 1, 1, 1, 7, 7, 7, 7, 1, 1, 1, 1, 1, 7, 7, 7, 7, 1, 1, 1, 1, 1],
        #'folder': 'Body_Rare',
        #'rarities': [1, 1, 1, 1, 1, 1, 1, 1],
        'required': True,
    },

    {
        'id': 3,
        'folder': 'Body_Pattern',
        'rarities': [2, 5, 1, 24, 12, 10, 7, 39],
        'required': False,
    },

    {
        'id': 4,
        'folder': 'Eyes',
        'rarities': [1, 21, 3, 1, 2, 69, 3],
        'required': True,
    },

    {
        'id': 5,
        'folder': 'Mouth',
        'rarities': [23, 2, 73, 2],
        'required': True,
    },

    {
        'id': 6,
        'folder': 'Transportation',
        'rarities': [8, 8, 5, 7, 2, 1, 14, 4, 1, 4, 6, 10, 5, 2, 23],
        'required': False,
    }
]
