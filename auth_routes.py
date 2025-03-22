from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models import register_user, get_user_by_email
import bcrypt

auth = Blueprint("auth", __name__)

# Register Route
@auth.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    response = register_user(data["username"], data["email"], data["password"], data.get("role", "user"))
    return jsonify(response), 201

# Login Route
@auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = get_user_by_email(data["email"])

    if not user or not bcrypt.checkpw(data["password"].encode('utf-8'), user["password"].encode('utf-8')):
        return jsonify({"error": "Invalid credentials"}), 401

    # 🚨 Ensure user ID is present & string
    if not user.get("id"):
        return jsonify({"error": "User ID is missing"}), 400

    user_id = str(user["id"])  # 🔥 Convert to string
    user_role = str(user["role"])

    # 🔍 Debugging: Print values before JWT creation
    print(f"User ID: {user_id} (Type: {type(user_id)})")
    print(f"User Role: {user['role']}")

    # ✅ Create JWT Token
    access_token = create_access_token(identity=user_id, additional_claims={"role": user["role"]})

    return jsonify({"token": access_token})
