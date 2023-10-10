from flask import Flask
from markupsafe import escape
app = Flask(__name__)
@app.route("/<name>")
def hello(name):
  return "<p>Hello, {escape(name)}!</p>"
