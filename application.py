from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        data = request.data.decode('utf-8')
        data = json.loads(data)
        with open('test.json', 'w') as f:
            json.dump(data, f, indent=4)
        return "complete"
    else:
        with open('test.json', 'r') as f:
            r_data = json.load(f)
        return jsonify(r_data)