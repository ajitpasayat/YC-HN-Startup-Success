import pymysql as mdb

con = mdb.connect('localhost', 'root', '', 'startupsuccess_db') #host, user, password, #database

# This is how you query SQL.
with con: 
    cur = con.cursor()
    cur.execute("SELECT company FROM startupdata LIMIT 10")
    rows = cur.fetchall()
    for row in rows:
        print row
