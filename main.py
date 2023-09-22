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


@app.route('/<user>',methods=['POST','GET'])
def user(user):
    session[request.form['username']] = request.form['password']

    with connection:
        with connection.cursor() as cr:
            cr.execute("SELECT * FROM users WHERE username = %s",(user,))
            user = cr.fetchone()
            if user is None:
                flash('User does not exist')
                return redirect(url_for('index'))

    return render_template('user.html',user=user)


