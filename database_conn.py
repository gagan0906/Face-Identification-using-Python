import sqlite3

class database():
    def __init__(self):
        self.conn=sqlite3.Connection('faces_collection.db')
        self.cur=self.conn.cursor()
        self.cur.execute('Create table if not exists faces(id INTEGER PRIMARY KEY,Name TEXT, AGE INTEGER)')
        self.conn.commit()

    def insert(self,id,name,age):
        self.cur.execute('insert into faces values(?,?,?)',(id,name,age))
        self.conn.commit()

    def display(self,id):
        self.cur.execute('select * from faces where id=?',(id,))
        rows=self.cur.fetchall()
        return rows            

    def checkid(self,id):
        self.cur.execute('select * from faces where id=?',(id,))    
        rows=self.cur.fetchall()
        return rows