""" Initialises layers for use in the program.
    Make sure to type the exact directory name into the folder value.

    Rarity weights are based on the order of the images in each folder, typically
    alphabetical.
"""
layers = [
    {
        'id': 1,
        'folder': 'Background',
        'rarities': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 1, 2, 10, 4],
        'required': True,
    },   
    
    {
        'id': 2,
        'folder': 'Weapon',
        'rarities': [8, 19, 12, 6, 2, 5, 1, 17, 1, 2, 2, 7, 14, 2, 1],
        'required': True,
    },

    {
        'id': 3,
        'folder': 'Body',
        'rarities': [7, 7, 7, 7, 1, 1, 1, 1, 1, 1, 7, 7, 7, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7, 7, 7, 7, 1, 1, 1, 1, 1, 1],
        #'folder': 'Body_Rare',
        #'rarities': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'required': True,
    },

    {
        'id': 4,
        'folder': 'Body_Pattern',
        'rarities': [2, 5, 1, 24, 12, 10, 7, 39],
        'required': False,
    },

    {
        'id': 5,
        'folder': 'Eyes',
        'rarities': [1, 21, 3, 1, 2, 69, 3],
        'required': True,
    },

    {
        'id': 6,
        'folder': 'Mouth',
        'rarities': [2, 17, 2, 2, 2, 2, 50, 2, 2, 2],
        'required': True,
    },

    {
        'id': 7,
        'folder': 'Air',
        'rarities': [6, 1, 2, 8, 4, 5, 7, 67],
        #'rarities': [0, 0, 0, 0, 0, 100, 0, 0],
        'required': False,
    },

    {
        'id': 8,
        'folder': 'Shells',
        'rarities': [17, 1, 17, 17, 17, 1, 1, 8, 1, 8, 8, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 1, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 14, 1, 14, 14, 14, 1, 1, 3, 1, 3, 3, 3, 1, 1, 37, 2, 37, 37, 37, 2, 2, 17, 1, 17, 17, 17, 1, 1, 3, 1, 3, 3, 3, 1, 1, 10, 1, 10, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 30, 2, 30, 30, 30, 2, 2, 6, 1, 6, 6, 6, 1, 1, 10, 1, 10, 10, 10, 1, 1, 5, 1, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 1, 8, 8, 8, 1, 1, 2, 1, 2, 2, 2, 1, 1, 3, 1, 3, 3, 3, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7, 1, 7, 7, 7, 1, 1, 3, 1, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 1, 6, 6, 6, 1, 1, 2, 1, 2, 2, 2, 1, 1, 68, 4, 68, 68, 68, 4, 4, 32, 2, 32, 32, 32, 2, 2, 5, 1, 5, 5, 5, 1, 1, 18, 1, 18, 18, 18, 1, 1, 2, 1, 2, 2, 2, 1, 1, 55, 3, 55, 55, 55, 3, 3, 12, 1, 12, 12, 12, 1, 1],
        'required': True,
    },

    {
        'id': 9,
        'folder': 'Transportation',
        'rarities': [8, 8, 5, 7, 2, 1, 14, 4, 1, 4, 6, 10, 5, 2, 23],
        'required': False,
    },

    {
        'id': 10,
        'folder': 'Accessories',
        'rarities': [1, 19, 14, 2, 17, 7, 12, 1, 7, 7, 7, 4, 2],
        'required': True,
    },
    {
        'id': 11,
        'folder': 'Propellent',
        'rarities': [8, 7, 5, 2, 6, 1, 4, 67],
        #'rarities': [0, 0, 0, 0, 0, 0, 100, 0],
        'required': False,
    },
    {
        'id': 12,
        'folder': 'Wing',
        'rarities': [0, 0, 0, 100],
        'required': False,
    }
]
