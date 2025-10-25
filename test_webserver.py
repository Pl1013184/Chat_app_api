from flask import Flask, request, jsonify,render_template
app = Flask(__name__)
@app.route('/')
def index():
@app.route('/<user>')
def chat():
@app.route('/<user>/<room>')
def chats(username):
    return render_template('main.html')
app.run()