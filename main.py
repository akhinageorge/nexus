import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, session, url_for, redirect, flash
import psycopg2

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

connection = psycopg2.connect(os.getenv('DATABASE_URL'))


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/signup', methods=["POST", "GET"])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(password, username)
        with connection:
            with connection.cursor() as cr:
                cr.execute(
                    "INSERT INTO public.users (username,password) VALUES (%s,%s)", (username, password))
                connection.commit()
                flash('User created')
                return redirect(url_for('signin'))

    else:

        return render_template('signup.html')


@app.route('/signin', methods=["POST", "GET"])
def signin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        with connection:
            with connection.cursor() as cr:
                cr.execute(
                    "SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
                user = cr.fetchone()
                if user is None:
                    flash('User does not exist')
                else:
                    flash('User logged in')
                    session['username'] = username
                    return redirect(url_for('dashboard'))
    return render_template('signin.html')


@app.route('/dashboard', methods=["POST", "GET"])
def dashboard():
    bus = []
    if 'username' not in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        startPoint = request.form.get('source')
        endPoint = request.form.get('destination')
        print(startPoint, endPoint)

        with connection:
            with connection.cursor() as cr:
                cr.execute(""" SELECT DISTINCT d1.schedule_id
                                FROM public.detailedschedule d1
                                WHERE
                                EXISTS (
                                SELECT 1
                                FROM public.detailedschedule d2
                                WHERE
                                d1.schedule_id = d2.schedule_id
                                AND d1.stop_name = %s -- Replace 'Source' with the actual source stop name
                                AND d2.stop_name = %s -- Replace 'Destination' with the actual destination stop name
                                AND d1.stop_number < d2.stop_number);""",(startPoint, endPoint))
                data = cr.fetchall()
                print(data)
                values = [item[0] for item in data]

                for point in values:
                    cr.execute("SELECT * FROM public.schedule WHERE scheduleid = %s;", (point,))
                    bus.append(cr.fetchone())



    return render_template('commute.html', buses= bus)

@app.route('/journey')
def journey():
    return render_template('journey.html')

@app.route('/route')
def routes():
    return render_template('route.html')