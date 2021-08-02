import pymongo
# app connects to DB
# Connect to the recipes database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["recipeDB"]
mycol = mydb["recipes"]

# takes user's input for preferences
fat = int(input("Fat: "))
calories = int(input("Calories: "))
protein = int(input("Protein: "))
# vegan"yes/no"
# sodium = int(input("sodium"))

# Selection of Size of Each Meal comparative to others
# meal1 = int(input("0 1 2 3:"))
# meal2 = int(input("0 1 2 3:"))
# meal3 = int(input("0 1 2 3:"))

# Set Search Ranges
fatRange = 5
caloriesRange = 100
proteinRange = 5

recipeNotFound = True
while recipeNotFound == True:
    
    # Query using variables provided.
    myquery = {
        "fat" : {"$gte": fat-fatRange,"$lte": fat+fatRange},
        'calories' : {"$gte": calories-caloriesRange,"$lte": calories+caloriesRange},
        'protein' : {"$gte": protein-proteinRange,"$lte": protein+proteinRange}
    }

    # List of all recipes within bounds:
    mydoc = mycol.find(myquery)
    
    # If we've got recipes to use here.
    if mydoc != None:
        recipeNotFound = False
    # Increase Search Parameters if none found within bounds.
    else:
        fatRange += 3
        caloriesRange +=50
        proteinRange +=3

    for x in mydoc:
            print(f"Fat: {x['fat']} Calories {x['calories']}, Protein {x['protein']}")

    
# Selection of recipes (tournament)


# print(mydoc[choose(rand int in range len mydoc )])

# generates recipe (randomly / ML) based on search 