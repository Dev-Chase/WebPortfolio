from flask import Flask, url_for, redirect, render_template
import numpy as np

# Creating Base Arrays
projects_arr = [
        ["Pythagorean Thereum", "004bd41daf", 0],
        ["Decimal2Binary", "4593ef57f4", 1]
    ]

app = Flask(__name__)

# Creating Pages
@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route("/about", methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

@app.route("/projects", methods=['GET', 'POST'])
def projects():
    return render_template('allprojects.html', project_list=projects_arr)

@app.route("/project/<ind>", methods=['GET', 'POST'])
def project(ind):
    return render_template('project.html', project_list=projects_arr, ind = int(ind))

if __name__ == "__main__":
    app.run(debug=True)