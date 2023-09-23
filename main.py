import os
from dotenv import load_dotenv
from flask import Flask , render_template,request,session,url_for,redirect,flash
import psycopg2

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

connection = psycopg2.connect(os.getenv('DATABASE_URL'))

@app.route('/')
def index():
    
    return render_template('index.html')


@app.route('/signin' ,methods=["POST","GET"])
def signin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        with connection:
            with connection.cursor() as cr:
                cr.execute("SELECT * FROM users WHERE username = %s AND password = %s",(username,password))
                user = cr.fetchone()
                if user is None:
                    flash('User does not exist')
                else:
                    flash('User logged in')
                    session[username] = request.form[password]
                    return redirect(url_for('dashboard'))
    return render_template('signin.html')


@app.route('/signup',methods=["POST","GET"])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        with connection:
            with connection.cursor() as cr:
                cr.execute("INSERT INTO users (username,password) VALUES (%s,%s)",(username,password))
                connection.commit()
                flash('User created')
                return redirect(url_for('signin'))
            
    else:
            
        return render_template('signup.html')

@app.route('/dashboard',methods=["POST","GET"] )
def dashboard():
    if session['username'] is None:
        return redirect(url_for('signin'))
    
    if request.method == 'POST':
        startPoint = request.form.get('startPoint')
        endPoint = request.form.get('endPoint')

        data
    


    return render_template('dashboard.html')