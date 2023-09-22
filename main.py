import os
from dotenv import load_dotenv
from flask import Flask , render_template,request,session
import psycopg2

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

@app.route('/')
def index():
    return render_template('index.html')
