from flask import render_template
from app import app
import pymysql as mdb
import json

db = mdb.connect(user="root", host="localhost", db="startupsuccess_db", charset='utf8')

@app.route('/ycstartuppredictor')
def startups_page_fancy():
    with db:
        cur_win = db.cursor()
        cur_win.execute("SELECT company, prediction, probability, totalfunds, investors, founders, titlepoints, topcomment, sentiment, logo FROM fullset LIMIT 15;")
        query_results_win = cur_win.fetchall()
    win = []
    for result in query_results_win:
        win.append(dict(company=result[0], prediction=result[1], probability=result[2], totalfunds=result[3], investors=result[4], founders=result[5], titlepoints=result[6], topcomment=result[7], sentiment=result[8], logo=result[9]))
        
    return render_template('startups.html', win=win)
