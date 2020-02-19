#!/usr/bin/python

import math

# The keys will be the ingredient names, with their associated values being the amounts. In the case of the recipe dictionary, these amounts will represent the amount of each ingredient needed for the recipe, while in the case of the ingredients dictionary, the amounts represent the amounts available to you. 

# Your function should output the maximum number of whole batches that can be made for the supplied recipe using the ingredients available to you, as indicated by the second dictionary. 


# ```python
# # should return 0 since we don't have enough butter!
# recipe_batches(
#   { 'milk': 100, 'butter': 50, 'flour': 5 },
#   { 'milk': 138, 'butter': 48, 'flour': 51 }
# )
# ```

# ## Hints

#  * What's the _minimum_ number of loops we need to perform in order to write a working implementation?

def recipe_batches(recipe, ingredients, count=0):
  '''
  Receives a recipe in the form of a dictionary
  Receives ingredients you have available to you, also in the form of a dictionary
  Return the maximum number of whole batches that can be made for the supplied recipe using the ingredients available to you
  '''
  '''
  base case: at least one of the ingredients will be negative
  get keys into list
  loop through list to get values
  subtract used ingredients
  add to counter
  '''
  
  for key in recipe.keys():
      if key not in ingredients.keys():
          print(count)
          return count
      else:
          ingredients[key] = ingredients[key] - recipe[key]
          if ingredients[key] < 0:
              print(count)
              return count

  count += 1

  recipe_batches(recipe, ingredients, count)


print(recipe_batches({ 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, { 'milk': 1288, 'flour': 9, 'sugar': 95 })) # 0
print(recipe_batches({ 'milk': 100, 'butter': 50, 'cheese': 10 }, { 'milk': 198, 'butter': 52, 'cheese': 10 })) # 1
print(recipe_batches({ 'milk': 2, 'sugar': 40, 'butter': 20 }, { 'milk': 5, 'sugar': 120, 'butter': 500 })) # 2
print(recipe_batches({ 'milk': 2 }, { 'milk': 200})) # 100

# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))