#!/usr/bin/python3
from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

DATA_FILE = "users.json"


def load_users():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}


def save_users():
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)


users = load_users()


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))


@app.route("/status")
def get_status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    username = data["username"]

    users[username] = data
    save_users()

    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
