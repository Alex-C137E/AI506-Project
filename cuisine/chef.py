"""
This Chef file is creating data (x_i, y_i) from the cookbook (recipe_i)
"""

import numpy as np


def make_binary_data(cookbook, ingredient_list):
    # X is a binary matrix with recipe rows and ingredients columns, 
    # where (recipe, ingredients) is 1 if the ingredient is present in the recipe

    n_recipies = len(cookbook)
    n_ingredients = len(ingredient_list)

    X = np.zeros((n_recipies, n_ingredients))
    y = np.zeros(n_recipies)
    for idx, recipe in enumerate(cookbook):
        y[idx] = recipe['kitchen_id']
        for ingredient_id in recipe['ingredients']:
            X[idx][ingredient_id] = 1
            
    return X,y
    