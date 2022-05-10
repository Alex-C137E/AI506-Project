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


def make_embedding_data(cookbook, embedding):
    # Make the data. X is a matrix with recipe rows and embedding dimension columns, 
    # where every row is the average of the embeddings in the recipes

    n_recipies = len(cookbook)
    embedding_dim = len(embedding[0])

    X = np.zeros((n_recipies, embedding_dim))
    y = np.zeros(n_recipies)
    for idx, recipe in enumerate(cookbook):
        embedding_avg = np.zeros(embedding_dim) 
        ingredient_count = len(recipe['ingredients'])
        y[idx] = recipe['kitchen_id']
        for ingredient_id in recipe['ingredients']:
            embedding_avg += embedding[ingredient_id] / ingredient_count
            
        X[idx, :] = embedding_avg
            
    return X,y
    
    