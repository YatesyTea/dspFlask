from main import main
from flask import Flask, render_template, redirect, request, url_for
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__, template_folder="./templates")
app.config['SECRET_KEY'] = "secret_key"

# form for user to input their preferences 
class DietaryForm(FlaskForm):
    fat = IntegerField("How many grams of fat would you like to consume per meal?", validators=[DataRequired()])
    calories = IntegerField("How many calories would you like to consume per meal?", validators=[DataRequired()])
    protein = IntegerField("How much protein would to consume per meal?", validators=[DataRequired()])
    submit = SubmitField("Submit")
    

@app.route("/", methods=["GET", "POST"])
def home():
    form = DietaryForm(request.form)
    message = "Please fill out this form with your dietary requirements, so we can find you some awesome recipes!"

    if request.method == "POST":
        fat = form.fat.data
        calories = form.calories.data
        protein = form.protein.data
        
        recipes = main(fat, calories, protein)
        print("Printing from app.. ")
        print(recipes)
        print(f"type, from app, is {type(recipes)}")

        form.fat.data = ""
        form.calories.data = ""
        form.protein.data = ""

        message = "Thank you. You will now be redirected to your bespoke recipe recommendations" 
        
        return render_template("recipes.html", recipes=recipes)
    
    return render_template("index.html", form=form, message=message)

@app.route("/my_recipes")
def my_recipes(fat, protein, calories):
    recipes = list(main(fat, protein, calories))
    return recipes

if __name__ == "__main__":
    app.run(port=5000, debug=True)