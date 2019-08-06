from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def add():
    if request.method == 'get':
        data = request.data.decode('utf-8')
        data = json.loads(data)
        with open('test.json', 'w') as f:
        	json.dump(data, f, indent=4)
    else:
        return "hello world"