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
        'required': False,
    },

    {
        'id': 8,
        'folder': 'Shells',
        'rarities': [170, 9, 170, 170, 170, 9, 9, 79, 4, 79, 79, 79, 4, 4, 11, 1, 11, 11, 11, 1, 1, 45, 2, 45, 45, 45, 2, 2, 6, 1, 6, 6, 6, 1, 1, 136, 7, 136, 136, 136, 7, 7, 28, 1, 28, 28, 28, 1, 1, 373, 20, 373, 373, 373, 20, 20, 174, 9, 174, 174, 174, 9, 9, 25, 1, 25, 25, 25, 1, 1, 100, 5, 100, 100, 100, 5, 5, 12, 1, 12, 12, 12, 1, 1, 299, 16, 299, 299, 299, 16, 16, 62, 3, 62, 62, 62, 3, 3, 102, 5, 102, 102, 102, 5, 5, 48, 3, 48, 48, 48, 3, 3, 7, 1, 7, 7, 7, 1, 1, 27, 1, 27, 27, 27, 1, 1, 3, 1, 3, 3, 3, 1, 1, 81, 4, 81, 81, 81, 4, 4, 17, 1, 17, 17, 17, 1, 1, 34, 2, 34, 34, 34, 2, 2, 16, 1, 16, 16, 16, 1, 1, 2, 1, 2, 2, 2, 1, 1, 9, 1, 9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 1, 1, 27, 1, 27, 27, 27, 1, 1, 6, 1, 6, 6, 6, 1, 1, 68, 4, 68, 68, 68, 4, 4, 32, 2, 32, 32, 32, 2, 2, 5, 1, 5, 5, 5, 1, 1, 18, 1, 18, 18, 18, 1, 1, 2, 1, 2, 2, 2, 1, 1, 54, 3, 54, 54, 54, 3, 3, 11, 1, 11, 11, 11, 1, 1, 679, 36, 679, 679, 679, 36, 36, 317, 17, 317, 317, 317, 17, 17, 45, 2, 45, 45, 45, 2, 2, 181, 10, 181, 181, 181, 10, 10, 23, 1, 23, 23, 23, 1, 1, 543, 29, 543, 543, 543, 29, 29, 113, 6, 113, 113, 113, 6, 6],
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
        'required': False,
    },

    {
        'id': 12,
        'folder': 'Wing',
        'rarities': [0, 0, 0, 100],
        'required': False,
    }
]
