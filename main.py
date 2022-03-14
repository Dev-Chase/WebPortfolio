import os
from flask import Flask, url_for, redirect, render_template, send_from_directory
import numpy as np
import pandas as pd

# Creating Base Arrays
df = pd.read_csv('./assets/projects.csv', index_col=0)
projects_arr = []
for i in range(len(df.index)):
    projects_arr.append([df.iloc[i]['Name'], df.iloc[i]['LinkID'], i])

app = Flask(__name__)

# Creating Pages
# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

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