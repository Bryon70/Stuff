from flask import Blueprint, request, jsonify
from models import db, User

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/signup", methods=["POST"])
def signup():
    data = request.json
    user = User(
        name=data["name"],
        national_id=data["national_id"],
        phone_number=data["phone_number"]
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "Signup successful!"}), 201

@bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(phone_number=data["phone_number"]).first()
    if user:
        return jsonify({"message": "Login successful!"})
    return jsonify({"error": "User not found"}), 404

