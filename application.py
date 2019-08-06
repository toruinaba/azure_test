from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def add():
    data = "hello world"
    if request.method == 'post':
        data = request.data.decode('utf-8')
        data = json.loads(data)
        print(data)
        with open('test.json', 'w') as f:
        	json.dump(data, f, indent=4)
    else:
        return str(data)