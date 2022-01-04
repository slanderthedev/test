from logging import debug
from flask import Flask
import os, re, json, random, platform, socket, uuid, requests
import main.py

app =  Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    
    return "Penis"


if __name__ == '__main__':
    app.run(debug=True, port=5001)