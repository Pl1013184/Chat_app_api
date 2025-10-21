from flask import Flask, request, jsonify,render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('main.html')
app.run()