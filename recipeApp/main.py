import pymongo
# app connects to DB
# Connect to the recipes database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["recipeDB"]
mycol = mydb["recipes"]

# takes user's input for preferences

# queries db as per ^
myquery = {"fat" : {"$gte": 20,"$lte": 21}}

# List of all recipes within bounds:
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)
    #print(f"Fat: {x['title']}")
# Selection of recipes (tournament)

# for calories selection slider for how 'big / heavy' each meal is and then weigh up calories for that meal 
# print(mydoc[choose(rand int in range len mydoc )])

# generates recipe (randomly / ML) based on search 