from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/greet/<name>")
def greet(name):
    return jsonify(message=f"Hello, {name}!")

app.run()
