""" Main process module - Generates layered image and metadata files """

from collections import Counter
import csv
import json
import os
import random

from PIL import Image

from config import layers


def make_dirs():
    """Creates the directories to store final images and later on, their corresponding json data. If
    the folders already exist, print to confirm and continue with the program.
    """
    print('Creating build directories')
    build_dirs = ['build', 'build/images', 'build/json']

    for _dir in build_dirs:
        if not os.path.isdir(_dir):
            print(f'Directory does not yet exist; creating {_dir}')
            os.mkdir(_dir)

    print('Build directories created')


def join_layers(assets: str) -> tuple():
    """Loops through each layer folder and chooses
        a layer from each folder based on the given
        rarity weights. It then appends all the paths
        to a list which act as the final layers for the image.
    """
    final_layers = []

    # For each layer in the config file:
    for layer in layers:

        # Joins absolute path with each layer directory for use in next step
        layer_path = os.path.join(assets, layer['folder'])

        # Sorts images into alphebetical order for use with rarities
        sorted_layers = sorted(os.listdir(layer_path))

        # If the layer is optional, add None value based on final rarity weight
        if not layer['required']:
            sorted_layers.append('None')

        # Choose an image from the given subdirectory based on rarities
        img = random.choices(sorted_layers, weights=(layer['rarities']))

        # Exceptions - sometimes a body for example, we wont want the body overlay
        # Body_Pattern Exclusions
        if layer['folder'] == 'Body_Pattern':
            # Rare_Cyborg.png
            if 'Rare_Cyborg.png' in final_layers[2]:
                img = ['None']
            # Large_Rare_Cheetah.png
            if 'Large_Rare_Cheetah.png' in final_layers[2]:
                img = ['None']
            # Medium_Rare_Cheetah.png
            if 'Medium_Rare_Cheetah.png' in final_layers[2]:
                img = ['None']
            # Small_Rare_Cheetah.png
            if 'Small_Rare_Cheetah.png' in final_layers[2]:
                img = ['None']
            # Rare_Pixelated.png
            if 'Rare_Pixelated.png' in final_layers[2]:
                img = ['None']
            # Rare_Reptilian.png
            if 'Rare_Reptilian.png' in final_layers[2]:
                img = ['None']    
            # Rare_Falcon.png
            if 'Rare_Falcon.png' in final_layers[2]:
                img = ['None']

        # Mouth Exclusions
        if layer['folder'] == 'Mouth':
            # Rare_Falcon.png
            if 'Rare_Falcon.png' in final_layers[2]:
                img = ['None']
            # Rare_Cyborg.png
            if 'Rare_Cyborg.png' in final_layers[2]:
                img = ['None']

        # Certain Neck Exclusions
        if layer['folder'] == 'Accessories':
            # Rare_Cyborg.png - Tattoo.png
            if 'Rare_Cyborg.png' in final_layers[2] and 'Tattoo.png' in img[0]:
                img = ['None']

        # Exclude Propellent
        if layer['folder'] == 'Propellent':
            # If the shell is exhaust, then delete propellant for this build
            if 'Exhaust' in final_layers[7]:
                img = ['None']
            # For Propeller.png and Vortex.png we also need to exlcude them from the spoiler body
            if 'Spoiler' in final_layers[7] and 'Propeller.png' in img[0]:
                img = ['None']
            if 'Spoiler' in final_layers[7] and 'Vortex.png' in img[0]:
                img = ['None']
            # For Propeller.png we need to check Weapoin layer for Salt_Dumptruck.png and exclude it.
            if 'Salt_Dumptruck.png' in final_layers[1] and 'Propeller.png' in img[0]:
                img = ['None']

        # Add additional layer in things that need it.
        if layer['folder'] == 'Wing':
            # Rare_Falcon.png - FalconWing.png
            if 'Rare_Falcon.png' in final_layers[2]:
                img = ['FalconWing.png']
            # Rare_Sailfish.png - SailfishWing.png
            if 'Rare_Sailfish.png' in final_layers[2]:
                img = ['SailfishWing.png']
            # Parachute.png - ParachuteTop.png
            if 'Parachute.png' in final_layers[6]:
                img = ['ParachuteTop.png']            

        # Store each chosen image path to a list
        final_layers.append(os.path.join(layer_path, img[0]))

    # Convert to hashable data type so duplicates can be checked for later on
    final_layers = tuple(final_layers)
    return final_layers


def create_metadata(description: str, token_name: str, edition: int, final_layers: list):
    """Takes in some user data, along with the layers of the image
        and create a metadata json for the image. The json object
        can be used to provide token data to IPFS or third-party websites such as OpenSea.
    """

    metadata = {
        'name': f'{token_name} #{edition}',
        'description': description,
        # for opensea
        #'image': f'ipfs://baseURI/{edition}.png',
        # for Zilliqa zrc7
        'resource': f'ipfs://baseURI/{edition}.png',
        'edition': edition,
        'attributes': [
            #{'trait_type': '', 'value': ''},
            #{'trait_type': '', 'value': ''},
            #{'trait_type': '', 'value': ''}
        ]
    }

    for layer in final_layers:

        attributes_dict = dict()
        data = layer.split('\\')
        # might be needed for linux, im using above with windows.
        #data = layer.split('/')

        # Add the trait category as a key in dict
        attributes_dict['trait_type'] = data[-2]

        trait_value = data[-1]

        if trait_value != 'None':
            # Remove png extension and add the trait value
            attributes_dict['value'] = trait_value.replace('.png', '')
        else:
            attributes_dict['value'] = trait_value
    
        metadata['attributes'].append(attributes_dict)

    with open(f'build/json/{edition}.json', 'w', encoding='utf-8') as outfile:
        json.dump(metadata, outfile, indent=2)


def create_image(token_name: str, edition: int, final_layers: list):
    """Takes a list of final layers, and pastes them all onto the background image to create one
    final image. Saves it in the images folder."""

    # Sets the background layer
    background_layer = Image.open(final_layers[0])

    # Adds each layer to the background
    for filepath in final_layers[1:]:

        # If the filepath isn't None
        if not filepath.endswith('None'):
            img = Image.open(filepath)

            # TODO: work out why some collections require paste rather than alpha composite.
            # background_layer.paste(img, img)
            background_layer.paste(img, img)

    background_layer.save(f'build/images/{token_name}-{edition}.png')


def main():
    """Takes inputs for the desired images. Creates a build directory, edition counter, then loops
    through for the desired amount. DNA keeps track of each created image to avoid duplicates."""

    token_name = input('Enter the name for your tokens. \
        This will appear as the name for each image\n')
    description = input('Enter the description for your tokens\n')
    amount = int(input('Enter the amount of images you would like created\n'))
    mock = input('Do you want to do a mock run for stats? (Yes or leave blank)\n')

    edition = 1
    dna_set = set()


    BackgroundList = list()
    BodyList = list()
    BodyPatternList = list()
    EyesList = list()
    MouthList = list()
    AirList = list()
    WeaponList = list()
    ShellsList = list()
    TransaportationList = list()
    AccessoriesList = list()
    PropellentList = list()

    make_dirs()
    assets_directory = os.path.join(os.getcwd(), 'assets')

    for _ in range(amount):

        final_layers = join_layers(assets_directory)

        if final_layers in dna_set:

            print(f'DNA already exists! Retrying token {edition}')
            continue

        if mock != 'Yes':
            create_metadata(description, token_name, edition, final_layers)
        
        if mock != 'Yes':
            create_image(token_name, edition, final_layers)
        
        dna_set.add(final_layers)
        
        # Trying to get stats
        BackgroundList.append(final_layers[0].split('\\')[-1])
        WeaponList.append(final_layers[1].split('\\')[-1])
        BodyList.append(final_layers[2].split('\\')[-1])
        BodyPatternList.append(final_layers[3].split('\\')[-1])
        EyesList.append(final_layers[4].split('\\')[-1])
        MouthList.append(final_layers[5].split('\\')[-1])
        AirList.append(final_layers[6].split('\\')[-1])
        ShellsList.append(final_layers[7].split('\\')[-1])
        TransaportationList.append(final_layers[8].split('\\')[-1])
        AccessoriesList.append(final_layers[9].split('\\')[-1])
        PropellentList.append(final_layers[10].split('\\')[-1])
        edition += 1

    print('Background Stats')
    cnt = Counter(BackgroundList)
    for value, count in cnt.most_common():
         print(value, count)

    print('Body Stats')
    cnt = Counter(BodyList)
    for value, count in cnt.most_common():
         print(value, count)

    print('BodyPattern Stats')
    cnt = Counter(BodyPatternList)
    for value, count in cnt.most_common():
         print(value, count)

    print('Eyes Stats')
    cnt = Counter(EyesList)
    for value, count in cnt.most_common():
         print(value, count)

    print('Mouth Stats')
    cnt = Counter(MouthList)
    for value, count in cnt.most_common():
         print(value, count)
    
    print('Air Stats')
    cnt = Counter(AirList)
    for value, count in cnt.most_common():
         print(value, count)

    print('Weapon Stats')
    cnt = Counter(WeaponList)
    for value, count in cnt.most_common():
         print(value, count)

    print('Shells Stats')
    cnt = Counter(ShellsList)
    for value, count in cnt.most_common():
         print(value, count)

    print('Transaportation Stats')
    cnt = Counter(TransaportationList)
    for value, count in cnt.most_common():
         print(value, count)

    print('Propellent Stats')
    cnt = Counter(PropellentList)
    for value, count in cnt.most_common():
         print(value, count)

    print('Accessories Stats')
    cnt = Counter(AccessoriesList)
    for value, count in cnt.most_common():
         print(value, count)

    print('Image creation complete')


if __name__ == '__main__':
    main()
