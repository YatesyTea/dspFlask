from main import main
from flask import Flask, render_template, redirect, request, url_for
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired



app = Flask(__name__)
app.config['SECRET_KEY'] = "secret_key"

# form for user to input their preferences 
class DietaryForm(FlaskForm):
    fat = IntegerField("How many grams of fat would you like to consume per day?", validators=[DataRequired()])
    calories = IntegerField("How many calories would you like to consume per day?", validators=[DataRequired()])
    protein = IntegerField("How much protein would to consumer per day?", validators=[DataRequired()])
    submit = SubmitField("Submit")
    

# homepage, displays the form asks user for input
@app.route("/", methods=["GET", "POST"])
def index():
    print("homepage loaded")
    form = DietaryForm(request.form)
    message = "Please fill out this form with your dietary requirements, so we can find you some awesome recipes!"

    if request.method == "POST":
        print("post method")
        fat = form.fat.data
        calories = form.calories.data
        protein = form.protein.data

        recipes = main(fat,calories,protein)

        form.fat.data = ""
        form.calories.data = ""
        form.protein.data = ""

        message = "Thank you. You will now be redirected to your bespoke recipe recommendations" 

        return redirect(url_for("recipes"), recipes=recipes)
    return render_template("index.html", form=form, message=message)


@app.route("/my_recipes")
def recipes():
    print("i'm showing recipes")
    # return render_template('my_recipes.html', recipes=recipes)

if __name__ == "__main__":
    app.run()