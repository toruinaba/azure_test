from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def add():
    if request.method == 'post':
        data = request.data.decode('utf-8')
        data = json.loads(data)
        print(data)
    else:
        return "hello world"