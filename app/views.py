from flask import render_template
from app import app
from flask import request
import pymysql as mdb

@app.route('/ycpredictorslides')
def slides_page():
    return render_template('ycpredictorslides.html')
    
@app.route('/ycstartuppredictor')
def startups_page_fancy():
    db = mdb.connect(user="root", host="localhost", db="startupsuccess_db", charset='utf8')
    with db:
        cur_s14 = db.cursor()
        cur_s14.execute("SELECT company, prediction, probability, totalfunds, investors, founders, titlepoints, sentiment, website, market, commentsurl, logo, fate FROM data WHERE ycyear = '2014' AND ycsession = 'Summer';")
        query_results_s14 = cur_s14.fetchall()
        cur_s14.close()

        cur_w14 = db.cursor()
        cur_w14.execute("SELECT company, prediction, probability, totalfunds, investors, founders, titlepoints, sentiment, website, market, commentsurl, logo, fate FROM data WHERE ycyear = '2014' AND ycsession = 'Winter';")
        query_results_w14 = cur_w14.fetchall()
        cur_w14.close()

        cur_s13 = db.cursor()
        cur_s13.execute("SELECT company, prediction, probability, totalfunds, investors, founders, titlepoints, sentiment, website, market, commentsurl, logo, fate FROM data WHERE ycyear = '2013' AND ycsession = 'Summer';")
        query_results_s13 = cur_s13.fetchall()
        cur_s13.close()

        cur_w13 = db.cursor()
        cur_w13.execute("SELECT company, prediction, probability, totalfunds, investors, founders, titlepoints, sentiment, website, market, commentsurl, logo, fate FROM data WHERE ycyear = '2013' AND ycsession = 'Winter';")
        query_results_w13 = cur_w13.fetchall()
        cur_w13.close()

        cur_s12 = db.cursor()
        cur_s12.execute("SELECT company, prediction, probability, totalfunds, investors, founders, titlepoints, sentiment, website, market, commentsurl, logo, fate FROM data WHERE ycyear = '2012' AND ycsession = 'Summer';")
        query_results_s12 = cur_s12.fetchall()
        cur_s12.close()

        cur_w12 = db.cursor()
        cur_w12.execute("SELECT company, prediction, probability, totalfunds, investors, founders, titlepoints, sentiment, website, market, commentsurl, logo, fate FROM data WHERE ycyear = '2012' AND ycsession = 'Winter';")
        query_results_w12 = cur_w12.fetchall()
        cur_w12.close()

        cur_s11 = db.cursor()
        cur_s11.execute("SELECT company, prediction, probability, totalfunds, investors, founders, titlepoints, sentiment, website, market, commentsurl, logo, fate FROM data WHERE ycyear = '2011' AND ycsession = 'Summer';")
        query_results_s11 = cur_s11.fetchall()
        cur_s11.close()

        cur_w11 = db.cursor()
        cur_w11.execute("SELECT company, prediction, probability, totalfunds, investors, founders, titlepoints, sentiment, website, market, commentsurl, logo, fate FROM data WHERE ycyear = '2011' AND ycsession = 'Winter';")
        query_results_w11 = cur_w11.fetchall()
        cur_w11.close()

        cur_s10 = db.cursor()
        cur_s10.execute("SELECT company, prediction, probability, totalfunds, investors, founders, titlepoints, sentiment, website, market, commentsurl, logo, fate FROM data WHERE ycyear = '2010' AND ycsession = 'Summer';")
        query_results_s10 = cur_s10.fetchall()
        cur_s10.close()

        cur_w10 = db.cursor()
        cur_w10.execute("SELECT company, prediction, probability, totalfunds, investors, founders, titlepoints, sentiment, website, market, commentsurl, logo, fate FROM data WHERE ycyear = '2010' AND ycsession = 'Winter';")
        query_results_w10 = cur_w10.fetchall()
        cur_w10.close()

        cur_s09 = db.cursor()
        cur_s09.execute("SELECT company, prediction, probability, totalfunds, investors, founders, titlepoints, sentiment, website, market, commentsurl, logo, fate FROM data WHERE ycyear = '2009' AND ycsession = 'Summer';")
        query_results_s09 = cur_s09.fetchall()
        cur_s09.close()

        cur_w09 = db.cursor()
        cur_w09.execute("SELECT company, prediction, probability, totalfunds, investors, founders, titlepoints, sentiment, website, market, commentsurl, logo, fate FROM data WHERE ycyear = '2009' AND ycsession = 'Winter';")
        query_results_w09 = cur_w09.fetchall()
        cur_w10.close()

        cur_s08 = db.cursor()
        cur_s08.execute("SELECT company, prediction, probability, totalfunds, investors, founders, titlepoints, sentiment, website, market, commentsurl, logo, fate FROM data WHERE ycyear = '2008' AND ycsession = 'Summer';")
        query_results_s08 = cur_s08.fetchall()
        cur_s08.close()

        cur_w08 = db.cursor()
        cur_w08.execute("SELECT company, prediction, probability, totalfunds, investors, founders, titlepoints, sentiment, website, market, commentsurl, logo, fate FROM data WHERE ycyear = '2008' AND ycsession = 'Winter';")
        query_results_w08 = cur_w08.fetchall()
        cur_w08.close()

        cur_070605 = db.cursor()
        cur_070605.execute("SELECT company, prediction, probability, totalfunds, investors, founders, titlepoints, sentiment, website, market, commentsurl, logo, fate FROM data WHERE ycyear IN ('2007', '2006', '2005');")
        query_results_070605 = cur_070605.fetchall()
        cur_070605.close()

        
    session_s14 = []
    session_w14 = []

    session_s13 = []
    session_w13 = []

    session_s12 = []
    session_w12 = []

    session_s11 = []
    session_w11 = []

    session_s10 = []
    session_w10 = []

    session_s09 = []
    session_w09 = []

    session_s08 = []
    session_w08 = []

    session_070605 = []

    for result in query_results_s14:
        session_s14.append(dict(company=result[0], prediction=result[1],  likelihood=result[2], 
            totalfunds = '${:,.2f}'.format(result[3]), investors=result[4], founders=result[5], 
            upvotes=result[6], sentiment=result[7], url=result[8], market=result[9], commentsurl=result[10], logo=result[11], status=result[12]))
        
    for result in query_results_w14:
        session_w14.append(dict(company=result[0], prediction=result[1],  likelihood=result[2], 
            totalfunds = '${:,.2f}'.format(result[3]), investors=result[4], founders=result[5], 
            upvotes=result[6], sentiment=result[7], url=result[8], market=result[9], commentsurl=result[10], logo=result[11], status=result[12]))

    for result in query_results_s13:
        session_s13.append(dict(company=result[0], prediction=result[1],  likelihood=result[2], 
            totalfunds = '${:,.2f}'.format(result[3]), investors=result[4], founders=result[5], 
            upvotes=result[6], sentiment=result[7], url=result[8], market=result[9], commentsurl=result[10], logo=result[11], status=result[12]))
        
    for result in query_results_w13:
        session_w13.append(dict(company=result[0], prediction=result[1],  likelihood=result[2], 
            totalfunds = '${:,.2f}'.format(result[3]), investors=result[4], founders=result[5], 
            upvotes=result[6], sentiment=result[7], url=result[8], market=result[9], commentsurl=result[10], logo=result[11], status=result[12]))

    for result in query_results_s12:
        session_s12.append(dict(company=result[0], prediction=result[1],  likelihood=result[2], 
            totalfunds = '${:,.2f}'.format(result[3]), investors=result[4], founders=result[5], 
            upvotes=result[6], sentiment=result[7], url=result[8], market=result[9], commentsurl=result[10], logo=result[11], status=result[12]))
        
    for result in query_results_w12:
        session_w12.append(dict(company=result[0], prediction=result[1],  likelihood=result[2], 
            totalfunds = '${:,.2f}'.format(result[3]), investors=result[4], founders=result[5], 
            upvotes=result[6], sentiment=result[7], url=result[8], market=result[9], commentsurl=result[10], logo=result[11], status=result[12]))

    for result in query_results_s11:
        session_s11.append(dict(company=result[0], prediction=result[1],  likelihood=result[2], 
            totalfunds = '${:,.2f}'.format(result[3]), investors=result[4], founders=result[5], 
            upvotes=result[6], sentiment=result[7], url=result[8], market=result[9], commentsurl=result[10], logo=result[11], status=result[12]))
        
    for result in query_results_w11:
        session_w11.append(dict(company=result[0], prediction=result[1],  likelihood=result[2], 
            totalfunds = '${:,.2f}'.format(result[3]), investors=result[4], founders=result[5], 
            upvotes=result[6], sentiment=result[7], url=result[8], market=result[9], commentsurl=result[10], logo=result[11], status=result[12]))

    for result in query_results_s10:
        session_s10.append(dict(company=result[0], prediction=result[1],  likelihood=result[2], 
            totalfunds = '${:,.2f}'.format(result[3]), investors=result[4], founders=result[5], 
            upvotes=result[6], sentiment=result[7], url=result[8], market=result[9], commentsurl=result[10], logo=result[11], status=result[12]))
        
    for result in query_results_w10:
        session_w10.append(dict(company=result[0], prediction=result[1],  likelihood=result[2], 
            totalfunds = '${:,.2f}'.format(result[3]), investors=result[4], founders=result[5], 
            upvotes=result[6], sentiment=result[7], url=result[8], market=result[9], commentsurl=result[10], logo=result[11], status=result[12]))

    for result in query_results_s09:
        session_s09.append(dict(company=result[0], prediction=result[1],  likelihood=result[2], 
            totalfunds = '${:,.2f}'.format(result[3]), investors=result[4], founders=result[5], 
            upvotes=result[6], sentiment=result[7], url=result[8], market=result[9], commentsurl=result[10], logo=result[11], status=result[12]))

    for result in query_results_w09:
        session_w09.append(dict(company=result[0], prediction=result[1],  likelihood=result[2], 
            totalfunds = '${:,.2f}'.format(result[3]), investors=result[4], founders=result[5], 
            upvotes=result[6], sentiment=result[7], url=result[8], market=result[9], commentsurl=result[10], logo=result[11], status=result[12]))

    for result in query_results_s08:
        session_s08.append(dict(company=result[0], prediction=result[1],  likelihood=result[2], 
            totalfunds = '${:,.2f}'.format(result[3]), investors=result[4], founders=result[5], 
            upvotes=result[6], sentiment=result[7], url=result[8], market=result[9], commentsurl=result[10], logo=result[11], status=result[12]))

    for result in query_results_w08:
        session_w08.append(dict(company=result[0], prediction=result[1],  likelihood=result[2], 
            totalfunds = '${:,.2f}'.format(result[3]), investors=result[4], founders=result[5], 
            upvotes=result[6], sentiment=result[7], url=result[8], market=result[9], commentsurl=result[10], logo=result[11], status=result[12]))

    for result in query_results_070605:
        session_070605.append(dict(company=result[0], prediction=result[1],  likelihood=result[2], 
            totalfunds = '${:,.2f}'.format(result[3]), investors=result[4], founders=result[5], 
            upvotes=result[6], sentiment=result[7], url=result[8], market=result[9], commentsurl=result[10], logo=result[11], status=result[12]))

    db.close()

    return render_template('startups.html', session_s14=session_s14, session_w14=session_w14,
            session_s13=session_s13, session_w13=session_w13,
            session_s12=session_s12, session_w12=session_w12,
            session_s11=session_s11, session_w11=session_w11,
            session_s10=session_s10, session_w10=session_w10,
            session_s09=session_s09, session_w09=session_w09,
            session_s08=session_s08, session_w08=session_w08,
            session_070605=session_070605)
    

@app.route('/ycstartuppredictor', methods=['POST'])
def my_form_post():
    db = mdb.connect(user="root", host="localhost", db="startupsuccess_db", charset='utf8')    
    startup = request.form['startupcompany']
    with db:
        cur_startup = db.cursor()
        cur_startup.execute("SELECT company, prediction, probability, totalfunds, investors, founders, titlepoints, sentiment, website, market, commentsurl, logo, fate FROM data WHERE company = '" + startup + "';")
        search_results = cur_startup.fetchall() 
        cur_startup.close()

        cur_s14 = db.cursor()
        cur_s14.execute("SELECT company, prediction, probability, totalfunds, investors, founders, titlepoints, sentiment, website, market, commentsurl, logo, fate FROM data WHERE ycyear = '2014' AND ycsession = 'Summer';")
        query_results_s14 = cur_s14.fetchall()
        cur_s14.close()

        cur_w14 = db.cursor()
        cur_w14.execute("SELECT company, prediction, probability, totalfunds, investors, founders, titlepoints, sentiment, website, market, commentsurl, logo, fate FROM data WHERE ycyear = '2014' AND ycsession = 'Winter';")
        query_results_w14 = cur_w14.fetchall()
        cur_w14.close()

        cur_s13 = db.cursor()
        cur_s13.execute("SELECT company, prediction, probability, totalfunds, investors, founders, titlepoints, sentiment, website, market, commentsurl, logo, fate FROM data WHERE ycyear = '2013' AND ycsession = 'Summer';")
        query_results_s13 = cur_s13.fetchall()
        cur_s13.close()

        cur_w13 = db.cursor()
        cur_w13.execute("SELECT company, prediction, probability, totalfunds, investors, founders, titlepoints, sentiment, website, market, commentsurl, logo, fate FROM data WHERE ycyear = '2013' AND ycsession = 'Winter';")
        query_results_w13 = cur_w13.fetchall()
        cur_w13.close()

        cur_s12 = db.cursor()
        cur_s12.execute("SELECT company, prediction, probability, totalfunds, investors, founders, titlepoints, sentiment, website, market, commentsurl, logo, fate FROM data WHERE ycyear = '2012' AND ycsession = 'Summer';")
        query_results_s12 = cur_s12.fetchall()
        cur_s12.close()

        cur_w12 = db.cursor()
        cur_w12.execute("SELECT company, prediction, probability, totalfunds, investors, founders, titlepoints, sentiment, website, market, commentsurl, logo, fate FROM data WHERE ycyear = '2012' AND ycsession = 'Winter';")
        query_results_w12 = cur_w12.fetchall()
        cur_w12.close()

        cur_s11 = db.cursor()
        cur_s11.execute("SELECT company, prediction, probability, totalfunds, investors, founders, titlepoints, sentiment, website, market, commentsurl, logo, fate FROM data WHERE ycyear = '2011' AND ycsession = 'Summer';")
        query_results_s11 = cur_s11.fetchall()
        cur_s11.close()

        cur_w11 = db.cursor()
        cur_w11.execute("SELECT company, prediction, probability, totalfunds, investors, founders, titlepoints, sentiment, website, market, commentsurl, logo, fate FROM data WHERE ycyear = '2011' AND ycsession = 'Winter';")
        query_results_w11 = cur_w11.fetchall()
        cur_w11.close()

        cur_s10 = db.cursor()
        cur_s10.execute("SELECT company, prediction, probability, totalfunds, investors, founders, titlepoints, sentiment, website, market, commentsurl, logo, fate FROM data WHERE ycyear = '2010' AND ycsession = 'Summer';")
        query_results_s10 = cur_s10.fetchall()
        cur_s10.close()

        cur_w10 = db.cursor()
        cur_w10.execute("SELECT company, prediction, probability, totalfunds, investors, founders, titlepoints, sentiment, website, market, commentsurl, logo, fate FROM data WHERE ycyear = '2010' AND ycsession = 'Winter';")
        query_results_w10 = cur_w10.fetchall()
        cur_w10.close()

        cur_s09 = db.cursor()
        cur_s09.execute("SELECT company, prediction, probability, totalfunds, investors, founders, titlepoints, sentiment, website, market, commentsurl, logo, fate FROM data WHERE ycyear = '2009' AND ycsession = 'Summer';")
        query_results_s09 = cur_s09.fetchall()
        cur_s09.close()

        cur_w09 = db.cursor()
        cur_w09.execute("SELECT company, prediction, probability, totalfunds, investors, founders, titlepoints, sentiment, website, market, commentsurl, logo, fate FROM data WHERE ycyear = '2009' AND ycsession = 'Winter';")
        query_results_w09 = cur_w09.fetchall()
        cur_w10.close()

        cur_s08 = db.cursor()
        cur_s08.execute("SELECT company, prediction, probability, totalfunds, investors, founders, titlepoints, sentiment, website, market, commentsurl, logo, fate FROM data WHERE ycyear = '2008' AND ycsession = 'Summer';")
        query_results_s08 = cur_s08.fetchall()
        cur_s08.close()

        cur_w08 = db.cursor()
        cur_w08.execute("SELECT company, prediction, probability, totalfunds, investors, founders, titlepoints, sentiment, website, market, commentsurl, logo, fate FROM data WHERE ycyear = '2008' AND ycsession = 'Winter';")
        query_results_w08 = cur_w08.fetchall()
        cur_w08.close()

        cur_070605 = db.cursor()
        cur_070605.execute("SELECT company, prediction, probability, totalfunds, investors, founders, titlepoints, sentiment, website, market, commentsurl, logo, fate FROM data WHERE ycyear IN ('2007', '2006', '2005');")
        query_results_070605 = cur_070605.fetchall()
        cur_070605.close()

        
    session_s14 = []
    session_w14 = []

    session_s13 = []
    session_w13 = []

    session_s12 = []
    session_w12 = []

    session_s11 = []
    session_w11 = []

    session_s10 = []
    session_w10 = []

    session_s09 = []
    session_w09 = []

    session_s08 = []
    session_w08 = []

    session_070605 = []

    for result in query_results_s14:
        session_s14.append(dict(company=result[0], prediction=result[1],  likelihood=result[2], 
            totalfunds = '${:,.2f}'.format(result[3]), investors=result[4], founders=result[5], 
            upvotes=result[6], sentiment=result[7], url=result[8], market=result[9], commentsurl=result[10], logo=result[11], status=result[12]))
        
    for result in query_results_w14:
        session_w14.append(dict(company=result[0], prediction=result[1],  likelihood=result[2], 
            totalfunds = '${:,.2f}'.format(result[3]), investors=result[4], founders=result[5], 
            upvotes=result[6], sentiment=result[7], url=result[8], market=result[9], commentsurl=result[10], logo=result[11], status=result[12]))

    for result in query_results_s13:
        session_s13.append(dict(company=result[0], prediction=result[1],  likelihood=result[2], 
            totalfunds = '${:,.2f}'.format(result[3]), investors=result[4], founders=result[5], 
            upvotes=result[6], sentiment=result[7], url=result[8], market=result[9], commentsurl=result[10], logo=result[11], status=result[12]))
        
    for result in query_results_w13:
        session_w13.append(dict(company=result[0], prediction=result[1],  likelihood=result[2], 
            totalfunds = '${:,.2f}'.format(result[3]), investors=result[4], founders=result[5], 
            upvotes=result[6], sentiment=result[7], url=result[8], market=result[9], commentsurl=result[10], logo=result[11], status=result[12]))

    for result in query_results_s12:
        session_s12.append(dict(company=result[0], prediction=result[1],  likelihood=result[2], 
            totalfunds = '${:,.2f}'.format(result[3]), investors=result[4], founders=result[5], 
            upvotes=result[6], sentiment=result[7], url=result[8], market=result[9], commentsurl=result[10], logo=result[11], status=result[12]))
        
    for result in query_results_w12:
        session_w12.append(dict(company=result[0], prediction=result[1],  likelihood=result[2], 
            totalfunds = '${:,.2f}'.format(result[3]), investors=result[4], founders=result[5], 
            upvotes=result[6], sentiment=result[7], url=result[8], market=result[9], commentsurl=result[10], logo=result[11], status=result[12]))

    for result in query_results_s11:
        session_s11.append(dict(company=result[0], prediction=result[1],  likelihood=result[2], 
            totalfunds = '${:,.2f}'.format(result[3]), investors=result[4], founders=result[5], 
            upvotes=result[6], sentiment=result[7], url=result[8], market=result[9], commentsurl=result[10], logo=result[11], status=result[12]))
        
    for result in query_results_w11:
        session_w11.append(dict(company=result[0], prediction=result[1],  likelihood=result[2], 
            totalfunds = '${:,.2f}'.format(result[3]), investors=result[4], founders=result[5], 
            upvotes=result[6], sentiment=result[7], url=result[8], market=result[9], commentsurl=result[10], logo=result[11], status=result[12]))

    for result in query_results_s10:
        session_s10.append(dict(company=result[0], prediction=result[1],  likelihood=result[2], 
            totalfunds = '${:,.2f}'.format(result[3]), investors=result[4], founders=result[5], 
            upvotes=result[6], sentiment=result[7], url=result[8], market=result[9], commentsurl=result[10], logo=result[11], status=result[12]))
        
    for result in query_results_w10:
        session_w10.append(dict(company=result[0], prediction=result[1],  likelihood=result[2], 
            totalfunds = '${:,.2f}'.format(result[3]), investors=result[4], founders=result[5], 
            upvotes=result[6], sentiment=result[7], url=result[8], market=result[9], commentsurl=result[10], logo=result[11], status=result[12]))

    for result in query_results_s09:
        session_s09.append(dict(company=result[0], prediction=result[1],  likelihood=result[2], 
            totalfunds = '${:,.2f}'.format(result[3]), investors=result[4], founders=result[5], 
            upvotes=result[6], sentiment=result[7], url=result[8], market=result[9], commentsurl=result[10], logo=result[11], status=result[12]))

    for result in query_results_w09:
        session_w09.append(dict(company=result[0], prediction=result[1],  likelihood=result[2], 
            totalfunds = '${:,.2f}'.format(result[3]), investors=result[4], founders=result[5], 
            upvotes=result[6], sentiment=result[7], url=result[8], market=result[9], commentsurl=result[10], logo=result[11], status=result[12]))

    for result in query_results_s08:
        session_s08.append(dict(company=result[0], prediction=result[1],  likelihood=result[2], 
            totalfunds = '${:,.2f}'.format(result[3]), investors=result[4], founders=result[5], 
            upvotes=result[6], sentiment=result[7], url=result[8], market=result[9], commentsurl=result[10], logo=result[11], status=result[12]))

    for result in query_results_w08:
        session_w08.append(dict(company=result[0], prediction=result[1],  likelihood=result[2], 
            totalfunds = '${:,.2f}'.format(result[3]), investors=result[4], founders=result[5], 
            upvotes=result[6], sentiment=result[7], url=result[8], market=result[9], commentsurl=result[10], logo=result[11], status=result[12]))

    for result in query_results_070605:
        session_070605.append(dict(company=result[0], prediction=result[1],  likelihood=result[2], 
            totalfunds = '${:,.2f}'.format(result[3]), investors=result[4], founders=result[5], 
            upvotes=result[6], sentiment=result[7], url=result[8], market=result[9], commentsurl=result[10], logo=result[11], status=result[12]))

    db.close()

    return render_template('startups.html', search_results=search_results, 
            session_s14=session_s14, session_w14=session_w14,
            session_s13=session_s13, session_w13=session_w13,
            session_s12=session_s12, session_w12=session_w12,
            session_s11=session_s11, session_w11=session_w11,
            session_s10=session_s10, session_w10=session_w10,
            session_s09=session_s09, session_w09=session_w09,
            session_s08=session_s08, session_w08=session_w08,
            session_070605=session_070605)

