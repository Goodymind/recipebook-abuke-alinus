'''
    Module providing a parser for recipes in JSON
'''

import json

PATH = 'ledger/recipes/recipes.json'

def parse_recipes():
    '''
        gets the recipes from the PATH file and returns it as object
        dict or list
    '''

    try:
        with open(PATH, 'r', encoding='UTF-8') as recipe_txt:
            unparsed_recipe = recipe_txt.read()
            parsed_recipe = json.loads(unparsed_recipe)
            return parsed_recipe

    except FileNotFoundError:
        print('Recipes not Found on ' + PATH + ' current directory ')

    except json.JSONDecodeError:
        print('Error parsing json text')

    return None
