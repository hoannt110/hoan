from flask import Flask, render_template, redirect, request

bikeapp = Flask(__name__)
allbike = [
    { 
    "model": "Honda dream",
    "price": "20000",
    "image": "",
    "year" : "1999"
    },
]

@bikeapp.route("/")
def home():
    return render_template("allfood.html")

@bikeapp.route('/add_bike', methods=["GET","POST"])
def add_bike():
    if request.method == "GET":
        return render_template("add_bike.html")
    elif request.method == "POST":
        form = request.form
        model = form["model"]
        price = form["price"]
        image = form["image"]
        year = form["year"]
        newbike = {
            "model": model,
            "price" : price,
            "image": image,
            "year": year,
        }
        allbike.append(newbike)
        return render_template("add_bike.html")