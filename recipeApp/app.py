import main
from flask import Flask, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

# form for user to input their preferences 
class DietaryForm(FlaskForm):
    fat = IntegerField('How many grams of fat would you like to consume per day?', validators=[DataRequired()])
    calories = IntegerField('How many calories would you like to consume per day?', validators=[DataRequired()])
    protein = IntegerField('How much protein would to consumer per day? ', validators=[DataRequired()])
    submit = SubmitField('Submit')
    

# homepage, displays the form asks user for input
@app.route('/', methods=['GET', 'POST'])
def index():
    form = DietaryForm(request.form)
    message = "Please fill out this form with your dietary requirements, so we can find you some awesome recipes!"

    if request.method == "POST":
    fat = form.fat.data
    calories = form.calories.data
    protein = form.protein.data

    
    form.fat.data = ""
    form.calories.data = ""
    form.protein.data = ""

    message = "Thank you." # can add a hyperlink to the recipes. 
    return render_template('index.html', form=form, message=message)


@application.route("/my_recipes")
def recipes():
    recipes = # from main.py
    return render_template('my_recipes.html', recipes=recipes)