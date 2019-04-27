from flask import Flask, render_template, request
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

@app.route("/")

def hello():
    return "<h1>Heroku App</h1>"







