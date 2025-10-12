import requests
from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/main/<username>', methods=['GET', 'POST'])
def main(username):
    global data
    if request.method == 'GET':
        return f'{username}:{data}'
    if request.method == 'POST':
        data = request.form.get('data')
        return (f'{username}:{data}')

app.run('0.0.0.0',debug=True)