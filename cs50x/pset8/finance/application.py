# set API key before flask run command
# export API_KEY=pk_cabbb321a2474545a8e70011c0746a0d 

import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

from datetime import datetime

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required 
def index():
    """Show portfolio of stocks"""
    
    # get stock symbol and shares owned by a particular user from database
    stocks = db.execute("select stock_symbol, owned_shares from portfolio \
        where user_id = :user_id order by stock_symbol desc",
        user_id = session["user_id"])

    # if no stocks in portfolio table, render index.html with a message
    if not stocks:
        return render_template("index.html", message = "Your stock portfolio is empty")

    # set total value of stocks at 0
    total = 0

    # loop through each row in portfolio table in database
    for stock in stocks:
        symbol = stock["stock_symbol"]
        stock = lookup(symbol)
        stock_name = stock["name"]
        owned_shares = stock["owned_shares"]
        stock_price = lookup(symbol)["price"]
        total = total + stock_price * owned_shares


    # get user's balance in users table in database
    user_balance = db.execute("select cash from users where user_id = :user_id",
        user_id = session["user_id"])[0]["cash"]

    # stock value plus user balance
    grand_total = user_balance + total

    # update portfolio table
    updated_stocks = db.execute("select * from portfolio where user_id = :user_id",
        user_id = session["user_id"])

    # render index.html homepage
    return render_template("index.html", stocks = updated_stocks, user_balance = usd(user_balance),\
        grand_total = usd(grand_total))




@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # POST method to access URL
    if request.method == "POST":
        symbol = request.form["symbol"]
        stock = lookup(symbol)
        if not stock:
            return apology("stock not found", 403)

        # number of share user inputs in the form
        num_shares = request.form["shares"]
        num_shares = int(num_shares)
        if num_shares <= 0:
            return apology("number of shares must be a positive integer", 403)
        
        # get current price for the stock
        current_price = stock["price"]

        # total money needed
        total_amount = num_shares * current_price

        # check user's balance in database
        user_balance = db.execute("select cash from users where id = :user_id", 
            user_id = session["user_id"])[0]["cash"] # returns a list of dict objects

        # check if user can afford
        if user_balance - total_amount < 0:
            return apology("you don't have enough balance for this transaction", 403)

        # insert transaction into transactions table in database
        db.execute("insert into transactions (user_id, stock_symbol, num_shares,\
            stock_price) values (:user_id, :stock_symbol, :num_shares, :stock_price)", 
            user_id = session["user_id"],
            stock_symbol = symbol,
            num_shares = num_shares,
            stock_price = current_price,
            # time = datetime.now()
        )
        
        # user's new balance after purchase
        user_new_balance = user_balance - total_amount
        
        # update user's balance in users table
        db.execute("update users set cash = :balance where id = :user_id", 
            user_id = session["user_id"],
            balance = user_new_balance)

        # check whether the wanted stock is in portfolio table
        stock_exists = db.execute("select owned_shares from portfolio where user_id = :user_id and stock_symbol = :stock_symbol", 
            user_id = session["user_id"], stock_symbol = symbol)

        # if stock exists, update portfolio table
        if stock_exists:
            owned_shares = owned_shares + stock_exists[0]["owned_shares"]
            db.execute("update portfolio set owned_shares = :owned_shares where user_id = :user_id and \
                stock_symbol = :stock_symbol", 
                user_id = session["user_id"], 
                stock_symbol = symbol,
                owned_shares = owned_shares)


        # if stock not exists, insert it into portfolio table in database
        else:
            db.execute("insert into portfolio (user_id, stock_symbol, owned_shares) \
                values (:user_id, :stock_symbol, :owned_shares)",
                user_id = session["user_id"],
                stock_symbol = symbol,
                owned_shares = num_shares)

        # redirect user to index page with a purchase success message
        flash(f"{num_shares} shares of {lookup(symbol)} successfully bought.")
        return redirect("/")


    # GET method to access URL
    return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    history = db.execute("select * from transactions where user_id = :user_id",
        user_id = session["user_id"])

    return render_template("history.html", history = history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # POST method to access URL
    if request.method == "POST":
        symbol = request.form["symbol"]
        stock = lookup(symbol)
        if not stock:
            return apology("stock not found", 403)
        return render_template("quote.html", stock = stock)

    # GET method to access URL
    return render_template("quote.html") # can add stock = "" in ()
        


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        if not request.form["username"]:
            return apology("username cannot be blank", 403)
        elif db.execute("select * from users where username = :username", username = \
            request.form["username"]):
            return apology("username already exists", 403)
        elif not request.form["password"] or not request.form["confirmation"] or \
            request.form["password"] != request.form["confirmation"]:
            return apology("password cannot be blank or passwords must match", 403)
        pwd = generate_password_hash(request.form["password"])
        db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)", username = request.form["username"], hash = pwd)
        return redirect("/login")
    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    # POST method to access URL
    if request.method == "POST":
        symbol = request.form["symbol"]
        stock = lookup(symbol)
        if not stock:
            return apology("Please select a stock or stocks not found", 403)
        
        # number of shares user inputs in the form
        num_shares = request.form["shares"]
        num_shares = int(num_shares)
        if num_shares <= 0:
            return apology("number of shares must be a positive integer", 403)

        # check how many wanted_to_sell stocks does user own in database
        owned_shares = db.execute("select owned_shares from portfolio where user_id = :user_id \
            and stock_symbol = :stock_symbol",
            user_id = session["user_id"], stock_symbol = symbol)[0]["owned_shares"] # returns a list of dict objects
        
        # if user doesn't have enough stocks to sell 
        if owned_shares < num_shares:
            return apology("shares you want to sell exceed the number you own", 403)

        # get current price for the stock
        current_price = stock["price"]

        # total money earned after selling
        total_amount = num_shares * current_price

        # insert transaction into transactions table in database
        db.execute("insert into transactions (user_id, stock_symbol, num_shares, stock_price) \
            values (:user_id, :stock_symbol, :num_shares, :stock_price)",
            user_id = session["user_id"],
            stock_symbol = symbol,
            num_shares = - num_shares, # negative means selling stocks
            stock_price = current_price)

        # user's balance before selling
        user_balance = db.execute("select cash from users where user_id = :user_id",
            user_id = session["user_id"])[0]["cash"]

        # user's new balance after selling
        user_new_balance = user_balance + total_amount

        # update user's balance in users table in database
        db.execute("update users set cash = :balance where id = :user_id",
            user_id = session["user_id"],
            balance = user_new_balance)

        # user's new owned_shares after selling
        new_owned_shares = owned_shares - num_shares

        # update portfolio table in database
        db.execute("update portfolio set owned_shares = :new_owned_shares where id = :user_id \
            and stock_symbol = :stock_symbol",
            user_id = session["user_id"],
            stock_symbol = symbol,
            new_owned_shares = new_owned_shares)

        # redirect user to index page with a selling success message
        flash(f"{num_shares} shares of {lookup(symbol)} successfully sold.")
        return redirect("/")

    # GET method to access URL
    return render_template("sell.html")



def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
