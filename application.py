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


# Custom filter
# app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
# app.config["SESSION_FILE_DIR"] = mkdtemp()
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)

# Configure CS50 Library to use SQLite database
# db = SQL("sqlite:///finance.db")
# number_of_users = db.execute("SELECT COUNT() FROM users")
# number_of_users = number_of_users[0]["COUNT()"]
# if number_of_users == 0:
#     number_of_users = 1
# else:
#     number_of_users = number_of_users + 1


# Make sure API key is set
# if not os.environ.get("API_KEY"):
#     raise RuntimeError("API_KEY not set")


@app.route("/", methods=["GET", "POST"])
def index():
    """Show portfolio of stocks"""
    return render_template("index.html")












# def errorhandler(e):
#     """Handle error"""
#     if not isinstance(e, HTTPException):
#         e = InternalServerError()
#     return apology(e.name, e.code)


# # Listen for errors
# for code in default_exceptions:
#     app.errorhandler(code)(errorhandler)