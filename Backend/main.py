from flask import Flask,jsonify,request
from flask_mail import Mail
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os


# Load variables from .env
load_dotenv()
app = Flask(__name__)
app.config.from_object(__name__)
CORS(app) # allow all for now



# Load database
client = MongoClient(os.getenv("MONGO_URI")) 
db = client["ioannisportfolio"] 

testimonials_collection = db["testimonials"]
projects_collection = db["projects"]
print(f"Connected to database {db}")



@app.route("/", methods=['GET'])
def greetings():
    return("Hello world")

##############            
#TESTIMONIALS#
##############

# Get All Testimonials
@app.route("/testimonials", methods=["GET"])
def get_all_testimonials():
    testimonials = list(testimonials_collection.find({}))
    # Convert ObjectId to string for JSON
    for testimonial in testimonials:
        testimonial['_id'] = str(testimonial['_id'])
    return jsonify(testimonials)


# Add a New Testimonial
@app.route("/testimonials", methods=['POST'])
def add_testimonials():
    new_testimonial = request.get_json()
    # Insert the new testimonial into the collection
    testimonials_collection.insert_one(new_testimonial)
    return jsonify({"message": "Testimonial added successfully"}), 201


# Delete testimonial by ID
@app.route('/testimonial/<testimonial_id>', methods=['DELETE'])
def delete_testimonial(testimonial_id):
    testimonial_id = ObjectId(testimonial_id)
    result = testimonials_collection.delete_one({"_id": testimonial_id})
    
    if result.deleted_count > 0:
        return jsonify({"message": f"Successfully deleted testimonial with {testimonial_id}"}), 200
    else:
        return jsonify({"error": f"Failed to delete testimonial with ID: {testimonial_id}"}), 404
    

##########            
#PROJECTS#
##########

# Get All Projects
@app.route('/projects', methods=['GET'])
def get_all_projects():
    projects = list(projects_collection.find({})) #this is a filter. empty means find all
    
    for project in projects:
        project["_id"] = str(project["_id"]) # convert dictionary key to a string. (prepping json)
        
    return jsonify(projects)



# Add new Project
@app.route('/projects', methods=['POST'])
def add_project():
    new_project = request.get_json()
    projects_collection.insert_one(new_project)
    
    return jsonify({"message" : "Project added successfully!"}), 200


# Delete project
@app.route('/project/<project_id>', methods=['DELETE'])
def delete_project(project_id):
    project_id = ObjectId(project_id)
    
    result = projects_collection.delete_one({"_id": project_id})
    if result.deleted_count > 0:
        return jsonify({"message": f"Successfully deleted project with {project_id}"}), 200
    else:
        return jsonify({"error": f"Failed to delete project with ID: {project_id}"}), 404
        
     
        
##########            
#Emailing#
##########

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('GMAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('GMAIL_APP_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('GMAIL_USERNAME')

mail = Mail(app)
        
        
@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()
    msg = mail.send_message(
        subject=data['subject'],
        sender=app.config['MAIL_DEFAULT_SENDER'],  # Your email
        recipients=[app.config['MAIL_USERNAME']],  # Your email (I receive the message)
        reply_to=data['sender_email'],  # User's email for replying
        body=f"Message from: {data['sender_email']}\n\n{data['message']}"
    )
    return jsonify({"message": "Email sent successfully!"}), 200



if __name__ == "__main__":
    app.run(debug=True)
