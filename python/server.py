from flask import Flask, request, redirect
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
from threekingdoms.generals import generals 
from threekingdoms.skills import skills 

googleSheepKey = os.environ['google_sheet_key']
@app.route("/threekingdoms/generals", methods=['GET'])
def threekingdomsGenerals():
    return generals(googleSheepKey)
@app.route("/threekingdoms/skills", methods=['GET'])
def threekingdomsSkills():
    return skills(googleSheepKey)
if __name__ == "__main__":
    app.run()