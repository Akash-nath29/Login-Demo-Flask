import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        
        

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get("username")
        email = request.form.get("useremail")
        password = request.form.get("userpassword")
        confirmation = request.form.get("confirmation")
        if password==confirmation:
            newUser = User(username=username, password=password, email=email)
            db.session.add(newUser)
            db.session.commit()
            redirect('/home')
        else:
            return redirect('/')
    return render_template('register.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('userpassword')
        users = User.query.all()
        userList = []
        for user in users:
            userList.append(user.username)
        print(userList)
        if username in userList:
            userPass = User.query.filter_by(username=username).all()
            for userdata in userPass:
                if userdata.password == password:
                    return redirect('/home')
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='80')