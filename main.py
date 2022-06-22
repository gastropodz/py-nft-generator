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
        
        # copy out absolute path for use for replacement of plate image later
        if layer['folder'] == 'Background':
            layer_path_background = os.path.join(assets, layer['folder'])

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
            #if 'Rare_Cyborg.png' in final_layers[2]:
            #robot    img = ['None']
            # If small body, then need to use thin mouths
            if 'Small' in final_layers[2]:
                if 'Beard' in img[0]:
                    img = ['Beard_Thin.png']
                if 'Braces' in img[0]:
                    img = ['Braces_Thin.png']
                if 'Drool' in img[0]:
                    img = ['Drool_Thin.png']
                if 'Female_Default' in img[0]:
                    img = ['Female_Default_Thin.png']  
                if 'Female_Piercing' in img[0]:
                    img = ['Female_Piercing_Thin.png']
                if 'Female_Rare' in img[0]:
                    img = ['Female_Rare_Thin.png']
                if 'Female_Smirk' in img[0]:
                    img = ['Female_Smirk_Thin.png']
                if 'Gold' in img[0]:
                    img = ['Gold_Thin.png']
                if 'Gum' in img[0]:
                    img = ['Gum_Thin.png']
                if 'Male_Default' in img[0]:
                    img = ['Male_Default_Thin.png'] 
                if 'Male_Rare' in img[0]:
                    img = ['Male_Rare_Thin.png'] 
                if 'Male_Smirk' in img[0]:
                    img = ['Male_Smirk_Thin.png']
                if 'Onegold' in img[0]:
                    img = ['Onegold_Thin.png']    
                if 'Shine' in img[0]:
                    img = ['Shine_Thin.png']    
                if 'Smoke' in img[0]:
                    img = ['Smoke_Thin.png']    
                if 'Stache' in img[0]:
                    img = ['Stache_Thin.png']
                if 'Toothout' in img[0]:
                    img = ['Toothout_Thin.png']   
                if 'Tounge' in img[0]:
                    img = ['Tounge_Thin.png']   
                if 'Vampire' in img[0]:
                    img = ['Vampire_Thin.png']         

        # Certain Neck Exclusions
        if layer['folder'] == 'Accessories':
            # Rare_Cyborg.png - Tattoo.png
            if 'Rare_Cyborg.png' in final_layers[2] and 'Tattoo.png' in img[0]:
                img = ['None']

        # Exclude Propellent
        if layer['folder'] == 'Propellent':
            # For Propeller.png and Vortex.png we also need to exlcude them from the spoiler body
            if 'Spoiler' in final_layers[5] and 'Propeller.png' in img[0]:
                img = ['None']
            if 'Spoiler' in final_layers[5] and 'Vortex.png' in img[0]:
                img = ['None']
            if 'Spoiler' in final_layers[5] and 'Exhaust.png' in img[0]:
                img = ['None']
            if 'Spoiler' in final_layers[5] and 'Booster2' in img[0]:
                img = ['None']
            
            # Some manifolds and boosters dont go together
            # Turbinate, Lenticular,  good
            if 'Manifold' in final_layers[5] and 'Ovate' in final_layers[5] and 'Booster2' in img[0]:
                img = ['None']
            if 'Manifold' in final_layers[5] and 'Obconic' in final_layers[5] and 'Booster2' in img[0]:
                img = ['None']          
            if 'Manifold' in final_layers[5] and 'Biconic' in final_layers[5] and 'Booster2' in img[0]:
                img = ['None']    
            if 'Manifold' in final_layers[5] and 'Trichoid' in final_layers[5] and 'Booster2' in img[0]:
                img = ['None']    

            # For Propeller.png we need to check Weapoin layer for Salt_Dumptruck.png and exclude it.
            if 'Salt_Dumptruck.png' in final_layers[1] and 'Propeller.png' in img[0]:
                img = ['None']
            # For Booster2, image is diff depending on the shell
            if 'Booster2' in img[0]:
                if 'Biconic' in final_layers[5]:
                    if 'Conical' in final_layers[5]:
                        img = ['Booster2_Shell_Biconic_Conical.png']
                    else:
                        img = ['Booster2_Shell_Biconic_Spiral.png']
                if 'Lenticular' in final_layers[5]:
                    if 'Conical' in final_layers[5]:
                        img = ['Booster2_Shell_Lenticular_Conical.png']
                    else:
                        img = ['Booster2_Shell_Lenticular_Spiral.png']
                if 'Obconic' in final_layers[5]:
                    if 'Conical' in final_layers[5]:
                        img = ['Booster2_Shell_Obconic_Conical.png']
                    else:
                        img = ['Booster2_Shell_Obconic_Spiral.png']
                if 'Ovate' in final_layers[5]:
                    if 'Conical' in final_layers[5]:
                        img = ['Booster2_Shell_Ovate_Conical.png']
                    else:
                        img = ['Booster2_Shell_Ovate_Spiral.png']
                if 'Trichoid' in final_layers[5]:
                    if 'Conical' in final_layers[5]:
                        img = ['Booster2_Shell_Trichoid_Conical.png']
                    else:
                        img = ['Booster2_Shell_Trichoid_Spiral.png']
                if 'Turbinate' in final_layers[5]:
                    if 'Conical' in final_layers[5]:
                        img = ['Booster2_Shell_Turbinate_Conical.png']
                    else:
                        img = ['Booster2_Shell_Turbinate_Spiral.png']                
            # If there is no shell, then we need to set other layers to none. 
            # if we move air back in the id, this will need changing from 6 to 7 
            if 'None' in final_layers[5]:
                img = ['None']

        # If there is no shell, then we need to set other layers to none.
        if layer['folder'] == 'Shells':
            if img[0] == 'None':
                final_layers[1] = os.path.join(layer_path, img[0])
                # if we move air back in the id, this will need adding
                #final_layers[5] = os.path.join(layer_path, img[0])

        # Exclude Propellent
        #if layer['folder'] == 'Air':
            # If there is no shell, then we need to set other layers to none.
            # this can be removed if we move air back to ID 6  
            #if 'None' in final_layers[5]:
            #    img = ['None']            

        # if there is no transportation, and the background is Plate, change to the alternate plate image.
        if layer['folder'] == 'Transportation':
            # if background is plate, and ing Bigwheel.png, exclude it and make it no vehicle
            if 'Bigwheel' in img[0] and 'Plate' in final_layers[0]:
                img = ['None']
            # skateboard and salt dumptruck conflict
            if 'Skateboard' in img[0] and 'Salt_Dumptruck.png' in final_layers[1]:
                img = ['None']
            # go kart and taco dont go well together
            if 'Gokart' in img[0] and 'Taco_Gun.png' in final_layers[1]:
                img = ['None']
            if img[0] == 'None' and 'Plate' in final_layers[0]:
                final_layers[0] = os.path.join(layer_path_background, 'Plate_NoTransportation.png')
            # i think Skateboard, Tank, Gokart will also look better with the new plate
            if 'Skateboard' in img[0] and 'Plate' in final_layers[0]:
                final_layers[0] = os.path.join(layer_path_background, 'Plate_NoTransportation.png')
            if 'Tank' in img[0] and 'Plate' in final_layers[0]:
                final_layers[0] = os.path.join(layer_path_background, 'Plate_NoTransportation.png')
            if 'Gokart' in img[0] and 'Plate' in final_layers[0]:
                final_layers[0] = os.path.join(layer_path_background, 'Plate_NoTransportation.png')

        # Add additional layer in things that need it.
        if layer['folder'] == 'Wing':
            # Rare_Sailfish.png - SailfishWing.png
            if 'Rare_Sailfish.png' in final_layers[2]:
                img = ['SailfishWing.png']

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
        ShellsList.append(final_layers[5].split('\\')[-1])
        MouthList.append(final_layers[6].split('\\')[-1])
        TransaportationList.append(final_layers[7].split('\\')[-1])
        AccessoriesList.append(final_layers[8].split('\\')[-1])
        PropellentList.append(final_layers[9].split('\\')[-1])
        AirList.append(final_layers[10].split('\\')[-1])
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
