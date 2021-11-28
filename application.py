import os

# from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
# from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

# from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
# app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

def final_output(price, km_driven,  no_of_owners ,age, diesel, petrol, seller_type_individual,transmission_manual):
    # importing libraries
    import pickle
    import numpy as np
    from joblib import load
    input_parameters = [[price, km_driven,  no_of_owners ,age, diesel, petrol, seller_type_individual, transmission_manual]]
    sc = load('scaler_model')

    ip = np.array(input_parameters)
    input_parameters_scaled = sc.transform(ip)

    with open('random_forest_regression_model.pkl', 'rb') as file:
        predictor = pickle.load(file)
    result = predictor.predict(input_parameters_scaled)
    return result




@app.route("/", methods=["GET", "POST"])
def index():
    """Show portfolio of stocks"""
    return render_template("index.html")

@app.route("/submit", methods=["GET","POST"])
def submit():
    """gets data from user, feeds it into the model to get prediction"""
    if request.method == "POST":
        # print(request.form)
        year = int(request.form.get('year'))
        age = 2021 - year
        km_driven = int(request.form.get('km_driven'))
        price = float(request.form.get('price'))
        no_of_owners = int(request.form.get('no_of_owners'))
        petrol = 0
        diesel = 0
        transmission = request.form.get('transmission')
        if transmission == "on":
            transmission_manual = 0
        else:
            transmission_manual = 1
        seller_type = request.form.get('buyer_kind')
        if seller_type == 'dealer':
            seller_type_individual = 0
        else:
            seller_type_individual = 1
        fuel = ['petrol','diesel','cng']
        if request.form.get(fuel[0]) == 'on':
            petrol = 1
            diesel = 0
            # fuel_type = fuel[0]
        if request.form.get(fuel[1]) == 'on':
            petrol = 0
            diesel = 1
            # fuel_type = fuel[1]
        if request.form.get(fuel[2]) == 'on':
            petrol = 0
            diesel = 0
            # fuel_type = fuel[2]
        output = final_output(price, km_driven,  no_of_owners ,age, diesel, petrol, seller_type_individual, transmission_manual)
        return f"{output}"


    
     
        

    # print(request.form["car"])
    return "<h1>Hello</h1>"







# ImmutableMultiDict([('year', '2019'), ('price', '14.22'), ('price_in_lakh', '49000'), ('petrol', 'on'), ('switch', 'on')])
