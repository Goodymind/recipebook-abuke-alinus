import json
import os
# My recipe parser module

PATH = 'ledger/recipes/recipes.json'


def parse_recipes():
    try:
        with open(PATH, 'r') as recipe_txt:
            unparsed_recipe = recipe_txt.read()
            parsed_recipe = json.loads(unparsed_recipe)
            return parsed_recipe
    except FileNotFoundError:
        print('Recipes not Found on ' + PATH + ' current directory ')
    except json.JSONDecodeError:
        print('Error parsing json text')