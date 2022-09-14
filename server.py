from flask import Flask, render_template, request
from flask import Flask
from os import path
from flask_login import LoginManager, login_required
from flask_sqlalchemy import SQLAlchemy
from bs4 import BeautifulSoup as Soup
import urllib
from keyboard import press
from formats import homePageFormat, homePageFormat1
from functions import addColorToClass, addToCss, p1, b1, i1, img1, li1, br1, bodyStart, bodyStop, title1, h1, em1, u1, a1, small1, strike1, ol1, comment1, center1, div1, div2, divColor, inputElem, createButton, font1, link1, hr1, meta1, tableStart, tableStop, trStart, trStop, th1, td1, formAction, formActionMethod, formStop, input1, option1, optionSelected1, sendToHtml, deleteHtmlTxt, changeNav2, deleteCssTxt, tagElem, profile
from pages import homePage
from werkzeug.datastructures import ImmutableMultiDict
from flask_login import LoginManager
login_manager = LoginManager()
from flask_login import LoginManager
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
import os
from flask_bcrypt import Bcrypt
from pages import homePage
from flask import request

app = Flask(__name__)
db = SQLAlchemy(app)
SECRET_KEY = os.urandom(32)
bcrypt = Bcrypt(app)
count = 0

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    html = db.Column(db.String(100000), default='')
    def get_id(self):
        return self.username
    

class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Register")

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        print(''+existing_username+' is in the database')
        if existing_user_username:
            raise ValidationError(
                "that username already exists. Please choose a different one.")

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Login")

@login_required
@app.route("/home")
def home2():
    return homePage('','','')

@app.route('/', methods=['GET', 'POST'])
def login():
    if(request.method == 'GET'):
        form = LoginForm()
        return render_template('login.html', form=form)
    if(request.method == 'POST'):
        request.method 

@app.route("/sunglasses")
def Sunglasses():
    return render_template("sunglasses.html")

@app.route("/api/inputElem", methods = ["POST"])
def inputElem51():
    global count
    response = request.form.getlist("inputElem")
    a = response[0]
    b = response[1]
    c = response[2]
    d = response[3]
    e = response[4]

    def Appendtext():
	    with open("htmlMemory.txt",'a+') as f:
		    f.write(''+inputElem(a, b, c, d, e)+'')
	    f.close()
    if(count == 0):
        Appendtext()
    count += 1
    return homePage(''+inputElem(a, b, c, d, e)+'','','')


@app.route("/api/tagElem", methods = ["POST"])
def tag2Elem51():
    global count
    response = request.form.getlist("tagElem")
    tag1 = response[0]
    yourClass1 = response[1]
    type11 = response[2]
    name1 = response[3]
    value1 = response[4]
    id11 = response[5]
    onblur1 = response[6]
    onchange1 = response[7]
    onclick1 = response[8]
    oncontextmenu1 = response[9]
    oncopy1 = response[10]
    oncut1 = response[11]
    ondblclick1 = response[12]
    ondrag1 = response[13]
    ondragend1 = response[14]
    ondragenter1 = response[15]
    ondragenter1 = response[16]
    ondragleave1 = response[17]
    ondragover1 = response[18]
    ondragstart1 = response[19]
    ondrop1 = response[20]
    onfocus1 = response[21]
    oninput1 = response[22]
    oninvalid1 = response[23]
    onkeydown1 = response[24]
    onkeypress1 = response[25]
    onkeyup1 = response[26]
    onmousedown1 = response[27]
    onmousemove1 = response[28]
    onmouseout1 = response[29]
    onmouseover1 = response[30]
    onmouseup1 = response[31]
    onmousewheel1 = response[32]
    onpaste1 = response[33]
    onscroll1 = response[34]
    onselect1 = response[35]
    onwheel1 = response[36]
    onmoreAttributes1 = response[37]
    internalText1 = response[38]
    if(count == 0):
        def Appendtext():
            with open("htmlMemory.txt",'a+') as f:
                f.write(''+tagElem(tag1,yourClass1,type11,name1,value1,id11,onblur1,onchange1,onclick1,oncontextmenu1,oncopy1,oncut1,ondblclick1,ondrag1,ondragend1,ondragenter1,ondragenter1,ondragleave1,ondragover1,ondragstart1,ondrop1,onfocus1,oninput1,oninvalid1,onkeydown1,onkeypress1,onkeyup1,onmousedown1,onmousemove1,onmouseout1,onmouseover1,onmouseup1,onmousewheel1,onpaste1,onscroll1,onselect1,onwheel1,internalText1)+'')
            f.close()
    count = count + 1
    return homePage(''+tagElem(tag1,yourClass1,type11,name1,value1,id11,onblur1,onchange1,onclick1,oncontextmenu1,oncopy1,oncut1,ondblclick1,ondrag1,ondragend1,ondragenter1,ondragenter1,ondragleave1,ondragover1,ondragstart1,ondrop1,onfocus1,oninput1,oninvalid1,onkeydown1,onkeypress1,onkeyup1,onmousedown1,onmousemove1,onmouseout1,onmouseover1,onmouseup1,onmousewheel1,onpaste1,onscroll1,onselect1,onwheel1,internalText1)+'', '','')


@app.route("/api/createButton3", methods = ["POST"])
def createButton31():
    response = request.form.getlist("createButton3")
    a = response[0]
    b = response[1]
    c = response[2]
    d = response[3]
    # print(response)

    global count
    if(count == 0):
	    with open("htmlMemory.txt",'a+') as f:
		    f.write(''+createButton(a,b,c,d)+'')
	    f.close()
    count = count + 1
    print(count)
    return homePage(''+createButton(a,b,c,d)+'','','')


@app.route("/api/addColorToClass3", methods = ["POST"])
def addColorToClass4():
    response = request.form.getlist("addColorToClass3")
    a = response[0]
    b = response[1]
    c = response[2]
    print(response)
    def Appendtext():
	    with open("cssMemory.txt",'a+') as f:
		    f.write(''+addColorToClass(a, b, c)+'')
	    f.close()
    global count
    if(count == 0):
        Appendtext()
    count += 1
    return homePage('',''+addColorToClass(a, b, c)+'','')

@app.route("/api/changeNav3", methods = ["POST"])
def changeNav4():
    response = request.form.getlist("changeNav3")
    a = response[0]
    b = response[1]
    # print(response)
    def Appendtext():
	    with open("cssMemory.txt",'a+') as f:
		    f.write(''+changeNav2(a, b)+'')
	    f.close()
    global count
    if(count == 0):
        Appendtext()
    count += 1
    return homePage('',''+changeNav2(a, b)+'','')


@app.route("/api/addToCss1", methods = ["POST"])
def addToCss2():
    response = request.form.getlist("addToCss1")
    a = response[0]
    def Appendtext():
	    with open("cssMemory.txt",'a+') as f:
		    f.write(''+addToCss(a)+'')
	    f.close()
    global count
    if(count == 0):
        Appendtext()
    count += 1
    return homePage('',''+addToCss(a)+'','')


@app.route("/api/p1", methods = ["POST"])
def p2():

    # print(urllib.request)
    # print(request.form)
    response = request.form.getlist("p1")
    a = response[0]
    # print(response)
    def Appendtext():
	    with open("htmlMemory.txt",'a+') as f:
		    f.write(p1(a))
	    f.close()
    global count
    if(count == 0):
        Appendtext()
    count += 1
    return homePage(''+p1(a)+'','','')


@app.route("/api/b1", methods = ["POST"])
def b2():
    response = request.form.getlist("b1")
    a = response[0]
    # print(response)
    def Appendtext():
	    with open("htmlMemory.txt",'a+') as f:
		    f.write(''+b1(a)+'')
	    f.close()
    global count
    if(count == 0):
        Appendtext()
    count += 1
    return homePage(''+b1(a)+'','','')
    

@app.route("/api/i1", methods = ["POST"])
def i2():
    response = request.form.getlist("i1")
    a = response[0]
    global count
    # print(count)
    count += 1
    b = str(count)
    def Appendtext():
	    with open("htmlMemory.txt",'a+') as f:
		    f.write(''+i1(a)+'')
	    f.close()
    if(count == 0):
        Appendtext()
    count += 1
    return homePage(''+i1(a)+''+b+'','','')






@app.route("/api/img1", methods = ["POST"])
def img2():
    response = request.form.getlist("img1")
    a = response[0]
    global countf
    # print(count)
    count += 1
    b = str(count)
    def Appendtext():
	    with open("htmlMemory.txt",'a+') as f:
		    f.write(''+img1(a)+'')
	    f.close()
    if(count == 0):
        Appendtext()
    count += 1
    return homePage(''+img1(a)+''+b+'','','')
@app.route("/api/li1", methods = ["POST"])
def li2():
    response = request.form.getlist("li1")
    a = response[0]
    global count
    count += 1
    b = str(count)
    def Appendtext():
	    with open("htmlMemory.txt",'a+') as f:
		    f.write(''+li1(a)+'')
	    f.close()
    if(count == 0):
        Appendtext()
    count += 1
    return homePage(''+li1(a)+''+b+'','','')








@app.route("/api/deleteHtmlTxt", methods = ["POST"])
def deleteHtmlTxt2():
    deleteHtmlTxt()
    return homePage('','','')

@app.route("/api/deleteCssTxt", methods = ["POST"])
def deleteCssTxt2():
    deleteCssTxt()
    return homePage('','','')

@app.route("/api/profile", methods = ["POST"])
def profile2():
    response = request.form.getlist("changeNav3")
    a = response[0]
    b = response[1]
    c = response[2]
    d = response[3]
    # print(response)
    bio = a
    profile = b
    background = c
    name = d
    global count
    # if(count == 0):
	#     with open("htmlMemory.txt",'a+') as f:
	# 	    f.write(''+homePageFormat(a,b,c,d)+'')
	#     f.close()
    with open ("htmlMemory.txt", "r") as myfile:
        html = myfile.read()
    
    with open ("cssMemory.txt", "r") as myfile:
        css = myfile.read()
    
    count = count + 1
    print(count)
    return homePageFormat1(html, css, bio,profile,background,name)


if __name__ == "__main__":
    app.run(debug=True, port=8000, host="localhost")

# app.run





db = SQLAlchemy()
DB_NAME = "database.db"


# Your app flask name & secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://dalli:December!999@localhost:5432/database.db'
print(SECRET_KEY)
app.config['SECRET_KEY'] = SECRET_KEY


app.register_blueprint('database', url_prefix='/')
app.register_blueprint('database', url_prefix='/')

from database import User#,  (name)


login_manager = LoginManager()
login_manager.login_databasename = 'data base + login name'# -- example(database.login)
print(login_manager.login_databasename)
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

    return app
#[10:40 AM]
@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(username = user_id).first()

def create_database(app):
    if not path.exists('./testcap/' + DB_NAME):
        db.create_all(app=app)
        print('Database')





bcrypt = Bcrypt(app)


login_manager = LoginManager()
login_manager.init_app(app)


# metadata = MetaData(naming_convention=convention)
# db = SQLAlchemy(app, metadata=metadata)

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(username = user_id).first()





@app.route('/profileHome', methods=['GET','POST'])
def profileHome():
    orders = request.form
    print(orders.getlist('username')[0])
    z = User.username
    print(z)
    return homePage('','','')


@login_manager.unauthorized_handler
@app.route('/login', methods=['GET', 'POST'])
def login():
    if(request.method == 'GET'):
        form = LoginForm()
        return render_template('login.html', form=form)
    if(request.method == 'POST'):
        request.method 

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    # print(db.User)

    return render_template('register.html', form=form)



