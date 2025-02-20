
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}, "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}}

@app.route("/")
def home():
    return "Welcome to the Flask API!", 200

@app.route("/data")
def get_data():
    return jsonify([username for username in users]), 200

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    username = data.get("username")
    if not username:
        return jsonify({"error":"Username is required"}), 400
    users[username] = data
    return jsonify({"message": "User added",
        "user": data
        }), 201

@app.route("/users/<username>")
def get_username(username):
    data = users.get(username)
    if data:
        return jsonify(data), 200
    return jsonify({"error": "User not found"}), 404



if __name__ == "__main__":
   app.run()