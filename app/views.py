from flask import render_template
from app import app
import pymysql as mdb

db = mdb.connect(user="root", host="localhost", db="startupsuccess_db", charset='utf8')

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

# This lets me now access the database and print it onto an HTML page. Cool.
@app.route('/db')
def startups_page():
	with db: 
		cur = db.cursor()
		cur.execute("SELECT company FROM startupdata LIMIT 15;")
		query_results = cur.fetchall()
	startups = ""
	for result in query_results:
		startups += result[0]
		startups += "<br>"
	return startups

@app.route('/startupdb')
def startups_page_fancy():
	with db:
		cur = db.cursor()
		cur.execute("SELECT company, sentiment FROM startupdata LIMIT 15;")
		query_results = cur.fetchall()
	startups = []
	for result in query_results:
		startups.append(dict(company=result[0], sentiment=result[1]))
	return render_template('startups.html', startups=startups)

