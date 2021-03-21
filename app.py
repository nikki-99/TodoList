from flask import Flask,render_template,flash,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from flask_sqlalchemy import SQLAlchemy
import os


app=Flask(__name__)
db=SQLAlchemy(app)
basedir = os.path.abspath(os.path.dirname(__file__))


app.config['SECRET_KEY']='asdfsadfasf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(60),nullable=False)
    email=db.Column(db.String(60),nullable=False)
    password=db.Column(db.String(60),nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.name

class RegistrationFrom(FlaskForm):
    name = StringField('Name',validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm = PasswordField('Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Register')



@app.route('/')
def home():
    return render_template('base.html')

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationFrom()
    if form.validate_on_submit():
        user=User(name=form.name.data,email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Thank You for registering','success')
        return redirect(url_for('login'))
    return render_template('register.html',form=form)


@app.route('/login')
def login():
    return "success login"