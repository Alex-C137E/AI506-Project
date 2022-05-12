import pandas as pd
import numpy as np
import re


def import_embedding(filename, ingredient_list):

    df = pd.read_csv(f'embeddings/{filename}.csv', delimiter=",")

    # Create an embedding dictionary from the file
    embedding = {}
    for index, row in df.iterrows():
        ingredient_id = row[1]
        embedding_string = row[2]
        embedding_formatted = re.findall(r'[\d|\.|e|\+|\-]+', embedding_string)
        embedding_array = np.asarray(embedding_formatted, dtype=float)
        embedding[ingredient_id] = embedding_array

        
    add_zero_embedding_for_unknown_ingredients(embedding, ingredient_list)
        
    return embedding


def add_zero_embedding_for_unknown_ingredients(embedding, ingredient_list):

    embedding_dim = len(embedding[0])

    for ingredient, _ in enumerate(ingredient_list):
        if ingredient not in embedding:
            embedding[ingredient] = np.zeros(embedding_dim)


def create_random_embedding(ingredient_list, dim):

    embedding = {}
    for ingredient, _ in enumerate(ingredient_list):
        embedding[ingredient] = np.random.rand(dim)

    return embedding


def create_one_hot_embedding(ingredient_list):

    embedding = {}
    num_ingredients = len(ingredient_list)
    for ingredient, _ in enumerate(ingredient_list):
        embedding[ingredient] = np.zeros(num_ingredients)
        embedding[ingredient][ingredient] = 1
    return embedding