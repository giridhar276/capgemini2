"""
Requirements:
 * A database created with some data about authors inside.
"""
import pymysql
from flask import Flask, render_template


app = Flask(__name__)


def connect_db():
    return pymysql.connect(host="localhost", port=3306, user="root", passwd="india@123", db="capgemini" )


@app.route('/')
def hello_world():
    db  = connect_db()
    cursor = db.cursor()
    sql = "select * from realestate"
    cursor.execute(sql)
    details = [ ",".join(row) for row in cursor.fetchall()]
    return render_template('database/authors_template_engine.html', authors=details)
