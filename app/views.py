from flask import render_template
from app import app
import pymysql as mdb

db = mdb.connect(user="root", host="localhost", db="startupsuccess_db", charset='utf8')

@app.route('/startupdb')
def startups_page_fancy():
    with db:
        cura = db.cursor()
        cura.execute("SELECT company, sentiment FROM startupdata LIMIT 15;")
        query_results_a = cura.fetchall()

        curb = db.cursor()
        curb.execute("SELECT totalfunds FROM startupdata LIMIT 15;")
        query_results_b = curb.fetchall()

    startups = []
    totalfunds = []
    for result in query_results_a:
        startups.append(dict(company=result[0], sentiment=result[1]))

    for result in query_results_b:
        totalfunds.append(result[0])
        
    return render_template('startups.html', startups=startups, totalfunds=totalfunds)
