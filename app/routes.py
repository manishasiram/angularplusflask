from app import app
from flask import render_template
from app.models import User
from flask import jsonify,request

@app.route("/hello", methods=['GET', 'POST'] )
def hello():
    print("I was here")
    return jsonify({'text':'Hello World!'})
    
@app.route('/')
@app.route('/index',methods=['GET','POST'])

def index():
    data=[]
    user = User.query.get(2)
    # for user in users:
    data.append({'username':user.username,'email':user.email})
    return jsonify(data)


@app.route('/login', methods=['GET','POST'])
def login():
    data1=[]
    values=request.json
    print(values['username'])
    users= User.query.all()
    index=0
    for user in users:
        data1.append({'username':user.username,'email':user.email})
        
        if(values['username'] == data1[index]['username'] and values['email']==data1[index]['email']):
            print "successful"
            break
        

    

    return jsonify({'status': 'ok'})
    




