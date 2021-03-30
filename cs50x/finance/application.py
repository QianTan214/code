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

    # get username
    username = db.execute("select username from users where id = :user_id", user_id = session["user_id"])[0]["username"]

    # get user's portfolio
    rows = db.execute("select * from portfolio where username = :username", username = username)

    total_stock_value = 0

    for row in rows:
        symbol = row["symbol"]
        shares = row["shares"]
        shares = int(shares)
        price = lookup(symbol)["price"]
        each_stock_value = shares * price
        total_stock_value = total_stock_value + each_stock_value

    # get user's cash balance from users database
    cash_balance = db.execute("select cash from users where username = :username", username = username])[0]["cash"]

    # user's grand total
    total_money = cash_balance + total_stock_value

    return render_template("index.html", symbol = symbol, shares = shares, each_stock_value = each_stock_value, total_stock_value = total_stock_value)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        input_symbol = request.form.get("symbol")
        input_shares = request.form.get("shares")

        if not input_symbol or not lookup(input_symbol):
            return apology("stock not found", 403)

        if not input_shares or not input_shares.isdigit() or int(input_shares) <= 0:
            return apology("number of shares must be a positive integer", 403)

        price = lookup(symbol)["price"]
        total_price = price * int(shares)

        rows = db.execute("select * from users where id = ?", session["user_id"]) # session["user_id"] is integer
        cash_balance = rows[0]["cash"]

        # if user can't afford
        if total_price > cash_balance:
            return apology("insufficient cash to buy the number of shares entered", 403)

        username = db.execute("select username from users where id = :user_id", user_id = session["user_id"])[0]["username"]

        # if user can afford, add transaction into history database
        db.execute("insert into history (username, symbol, price, shares, operation) values (:username, :symbol, :price, :shares, "BUY")",
            username = username,
            symbol = symbol,
            price = price,
            shares = shares)

        # add stock to user's portfolio database
        db.execute("insert into portfolio (username, symbol, shares) values (:username, :symbol, :shares)",
            username = username,
            symbol = input_symbol,
            shares = int(input_shares))

        cash_balance = cash_balance - total_price

        # update user's cash balance in users database
        db.execute("update users set cash = :cash where id = :user_id", cash = cash_balance, user_id = session[user_id])

        return redirect("/")

    else:
        return render_template("/buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    stock_bought =
    return apology("TODO")


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

    if request.method == "POST":
        input_symbol = request.form.get("symbol")

        if not input_symbol or not lookup(input_symbol):
            return apology("stock not found", 403)

        stock = lookup(input_symbol)

        return render_template("/quote.html", stock = stock)

    else:
        return render_template("/quote.html", stock = "")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        input_username = request.form.get("username")
        input_password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # check username
        if not input_username:
            return apology("must provide username", 403)

        rows = db.execute("select * from user where username = ?", input_username)

        if len(rows) != 0:
            return apology("username already exists", 403)

        # check password
        if not input_password:
            return apology("must provide password", 403)

        # double check password
        if input_password != confirmation:
            return apology("passwords do not match, please re-enter", 403)

        # add a new user to users database
        db.execute("insert into users (username, hash) values (?, ?)", input_username, generate_password_hash(input_password))

        # return to login page
        return render_template("/login.html")

    else:
        return render_template("/register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "POST":
        input_symbol = request.form.get("symbol")
        input_shares = request.form.get("shares")

        if not input_symbol or not lookup(input_symbol):
            return apology("stock not found", 403)

        if not input_shares or not input_shares.isdigit() or int(input_shares) <= 0:
            return apology("number of shares must be a positive integer", 403)

        # get username
        username = db.execute("select username from users where id = :user_id",
            user_id = session["user_id"])[0]["username"]

        # check shares of a stock in portfolio database
        total_shares = db.execute("select shares from portfolio where username = :username and symbol = :symbol",
            username = username,
            symbol = symbol)

        # check if user has the stock and if user sells more than he owns
        if not total_stocks or total_stocks[0]["shares"] < input_shares:
            return apology("insufficient shares to sell", 403)

        # add selling transaction in history database
        db.execute("insert into history (username, symbol, price, shares, operation) values (:username, :symbol, :price, :shares, "SELL")",
            username = username,
            symbol = input_symbol,
            price = lookup(symbol)["price"],
            shares = int(input_shares))

        # money earned by selling a stock
        money_earned = int(input_shares) * lookup(symbol)["price"]

        # check user's current cash balance
        cash_balance = db.execute("select cash from users where id = :user_id", user_id = session["user_id"])[0]["cash"]

        # user's cash balance after selling a stock
        cash_balance = cash_balance + money_earned

        # update user's cash in users database
        db.execute("update users set cash = :cash where id = :user_id",
            cash = cash_balance,
            user_id = session["user_id"])

        # user's new shares of a stock after selling
        new_shares = total_shares[0]["shares"] - int(input_shares)

        # update user's portfolio in portfolio database
        db.execute("update portfolio set shares = :shares where username = :username",
            shares = new_shares,
            username = username)

        # flash user the selling alert
        flash(f"Sold {input_shares} of shares of {input_symbol}")

        # redirect user to homepage
        return redirect("/")

    else:
        return render_template("sell.html")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
