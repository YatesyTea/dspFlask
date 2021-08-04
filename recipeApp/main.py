import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["recipeDB"]
mycol = mydb["recipes"]



'''
Given parameters (fat, calories, protein) and the ranges (set to 5, 100, 5 by default):
Returns a mongodb query
'''
def get_query(fat, calories, protein, fat_range, calories_range, protein_range):
    
    fat, calories, protein = int(fat), int(calories), int(protein)

    myquery = {
    "fat" : {"$gte": fat-fat_range,"$lte": fat+fat_range},
    'calories' : {"$gte": calories-calories_range,"$lte": calories+calories_range},
    'protein' : {"$gte": protein-protein_range,"$lte": protein+protein_range}
    }

    return myquery



'''
Given parameters fat / g, calories /cal, and protein / g: 
Returns a list of dictionaries, each dict item is a recipe.
If less than three results are found, updates the query and runs the search again until enough results are found.
'''
# Parameter-based MLto widen search if necessary
def find_recipes(fat, calories, protein):
    fat_range = 5
    calories_range = 100
    protein_range = 5

    query = get_query(fat, calories, protein, fat_range, calories_range, protein_range)
    results_count = mycol.count_documents(query)

    while results_count < 10:
        print(f"Only {results_count} results can be found, widening the search... ")
        fat_range += 5
        calories_range +=50
        protein_range +=5
        
        query = get_query(fat, calories, protein, fat_range, calories_range, protein_range)
        results_count = mycol.count_documents(query)

    
    mydoc = mycol.find(query)
    # print("Printing from main...")
    # print(f"type, from main, is {type(mydoc)} of length {len(list(mydoc))}")

    # for count,x in enumerate(mydoc,1):
    #     print(f"{count}. {x['title']}")

    return mydoc


if __name__ == "__main__":
    fat, calories, protein = 20, 600, 20
    find_recipes(fat,calories,protein)