from flask import Flask, jsonify, request, send_file, send_from_directory
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
    JWTManager,
    get_jwt,
)
from datetime import timedelta
from flask_mail import Mail
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
from flasgger import Swagger
import os
import bcrypt


# Load variables from .env
load_dotenv()
app = Flask(__name__)
swagger = Swagger(app)
app.config.from_object(__name__)
CORS(app)

# Load database
client = MongoClient(os.getenv("MONGO_URI"))
db = client["ioannisportfolio"]

# Auth
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

jwt = JWTManager(app)

testimonials_collection = db["testimonials"]
projects_collection = db["projects"]
users_collection = db["users"]
print(f"Connected to database {db}")


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data.get("username") or not data.get("password"):
        return jsonify({"message": "Username and password is required"}), 400

    existing_user = users_collection.find_one({"username": data["username"]})
    if existing_user:
        return jsonify({"message": "User already exists"}), 400

    hashed_password = bcrypt.hashpw(data["password"].encode("utf-8"), bcrypt.gensalt())

    # Assign default role "user" to everyone who registers
    role = data.get("role", "user")

    users_collection.insert_one(
        {"username": data["username"], "password": hashed_password, "role": role}
    )

    return jsonify({"message": "User registered successfully"}), 201


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = users_collection.find_one({"username": data["username"]})

    if not user or not bcrypt.checkpw(
        data["password"].encode("utf-8"), user["password"]
    ):
        return jsonify({"message": "Invalid credentials"}), 400

    access_token = create_access_token(
        identity=data["username"], additional_claims={"role": user["role"]}
    )

    return jsonify({"token": access_token}), 200


@app.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    return jsonify({"message": "Logout successfully"}), 200


@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({"message": f"Hello {current_user}, you have access!"}), 200


@app.route("/api/user", methods=["GET"])
@jwt_required()
def get_user_info():
    current_user = get_jwt_identity()
    claims = get_jwt()

    return jsonify(
        {
            "message": "User data fetched",
            "data": {"username": current_user, "role": claims["role"]},
        }
    ), 200


##############
# TESTIMONIALS#
##############


# Get All Testimonials
@app.route("/testimonials", methods=["GET"])
def get_all_testimonials():
    testimonials = list(testimonials_collection.find({}))
    # Convert ObjectId to string for JSON
    for testimonial in testimonials:
        testimonial["_id"] = str(testimonial["_id"])
    return jsonify(testimonials)


# Add a New Testimonial
@app.route("/testimonials", methods=["POST"])
def add_testimonials():
    new_testimonial = request.get_json()
    # Insert the new testimonial into the collection
    new_testimonial["status"] = "hidden"
    testimonials_collection.insert_one(new_testimonial)
    return jsonify({"message": "Testimonial added successfully"}), 201


# Update Testimonial by ID
@app.route("/testimonial/<testimonial_id>", methods=["PUT"])
def update_testimonial(testimonial_id):
    testimonial_id = ObjectId(testimonial_id)
    updated_data = request.get_json()

    # removes '_id' from the request if it exists
    updated_data.pop("_id", None)
    result = testimonials_collection.update_one(
        {"_id": testimonial_id}, {"$set": updated_data}
    )

    if result.matched_count > 0:
        return jsonify(
            {"message": f"Successfully updated testimonial with ID: {testimonial_id}"}
        ), 200
    else:
        return jsonify(
            {"error": f"Failed to update testimonial with ID: {testimonial_id}"}
        ), 404


# Delete testimonial by ID
@app.route("/testimonial/<testimonial_id>", methods=["DELETE"])
def delete_testimonial(testimonial_id):
    testimonial_id = ObjectId(testimonial_id)
    result = testimonials_collection.delete_one({"_id": testimonial_id})

    if result.deleted_count > 0:
        return jsonify(
            {"message": f"Successfully deleted testimonial with {testimonial_id}"}
        ), 200
    else:
        return jsonify(
            {"error": f"Failed to delete testimonial with ID: {testimonial_id}"}
        ), 404


##########
# PROJECTS#
##########


# Get All Projects
@app.route("/projects", methods=["GET"])
def get_all_projects():
    projects = list(
        projects_collection.find({})
    )  # this is a filter. empty means find all

    for project in projects:
        project["_id"] = str(
            project["_id"]
        )  # convert dictionary key to a string. (prepping json)

    return jsonify(projects)


# Get Project by ID
@app.route("/projects/<projectId>", methods=["GET"])
def get_project_by_id(projectId):
    project_id = ObjectId(projectId)
    projects = list(projects_collection.find({"_id": project_id}))

    for project in projects:
        project["_id"] = str(project["_id"])

    return jsonify(projects)


@app.route("/project/<projectId>", methods=["PUT"])
def update_project(projectId):
    project_id = ObjectId(projectId)
    updated_project = request.get_json()

    if not isinstance(updated_project.get("name"), dict):
        name_value = updated_project.get("name", "")
        updated_project["name"] = {"en": name_value, "fr": name_value}

    if not isinstance(updated_project.get("description"), dict):
        desc_value = updated_project.get("description", "")
        updated_project["description"] = {"en": desc_value, "fr": desc_value}

    updated_project.pop("_id", None)

    result = projects_collection.update_one(
        {"_id": project_id}, {"$set": updated_project}
    )

    if result.matched_count > 0:
        return jsonify(
            {"message": f"Successfully updated project with ID: {project_id}"}
        ), 200
    else:
        return jsonify(
            {"error": f"Failed to update project with ID: {project_id}"}
        ), 404


@app.route("/projects", methods=["POST"])
def add_project():
    new_project = request.get_json()

    if not isinstance(new_project.get("name"), dict):
        name_value = new_project.get("name", "")
        new_project["name"] = {"en": name_value, "fr": name_value}

    if not isinstance(new_project.get("description"), dict):
        desc_value = new_project.get("description", "")
        new_project["description"] = {"en": desc_value, "fr": desc_value}

    if "status" not in new_project:
        new_project["status"] = "shown"

    projects_collection.insert_one(new_project)

    return jsonify({"message": "Project added successfully!"}), 200


# Delete project
@app.route("/project/<project_id>", methods=["DELETE"])
def delete_project(project_id):
    project_id = ObjectId(project_id)

    result = projects_collection.delete_one({"_id": project_id})
    if result.deleted_count > 0:
        return jsonify(
            {"message": f"Successfully deleted project with {project_id}"}
        ), 200
    else:
        return jsonify(
            {"error": f"Failed to delete project with ID: {project_id}"}
        ), 404


##########
# Emailing#
##########

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.getenv("GMAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("GMAIL_APP_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.getenv("GMAIL_USERNAME")

mail = Mail(app)


@app.route("/send-email", methods=["POST"])
def send_email():
    data = request.get_json()
    msg = mail.send_message(
        subject=data["subject"],
        sender=app.config["MAIL_DEFAULT_SENDER"],  # Your email
        recipients=[app.config["MAIL_USERNAME"]],  # Your email (I receive the message)
        reply_to=data["sender_email"],  # User's email for replying
        body=f"Message from: {data['sender_email']}\n\n{data['message']}",
    )
    return jsonify({"message": "Email sent successfully!"}), 200


#############
# CV Download#
#############


@app.route("/download-pdf")
def download_CV_pdf():
    try:
        cv_filename = "IoannisPanaritis_CV.pdf"  # Use the new file name
        cv_location = os.path.join("CV", cv_filename)
        print("Serving file:", cv_location)
        return send_from_directory("CV", cv_filename, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Debugging in case of issues


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Use 8080
    app.run(host="0.0.0.0", port=port)
