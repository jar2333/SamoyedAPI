from flask import Flask

"""
The main application
"""
app = Flask(__name__)

@app.route("/")
def root():
    return "hello world"
