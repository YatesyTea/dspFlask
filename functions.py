import pymongo

# connect to DB
def connect_db():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["recipeDB"]
    mycol = mydb["recipes"]
    return mycol


# Query DB
def query_db(fat, fat_range, calories, calories_range, protein, protein_range):

    mycol = connect_db()

    myquery = {
        "fat" : {"$gte": fat-fat_range,"$lte": fat+fat_range},
        'calories' : {"$gte": calories-calories_range,"$lte": calories+calories_range},
        'protein' : {"$gte": protein-protein_range,"$lte": protein+protein_range},
    }

    results = mycol.find(myquery)

    for count, result in enumerate(results):
        print(f"{count}. Fat: {result['fat']} Calories {result['calories']}, Protein {result['protein']}")
    
    return results


# Parameter-based MLto widen search if necessary
def find_recipes(fat, calories, protein):
    fat_range = 5
    calories_range = 100
    protein_range = 5

    results = query_db(
        fat,fat_range,
        calories, calories_range,
        protein, protein_range
        )
    
    while len(list(results)) < 3:
        fat_range += 3
        calories_range +=50
        protein_range +=3
        print(f"NOT ENOUGH, length = {len(list(results))}")




# interface (gets user's input and displays terminal print statements)
def main():
    fat = int(input("Fat: "))
    calories = int(input("Calories: "))
    protein = int(input("Protein: "))

    query_db(
        fat,fat_range,
        calories, calories_range,
        protein, protein_range
        )

main()