from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    return render_template('index.html')
#to pass info render_template('index.html, info="Hello")

@app.route('/<name>')
def chat(name):
    return f"chat with {name}"

if __name__ == '__main__':
    app.run(debug=True)