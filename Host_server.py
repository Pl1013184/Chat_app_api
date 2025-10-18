from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/main/<room>', methods=['GET', 'POST'])
def main(room):
    try:
        f=open(f'data_{room}.txt','x')
        f.close()
    except:
        pass
    if request.method == 'GET':
        username = request.form.get('username')
        data=open(f'data_{room}.txt','r').read()
        if data is None:
            data="nothing"
        return f'{username}:{data}'
    if request.method == 'POST':
        data = request.form.get('data')
        username = request.form.get('username')
        f=open(f'data_{room}.txt','a')
        f.write(username+":"+data+"\n")
        f.close()
        return (f'{username}:{data}')

app.run('0.0.0.0',debug=True)