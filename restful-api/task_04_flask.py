#!/usr/bin/python3
"""
This module provides a simple RESTful API using Flask
to manage a collection of users.
"""

from flask import Flask, jsonify, request


app = Flask(__name__)
users = {}


@app.route('/')
def home():
    """
    Handle the home route of the Flask API.
    """
    return "Welcome to the Flask API!"


@app.route('/status')
def get_status():
    """
    Returns the status of the application.
    """
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """
    Retrieve user information based on the provided username.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/data')
def get_all_users():
    """Returns a list of all usernames stored in the API."""
    return jsonify(list(users.keys()))


@app.route("/add_user", methods=["POST"])
def post_user():
    """
    Add a new user to the users dictionary.
    """
    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    users[username] = data
    return jsonify({"message": "User added",
                    "user": data
                    }), 201

    return jsonify({"error": "Request must be JSON"}), 400


if __name__ == "__main__":
    app.run()
