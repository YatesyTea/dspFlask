import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["recipeDB"]
mycol = mydb["recipes"]

'''
Given parameters fat / g, calories /cal, and protein / g: 
Returns at least three recipe suggestions.
-> list of dictionaries, each dict item is a recipe.
'''
def main(fat, calories, protein):
    # fat = int(input("Fat: "))
    # calories = int(input("Calories: "))
    # protein = int(input("Protein: "))

    find_recipes(fat,calories,protein)

'''
Given parameters (fat, calories, protein) anf the ranges (set to 5, 100, 5 by default):
Returns a mongodb query
'''
def get_query(fat, calories, protein, fat_range, calories_range, protein_range):
    
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

    while results_count < 3:
        print(f"Only {results_count} results can be found, widening the search... ")
        print(calories_range, protein_range, fat_range)        
        
        fat_range += 3
        calories_range +=50
        protein_range +=3
        
        query = get_query(fat, calories, protein, fat_range, calories_range, protein_range)
        results_count = mycol.count_documents(query)

    
    mydoc = mycol.find(query)
    for count,x in enumerate(mydoc,1):
        print(f"{count}. {x['title']}")
        print(f"Fat: {x['fat']}, Calories: {x['calories']}, Protein {x['protein']}")

        # if count == 10:
        #     more = input("Would you like to see the remaining recipes? Y/N").upper()
        #     if more == "Y":
        #         continue
        #     else: 
        #         break
        return list(mydoc)


if __name__ == "__main__":
    main()