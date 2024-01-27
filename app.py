from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
#to pass info render_template('index.html, info="Hello")

@app.route('/<name>')
def home(name):
    return f"chat with {name}"

if __name__ == '__main__':
    app.run(debug=True)