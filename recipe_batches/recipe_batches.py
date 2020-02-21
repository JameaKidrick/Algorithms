#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
        '''
        Receives a recipe in the form of a dictionary
        Receives ingredients you have available to you, also in the form of a dictionary
        Return the maximum number of whole batches that can be made for the supplied recipe using the ingredients available to you
        '''

        # base case: at least one of the ingredients will be negative
        # get keys into list
        # loop through list to get values
        # divide values from each other
        # add to array
        # compare numbers to make sure there is enough ingredients

        arr = []
        smallest = 0
        for key in recipe.keys():
            if key not in ingredients.keys():
                return 0
        y = [key for key, value in recipe.items()]
        for name in y:
            arr.append(math.floor(ingredients[name]/recipe[name]))
            for i in range(0, len(arr)):
                if arr[i] < arr[smallest]:
                    smallest = i
        return arr[smallest]

if __name__ == '__main__':
    # Change the entries of these dictionaries to test 
    # your implementation with different inputs
    recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
    ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))