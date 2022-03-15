import os
from flask import Flask, url_for, redirect, render_template, send_from_directory
import numpy as np
import pandas as pd

# Creating Base Arrays
df = pd.read_csv(os.path.dirname(os.path.abspath(__file__)) +
                 '/assets/projects.csv', index_col=0)
projects_arr = []
for i in range(len(df.index)):
    projects_arr.append([df.iloc[i]['Name'], df.iloc[i]['LinkID'], i])

app = Flask(__name__)

# Creating Pages
# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

# app name
@app.errorhandler(404)
  
# inbuilt function which takes error as parameter
def not_found(e):
  
# defining function
  return render_template("404.html")

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
    df = pd.read_csv(os.path.dirname(os.path.abspath(__file__)) +
                     '/assets/projects.csv', index_col=0)
    projects_arr = []
    for i in range(len(df.index)):
        projects_arr.append([df.iloc[i]['Name'], df.iloc[i]['LinkID'], i])
    return render_template('allprojects.html', project_list=projects_arr)

@app.route("/project/<ind>", methods=['GET', 'POST'])
def project(ind):
    df = pd.read_csv(os.path.dirname(os.path.abspath(__file__)) +
                 '/assets/projects.csv', index_col=0)
    projects_arr = []
    for i in range(len(df.index)):
        projects_arr.append([df.iloc[i]['Name'], df.iloc[i]['LinkID'], i])

    filepath = f"{os.path.dirname(os.path.abspath(__file__))}/static/{df.iloc[i]['File']}"
    with open(filepath, 'r') as f:
        lines = f.read()
        print(lines)
    f.close()
    return render_template('project.html', project_list=projects_arr, ind = int(ind))

if __name__ == "__main__":
    app.run(debug=True)