from csv import reader
import pandas as pd


__kitchen_list = []


def get_cookbook_train():

    cookbook_train = []

    with open('data/train.csv', 'r') as file:

        csv_reader = reader(file, delimiter=",")

        for i, row in enumerate(csv_reader):
            
            kitchen = row[-1]
            ingredient_strings = row[1:-1]
            ingredients = [ int(s) for s in ingredient_strings ]
            
            cookbook_train.append({
                'recipe_id': i,
                'ingredients': ingredients,
                'kitchen_name': kitchen
            })      

    fill_kitchen_list(cookbook_train)
    add_kitchen_id_to_cookbook(cookbook_train)
    return cookbook_train


def get_cookbook_valid_question():

    cookbook_valid_question = []

    with open('data/validation_classification_question.csv', 'r') as file:

        csv_reader = reader(file, delimiter=",")

        for i, row in enumerate(csv_reader):
            ingredients = [ int(s) for s in row ]
            cookbook_valid_question.append({
                'recipe_id': i,
                'ingredients': ingredients,
                'kitchen_name': "UNKNOWNKITCHEN",
                'kitchen_id': "-999"
            })     

    return cookbook_valid_question


       
def get_cookbook_valid_answer():

    cookbook_valid_answer = []

    with open('data/validation_classification_answer.csv', 'r') as file:

        csv_reader = reader(file, delimiter=",")

        for i, row in enumerate(csv_reader):        
            kitchen = row[0]        
            cookbook_valid_answer.append({
                'recipe_id': i,
                'ingredients': [],
                'kitchen_name': kitchen
            })

    fill_kitchen_list(cookbook_valid_answer)
    add_kitchen_id_to_cookbook(cookbook_valid_answer)
    return cookbook_valid_answer


def get_cookbook_test_question():

    cookbook_valid_question = []

    with open('data/test_classification_question.csv', 'r') as file:

        csv_reader = reader(file, delimiter=",")

        for i, row in enumerate(csv_reader):
            ingredients = [ int(s) for s in row ]
            cookbook_valid_question.append({
                'recipe_id': i,
                'ingredients': ingredients,
                'kitchen_name': "UNKNOWNKITCHEN",
                'kitchen_id': "-999"
            })     

    return cookbook_valid_question


def get_cookbook_test_answer():

    cookbook_valid_answer = []

    with open('data/test_classification_answer.csv', 'r') as file:

        csv_reader = reader(file, delimiter=",")

        for i, row in enumerate(csv_reader):        
            kitchen = row[0]        
            cookbook_valid_answer.append({
                'recipe_id': i,
                'ingredients': [],
                'kitchen_name': kitchen
            })

    fill_kitchen_list(cookbook_valid_answer)
    add_kitchen_id_to_cookbook(cookbook_valid_answer)
    return cookbook_valid_answer


def get_ingredient_list():

    node_ingredient = pd.read_fwf('data/node_ingredient.csv', header=None)
    ingredient_list = [None] * node_ingredient.shape[0]
    for index , row in node_ingredient.iterrows():
        ingredient_list[index] = row[0]

    return ingredient_list


def fill_kitchen_list(cookbook):

    for recipe in cookbook:
        if recipe['kitchen_name'] not in __kitchen_list:
            __kitchen_list.append(recipe['kitchen_name'])



def add_kitchen_id_to_cookbook(cookbook):   

    for recipe in cookbook:
        kitchen_id = __kitchen_list.index(recipe['kitchen_name'])
        recipe['kitchen_id'] = kitchen_id
        
