from flask import Flask, request, jsonify
def get_admins():
    return ['Ezra','ezra','1','ADMIN13']
app = Flask(__name__)
@app.route('/main/<room>/<username>', methods=['GET', 'PUT'])
def main(room,username):
    if username in get_admins():
        try:
            rooms=open('rooms.txt','a')
            f=open(f'data_{room}.txt','x')
            rooms.write(room+'\n')
            f.close()
            rooms.close()
            f.close()
        except:
            pass
    else:
        print('Username not found in ADMINS. Please Use rooms already created.')
    if request.method == 'GET':
        username = request.form.get('username')
        data=open(f'data_{room}.txt','r').read()
        if data is None:
            data="nothing"
        return f'{username}:{data}'
    if request.method == 'PUT':
        data = request.form.get('data')
        username = request.form.get('username')
        f=open(f'data_{room}.txt','a')
        f.write(username+":"+data+"\n")
        f.close()
        return (f'{username}:{data}')

app.run('0.0.0.0',debug=True)