#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = []
  if not set(ingredients).issuperset(set(recipe)):
    return 0
  else:
    for k in set(recipe) & set(ingredients):
      print( ingredients[k], recipe[k] )
      print(int(ingredients[k] /recipe[k] ))

      batches.append( int(ingredients[k] /recipe[k] ) )
  
  batches.sort()
  print(batches)
  return batches[0]


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))


  # Plan 

  # Loop through recipes 
  # check for matching keys in a ingredients
  # if mod recipe item 