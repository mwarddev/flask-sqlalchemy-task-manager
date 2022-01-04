from flask import render_template
from taskmanager import app, db
from taskmanger.models import Category, Task

@app.route("/")
def home():
    return render_template("base.html")