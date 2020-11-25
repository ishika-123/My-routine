import sqlite3

def connect():
    conn=sqlite3.connect('routine.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS routine(Id INTEGER PRIMARY KEY, date text,expenditure integer,exercise text,study text,diet text,python text)")
    conn.commit()
    conn.close()

def insert(date,expenditure,exercise,study,diet,python):
    conn=sqlite3.connect('routine.db')
    cur=conn.cursor()
    cur.execute("insert into routine values(NULL,?,?,?,?,?,?)",(date,expenditure,exercise,study,diet,python))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect('routine.db')
    cur=conn.cursor()
    cur.execute("select * from routine")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def search(date='',expenditure='',exercise='',study='',diet='',python=''):
    conn=sqlite3.connect('routine.db')
    cur=conn.cursor()
    cur.execute("select * from routine where date=? or expenditure=? or exercise=?",(date,earnings,exercise))
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect('routine.db')
    cur=conn.cursor()
    cur.execute("delete from routine where id=?",(id,))
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    
#x=search(earnings=300)
#print(x)

connect()

#print(view())
