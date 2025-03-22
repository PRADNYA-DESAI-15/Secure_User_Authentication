from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from auth_routes import auth
from middleware import jwt_required_role

app = Flask(__name__)
CORS(app)

# Configuration
app.config["JWT_SECRET_KEY"] = "supersecretkey"
jwt = JWTManager(app)

# Register Blueprints
app.register_blueprint(auth, url_prefix="/api/auth")

# Protected Route (Accessible only to logged-in users)
@app.route("/api/profile", methods=["GET"])
@jwt_required_role(["user", "admin"])
def profile():
    return jsonify({"message": "Welcome to your profile!"})

# Admin Route
@app.route("/api/admin", methods=["GET"])
@jwt_required_role(["admin"])
def admin_dashboard():
    return jsonify({"message": "Welcome Admin!"})

if __name__ == "__main__":
    app.run(debug=True)
