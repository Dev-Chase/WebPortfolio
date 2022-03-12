from flask import Flask, url_for, redirect, render_template

app = Flask(__name__)

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
    return render_template('allprojects.html')

@app.route("/project/<name>", methods=['GET', 'POST'])
def project(name):
    return render_template('project.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)