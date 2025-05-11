from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity 
import random 

lessons_bp = Blueprint("lessons", __name__)

logicwordpuzzles = [
    {
        "question": "I am taken from a mine and shut up in a wooden case, from which I am never released, and yet I am used by almost everybody. What am I?",
        "hints": ["you put it in something to write with"],
        "answers": ["pencil lead", "graphite"]
    },
    {
        "question": "A man stands on one side of a river, his dog on the other. The man calls his dog, who immediately crosses the river without getting wet and without using a bridge or a boat. How did the dog do it?",
        "hints": ["in winter, things are cold"],
        "answers": ["the river was frozen", "frozen river", "ice"]
    },
    {
        "question": "Turn me on my side, and I am everything. Cut me in half, and I am nothing. What am I?",
        "hints": ["think of a number"],
        "answers": ["eight", "8"]
    },
    {
        "question": "Last week I drove from Aardvark to Beeville. On the first day, I travelled 1/3 of the starting distance."
        "On day two, I travelled 1/2 of the remaining distance. On day three, I travelled 2/3 of the remaining distance. At the end of day four, after"
        "travelling 3/4 of the remaining distance, I was still 5 miles away from Beeville. How many miles had I travelled so far?",
        "hints": ["try working backwards"],
        "answers": ["175 miles", "175", "175mi", "175 mi"]
    }
]

@lessons_bp.route("/", methods=["GET"])
@jwt_required() 
def get_lessons():
    print("Token passed validation.")
    identity = get_jwt_identity()
    print("User ID from token:", identity)
    print("User ID from token:", identity)
    puzzle = random.choice(logicwordpuzzles)
    return jsonify({
        "message": "Solve this puzzle!",
        "puzzle": puzzle["question"],
        "answers": puzzle["answers"]
    })
