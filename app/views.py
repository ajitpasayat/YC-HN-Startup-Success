from flask import render_template
from app import app
import pymysql as mdb

db = mdb.connect(user="root", host="localhost", db="startupsuccess_db", charset='utf8')

@app.route('/ycstartuppredictor')
def startups_page_fancy():
    with db:
        cur_s14 = db.cursor()
        cur_s14.execute("SELECT company, prediction, probability, totalfunds, investors, founders, titlepoints, sentiment FROM fullset WHERE ycyear = '2014' AND ycsession = 'Summer';")
        query_results_s14 = cur_s14.fetchall()

        cur_w14 = db.cursor()
        cur_w14.execute("SELECT company, prediction, probability FROM fullset WHERE ycyear = '2014' AND ycsession = 'Winter';")
        query_results_w14 = cur_w14.fetchall()
        
    session_s14 = []
    session_w14 = []
    
    for result in query_results_s14:
        session_s14.append(dict(company=result[0], prediction=result[1],  likelihood=result[2], 
            totalfunds=result[3], investors=result[4], founders=result[5], 
            upvotes=result[6], sentiment=result[7]))
        
    for result in query_results_w14:
        session_w14.append(dict(company=result[0], prediction=result[1], likelihood=result[2]))
        
    return render_template('startups2.html', session_s14=session_s14, session_w14=session_w14)
