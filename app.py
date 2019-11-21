# import necessary libraries
from flask import (
    Flask,
    render_template,
    jsonify,
    request)
from flask_pymongo import PyMongo
import csv
import pandas as pd
import time

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/phone_app_data"
mongo = PyMongo(app)
#jazz = "src/assets/appstore_games.csv"
#df = pd.read_csv(jazz)
#df = df.to_dict(orient = 'records')
app_data = mongo.db.phone_app_data
#app_data.insert_many(df)

@app.route("/")
def home():
    return render_template("index.html", app_data=app_data)

@app.route("/metadata/")
def metadata():
    """Return the MetaData for a given sample."""
    app = app_data.find_one()
    return render_template("metadata.html", app=app)

@app.route("/names")
def names():
    """Return a list of sample names."""
    app = app_data
    cursor = app.find({}).limit(100)
    name_stuff = []
    for document in cursor:
        stuff = {}
        stuff["Name"] = document["Name"]
        stuff["ID"] = document["_id"]
        stuff["Price"] = document["Price"]
        stuff["Age_Rating"] = document["Age_Rating"]
        stuff["Developer"] = document["Developer"]
        name_stuff.append(stuff)
    df_name = pd.DataFrame(name_stuff)
    return jsonify(list(df_name.Name)[1:])

@app.route("/yikes")
def yikes():
    """Return the MetaData for a given sample."""
    app = {}
    for data in app_data.find():
        app["Name"] = data["Name"]
        app["Price"] = data["Price"]
        app["Description"] = data["Description"]
        app["Genre"] = data["Genres"]
        app["Age_Rating"] = data["Age_Rating"]
        app["Developer"] = data["Developer"]
        app["Languages"] = data["Languages"]
        app["Original_Release_Date"] = data["Original_Release_Date"]
        app["Current_Version_Release_Date"] = data["Current_Version_Release_Date"]
    return jsonify(app)

@app.route("/crying")
def crying():
    app = app_data
    cursor = app.find({}).limit(100)
    
    plus_stuff = []
    for document in cursor:
        stuff = {}
        stuff["Name"] = document["Name"]
        stuff["Price"] = document["Price"]
        stuff["Description"] = document["Description"]
        stuff["Genres"] = document["Genres"]
        stuff["Age_Rating"] = document["Age_Rating"]
        stuff["Developer"] = document["Developer"]
        stuff["Languages"] = document["Languages"]
        stuff["Original_Release_Date"] = document["Original_Release_Date"]
        stuff["Current_Version_Release_Date"] = document["Current_Version_Release_Date"]
        plus_stuff.append(stuff)
    return(jsonify(plus_stuff))

@app.route("/yes")
def yes():
    app = app_data
    cursor = app.find({}).limit(15)
    
    plus_stuff = []
    for document in cursor:
        stuff = {}
        stuff["Name"] = document["Name"]
        stuff["Price"] = document["Price"]
        stuff["Description"] = document["Description"]
        stuff["Genres"] = document["Genres"]
        stuff["Age_Rating"] = document["Age_Rating"]
        stuff["Developer"] = document["Developer"]
        stuff["Languages"] = document["Languages"]
        stuff["Original_Release_Date"] = document["Original_Release_Date"]
        stuff["Current_Version_Release_Date"] = document["Current_Version_Release_Date"]
        plus_stuff.append(stuff)
    return  render_template("yes.html", plus_stuff=plus_stuff)

@app.route("/graphs")
def graphing():
    app = app_data
    cursor = app.find({}).limit(100)
    plus_stuff = []
    for document in cursor:
        stuff = {}
        stuff["Name"] = document["Name"]
        stuff["Price"] = document["Price"]
        stuff["Age_Rating"] = document["Age_Rating"]
        plus_stuff.append(stuff)
    df = pd.DataFrame(plus_stuff)
    df_counts = df.count()
    return render_template("graphs.html", df_counts = df_counts)

@app.route("/games/<title>")
def games(title):
    app = app_data
    result = {"Name": "", "Price": 0.0, "Description": "", "Genres": "",
        "Age_Rating": "", "Developer": "", "Languages": "", "Original_Release_Date": "",
         "Current_Version_Release_Date": ""}
    result = app.find({"Name": "title"})
    rip = []
    for results in result:
        sample_metadata = {}
        sample_metadata["Name"] = results["Name"]
        sample_metadata["Price"] = results["Price"]
        sample_metadata["Description"] = results["Description"]
        sample_metadata["Genres"] = results["Genres"]
        sample_metadata["Age_Rating"] = results["Age_Rating"]
        sample_metadata["Developer"] = results["Developer"]
        sample_metadata["Languages"] = results["Languages"]
        sample_metadata["Original_Release_Date"] = results["Original_Release_Date"]
        sample_metadata["Current_Version_Release_Date"] = results["Current_Version_Release_Date"]
        rip.append(sample_metadata)
    return jsonify(rip)

@app.route("/graph_try")
def stuff():
    return render_template("graph_try.html")

if __name__ == "__main__":
    app.run(debug=True)
