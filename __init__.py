from flask import Flask
import psycopg2
import moviesModels

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fc089b9218301ad987914c53481bff04'
# set your own database name, user name and password
db = "dbname='DBNAME' user='USERNAME' host='localhost' password='PASSWORD'" #potentially wrong password
conn = psycopg2.connect(db)
