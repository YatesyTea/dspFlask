import main
import json
import random
from flask import Flask, render_template, redirect, request, url_for, jsonify
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__, template_folder="./templates")
app.config['SECRET_KEY'] = "secret_key"

recipe_details = {}

# form for user to input their preferences 
class DietaryForm(FlaskForm):
    fat = IntegerField("How many grams of fat would you like to consume per meal?", validators=[DataRequired()])
    calories = IntegerField("How many calories would you like to consume per meal?", validators=[DataRequired()])
    protein = IntegerField("How much protein would to consume per meal?", validators=[DataRequired()])
    submit = SubmitField("Submit")
    
# Setting http methods, where the requests are going.
@app.route("/", methods=["GET", "POST"])
def home():
    form = DietaryForm(request.form)
    message = "Please fill out this form with your dietary requirements, so we can find you some awesome recipes!"

    if request.method == "POST":
        fat = form.fat.data
        calories = form.calories.data
        protein = form.protein.data

        form.fat.data = ""
        form.calories.data = ""
        form.protein.data = ""

        message = "Thank you. You will now be redirected to your bespoke recipe recommendations" 
        
        return redirect(url_for("recipes", fat=fat, calories=calories, protein=protein))
    
    return render_template("index.html", form=form, message=message)

@app.route("/recipes/<fat>_<calories>_<protein>/")
def recipes(fat, calories, protein):
    # error exception here to redirect them to homepage if they enter nothing 
    recipes = random.choices(list(main.find_recipes(fat,calories,protein)), k=3)
    return render_template("recipes.html", recipes=recipes) 


@app.route("/recipes/<fat>_<calories>_<protein>/<recipe_id>") 
def instructions(fat, calories, protein, recipe_id): 
    recipes = main.find_recipes(fat,calories,protein)
    recipes.rewind()

    for recipe in recipes:
        if str(recipe["_id"]) == str(recipe_id):
            return render_template("instructions.html", recipe=recipe)

if __name__ == "__main__":
    app.run(port=5000, debug=True) 