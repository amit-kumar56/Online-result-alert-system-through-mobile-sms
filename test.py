from flask import Flask,render_template,request,redirect,flash,url_for
from flask import jsonify

app = Flask(__name__)
@app.route('/api/add ', methods = ['POST','GET'])
def print_list():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    result=a+b
    return jsonify({'sum':result})

@app.route('/person/')
def hello():
    return jsonify({'name':'Jimit',
                    'address':'India'})

if __name__ == '__main__' :
    app.run(debug=True)