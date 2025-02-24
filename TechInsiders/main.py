
from flask import Flask, jsonify
import json

app = Flask(__name__)
@app.route("/")  # This defines the homepage route
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)

# Load JSON data from file
with open("data.json", "r") as file:
    data = json.load(file)

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(data["users"])  # Sends the users as JSON

@app.route("/categories", methods=["GET"])
def get_categories():
    return jsonify(data["categories"])  # Sends categories as JSON

@app.route("/progress", methods=["GET"])
def get_progress():
    return jsonify(data["progress"])  # Sends progress as JSON

@app.route("/history", methods=["GET"])
def get_history():
    return jsonify(data["history"])  # Sends history as JSON

if __name__ == "__main__":
    app.run(debug=True)


'''
import json

with open("data.json", "r") as file:
    data = json.load(file)  # Loads JSON as a Python dictionary

print(data["users"])  # Accessing user data
'''
