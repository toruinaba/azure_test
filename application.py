from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def add(): return "hello world"