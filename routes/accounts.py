from flask import Blueprint, request, jsonify
from models import db, User, Transaction

bp = Blueprint("accounts", __name__, url_prefix="/accounts")

@bp.route("/balance/<int:user_id>", methods=["GET"])
def balance(user_id):
    user = User.query.get(user_id)
    return jsonify({"balance": user.balance})

@bp.route("/deposit", methods=["POST"])
def deposit():
    data = request.json
    user = User.query.get(data["user_id"])
    user.balance += data["amount"]
    txn = Transaction(user_id=user.id, type="deposit", amount=data["amount"])
    db.session.add(txn)
    db.session.commit()
    return jsonify({"message": "Deposit successful", "balance": user.balance})
