import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

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

    # check username of the user currently logged in
    username = db.execute("select username from users where id = ?", session["user_id"])[0]["username"]

    # check what stocks the user owns
    user_portfolio = db.execute("select symbol, shares from portfolio where username = ? order by symbol desc", username)

    # check if user has portfolio, pass in parameter message
    if not user_portfolio:
        return render_template("index.html", message="Your portfolio is empty.")

    total = 0

    # loop through user_portfolio
    for portfolio in user_portfolio:
        symbol = portfolio["symbol"]
        stock_company = lookup(symbol)["name"]
        shares = portfolio["shares"]
        current_price = lookup(symbol)["price"]
        total_value = shares * current_price
        total = total + total_value

    cash_balance = db.execute("select cash from users where id = ?", session["user_id"])[0]["cash"]

    return render_template("index.html", username = username, user_portfolio = user_portfolio, cash_balance = cash_balance, total = total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":
        input_symbol = request.form.get("symbol")
        input_shares = request.form.get("shares")

        if not input_symbol or not lookup(input_symbol):
            return apology("stock not found", 400)

        if not input_shares or int(input_shares) <= 0:
            return apology("number of shares must be a positive integer", 400)

        stock = lookup(input_symbol)

        # get current price of a stock, not stock[0]["price"]
        current_price = stock["price"]

        # caculate total price needed
        total_price = current_price * int(input_shares)

        # check user's cash balance in users table
        cash_balance = db.execute("select cash from users where id = ?", session["user_id"])[0]["cash"]

        # error message if user can't afford
        if cash_balance < total_price:
            return apology("you don't have enough money to buy the shares", 403)

        # new user's cash balance after buying
        new_cash_balance = cash_balance - total_price

        # insert transaction into history table
        username = db.execute("select * from users where id = ?", session["user_id"])[0]["username"]

        db.execute("insert into history (username, symbol, price, shares, operation) values (?, ?, ?, ?, ?)",
            username, input_symbol, current_price, input_shares, "BUY")

        # update user's cash balance in users table
        db.execute("update users set cash = ? where id = ?", new_cash_balance, session["user_id"])

        # check if user has shares of a particular stock before buying
        # no [0]["shares"] follows after, will cause index out of range
        shares_owned_before = db.execute("select shares from portfolio where username = ? and symbol = ?", username, input_symbol)

        # if user doesn't have this particular stock before buying, insert into portfolio table
        if not shares_owned_before:
            db.execute("insert into portfolio (symbol, shares, username) values (?, ?, ?)", input_symbol, input_shares, username)

        # if user already has this stock before buying
        else:
            shares_owned_after = shares_owned_before[0]["shares"] + int(input_shares)

            # update user's portfolio in portfolio table
            db.execute("update portfolio set shares = ? where symbol = ? and username = ?",
                shares_owned_after, input_symbol, username)

        # get company name
        company_name = lookup(input_symbol)["name"]

        # flash user with successfully buy message
        # flash is like print in python, use {}
        flash(f"Bought {input_shares} share(s) of {company_name} ({input_symbol}) successfully!")

        # redirect user to homepage
        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    # get username of the user currently logged in
    username = db.execute("select username from users where id = ?", session["user_id"])[0]["username"]

    # get all the transactions in history table, "transactions" is a list of dictionaries
    transactions = db.execute("select * from history where username = ?", username)

    # pass transactions into history.html page
    return render_template("history.html", transactions = transactions)


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
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

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

    # "POST" has to be capital letters
    if request.method == "POST":
        input_symbol = request.form.get("symbol")

        if not input_symbol or not lookup(input_symbol):
            return apology("stock not found", 400)

        stock = lookup(input_symbol)

        return render_template("quote.html", stock = stock)

    else:
        return render_template("quote.html", stock ="")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # if method of request is "POST"
    if request.method == "POST":
        input_username = request.form.get("username")
        input_password = request.form.get("password")
        input_confirmation = request.form.get("confirmation")

        # check username
        if not input_username:
            return apology("must provide username", 400)

        rows = db.execute("select * from users where username = ?", input_username)

        if len(rows) != 0:
            return apology("username already exists", 400)

        # check password
        if not input_password:
            return apology("must provide password", 400)

        # double check password
        if input_password != input_confirmation:
            return apology("passwords do not match, please re-enter", 400)

        # add a new user to users table
        db.execute("insert into users (username, hash) values (?, ?)", input_username, generate_password_hash(input_password))

        # return to login page
        return render_template("login.html")

    # if method of request is "GET"
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    # get username of the user currently logged in
    username = db.execute("select username from users where id = ?", session["user_id"])[0]["username"]

    # check what stock symbols user has
    symbols = db.execute("select symbol from portfolio where username = ?", username)

    # if method of request is "POST"
    if request.method == "POST":
        input_symbol = request.form.get("symbol")
        input_shares = request.form.get("shares")

        if not input_symbol or not lookup(input_symbol):
            return apology("stock not found", 400)

        if not input_shares or int(input_shares) <= 0:
            return apology("number of shares must be a positive integer", 400)

        # check user's shares of a stock
        shares_owned_before = db.execute("select shares from portfolio where username = ? and symbol = ?", username, input_symbol)

        # check whether user owns this stock or has enough shares of this stock
        if not shares_owned_before or shares_owned_before[0]["shares"] < int(input_shares):
            return apology("you don't have enough shares to sell", 403)

        # shares owned after selling
        shares_owned_after = shares_owned_before[0]["shares"] - int(input_shares)

        # if user has no shares left after selling, delete it in user's portfolio
        if shares_owned_after == 0:
            db.execute("delete from portfolio where symbol = ? and username = ?", input_symbol, username)

        # if user has shares left after selling, update user's portfolio
        db.execute("update portfolio set shares = ? where username = ? and symbol = ?", shares_owned_after, username, input_symbol)

        # check current price of the stock
        current_price = lookup(input_symbol)["price"]

        # money earned after selling
        money_earned = current_price * int(input_shares)

        # check user's cash balance
        cash_balance = db.execute("select cash from users where id = ?", session["user_id"])[0]["cash"]

        # user's new cash balance after selling
        new_cash_balance = cash_balance + money_earned

        # update user's cash balance after selling
        db.execute("update users set cash = ? where id = ?", new_cash_balance, session["user_id"])

        # insert this transaction into history table
        db.execute("insert into history (username, symbol, price, shares, operation) values (?, ?, ?, ?, ?)",
            username, input_symbol, current_price, input_shares, "SELL")

        # get company name
        company_name = lookup(input_symbol)["name"]

        # flash user with successfully sold message
        # flash is like print in python, use {}
        flash(f"Sold {input_shares} share(s) of {company_name} ({input_symbol}) successfully!")

        # redirect user to homepage
        return redirect("/")

    # if method of request is "GET"
    # symbols defined on top, it is a list of dictionaries
    # pass symbols into sell.html page
    else:
        return render_template("sell.html", symbols = symbols)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
