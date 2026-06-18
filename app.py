from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# SQLite Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///loyalty.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Customer Table
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    total_points = db.Column(db.Integer, default=0)


# Transaction Table
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    customer_id = db.Column(
        db.Integer,
        db.ForeignKey("customer.id"),
        nullable=False
    )

    spend = db.Column(db.Float, nullable=False)
    points = db.Column(db.Integer, nullable=False)
    bonus = db.Column(db.Integer, nullable=False)


@app.route("/")
def home():

    customers = Customer.query.all()

    transactions = Transaction.query.order_by(
        Transaction.id.desc()
    ).all()

    return render_template(
        "index.html",
        customers=customers,
        transactions=transactions
    )


@app.route("/add_customer", methods=["POST"])
def add_customer():

    name = request.form["name"].strip()
    email = request.form["email"].strip()

    if not name or not email:
        return redirect("/")

    existing_customer = Customer.query.filter_by(
        email=email
    ).first()

    if existing_customer:
        return redirect("/")

    customer = Customer(
        name=name,
        email=email
    )

    db.session.add(customer)
    db.session.commit()

    return redirect("/")


@app.route("/add_points", methods=["POST"])
def add_points():

    customer_id = request.form["customer_id"]

    try:
        spend = float(request.form["spend"])
    except ValueError:
        return redirect("/")

    if spend <= 0:
        return redirect("/")

    customer = Customer.query.get(customer_id)

    if not customer:
        return redirect("/")

    points = int(spend // 100)

    bonus = 0
    if spend > 5000:
        bonus = 50

    customer.total_points += points + bonus

    transaction = Transaction(
        customer_id=customer.id,
        spend=spend,
        points=points,
        bonus=bonus
    )

    db.session.add(transaction)

    db.session.commit()

    return redirect("/")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)