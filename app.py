#this is maya's attempt at a summer project
from flask import Flask, jsonify, request
from random import randint 
from flask_cors import CORS 
import json 
import os 

app = Flask(__name__)
CORS(app, origins=["https://deft-mooncake-094a90.netlify.app"])

#users = {}
USERS_FILE = 'users.json'

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f)

logicwordpuzzles = [
    {
        "question": "I am taken from a mine and shut up in a wooden case, from which I am never released, and yet I am used by almost everybody. What am I?",
        "answers": ["pencil lead", "graphite"]
    },
    {
        "question": "A man stands on one side of a river, his dog on the other. The man calls his dog, who immediately crosses the river without getting wet and without using a bridge or a boat. How did the dog do it?",
        "answers": ["the river was frozen", "frozen river", "ice"]
    },
    {
        "question": "Turn me on my side, and I am everything. Cut me in half, and I am nothing. What am I?",
        "answers": ["eight", "8"]
    }
]

@app.route('/api/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']
    users = load_users() 

    if username in users:
        return jsonify({"error": "User already exists"}), 400
    users[username] = password 
    save_users(users)
    
    return jsonify({
        "message": "User registered successfully",
        "access_token": "fake-jwt-token"
    }), 200

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    users = load_users()

    if username not in users or users[username] != password:
        return jsonify({"error": "Invalid username or password"}), 401

    return jsonify({"message": "Login successful", "username": username}), 200

@app.route("/members")
def members():
    username = request.args.get('username', 'Guest')  # Default to 'Guest' if not provided
    random_index = randint(0, len(logicwordpuzzles) - 1)
    puzzle = logicwordpuzzles[random_index]
    
    return jsonify({
        "message": f"Hello, {username}!",
        "puzzle": puzzle["question"],
        "answers": puzzle["answers"]
    }) 

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)