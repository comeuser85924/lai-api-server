from flask import Flask, request, redirect
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
from threekingdoms.generals import generals 
from threekingdoms.skills import skills 

@app.route("/threekingdoms/generals", methods=['GET'])
def threekingdomsGenerals():
    return generals()
@app.route("/threekingdoms/skills", methods=['GET'])
def threekingdomsSkills():
    return skills()
if __name__ == "__main__":
    app.run()